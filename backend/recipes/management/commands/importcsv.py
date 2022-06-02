# import csv
# from importlib.resources import path
# from django.core.management import BaseCommand
# from recipes.models import Ingredient


# class Command(BaseCommand):
#     help = 'Load ingredients csv into DB'

#     def add_arguments(self, parser):
#         parser.add_argument('--path', type=str)
#     print(path)
#     def handle(self, *args, **kwargs):
#         path = kwargs['path']
#         with open(path, 'rt') as f:
#             reader = csv.reader(f, delimiter=',')
#             for row in reader:
#                 Ingredient.objects.create(
#                     name=row[0],
#                     measurement_unit=row[1]
#                 )

# #python manage.py importcsv --path fixtures/ingredients.csv



import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from recipes.models import Ingredient


DATA_ROOT = os.path.join(settings.BASE_DIR, 'data')


class Command(BaseCommand):
    """Добавляем ингредиенты из файла CSV"""
    help = 'loading ingredients from data in json or csv'

    def add_arguments(self, parser):
        parser.add_argument('filename', default='ingredients.csv', nargs='?',
                            type=str)

    def handle(self, *args, **options):
        try:
            with open(os.path.join(DATA_ROOT, options['filename']), 'r',
                      encoding='utf-8') as f:
                data = csv.reader(f)
                for row in data:
                    name, measure = row
                    Ingredient.objects.get_or_create(
                        name=name,
                        measurement_unit=measure
                    )
        except FileNotFoundError:
            raise CommandError('Добавьте файл ingredients в директорию data')