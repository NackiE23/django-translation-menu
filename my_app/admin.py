from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from my_app.models import MenuItem


admin.site.register(MenuItem, TranslationAdmin)
