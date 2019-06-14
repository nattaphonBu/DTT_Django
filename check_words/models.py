from django.db import models


class Sentiment(models.Model):
    word = models.CharField(max_length=200, blank = True, null = True)
    sentiments = models.CharField(max_length = 20, blank = True, null = True)

    def __unicode__(self):
        return self.word

    def __unicode1__(self):
        return self.sentiments
