
from django.contrib import admin
from django.urls import path, include
# from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api.urls'), name= 'api'), 
    # path('api-auth/', include('rest_framework.urls')), 
    path('account/', include('user_app.api.urls'))


]

