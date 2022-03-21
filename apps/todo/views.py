from multiprocessing import context
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, QueryDict
from django.db.models import QuerySet
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import (
    authenticate as dj_authenticate,
    login as dj_login,
    logout as dj_logout,
)

def index(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        'index.html',
    )
    