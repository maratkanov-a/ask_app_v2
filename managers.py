from django.db import models


class QuestionManager(models.Manager):
    def hot(self):
        return self.order_by('-rating')

    def newest(self):
        return self.order_by('-date')

    def findByTag(self, tag_to_find):
        return self.filter(tags=tag_to_find)
