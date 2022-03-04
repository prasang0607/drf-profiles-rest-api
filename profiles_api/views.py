from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Test API view """

    def get(self, request, format=None):
        """ Return a list of APIView features """
        an_apiview = [
            'Uses HTTP methods as functions (get, post, put, patch, delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over your application logic'
        ]

        response = {
            'message': 'Hello world',
            'an_apiview': an_apiview
        }

        return Response(response, status=status.HTTP_200_OK)
