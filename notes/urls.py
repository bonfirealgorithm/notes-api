from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import NoteViewSet

router = SimpleRouter()
router.register('notes', NoteViewSet, basename="notes")
urlpatterns = router.urls
