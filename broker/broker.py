class Broker:
    def __init__(self):
        self.servers = {}

    def register_server(self, server):
        self.servers[server.name] = server

    def route_request(self, request):
        server = self.servers.get(request.server_name)
        if server:
            return server.process_request(request)
        else:
            raise ValueError("Server not found: " + request.server_name)


class Server:
    def __init__(self, name):
        self.name = name

    def process_request(self, request):
        pass


class Request:
    def __init__(self, server_name, data):
        self.server_name = server_name
        self.data = data


class Response:
    def __init__(self, server_name, result):
        self.server_name = server_name
        self.result = result
