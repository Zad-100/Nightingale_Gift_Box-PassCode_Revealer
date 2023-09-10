"""
URL configuration for passcode_revealer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from django.conf import settings # For static files
# from django.conf.urls.static import static # For static files

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # include urls from the users app
    path("users/", include('users.urls')),
    
    # include urls from the puzzles app
    path("", include('puzzles.urls')),
]



# ***************NOT WORKING***************
# Only for development (DEBUG = False)
# Comment this section before deploying to Azure!!!
# Add URL maps to redirect the base URL to our application
# if settings.DEBUG is False:
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)
# end if