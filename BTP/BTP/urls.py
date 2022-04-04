
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('doctors/', include('doctors.urls')),
    path('clients/', include('clients.urls')),
    path('blogs/', include('blogs.urls')),
    path('messages/', include('conversations.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
