from django.db import models
from django.db import models

gender_choice = [
    ('lehilahy', 'lehilahy'),
    ('vehivavy', 'vehivavy'),
]


class User(models.Model):
    full_name = models.CharField(max_length=50)
    picture = models.FileField(upload_to='static/media/images/user/')
    gender = models.CharField(max_length=8, choices=gender_choice, default='lehilahy')

    tel = models.IntegerField()
    mail = models.EmailField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)

    password = models.CharField(max_length=200)


class Sudo(models.Model):
    tel = models.IntegerField()
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=50)


class Sampana(models.Model):
    name = models.CharField(max_length=10)
    picture = models.FileField(upload_to='static/images/sampana/identite/')
    famariparitana = models.CharField(max_length=200)


class Rafitra(models.Model):
    type = models.CharField(max_length=20)  # mofonaina, sampana, fiangonana
    sudo = models.CharField(max_length=20)  # stk, pasteur, mpilaza raharaha
    picture = models.FileField(upload_to=' /app/static/images/sampana/rafitra')
    name = models.CharField(max_length=10)
    function = models.CharField(max_length=20)


class Asa(models.Model):
    type = models.CharField(max_length=10)
    sudo = models.CharField(max_length=10)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=20)


class Fampianarana(models.Model):
    type = models.CharField(max_length=10)
    sudo = models.CharField(max_length=10)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=20)


class Vaovao(models.Model):
    type = models.CharField(max_length=10)
    sudo = models.CharField(max_length=10)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=20)
    sokajy = models.CharField(max_length=30)


class Archive(models.Model):
    type = models.CharField(max_length=20)   # mofonaina, sampana, fiangonana
    sudo = models.CharField(max_length=20)  # stk, pasteur, mpilaza raharaha
    context = models.TextField()
    media = models.FileField(upload_to='static/media/archives/')


class Mofonaina(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    content = models.TextField()


class Fandaharana(models.Model):
    content = models.TextField()

