from rest_framework import serializers


class DeviceSerializer(serializers.Serializer):
    id = serializers.CharField()
    deviceModel = serializers.CharField()
    name = serializers.CharField()
    note = serializers.CharField()
    serial = serializers.CharField()

    class Meta():
        fields = ('id', 'deviceModel', 'name', 'note', 'serial')


class DeviceDeserializer(serializers.Serializer):
    id = serializers.SerializerMethodField()
    deviceModel = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    note = serializers.SerializerMethodField()
    serial = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj['id']['S']

    def get_deviceModel(self, obj):
        return obj['deviceModel']['S']        

    def get_name(self, obj):
        return obj['name']['S']

    def get_note(self, obj):
        return obj['note']['S']        

    def get_serial(self, obj):
        return obj['serial']['S']       

    class Meta():
        fields = ('id', 'deviceModel', 'name', 'note', 'serial')