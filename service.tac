import os
try:
    import app
except ImportError:
    import sys
    sys.path.append('.')
    import app

from twisted.application import service, internet
from twisted.web import server

def getWebService():
    """
    Return a service suitable for creating an application object.

    This service is a simple web server that serves files on port 8080 from
    underneath the current working directory.
    """
    # create a resource to serve static files
    r = app.XMLRPC()
    xmlrpcServer = server.Site(r)
    return internet.TCPServer(int(os.environ.get("PORT", 7080)), xmlrpcServer)

# this is the core part of any tac file, the creation of the root-level
# application object
application = service.Application("Blender XMLRPC Server")

# attach the service to its parent application
service = getWebService()
service.setServiceParent(application)