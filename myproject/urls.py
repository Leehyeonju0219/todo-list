"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from todos.views import todo_list, todo_detail, todo_create, todo_update, todo_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_list, name='todo_list'),
    path('todo/<int:id>/', todo_detail, name='todo_detail'),
    path('todo/new/', todo_create, name='todo_create'),
    path('todo/<int:id>/edit/', todo_update, name='todo_update'),
    path('todo/<int:id>/delete/', todo_delete, name='todo_delete'),
]
