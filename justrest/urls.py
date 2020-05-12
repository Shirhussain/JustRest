from django.contrib import admin
from django.urls import path, include

# this (obtain_auth_token) will return the token for user
#  when we send the username and password like login view
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', obtain_auth_token, name="obtain-token"),
    path('rest-auth/', include('rest_auth.urls'))

]
