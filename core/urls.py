from django.urls import path
from . views import TestView, GenericView, GenericCreateView, ListCreate

urlpatterns = [
    path('', TestView.as_view(), name="test"),
    path('generic/', GenericView.as_view(), name="generic"),
    path('create/', GenericCreateView.as_view(), name="create"),
    path('list-create/', ListCreate.as_view(), name='list-create'),
]
