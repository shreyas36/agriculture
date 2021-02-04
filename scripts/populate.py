from crop.models import Rice
import django
import csv
import os


def run():
    tmp_data = open('../rice_crops.csv')
    reader = csv.reader(tmp_data)
    Rice.objects.all().delete()

    crops = [
        Rice(
            state=row[2],
            year=int(row[3]),
            season=row[4],
            area=float(row[6]),
            production=float(row[7]),
            rainfall=float(row[8])
        )
        for row in reader
    ]
    Rice.objects.bulk_create(crops)


'''
if __name__ == "__main__":
    print("populating")
    os.environ['DJANGO_SETTINGS_MODULE'] = 'agriculture.settings'
    django.setup()
    populate()
    print("done")'''
