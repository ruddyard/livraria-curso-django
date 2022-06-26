from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Catagoria(models.Model):
    class Meta:
        verbose_name_plural="Categoria"
    descricao =models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Editor(models.Model):
    class Meta:
        verbose_name_plural="Editor"
    nome = models.CharField(max_length=100)
    site=models.URLField()

    def __str__(self):
        return self.nome

class Autor(models.Model):
    class Meta:
        verbose_name_plural="Autor"
    nome=models.CharField(max_length=100,verbose_name="Autores")
    def __str__(self):
        return self.nome

class Livro(models.Model):

    titulo=models.CharField(max_length=100)
    isbn=models.CharField(max_length=32)
    quantidade=models.IntegerField()
    preco=models.FloatField()
    categoria=models.ForeignKey(Catagoria,on_delete=models.PROTECT,related_name="livros")
    editora =models.ForeignKey(Editor,on_delete=models.PROTECT,related_name="livros")
    autor=models.ManyToManyField(Autor,related_name="livros")
    def __str__(self):
        return "%s (%s)" %(self.titulo,self.editora)

class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO= 1, "Carrinho"
        REALIZADO=2,"Realizado"
        PaGO=3,"Pago"
        ENTREGUE=4,"Entregue"

    usuario=models.ForeignKey(User,on_delete=models.PROTECT,related_name="compras")
    status=models.IntegerField(choices=StatusCompra.choices,default=StatusCompra.CARRINHO)
    def __str__(self):
        return "{} ({})" .format(self.usuario,self.status)



class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra,on_delete=models.CASCADE,related_name="itens")
    livro = models.ForeignKey(Livro,on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField()