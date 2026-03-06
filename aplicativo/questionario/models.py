from django.db import models

# Classe é um conjunto de objetos
# Objeto é uma instância da classe
# Atributos são as características do objeto
# Métodos ações do objeto
# Toda classe começa com letra maiúscula
# classe Lucio(Antonio) - Herança, Lucio é uma classe filha de Antonio, Antonio é a classe pai

class Questionario(models.Model):
    descricao  = models.CharField(max_length=60,null=False, blank=False)
    def __str__(self):
        return f"Questionário [descricao={self.descricao}]"