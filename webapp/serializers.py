from rest_framework import serializers
from . models import speedtest_result

class resultSerializer(serializers.ModelSerializer):

    class Meta:
        model = speedtest_result
        fields = ("date","download", "upload")
        fields = "__all__"