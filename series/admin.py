from django.contrib import admin

from series.models import Series, Episode, Casts


# Register your models here.

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'producer')
    search_fields = ('title', 'description')


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('series', 'title', 'link')


@admin.register(Casts)
class CastsAdmin(admin.ModelAdmin):
    list_display = ('series', 'cast', 'description')
    search_fields = ('series__title', 'cast', 'description')
