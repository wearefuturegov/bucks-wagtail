from django.conf.urls import url, include
from .models import CommunityAsset
from rest_framework import routers, serializers, viewsets
from django_filters import rest_framework as filters

# Serializers define the API representation.
class CommunityAssetSerializer(serializers.HyperlinkedModelSerializer):
    
    category = serializers.CharField()
    keywords = serializers.StringRelatedField(many=True)
    age_groups = serializers.StringRelatedField(many=True)
    suitability = serializers.StringRelatedField(many=True)
    accessibility = serializers.StringRelatedField(many=True)
    days = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = CommunityAsset
        fields = (
            'id',
            'name', 
            'parent_organisation', 
            'description', 
            'price', 
            
            'category',
            'keywords',
            'age_groups',
            'suitability',
            'accessibility',

            'days',
            'frequency',
            'daytime',

            'venue',
            'area',
            'postcode',

            'contact_name',
            'url',
            'phone',
            'email',
        )



class CommunityAssetFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = CommunityAsset
        fields = ('name', 'category')

class CommunityAssetViewSet(viewsets.ModelViewSet):
    queryset = CommunityAsset.objects.all()
    serializer_class = CommunityAssetSerializer
    filterset_class = CommunityAssetFilter