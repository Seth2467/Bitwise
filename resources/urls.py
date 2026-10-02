from django.urls import path
from . import views

urlpatterns = [
    path('', views.unit_list, name='resource_list'),
    path(
      '<int:unit_id>/',
      views.unit_resource_categories,
      name='unit_resource_categories'
    ),

    path(
      '<int:unit_id>/<str:category>/',
      views.resource_list_by_category,
      name='resource_list_by_category'
    ),
]
