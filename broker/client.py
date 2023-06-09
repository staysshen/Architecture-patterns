class Client:
    def __init__(self, broker):
        self.broker = broker

    def send_request(self, server_name, request_data):
        request = Request(server_name, request_data)
        return self.broker.route_request(request)
