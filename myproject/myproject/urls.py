"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from webapp.views.polls import IndexPoll, PollView, AddPoll, PollUpdate, DeletePoll

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexPoll.as_view(), name='main_page'),
    path('poll/<int:pk>/', PollView.as_view(), name='poll_more'),
    path('add/', AddPoll.as_view(), name='adding_poll'),
    path('update/<int:pk>/poll/', PollUpdate.as_view(), name='poll_update'),
    path('delete/<int:pk>/poll/', DeletePoll.as_view(), name='delete_poll'),
]
