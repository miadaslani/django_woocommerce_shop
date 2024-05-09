from . import views
from django.urls import path

urlpatterns=[

    path('',views.aboutme),
    path('<about>',views.dynamic_about)

]
