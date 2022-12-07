
from django.contrib import admin
from django.urls import path

from blog.views import frontpage,postdetail


urlpatterns = [
    path('admin/', admin.site.urls),
    path("blog/", frontpage),
    path("<slug:slug>/", postdetail, name="post_detail")
]
