from django.db import models


class PackageInfo(models.Model):
    package_id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=255)


class PackageVersionInfo(models.Model):
    package_version_id = models.AutoField(primary_key=True)
    package_version_name = models.CharField(max_length=255)
    package_id = models.ForeignKey(PackageInfo, to_field='package_id', on_delete=models.SET_NULL, null=True)
