from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Job, Application

class ApplicationViewSetTests(APITestCase):
    def setUp(self):
        self.job = Job.objects.create(title='Software Engineer', description='Develop software.', location='Remote')

    def test_list_applications(self):
        response = self.client.get(reverse('application-list', kwargs={'job_id': self.job.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)  # No applications yet

    def test_update_application_status(self):
        application = Application.objects.create(job=self.job, applicant_name='John Doe', applicant_email='john@example.com')
        response = self.client.patch(reverse('application-update', kwargs={'application_id': application.id}), {'status': 'shortlisted'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        application.refresh_from_db()
        self.assertEqual(application.status, 'shortlisted')

    def test_update_nonexistent_application(self):
        response = self.client.patch(reverse('application-update', kwargs={'application_id': 999}), {'status': 'shortlisted'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
