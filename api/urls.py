from unicodedata import name
from django.urls import path
from .views import BookAPIView

urlpatterns = [
    path('', BookAPIView.as_view())
]