from django.contrib import admin
from core.models import Catagoria,Editor,Autor,Livro,Compra,ItensCompra

admin.site.register(Catagoria)
admin.site.register(Editor)
admin.site.register(Autor)
admin.site.register(Livro)
#admin.site.register(Compra)
#admin.site.register(ItensCompra)
# Register your models here.

class ItensInline(admin.TabularInline):
    model =ItensCompra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = (ItensInline,)