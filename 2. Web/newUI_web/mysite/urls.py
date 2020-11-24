from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from mysite.core import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('closet/', views.closet, name='closet'),
    path('add_clothing', views.add_clothing, name='add_clothing'),
    path('clothings/<int:pk>/', views.delete_clothing, name='delete_clothing'),
    path('coordinate/<int:pk>/',
         views.coordinate_clothing, name='coordinate_clothing'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
