from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Genre(UUIDMixin, TimeStampedMixin):
    name = models.CharField(_('name'), max_length=255, unique=True)
    description = models.TextField(_('description'), blank=True)

    class Meta:
        db_table = "genre"
        ordering = ("name",)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.CharField(
        _('full name'),
        max_length=255
    )

    class Meta:
        db_table = "person"
        ordering = ("full_name",)
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

    def __str__(self):
        return self.full_name


class Filmwork(UUIDMixin, TimeStampedMixin):

    class FilmworkTypes(models.TextChoices):
        MOVIE = 'movie', _('movie'),
        TV_SHOW = 'tv_show', _('tv_show')

    title = models.CharField(
        _('title'),
        max_length=255,
        unique=True
    )
    description = models.TextField(_('description'), blank=True)
    creation_date = models.DateField(_('creation date'))
    file_path = models.FileField(
        _('file'),
        blank=True,
        null=True,
        upload_to='movies/'
    )
    rating = models.FloatField(
        _('rating'),
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    type = models.CharField(
        _('type'),
        max_length=7,
        choices=FilmworkTypes.choices,
        help_text="Выберите тип произведения"
    )
    genres = models.ManyToManyField(Genre, through='GenreFilmwork')
    persons = models.ManyToManyField(Person, through='PersonFilmwork')

    class Meta:
        db_table = "film_work"
        ordering = ("-creation_date",)
        verbose_name = 'Кинопроизведение'
        verbose_name_plural = 'Кинопроизведения'

    def __str__(self):
        return self.title


class GenreFilmwork(UUIDMixin):
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "genre_film_work"
        constraints = [
            models.UniqueConstraint(
                fields=['film_work', 'genre'],
                name='unique_film_work_genre'
            )]
        verbose_name = 'Жанр фильма'
        verbose_name_plural = 'Жанры фильма'

    def __str__(self):
        return ''


class RoleTypes(models.TextChoices):
    ACTOR = 'actor', _('actor')
    DIRECTOR = 'director', _('director')
    WRITER = 'writer', _('writer')


class PersonFilmwork(UUIDMixin):

    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    role = models.TextField(
        _('role'),
        max_length=8,
        choices=RoleTypes.choices,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "person_film_work"
        constraints = [
            models.UniqueConstraint(
                fields=['film_work', 'person', 'role'],
                name='unique_film_work_person'
            )]
        verbose_name = 'Участник фильма'
        verbose_name_plural = 'Участники фильма'

    def __str__(self):
        return ''