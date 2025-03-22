from django.db.models import Count
from rest_framework import generics

from courses.api.pagination import StandardPagination
from courses.api.serializers import SubjectSerializer
from courses.models import Subject


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.annotate(
        total_courses=Count('courses')
        )
    serializer_class = SubjectSerializer
    pagination_class = StandardPagination


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.annotate(
        total_courses=Count('courses')
        )
    serializer_class = SubjectSerializer
