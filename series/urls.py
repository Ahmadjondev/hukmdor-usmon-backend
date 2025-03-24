from django.urls import path
from rest_framework.routers import DefaultRouter

from series.views import SeriesView, EpisodesView, CastsView

# router = DefaultRouter()
# router.register(r'admin/series', SeriesViewSet, basename='Series')
# router.register(r'admin/episodes', EpisodesViewSet)

urlpatterns = [
    path('series/', SeriesView.as_view()),
    path('episodes/', EpisodesView.as_view()),
    path('casts/', CastsView.as_view()),
    # path('admin/', include(router.urls)),
    # path('admin/login/', AdminLoginView.as_view(), name='admin-login'),
    # path('admin/check/', TokenExpireCheckView.as_view(), name='admin-login'),

    # path('admin/login/', AdminLoginView.as_view(), name='admin_login'),
]
