from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from mysite.core import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('clothings/', views.clothing_list, name='clothing_list'),
    path('clothings/upload/', views.upload_clothing, name='upload_clothing'),
    path('clothings/<int:pk>/', views.delete_clothing, name='delete_clothing'),

    path('class/clothings/', views.ClothingListView.as_view(),
         name='class_clothing_list'),
    path('class/clothings/upload/', views.UploadClothingView.as_view(),
         name='class_upload_clothing'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
