"""tutorialdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from main.views import index, cafelist, restau_list, restau_list2, event, review, cafedetails, sample
#main 폴더의 views.py
# from main import views해서 views.cafelist (views.py의 cafelist 메서드) 등으로 할 수도 있다.
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('cafelist/', cafelist),
    path('restau_list/', restau_list),
    path('restau_list2/', restau_list2),
    path('review/', review),
    path('event/', event),
    path('cafelist/<int:pk>', cafedetails),
    path('sample', sample),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)