from .models import CommunityAsset
from rest_framework import serializers

class CommunityAssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommunityAsset
        fields = ('url', 'name')
