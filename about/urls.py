from . import views
from django.urls import path

urlpatterns=[

    path('',views.aboutme,name='about'),
    path('<about>',views.dynamic_about)

]
