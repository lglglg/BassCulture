from rest_framework import serializers

class SearchSerializer(serializers.Serializer):
    
    class Meta:
        fields = ('url', 'source_id')

    url = serializers.SerializerMethodField("record_url")

    def record_url(self, obj, *args, **kwargs):
        print(obj)
        return 'Luca'

#    def to_representation(self, *args, **kwargs):
#        print(args)
#        print(kwargs)
