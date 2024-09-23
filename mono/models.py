from django.db import models

# Create your models here.
class office(models.Model):
    kobina = models.CharField(max_length=250)
    stol = models.CharField(max_length=250)
    turi = models.CharField(max_length=14)

class Soups_foot(models.Model):
    name = models.CharField(max_length=300)
    lang = models.IntegerField()
    price = models.IntegerField()

class Salads_foot(models.Model):
    name = models.CharField(max_length=300)
    lang = models.IntegerField()
    price = models.IntegerField()

class Dishes_to_order(models.Model):
    name = models.CharField(max_length=300)
    lang = models.IntegerField()
    price = models.IntegerField()

class Pizza_foot(models.Model):
    name = models.CharField(max_length=300)
    lang = models.IntegerField()
    price = models.IntegerField()

class Bread(models.Model):
    name = models.CharField(max_length=300)
    lang = models.IntegerField()
    price = models.IntegerField()

class Breadbaza(models.Model):
    name = models.CharField(max_length=300)
    lang = models.IntegerField()
    price = models.IntegerField()

class Vynechka_foot(models.Model):
    name = models.CharField(max_length=300)
    lang = models.IntegerField()
    price = models.IntegerField()

class Giril_foot(models.Model):
    name = models.CharField(max_length=300)
    lang = models.IntegerField()
    price = models.IntegerField()

class Home_foot(models.Model):
    name = models.CharField(max_length=300)
    lang = models.IntegerField()
    price = models.IntegerField()

class Tea_Karna_foot(models.Model):
    name = models.CharField(max_length=300)
    lang = models.IntegerField()
    price = models.IntegerField()

class Cold_drinks(models.Model):
    name = models.CharField(max_length=300)
    lang = models.IntegerField()
    price = models.IntegerField()


class Vodka_drinks(models.Model):
    name = models.CharField(max_length=300)
    lang = models.IntegerField()
    price = models.IntegerField()

class Beer_drinks(models.Model):
    name = models.CharField(max_length=300)
    lang = models.IntegerField()
    price = models.IntegerField()

class Knivu_foot(models.Model):
    name = models.CharField(max_length=300)
    lang = models.IntegerField()
    price = models.IntegerField()




class OrderNew(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    piece = models.IntegerField()
    money = models.CharField(max_length=50)
    time_of_year = models.CharField(max_length=50)


class OrderBaza(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    piece = models.IntegerField()
    time_of_year = models.DateTimeField()

    PAYMENT_CHOICES = [
        ('1', 'Наличные'),  # Cash
        ('2', 'Пластик'),   # Card
    ]
    payment_method = models.CharField(max_length=1, choices=PAYMENT_CHOICES, default='1')