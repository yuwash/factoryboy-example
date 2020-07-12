from django.core.management.base import BaseCommand
from core import factories


class Command(BaseCommand):
    help = 'Populate fake data'

    def add_arguments(self, parser):
        parser.add_argument('--huge', action='store_true')

    def handle(self, *args, **options):
        populate(huge=options.get('huge'))


def populate(huge=False):
    model_objs = {}
    contract_variants = [
        {
            'key': 'default',
        },
        {
            'key': 'inactive',
            'data': {
                'is_active': False,
            }
        },
        {
            'data': {
                'name': 'Víēlé Ǘmłåūţè',
            },
        },
        {
            'data': {
                'address':
                '11223344\nPackstation 987\n12345 Kein-Richtiges-Haus',
            },
        },
    ]
    model_objs['Contract'] = populate_model(
        factories.ContractFactory,
        variants=contract_variants,
        model_objs=model_objs,
        huge_size=100 if huge else None,
    )

    meter_variants = [
        {
            'key': 'default',
        },
    ]
    model_objs['Meter'] = populate_model(
        factories.MeterFactory,
        variants=meter_variants,
        model_objs=model_objs,
        huge_size=50 if huge else None,
    )

    drainage_area_variants = [
        {
            'key': 'default',
        },
    ]
    model_objs['DrainageArea'] = populate_model(
        factories.DrainageAreaFactory,
        variants=drainage_area_variants,
        model_objs=model_objs,
        huge_size=60 if huge else None,
    )

    contract_history_variants = [
        {
            'key': 'default',
        },
        {
            'key_data': {
                'contract': 'Contract.inactive',
            },
        },
    ]
    model_objs['ContractHistory'] = populate_model(
        factories.ContractHistoryFactory,
        variants=contract_history_variants,
        model_objs=model_objs,
        huge_size=200 if huge else None,
    )


def lookup_model_objs(model_objs, model_key):
    model, key = model_key.split('.', maxsplit=1)
    return model_objs.get(model).get(key)


def populate_model(factory, variants, model_objs, huge_size=None):
    objs = {}
    for variant_data in variants:
        init_data = variant_data.get('data', {})
        if 'key_data' in variant_data:
            init_data.update(
                (field, lookup_model_objs(model_objs, model_key))
                for field, model_key in variant_data['key_data'].items())
        obj = factory(**init_data)
        if 'key' in variant_data:
            objs[variant_data['key']] = obj
    if huge_size:
        factory.create_batch(huge_size)
    return objs
