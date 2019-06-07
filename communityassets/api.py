from django.conf.urls import url, include
from .models import CommunityAsset
from rest_framework import routers, serializers, viewsets
from django_filters import rest_framework as filters

from rest_framework.filters import SearchFilter, OrderingFilter

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

    class Meta:
        model = CommunityAsset
        fields = (
            'category__name',
            'days__name',
            'accessibility__name',
            'suitability__name',
            'age_groups__name'
        )

class CommunityAssetViewSet(viewsets.ModelViewSet):
    queryset = CommunityAsset.objects.all()
    serializer_class = CommunityAssetSerializer
    filterset_class = CommunityAssetFilter

    filter_backends = (SearchFilter, filters.DjangoFilterBackend)
    search_fields = (
        'name', 
        'parent_organisation',
        'description',
        'keywords__name',
        'venue',
        'url'
    )