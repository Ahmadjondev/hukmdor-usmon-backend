from django.contrib import admin

from series.models import Series, Episode


# Register your models here.

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'producer')
    search_fields = ('title', 'description')


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('series', 'title', 'link')
