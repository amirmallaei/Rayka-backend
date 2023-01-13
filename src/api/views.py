from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from api.serializers import DeviceSerializer, DeviceDeserializer
from RaykaDB import put_device, get_device

# Create your views here.
class DeviceCreateAPIView(APIView):
    serializer_class = DeviceSerializer

    def post(self, request, format=None):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            put_device(
                serializer.validated_data['id'],
                serializer.validated_data['deviceModel'],
                serializer.validated_data['name'],
                serializer.validated_data['note'],
                serializer.validated_data['deviceModel']
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DeviceRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = DeviceDeserializer

    def get_object(self):
        obj = get_device(self.kwargs['order_id'])
        print(obj)
        if obj is not None:
            return obj
        return Response("Not Found", status=status.HTTP_404_NOT_FOUND)