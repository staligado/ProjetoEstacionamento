from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('sistema/', include('core.urls')),
    path("accounts/", include('django.contrib.auth.urls')),

]
