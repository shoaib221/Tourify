

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path( 'admin/', admin.site.urls),
    path( 'api/accounts/', include('accounts.urls')),
    path( 'api/residence/', include('residence.urls')),
    path( '',  include( 'frontend.urls' ) )
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


