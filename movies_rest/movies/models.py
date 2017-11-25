from django.db import models
from persons.models import Person

MOVIE_RANK = (
    (1, "very bad"),
    (2, "poor"),
    (3, "average"),
    (4, "good"),
    (5, "masterpiece"),
)

GENRE = (
    ('sci-fi', "science-fiction"),
    ('fantasy', "fantasy"),
    ('historical', "historical"),
    ('drama', "drama"),
    ('comedy', "comedy"),
    ('romance', "romance"),
    ('adult', "adult"),
    ('cartoon', "cartoon"),
)


class Movie(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    director = models.ForeignKey(Person,
                                 on_delete=models.CASCADE,
                                 related_name="movie_director")
    actors = models.ManyToManyField(Person, through='Role')
    year = models.IntegerField()
    ranking = models.IntegerField(choices=MOVIE_RANK)
    genre = models.CharField(max_length=128, choices=GENRE)

    def __str__(self):
        return self.title


class Role(models.Model):
    movie = models.ForeignKey(Movie, related_name="movie_role")
    person = models.ForeignKey(Person, related_name="person_role")
    role = models.CharField(max_length=64, null=True)

    def __str__(self):
        return "{} - {} {}".format(self.movie,
                                   self.person,
                                   self.role)

