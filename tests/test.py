import os
import threading
import subprocess
import xmlrpc.client

DEBUG = bool(os.environ.get("DEBUG", False))
NUM_CLIENTS = 1

if DEBUG:
    URL = "http://localhost:7080/"
else:
    URL = subprocess.check_output("heroku info -s | grep web_url | cut -d= -f2", shell=True).decode().strip()

def request():
  with xmlrpc.client.ServerProxy(URL, allow_none=True, use_builtin_types=True) as proxy:
        print(proxy.get_message())
        lst = proxy.get_list()
        data = proxy.get_data()
        print("List length: ", len(lst))
        print("Image Length: ", len(data['bin']))
        for k,v in data.items():
            if k != "bin":
                print(k, v)

        # print(lst)
        # print(data['bin'])

if __name__ == "__main__":
  threads = [threading.Thread(target=request) for _ in range(NUM_CLIENTS)]
  [t.start() for t in threads]
  [t.join() for t in threads]
