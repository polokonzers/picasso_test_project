from django.urls import path
from .views import FileUpload, FileList

app_name = 'api'
urlpatterns = [
    path('upload/', FileUpload.as_view(), name='upload'),
    path('files/', FileList.as_view(), name='files'),
]
