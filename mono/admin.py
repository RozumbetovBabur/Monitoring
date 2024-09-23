from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(office)
class OficceAdmin(admin.ModelAdmin):
    list_display = ['id','kobina','stol','turi']


@admin.register(Soups_foot)
class SoupsFootAdmin(admin.ModelAdmin):
    list_display = ['id','name','lang','price']

@admin.register(Salads_foot)
class SaladsFootAdmin(admin.ModelAdmin):
    list_display = ['id','name','lang','price']

@admin.register(Dishes_to_order)
class DishesOrderAdmin(admin.ModelAdmin):
    list_display = ['id','name','lang','price']

@admin.register(Pizza_foot)
class PizzaFootAdmin(admin.ModelAdmin):
    list_display = ['id','name','lang','price']

@admin.register(Bread)
class BreadAdmin(admin.ModelAdmin):
    list_display = ['id','name','lang','price']

@admin.register(Vynechka_foot)
class VynechkaFootAdmin(admin.ModelAdmin):
    list_display = ['id','name','lang','price']

@admin.register(Giril_foot)
class GirilFootAdmin(admin.ModelAdmin):
    list_display = ['id','name','lang','price']

@admin.register(Home_foot)
class HomefootAdmin(admin.ModelAdmin):
    list_display = ['id','name','lang','price']

@admin.register(Tea_Karna_foot)
class TeaKarnaFootAdmin(admin.ModelAdmin):
    list_display = ['id','name','lang','price']

@admin.register(Cold_drinks)
class ColdDrinksAdmin(admin.ModelAdmin):
    list_display = ['id','name','lang','price']

@admin.register(Vodka_drinks)
class VodkaDrinksAdmin(admin.ModelAdmin):
    list_display = ['id','name','lang','price']

@admin.register(Beer_drinks)
class BeerDrinksAdmin(admin.ModelAdmin):
    list_display = ['id','name','lang','price']

@admin.register(Knivu_foot)
class KnivuFootAdmin(admin.ModelAdmin):
    list_display = ['id','name','lang','price']

@admin.register(Breadbaza)
class BreadAdmin(admin.ModelAdmin):
    list_display = ['id','name','lang','price']

@admin.register(OrderNew)
class OrderNewAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','piece','money','time_of_year']

@admin.register(OrderBaza)
class OrderBazaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'piece', 'time_of_year', 'payment_method']
