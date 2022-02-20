from django.urls import path
from api.views import get_all_objects,get_object

urlpatterns = [
    path("", get_all_objects, name="all object"),
    path("<int:pk>/", get_object),

]
