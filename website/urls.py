from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # /admin
    path('admin/', admin.site.urls),

    # /packages/
    path('packages/', include('packages.urls', namespace='packages')),
]
