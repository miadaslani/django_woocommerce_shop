from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from datetime import date

# Create your views here.

all_posts = [
    {
        "slug":"Python-Programming",
        "title":"Python",
        "author":"Aslani",
        "date":date(2022,12,10),
        "image":"python.png",
        "short_description":"Python is High level",
        "content":"""Python is an interpreted, object-oriented, high-level programming language with dynamic
        """,
    },
    # {
    #     "slug":"",
    #     "title":"",
    #     "author":"",
    #     "date":"",
    #     "image":"",
    #     "short_description":"",
    #     "content":"""
    #     """,
    # },
    {
        "slug":"Framework-django",
        "title":"Django",
        "author":"Aslani",
        "date":date(2021,12,10),
        "image":"django.png",
        "short_description":"django is a Framework",
        "content":"""Django is a high-level Python web framework that encourages rapid development and clean
        """,
    },
     {
        "slug":"Framework-django",
        "title":"Django",
        "author":"Aslani",
        "date":date(2020,12,10),
        "image":"django.png",
        "short_description":"django is a Framework",
        "content":"""Django is a high-level Python web framework that encourages rapid development and clean
        """,
    },
     {
        "slug":"Framework-django",
        "title":"Django",
        "author":"Aslani",
        "date":date(2019,12,10),
        "image":"django.png",
        "short_description":"django is a Framework",
        "content":"""Django is a high-level Python web framework that encourages rapid development and clean
        """,
    }
]

 
def get_date(post):
    return post['date']
 


# def index(request):
#     # lst=list(all_posts)
#     # context = {"a":lst}
#     # return render(request, 'blogs/index.html',context)
#     sort_lst = sorted(all_posts,key=get_date)
#     latest=sort_lst[-2:]
#     return render(request, 'blogs/index.html',context={"a":latest})
 
def posts(request):
    return render(request, 'blogs/blog.html',{"b":all_posts})

def single_post(request,slug):
    post=next(post for post in all_posts if post['slug']==slug)
    return render(request, 'blogs/post_details.html',{"post":post})

