from django.db import models

# Create your models here.

class Filme(models.Model):
    NOTA_CHOICES = {
        0: "0 - Péssimo",
        1: "1 - Muito Ruim",
        2: "2 - Ruim",
        3: "3 - Ok",
        4: "4 - Bom",
        5: "5 - Fantástico",
    }
    titulo = models.CharField(max_length=50)
    visto = models.BooleanField(default=False)
    nota = models.IntegerField(choices = NOTA_CHOICES)
    review = models.TextField(blank=True, null=True)
    filme_id = models.IntegerField(null = False)

    def __str__(self):
        return self.titulo