from django.db import models


class Cadastro(models.Model):
    name = models.CharField(max_length=120)
    cpf = models.CharField(max_length=15)
    email = models.CharField(max_length=120)
    gender_choice = [('F', 'Feminino'), ('M', 'Masculino'), ('O', 'Outros')]
    gender = models.CharField(max_length=30, null=True,
                              blank=True, choices=gender_choice)

    def __str__(self):
        return self.name
