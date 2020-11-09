from django.urls import path
from . import views

app_name = 'packages'

urlpatterns = [
    # http://127.0.0.1:8000/packages/home/
    path('home/', views.home, name='home_url'),

    # /packages/4/
    path('<int:package_id>/', views.package_information, name='package_url'),

    # /packages/4/end_page/
    path('<int:package_id>/end_page/', views.end_page, name='end_page_url'),
]
