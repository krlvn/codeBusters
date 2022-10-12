from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('mainapp.urls', namespace='mainapp')),
    path('users/', include('userapp.urls')),
]

handler400 = 'mainapp.views_errors.handler400'
handler403 = 'mainapp.views_errors.handler403'
handler404 = 'mainapp.views_errors.handler404'
handler500 = 'mainapp.views_errors.handler500'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
