"""
URL configuration for HukmdorUsmon project.

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
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

from HukmdorUsmon import settings

# schema_view = get_schema_view(
#     openapi.Info(
#         title="HukmdorUsmon API",
#         default_version='v1',
#         description="API documentation for HukmdorUsmon",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="ahmadjondevv@gmail.com"),
#         license=openapi.License(name="2BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )
urlpatterns = [
                  path('manager/', admin.site.urls),
                  path('api/', include('series.urls')),
                  # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
