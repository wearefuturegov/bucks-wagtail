from django.conf.urls import url, include
from .models import CommunityAsset
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class CommunityAssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommunityAsset
        fields = (
            'name', 
            'parent_organisation', 
            'description', 
            'price', 
            
            # 'category',

            'venue',
            'area',
            'postcode',

            'frequency',
            'daytime',

            'contact_name',
            'url',
            'phone',
            'email',
        )

# ViewSets define the view behavior.
class CommunityAssetViewSet(viewsets.ModelViewSet):
    queryset = CommunityAsset.objects.all()
    serializer_class = CommunityAssetSerializer

