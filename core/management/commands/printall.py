from django.core.management.base import BaseCommand
from core import models


class Command(BaseCommand):
    help = 'Print all data (for debugging)'

    def handle(self, *args, **options):
        print_all()


def print_all():
    for model in (
            models.Contract,
            models.Meter,
            models.DrainageArea,
            models.ContractHistory,
            ):
        print(model.objects.values())
