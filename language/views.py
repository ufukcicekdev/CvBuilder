from django.shortcuts import redirect
from django.utils import translation
from cv_builder.settings import *

def set_language(request):
    language_code = request.GET.get('language', 'en')
    translation.activate(language_code)
    request.session[LANGUAGE_COOKIE_NAME] = language_code
    return redirect(request.GET.get('next', '/'))