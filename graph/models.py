from django.db import models


class Person(models.Model):
    rut = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Relation(models.Model):
    count = models.IntegerField()
    person_one = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='person_one')
    person_two = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='person_two')

    def __str__(self):
        return '{} relacionado con {}'.format(self.person_one, self.person_two)
