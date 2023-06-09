class Master:
    def __init__(self):
        self.slaves = []

    def add_slave(self, slave):
        self.slaves.append(slave)

    def process_request(self, request):
        results = []
        for slave in self.slaves:
            result = slave.process_request(request)
            results.append(result)
        return results
