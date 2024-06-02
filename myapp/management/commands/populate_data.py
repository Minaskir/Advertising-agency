# myapp/management/commands/populate_data.py

from django.core.management.base import BaseCommand
from myapp.populate_data import populate

class Command(BaseCommand):
    help = 'Заполняет базу данных начальными данными'

    def handle(self, *args, **kwargs):
        populate()
