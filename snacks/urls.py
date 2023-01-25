from .views import index
from django.urls import path


urlpatterns = [
    path('snacks', index, name='snacks')
    path('detail', index, name='detail')