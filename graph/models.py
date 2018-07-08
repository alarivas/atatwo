from django.db import models


class Person(models.Model):
    rut = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)


class Relation(models.Model):
    count = models.IntegerField(default=0)
    person_one = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='person_one')
    person_two = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='person_two')

    def __str__(self):
        return '{} relacionado con {}'.format(self.person_one, self.person_two)
