

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django import views
from django.shortcuts import redirect, render

class FrontEnd(views.View):

    def get(self, request):
        return render(request, "index.html")
    
    def post(self, request):
        return render(request, "index.html")
        
  

urlpatterns = [
    path( 'admin/', admin.site.urls),
    path( 'api/accounts/', include('accounts.urls')),
    path( 'api/residence/', include('residence.urls')),
    
    # Catch all remaining URLs
    re_path(r"^(?!api/|admin/).*", FrontEnd.as_view(), name="frontend"),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


