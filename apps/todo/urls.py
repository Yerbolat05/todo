from django.urls import path, re_path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',    views.index,    name='page_main'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)