from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index , name = 'home'),
    path('analyze', views.analyze , name = 'analyze'),
    path('contact', views.contact , name = 'contact'),
    # path('capatilizefirst', views.capatilizefirst , name = 'capatilizefirst'),
    # path('newlineremove', views.newlineremove , name = 'newlineremove'),
    # path('spaceremove', views.spaceremove , name = 'spaceremove'),
    # path('charcount', views.charcount , name = 'charcount'),
]
