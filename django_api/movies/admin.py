from django.contrib import admin
from .models import Filmwork, Genre, GenreFilmwork, Person, PersonFilmwork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',) 

class PersonFilmworkInline(admin.TabularInline):
    model = PersonFilmwork
    list_select_related = ['person', ]
    raw_id_fields = ('person',)


class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmwork


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmworkInline, PersonFilmworkInline)
    list_display = ('title', 'type', 'creation_date', 'rating', 'get_genres')
    list_filter = ('type',)
    search_fields = ('title', 'description', 'id')

    def get_genres(self, obj):
        return ','.join([genre.name for genre in obj.genres.all()])

    get_genres.short_description = 'Жанры фильма'


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    search_fields = ('full_name',)