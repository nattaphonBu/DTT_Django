from django.db.models import CharField
from django.test import TestCase

from .models import Sentiment


class SentimentTest(TestCase):
    def test_should_have_field(self):
        wordfield = Sentiment._meta.get_field('word')
        sentimentfield = Sentiment._meta.get_field('sentiments')

        self.assertTrue(isinstance(sentimentfield, CharField))
        self.assertTrue(isinstance(wordfield, CharField))

    def create_datas(self, word ='love', sentiments = 'Good'):
            return Sentiment.objects.create(word = word, sentiments = sentiments)

    def test_insert_data(self):
        create = self.create_datas()
        self.assertEqual(create.__unicode__(), create.word)
        self.assertEqual(create.__unicode1__(), create.sentiments)
