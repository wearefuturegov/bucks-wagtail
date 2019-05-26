from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from export_csv.views import ExportCSV
from .models import CommunityAsset

@method_decorator(login_required, name='dispatch')
class CommunityAssetCSV(ExportCSV):
    model = CommunityAsset
    field_names = [
        'name', 
        'parent_organisation', 
        'description', 
        'price', 
        
        'category',

        'venue',
        'area',
        'postcode',

        'frequency',
        'daytime',

        'contact_name',
        'url',
        'phone',
        'email',

        'review_notes',
        'assigned_to',
        'review_number',
        'review_status',

        'last_updated',
        'review_date',

        'laf_areas',
        'ccg_locality',

        'vol_dbs_check',
        'safeguarding',
        'health_safety',
        'insurance',
        
        'clo_notes'
    ]