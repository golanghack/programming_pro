from django.db import models

class Singer(models.Model):
    name = models.CharField(max_length=200, help_text='Singer')

    def __str__(self):
        return self.name 

class Album(models.Model):
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    start = models.DateField(blank=True)

    def __str__(self):
        return f'album {self.singer} from {self.start}'

class Song(models.Model):
    name = models.CharField(max_length=200)
    in_album = models.ForeignKey(Album, on_delete=models.CASCADE)
    number_in = models.IntegerField(default=1)

    def __str__(self):
        return self.name