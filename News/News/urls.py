from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from News import settings

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('', include('Blog.urls')),
]
if settings.DEBUG:#если проект запускается на реальном сервере то будет созданна отдельная папка для всех медиа
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)