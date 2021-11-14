from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('main.api.api_urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.authtoken')),
    path('i18n/', include('django.conf.urls.i18n')),

]
urlpatterns += i18n_patterns(
    path('accounts/',include('allauth.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', include('main.urls')),
    path('contact/', include('contact.urls')),
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
