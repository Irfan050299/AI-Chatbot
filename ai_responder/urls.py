from django.urls import path
from .views import QueryResponseView
from ai_responder import views
from django.contrib import admin
urlpatterns = [
    path('query/', QueryResponseView.as_view(), name='query-response'),
]
