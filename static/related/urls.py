from django.urls import path
from . import views

urlpatterns = [
    path('', views.related, name='related'),
    path('<int:id>', views.related_detail, name='related_detail')
]
