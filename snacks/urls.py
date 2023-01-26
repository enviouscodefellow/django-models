# from .views import index
from django.urls import path

from .views import my_view
from .views import (
    AboutPageView,
    HomePageView,
    SnackListView,
    SnackDetailView,
    SnackUpdateView,
    SnackCreateView,
    SnackDeleteView
)


# urlpatterns = [
#     path('snacks', index, name='snacks')
#     path('detail', index, name='detail')

urlpatterns = [
    path('', HomePageView.as_view(), name = 'index'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('snacks/', SnackListView.as_view(), name='snack_list'),
    path('<int:pk>/', SnackDetailView.as_view(), name='snack_detail'),
    path('<int:pk>/update/', SnackUpdateView.as_view(), name='snack_update'),
    # path('create/', SnackCreateView.as_view(), name='snack_create'),
    path('create/', my_view, name='snack_create'),
    path('<int:pk>/delete/', SnackDeleteView.as_view(), name='snack_delete'),
]