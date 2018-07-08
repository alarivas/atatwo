from django.db import models


class Person(models.Model):
    rut = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    is_good_payer = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.name)


class Benefit(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)


class Relation(models.Model):
    count = models.IntegerField(default=1)
    person_one = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person_one')
    person_two = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person_two')
    benefits = models.ManyToManyField(Benefit)

    def __str__(self):
        return '{} relacionado con {}'.format(self.person_one, self.person_two)
