import datetime
import string

import factory
import factory.django
import factory.fuzzy
import core.models


class ContractFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = core.models.Contract

    name = factory.Faker('name', locale='de_DE')
    email = factory.Faker('ascii_email', locale='de_DE')
    address = factory.Faker('address', locale='de_DE')
    contract_number = factory.fuzzy.FuzzyText(length=8, chars=string.digits)
    is_active = True


class MeterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = core.models.Meter

    contract = factory.SubFactory(ContractFactory)
    meter_number = factory.fuzzy.FuzzyText(length=10, chars=string.digits)
    size = factory.fuzzy.FuzzyInteger(4, 16)


class DrainageAreaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = core.models.DrainageArea

    contract = factory.SubFactory(ContractFactory)
    size = factory.fuzzy.FuzzyFloat(1, 1000)


class ContractHistoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = core.models.ContractHistory

    contract = factory.SubFactory(ContractFactory, is_active=False)
    meter = factory.SubFactory(MeterFactory)
    begin = factory.fuzzy.FuzzyDate(
        datetime.date(2000, 1, 1), datetime.date.today())
    end = factory.Maybe(
        'contract.is_active',
        yes_declaration=None,
        no_declaration=factory.fuzzy.FuzzyDate(
            datetime.date(2000, 1, 1), datetime.date.today()),
        )
