from rest_framework import serializers
from bassculture.models.printer import Printer


class PrinterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Printer
