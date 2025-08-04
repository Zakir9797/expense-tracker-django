from django.urls import path, include
from .views import EntryViewSet, report, add_entry
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'entries', EntryViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('report/', report, name='report'),
    path('add/', add_entry, name='add_entry'),
]