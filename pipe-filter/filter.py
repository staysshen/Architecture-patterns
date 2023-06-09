class Filter:
    def process(self, data):
        raise NotImplementedError("Subclasses must implement the process method.")


class UppercaseFilter(Filter):
    def process(self, data):
        return data.upper()


class ReverseFilter(Filter):
    def process(self, data):
        return data[::-1]


class Pipe:
    def __init__(self):
        self.filters = []

    def add_filter(self, filter):
        self.filters.append(filter)

    def process_data(self, data):
        for filter in self.filters:
            data = filter.process(data)
        return data
