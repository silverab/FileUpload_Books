from django.contrib import admin
from django.urls import path

# from myapp.views import Home 
from myapp import views 

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
    path('book_list/', views.book_list, name='book_list'),
    path('upload_book/', views.upload_book, name='upload_book'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)