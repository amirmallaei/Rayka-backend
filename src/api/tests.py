from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

# Create your tests here.
baseurl = 'http://127.0.0.1:8083'

class AddDevice(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_add_device(self):
        """test if adding new device will work"""
        payload = {
            'id': 'test',
            'deviceModel': 'testDevice',
            'name': 'testname',
            'note': 'testNote',
            'serial': 'testSerial',
        }
        res = self.client.post('{}/api/devices/'.format(baseurl), payload) 
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)

    def test_add_device_fails(self):
        """test if adding new device will work"""
        payload = {
            'id': 'test',
            'deviceModel': 'testDevice',
            'serial': 'testSerial',
        }
        res = self.client.post('{}/api/devices/'.format(baseurl), payload) 
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)


class GetDevice(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_device_exists(self):
        """test if retrieving works"""
        payload = {
            'id': 'test',
            'deviceModel': 'testDevice',
            'name': 'testname',
            'note': 'testNote',
            'serial': 'testSerial',
        }
        self.client.post('{}/api/devices/'.format(baseurl), payload)         
        res = self.client.get('{}/api/devices/{}/'.format(baseurl, payload['id']))
        self.assertEqual(res.status_code,status.HTTP_200_OK)
    
    def test_get_device_not_exists(self):
        """test id Device does not exist works properly"""
        res = self.client.get('{}/api/devices/{}/'.format(baseurl, "TestTest"))
        self.assertEqual(res.status_code,status.HTTP_404_NOT_FOUND)