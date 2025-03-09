from django.views.generic.edit. import (
    CreateView,
    DeleteView,
    UpdateView
)
from django.views.generic.list import ListView

from .mixins import OwnerCourseMixin, OwnerCourseEditMixin


class ManageCourseListView(OwnerCourseMixin, ListView):
    template_name = 'courses/mange/course/list.html'


class CourseCreateView(OwnerCourseEditMixin, CreateView):
    pass


class CourseUpdateView(OwnerCourseEditMixin):
    pass


class CourseDeleteView(OwnerCourseMixin, DeleteView):
    template_name = 'courses/mange/course/delete.html'

