from . import views
from django.urls import path

urlpatterns = [
    # path("",views.index,name='stating_page'),
    path("",views.posts,name='post_page'),
    path("posts/<slug:slug>",views.single_post,name='post_details'),
    
] 