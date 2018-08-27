from django.test import TestCase

from followup.models import ContactMethod, NoAptReason, NoShowReason, ContactResult
from django.contrib.auth.models import User
from pttrack.models import (
    Gender, Patient, Provider, ProviderType,
    ReferralType, ReferralLocation, Note, ContactMethod, CompletableMixin,
    CompleteableManager)
#from pttrack.test_views import build_provider
import datetime
from . import forms
from . import models
from . import urls

# Create your tests here.
class TestPatientContactForm(TestCase):
    '''
    Tests the beahvior of the PatientContactForm which has a lot of
    complicated logic around valid form submission
    '''

    def setUp(self):
        ''' Provides the same context in all the tests '''

        self.contact_method = ContactMethod.objects.create(
            name="Carrier Pidgeon")
        self.pt = Patient.objects.create(
            first_name="Juggie",
            last_name="Brodeltein",
            middle_name="Bayer",
            phone='+49 178 236 5288',
            gender=Gender.objects.create(long_name="Male",
                                         short_name="M"),
            address='Schulstrasse 9',
            city='Munich',
            state='BA',
            zip_code='63108',
            pcp_preferred_zip='63018',
            date_of_birth=datetime.date(1990, 01, 01),
            patient_comfortable_with_english=False,
            preferred_contact_method=self.contact_method,
        )
        # Create provider because referral requires a provider
        #build_provider()
        casemanager = ProviderType.objects.create(
            long_name='Case Manager', short_name='CM',
            signs_charts=False, staff_view=True)

        user = User.objects.create_user(
            "username",
            "a@wustl.edu", "password")
        g = Gender.objects.first()
        prov = Provider.objects.create(
            first_name="Tommy", middle_name="Lee", last_name="Jones",
            phone="425-243-9115", gender=g, associated_user=user)

        reftype = ReferralType.objects.create(
            name="Specialty", is_fqhc=False)
        refloc = ReferralLocation.objects.create(
            name='COH', address='Euclid Ave.')
        refloc.care_availiable.add(reftype)

        # Note location might not work
        self.referral = models.Referral.objects.create(
            # location=[ReferralLocation.objects.first()],
            comments="Needs his back checked",
            status='P',
            kind=reftype,
            author=Provider.objects.first(),
            author_type=ProviderType.objects.first(),
            patient=self.pt
        )
        self.referral.location.add(refloc)

        # self.location = self.referral.location.create(name="COH", address="Euclid Ave")
        # self.location.save()

        self.followupRequest = models.FollowupRequest.objects.create(
            referral=self.referral,
            contact_instructions="Call him",
            due_date=datetime.date(2018, 9, 01),
            author=Provider.objects.first(),
            author_type=ProviderType.objects.first(),
            patient=self.pt
        )

        self.successful_res = ContactResult.objects.create(
            name="Got him", patient_reached=True)
        self.unsuccessful_res = ContactResult.objects.create(
            name="Disaster", patient_reached=False)
        # Need to update referral location
        self.referral_location = ReferralLocation.objects.create(
            name="Franklin's Back Adjustment",
            address="1435 Sillypants Drive")
        self.noapt_reason = NoAptReason.objects.create(
            name="better things to do")
        self.noshow_reason = NoShowReason.objects.create(
            name="Hella busy.")

    def build_form(self, contact_successful, has_appointment, apt_location,
                   noapt_reason, pt_showed, noshow_reason):
        """Utility method used to construct a PatientContactForm to suit the
        needs of the testing subroutines based upon what is provided and not
        provided.
        """
        contact_resolution = (self.successful_res if contact_successful
                              else self.unsuccessful_res)

        form_data = {
            'contact_method': self.contact_method,
            'contact_status': contact_resolution,
            'patient': self.pt,
            'referral': self.referral,
            'followupRequest': self.followupRequest
        }

        form_data['has_appointment'] = has_appointment
        form_data['pt_showed'] = pt_showed

        if apt_location:
            form_data['appointment_location'] = [ReferralLocation.objects.first().pk]

        if noapt_reason:
            form_data['no_apt_reason'] = self.noapt_reason

        if noshow_reason:
            form_data['no_show_reason'] = self.noshow_reason

        return forms.PatientContactForm(data=form_data)

    def test_has_appointment_and_pt_showed(self):
        # correct: pt didn't show, noshow reason is supplied
        form = self.build_form(
            contact_successful=True,
            has_appointment="Yes",
            apt_location=True,
            noapt_reason=False,
            noshow_reason=False,
            pt_showed="Yes")

        print(ReferralLocation.objects.all())

        print(form.errors)
        # Might want to assert a specific error
        self.assertEqual(len(form.errors), 0)

        # incorrect - no show reason is supplied

        # incorrect - no appointment reason is supplied

        # incorrect - no appointment location is selected

    def test_has_appointment_and_pt_no_show(self):
        """Verify that a provider is selected and a reason is provided for
        the no show
        """
        form = self.build_form(
            contact_successful=True,
            has_appointment="Yes",
            apt_location=True,
            noapt_reason=False,
            noshow_reason=True,
            pt_showed="No")

        self.assertEqual(len(form.errors), 0)

        # incorrect - no show reason is not supplied

        # incorrect - no appointment reason is supplied

        # incorrect - appointment location is not selected

        # Remember to add Not Yets

def test_no_appointment(self):
    # verify that there are no errors when a patient has not made an appointment
    form = self.build_form(
        contact_successful=True,
        has_appointment="No",
        apt_location=False,
        noapt_reason=False,
        noshow_reason=False,
        pt_showed="No")

    self.assertEqual(len(form.errors), 0)