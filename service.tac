import os
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
    r = app.BlenderXMLRPC()
    xmlrpcServer = server.Site(r)
    print(os.environ.get("PORT"))
    return internet.TCPServer(int(os.environ.get("PORT")), xmlrpcServer)

# this is the core part of any tac file, the creation of the root-level
# application object
application = service.Application("Blender XMLRPC Server")

# attach the service to its parent application
service = getWebService()
service.setServiceParent(application)