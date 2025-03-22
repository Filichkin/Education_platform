from django.db.models import Count
from rest_framework import generics

from courses.api.serializers import SubjectSerializer
from courses.models import Subject


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.annotate(
        total_courses=Count('courses')
        )
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.annotate(
        total_courses=Count('courses')
        )
    serializer_class = SubjectSerializer
