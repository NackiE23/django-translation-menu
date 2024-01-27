from modeltranslation.translator import translator, TranslationOptions
from .models import MenuItem


class MenuItemTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


translator.register(MenuItem, MenuItemTranslationOptions)
