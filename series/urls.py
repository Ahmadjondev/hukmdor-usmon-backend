from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.urls import urlpatterns

from series.views import SeriesView, SeriesViewSet, EpisodesViewSet, EpisodesView, CastsView, AdminLoginView, \
    TokenExpireCheckView

router = DefaultRouter()
router.register(r'admin/series', SeriesViewSet, basename='Series')
router.register(r'admin/episodes', EpisodesViewSet)

urlpatterns = [
    path('series/', SeriesView.as_view()),
    path('episodes/', EpisodesView.as_view()),
    path('casts/', CastsView.as_view()),
    # path('admin/', include(router.urls)),
    # path('admin/login/', AdminLoginView.as_view(), name='admin-login'),
    # path('admin/check/', TokenExpireCheckView.as_view(), name='admin-login'),

    # path('admin/login/', AdminLoginView.as_view(), name='admin_login'),
]
