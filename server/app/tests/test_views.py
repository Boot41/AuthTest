from rest_framework.test import APITestCase
from rest_framework import status
from .models import Employer, Job
from django.urls import reverse

class JobViewSetTests(APITestCase):
    def setUp(self):
        self.employer = Employer.objects.create(name='Employer Name', email='employer@example.com')

    def test_create_job(self):
        url = reverse('job-list')
        data = {
            'title': 'Software Engineer',
            'description': 'Job description here',
            'location': 'Remote',
        }
        self.client.force_authenticate(user=self.employer)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Job.objects.count(), 1)
        self.assertEqual(Job.objects.get().title, 'Software Engineer')

    def test_list_jobs(self):
        Job.objects.create(employer=self.employer, title='Software Engineer', description='Job description here', location='Remote')
        url = reverse('job-list', args=[self.employer.id])
        self.client.force_authenticate(user=self.employer)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
