class PresentationLayer:
    def __init__(self, application_layer):
        self.application_layer = application_layer

    def process_request(self, request):
        # Perform any necessary data validation or transformation
        transformed_request = request

        # Pass the transformed request to the application layer
        response = self.application_layer.process_request(transformed_request)

        # Perform any necessary data formatting or transformation on the response
        transformed_response = response

        # Return the transformed response
        return transformed_response
