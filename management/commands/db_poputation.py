from django.core.management.base import BaseCommand
from ask_app.models import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in xrange(0, 10005):
            u = User(username='User{}'.format(i), email='user{}@mail.ru'.format(i), password=i)
            u.save()
        self.stdout.write('Successfully added 10000 users')

        for i in xrange(1, 10001):
            t = Tags(text='Tag {}'.format(i))
            t.save()
        self.stdout.write('Successfully added 10000 tags')

        u = User.objects.get(id=1)
        t1 = Tags.objects.get(id=3)
        t2 = Tags.objects.get(id=4)

        for i in xrange(1, 10001):
            q = Question(header='Question {}'.format(i), body='Body {}'.format(i), author=u, rating=i)
            q.save()
            q.tags.add(t1, t2)
        self.stdout.write('Successfully added 100000 questions')

        for i in xrange(1, 100001):
            q = Question.my.hot().filter(id=i)[0]
            try:
                u = User.objects.get(id=i/10)
            except User.DoesNotExist:
                u = User.objects.get(id=1)
            for j in xrange(1, 91):
                a = Answer(body='Answer new {} {}'.format(i, j), author=u, which_question=q, rating=i)
                a.save()
        self.stdout.write('Successfully added 1000000 answers')

        return
