from django.contrib import admin
from .models import PackageInfo, PackageVersionInfo

# Register your models here.
admin.site.register(PackageInfo)
admin.site.register(PackageVersionInfo)
