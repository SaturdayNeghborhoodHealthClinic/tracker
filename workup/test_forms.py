import decimal

from django.test import TestCase

from .models import DiagnosisType
from .forms import WorkupForm

from .tests import wu_dict

class TestUnitChangeForms(TestCase):

    def setUp(self):
        DiagnosisType.objects.create(name='Cardiovascular')

        wu_data = wu_dict()
        wu_data['diagnosis_categories'] = [DiagnosisType.objects.first().pk]
        wu_data['got_imaging_voucher'] = False
        wu_data['got_voucher'] = False

        wu_data['temperature_units'] = 'C'
        wu_data['height_units'] = 'in'
        wu_data['weight_units'] = 'lbs'

        self.wu_data = wu_data

    def test_note_temp_conversion(self):

        wu_data = self.wu_data

        # temperatures with centigrade should be the same
        wu_data['temperature_units'] = 'C'
        wu_data['t'] = 37

        form = WorkupForm(data=wu_data)

        self.assertTrue(form.is_valid())
        self.assertEquals(
            form.cleaned_data['t'],
            wu_data['t'])

        # temperatures given centigrade should be converted
        wu_data['temperature_units'] = 'F'
        wu_data['t'] = 98
        form = WorkupForm(data=wu_data)

        self.assertTrue(form.is_valid())
        self.assertEquals(
            round((wu_data['t'] - 32) * decimal.Decimal(5 / 9.0)),
            round(decimal.Decimal(form.cleaned_data['t'])))

    def test_note_height_conversion(self):

        wu_data = self.wu_data

        # heights with cm should be the same
        wu_data['height_units'] = 'cm'
        wu_data['height'] = 180

        form = WorkupForm(data=wu_data)

        self.assertTrue(form.is_valid())
        self.assertEquals(
            form.cleaned_data['height'],
            wu_data['height'])

        # heights given inches should be converted
        wu_data['height_units'] = 'in'
        wu_data['height'] = 71

        form = WorkupForm(data=wu_data)

        self.assertTrue(form.is_valid())
        self.assertEquals(
            form.cleaned_data['height'],
            wu_data['height'] * decimal.Decimal(2.54))

    def test_note_weight_conversion(self):

        wu_data = self.wu_data

        # weights with kilograms should be the same
        wu_data['weight_units'] = 'kg'
        wu_data['weight'] = 81

        form = WorkupForm(data=wu_data)

        self.assertTrue(form.is_valid())
        self.assertEquals(
            form.cleaned_data['weight'],
            wu_data['weight'])

        # weights given lbs should be converted
        wu_data['weight_units'] = 'lbs'

        form = WorkupForm(data=wu_data)

        self.assertTrue(form.is_valid())
        self.assertEquals(
            round(form.cleaned_data['weight']),
            round(wu_data['weight'] / decimal.Decimal(2.2)))