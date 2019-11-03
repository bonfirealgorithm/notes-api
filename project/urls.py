from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('notes.urls')),
    path('auth/', include('rest_framework.urls')),
    path('api/jwtauth/', include('jwtauth.urls'), name='accounts')
]
