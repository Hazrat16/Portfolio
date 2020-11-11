# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.contrib import admin
from .models import Education
from .models import Experience
from .models import Awards
from .models import Projects
from .models import Blog

# Register your models here.
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Awards)
admin.site.register(Projects)
admin.site.register(Blog)
