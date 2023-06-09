from broker import Server, Response


class ServerA(Server):
    def process_request(self, request):
        # Process the request specific to ServerA
        result = "ServerA processed: " + request.data
        return Response(self.name, result)
