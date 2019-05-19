from wagtail.api.v2.router import WagtailAPIRouter

from wagtail.api.v2.endpoints import PagesAPIEndpoint
from wagtail.images.api.v2.endpoints import ImagesAPIEndpoint
from wagtail.documents.api.v2.endpoints import DocumentsAPIEndpoint
from wagtail.api.v2.endpoints import BaseAPIEndpoint

from communityassets.models import CommunityAsset

class CommunityAssetsAPIEndpoint(BaseAPIEndpoint):
    body_fields = BaseAPIEndpoint.body_fields + [
        'title', 
        'description'
    ]
    listing_default_fields = BaseAPIEndpoint.listing_default_fields + [
        'title', 
        'description'
    ]
    model = CommunityAsset

api_router = WagtailAPIRouter('wagtailapi')

api_router.register_endpoint('pages', PagesAPIEndpoint)
api_router.register_endpoint('images', ImagesAPIEndpoint)
api_router.register_endpoint('documents', DocumentsAPIEndpoint)
api_router.register_endpoint('community-assets', CommunityAssetsAPIEndpoint)