from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="Notes API")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('notes.urls')),
    path('auth/', include('rest_framework.urls')),
    path('api/jwtauth/', include('jwtauth.urls'), name='jwtauth'),
    path('api/docs/', schema_view),
]
