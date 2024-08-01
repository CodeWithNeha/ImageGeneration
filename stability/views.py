from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from utils.constants import CONSTANTS
from stability.services import StabilityAiService
from .models import GeneratedImage
from .serializers import GeneratedImageSerializer


class ImageGeneration(ModelViewSet):
    queryset = GeneratedImage.objects.all()
    serializer_class = GeneratedImageSerializer
    http_method_names = ["get", "post"]

    def create(self, request, *args, **kwargs):
        try:
            prompt = request.data.get("prompt")
            data = {
                "generator": "image",
                "prompt": prompt,
            }
            stability_ai_service = StabilityAiService()
            stability_ai_service.generate(data=data)
            return Response(
                {
                    CONSTANTS.MESSAGE: "Image generated successfully.",
                },
                status=status.HTTP_200_OK,
            )
        except Exception as error:
            return Response(
                {
                    CONSTANTS.MESSAGE: str(error),
                    CONSTANTS.STATUS: status.HTTP_400_BAD_REQUEST,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def list(self, request, *args, **kwargs):
        try:
            all = self.get_queryset()
            serialized = self.serializer_class(all, many=True).data
            return Response(
                {CONSTANTS.DATA: serialized},
                status=status.HTTP_200_OK,
            )
        except Exception as error:
            return Response(
                {
                    CONSTANTS.MESSAGE: str(error),
                    CONSTANTS.STATUS: status.HTTP_400_BAD_REQUEST,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
