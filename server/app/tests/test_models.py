from django.test import TestCase
from .models import Employer, Job, Application

class ApplicationModelTests(TestCase):
    def setUp(self):
        self.employer = Employer.objects.create(name='Tech Corp', email='hr@techcorp.com')
        self.job = Job.objects.create(employer=self.employer, title='Software Engineer', description='Develop software.', location='Remote')

    def test_application_creation(self):
        application = Application.objects.create(job=self.job, applicant_name='Jane Smith', applicant_email='jane@example.com')
        self.assertEqual(application.job, self.job)
        self.assertEqual(application.applicant_name, 'Jane Smith')
        self.assertEqual(application.status, 'submitted')
