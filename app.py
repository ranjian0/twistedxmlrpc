import datetime
from twisted.web import xmlrpc

class XMLRPC(xmlrpc.XMLRPC):
    """access api with xmlrpc"""

    def xmlrpc_get_message(self):
        return "This is the message you requested"

    def xmlrpc_get_list(self):
        return list(range(1000_000))

    def xmlrpc_get_data(self):
        image = None 
        with open("cat.jpeg", "rb") as f:
            image = f.read()

        return {
            "int" : 1000,
            "float" : 1000.0,
            "str" : "The quick brown fox jumped over the lazy dog",
            "tuple": (3, 4, 5),
            "list": [1,2,3,4,5,6,7,8,9],
            "dict": {"a":1, "b":(1,2), "c":"other"},
            "bin": image,
            "date": datetime.datetime.now(),
        }
