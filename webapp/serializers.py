from rest_framework import serializers
from . models import speedtest_result

class resultSerializer(serializers.ModelSerializer):

    class Meta:
        model = speedtest_result
        fields = ("logfile","token","timestamp")
        fields = "__all__"