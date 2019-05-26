from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify
from communityassets.models import CommunityAsset, Categories, ReviewStatus, LAFAreas, CCGLocalities, Accessibilities, Days, Suitabilities, AgeGroups, LegacyCategories, Keywords
import csv

def str_to_bool(s):
    if s == 'TRUE':
         return True
    elif s == 'FALSE':
         return False
    else:
         raise ValueError

class Command(BaseCommand):

    # Accept a filename from the root as an argument
    def add_arguments(self, parser):
        parser.add_argument('file')

    # Handle command
    def handle(self, *args, **options):

        # Delete all records
        CommunityAsset.objects.all().delete()

        with open (options['file']) as file: 
            reader = csv.DictReader(file)
            for row in reader:

                # print("importing ", row["name"], "...")

                review_status, x = ReviewStatus.objects.get_or_create(name=row["review_status"])
                laf_area, x = LAFAreas.objects.get_or_create(name=row["laf_area"])
                ccg_locality, x = CCGLocalities.objects.get_or_create(name=row["ccg_locality"])

                new_asset = CommunityAsset(
                    name=row["name"],
                    parent_organisation=row["parent_organisation"],
                    description=row["description"],
                    price=row["price"],

                    venue=row["venue"],
                    area=row["area"],
                    postcode=row["postcode"],

                    frequency=row["frequency"],
                    daytime=str_to_bool(row["daytime"]),

                    contact_name=row["contact_name"],
                    email=row["email"],
                    phone=row["phone"],
                    url=row["url"],

                    review_notes=row["review_notes"],
                    assigned_to=row["assigned_to"],
                    review_number=row["review_number"],
                    review_status_id=review_status.id,

                    last_updated=row["last_updated"],
                    review_date=row["review_date"],

                    laf_areas_id=laf_area.id,
                    ccg_locality_id=ccg_locality.id,

                    vol_dbs_check=row["vol_dbs_check"],
                    safeguarding=row["safeguarding"],
                    health_safety=row["health_safety"],
                    insurance=row["insurance"],

                    clo_notes=row["clo_notes"],
                )
                new_asset.save()

                if(row["category"] != ""):
                    object, x = Categories.objects.get_or_create(name=row["category"])
                    new_asset.category_id = object

                keywords_array = list(filter(None, row["keywords"].split(";")))
                for keyword in keywords_array:
                    new_asset.keywords.add(keyword)

                accessibility_array = list(filter(None, row["accessibility"].split(";")))
                for value in accessibility_array:
                    object, x = Accessibilities.objects.get_or_create(name=value)
                    new_asset.accessibility.add(object.id)

                days_array = list(filter(None, row["days"].split(";")))
                for value in days_array:
                    object, x = Days.objects.get_or_create(name=value)
                    new_asset.days.add(object.id)

                age_groups_array = list(filter(None, row["age_groups"].split(";")))
                for value in age_groups_array:
                    object, x = AgeGroups.objects.get_or_create(name=value)
                    new_asset.age_groups.add(object.id)

                suitabilities_array = list(filter(None, row["suitability"].split(";")))
                for value in suitabilities_array:
                    object, x = Suitabilities.objects.get_or_create(name=value)
                    new_asset.suitability.add(object.id)

                legacy_categories_array = list(filter(None, row["legacy_categories"].split(";")))
                for value in legacy_categories_array:
                    object, x = LegacyCategories.objects.get_or_create(name=value)
                    new_asset.legacy_categories.add(object.id)

                new_asset.save()

            print("Import completed successfully")
