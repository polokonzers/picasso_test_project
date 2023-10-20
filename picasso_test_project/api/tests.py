"""
Can't test post-requests to endpoint /upload/ due to
running redis and celery in docker-compose
"""

from rest_framework import status
from rest_framework.test import APITestCase


class EndpointTests(APITestCase):
    def test_get_files_endpoint(self):
        '''Ensure availability of endpoint /files/'''
        response = self.client.get('/files/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
