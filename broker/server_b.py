from broker import Server, Response

class ServerB(Server):
    def process_request(self, request):
        # Process the request specific to ServerB
        result = "ServerB processed: " + request.data
        return Response(self.name, result)
