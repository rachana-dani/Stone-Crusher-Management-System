"""stonecrusher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from moneymanager.views import Login,WorkerView,SalesView, ResourceView, StoneTypeView, DieselStockView, SaleBillView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", Login.as_view()),
    path("worker/", WorkerView.as_view()),
    re_path(r"worker/(?P<aadhar>\w+)$", WorkerView.as_view()),
    path("sales/",SalesView.as_view()),
    path("resources/", ResourceView.as_view()),
    path("stone_types/", StoneTypeView.as_view()),
    path("diesel_stocks/", DieselStockView.as_view()),
    path("bills/", SaleBillView.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
