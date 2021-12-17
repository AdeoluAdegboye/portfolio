from django.urls import include, path
from .views import Portfolio

urlpatterns = [
    path('', Portfolio.as_view(), name='home_page')
]