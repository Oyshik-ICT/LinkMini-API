import logging

import shortuuid
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from .models import UrlMapping
from .serializers import UrlMappingSerializer

logger = logging.getLogger(__name__)


class CreateUrlAPIView(APIView):
    """
    API view to create a short URL from a given long URL.
    """

    serializer_class = UrlMappingSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    prefix_url = "myurl/"

    def generate_short_url(self):
        """
        Generates an 8-character unique short URL.
        """
        return shortuuid.uuid()[:8]

    def post(self, request):
        """
        Handles the creation of a short URL.
        - Generates a unique short URL.
        - Stores it in the database.
        - Returns the short URL in the response.
        """
        try:

            while True:
                short_url = self.prefix_url + self.generate_short_url()

                if not UrlMapping.objects.filter(short_url=short_url).exists():
                    break

            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save(short_url=short_url)
                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logger.error(f"Unexpected error while creating url: {str(e)}")
            return Response(
                {"error": "An unexpected error occurred"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class RetriveUpdateDeleteUrlAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a short URL entry.
    """

    serializer_class = UrlMappingSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    queryset = UrlMapping.objects.all()
    lookup_field = "short_url"
    lookup_url_kwarg = "short_url"
