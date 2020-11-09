from django.shortcuts import render
from .models import PackageInfo


def home(request):
    packages = PackageInfo.objects.all()
    return render(request, 'packages/home.html', {'packages': packages})


def package_information(request, package_id):
    package = PackageInfo.objects.get(pk=package_id)
    return render(request, 'packages/package_information.html', {'package': package})


def end_page(request, package_id):
    return render(request, 'packages/package_end_page.html', {'package_id': package_id})
