from django.db import models

class UrlToVisit(models.Model):
    name = models.CharField(max_length = 100)
    url = models.URLField(max_length=250)
    # iteration time in minutes
    iterationTime = models.PositiveSmallIntegerField()


    def __str__(self):
        return '{} every {} mins'.format(str(self.name), self.iterationTime)
