import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import File
from .serializers import FileSerializer
from .tasks import uploading_handler


class FileUpload(APIView):
    def post(self, request):
        '''APIView for post-requests to endpoint /upload/'''
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            logging.info(f"File saved with id {instance.id}")
            uploading_handler.delay(instance.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            logging.error(f"Invalid data received: {serializer.errors}")
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class FileList(APIView):
    def get(self, request):
        '''APIView for get-requests to endpoint /files/'''
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)
