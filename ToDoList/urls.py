"""ToDoList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from main import views

router = DefaultRouter()
router.register(r'lists', views.ListModelViewSet, base_name='lists')
router.register(r'tasks', views.TaskModelViewSet, base_name='tasks')
router.register(r'sublists', views.SublistModelViewSet, base_name='sublists')
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^add/(?P<list_id>\d+)/(?P<user_id>\d+)/$',views.AddToList.as_view(), name="add-list"),
    url(r'^admin/', admin.site.urls),
]
