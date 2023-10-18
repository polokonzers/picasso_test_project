from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import File
from .serializers import FileSerializer


class FileUpload(APIView):
    def post(self, request):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileList(APIView):
    def get(self, request):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)
