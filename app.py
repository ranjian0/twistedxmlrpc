from twisted.web import xmlrpc

class BlenderXMLRPC(xmlrpc.XMLRPC):
    """access api with xmlrpc"""

    def xmlrpc_list_objects(self):
        return [1,2,3,4,5]

    def xmlrpc_make_cube(self):
        return "Cube created"
