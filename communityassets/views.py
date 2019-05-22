from .models import CommunityAsset
from rest_framework import viewsets
from .serializers import CommunityAssetSerializer


class CommunityAssetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CommunityAsset.objects.all()
    serializer_class = CommunityAssetSerializer