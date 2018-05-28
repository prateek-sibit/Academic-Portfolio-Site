from django.contrib import admin
from basic_app.models import Publication,About,Student,Project,Course,Talk

# Register your models here.
admin.site.register(Publication)
admin.site.register(About)
admin.site.register(Student)
admin.site.register(Project)
admin.site.register(Course)
admin.site.register(Talk)
