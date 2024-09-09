from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer

class JobViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(employer=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, employer_id):
        jobs = Job.objects.filter(employer_id=employer_id)
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

class ApplicationViewSet(viewsets.ViewSet):
    def list(self, request, job_id):
        applications = Application.objects.filter(job_id=job_id)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)

    def partial_update(self, request, application_id):
        try:
            application = Application.objects.get(id=application_id)
        except Application.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ApplicationSerializer(application, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
