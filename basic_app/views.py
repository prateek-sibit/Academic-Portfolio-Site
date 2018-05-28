from django.views.generic import View,TemplateView,DetailView,ListView
from basic_app.models import Publication,About,Student,Project,Course,Talk
from basic_app.forms import ContactForm
from django.shortcuts import render

# Create your views here.

class IndexView(ListView):
    context_object_name = 'publications'
    model = Publication
    template_name = 'basic_app/index.html'

    def get_queryset(self):
        return Publication.objects.filter(published=True).order_by('-publish_year')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all().order_by('-end_year')[:3]
        context['courses'] = Course.objects.filter(active=True).order_by('-end_year')
        return context

class AboutView(ListView):
    context_object_name = 'about_me'
    model = About

class PublicationView(ListView):
        context_object_name = 'publications'
        model = Publication

        def get_context_data(self, *args, **kwargs):
            context = super(PublicationView, self).get_context_data(*args, **kwargs)
            # Create object list with unique publication dates
            context['unique_publish'] = Publication.objects.values_list('publish_year', flat=True).distinct().order_by('-publish_year')
            return context

        def get_queryset(self):
            return Publication.objects.filter(published=True).order_by('-publish_year')

class StudentView(ListView):
    context_object_name = 'students'
    model = Student
    template_name = 'basic_app/student.html'

class ProjectView(ListView):
    context_object_name = 'projects'
    model = Project
    template_name = 'basic_app/project.html'

    def get_queryset(self):
        return Project.objects.filter().order_by('-end_year')

class CourseView(ListView):
    context_object_name = 'courses'
    model = Course
    template_name = 'basic_app/courses.html'

    def get_queryset(self):
        return Course.objects.all().order_by('-end_year')

class TalkView(ListView):
    context_object_name = 'talks'
    model = Talk
    template_name = 'basic_app/talk.html'

    def get_queryset(self):
        return Talk.objects.all().order_by('-end_date')

class ContactView(TemplateView):
    template_name = 'basic_app/contact.html'
