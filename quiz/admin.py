from django.contrib import admin

from .models import Choice, Question, Register

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Register)
