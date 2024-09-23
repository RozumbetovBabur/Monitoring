from django.urls import path
from .views import *

urlpatterns = [
    path('',Login_page,name="login"),
    path('home/',Home_page,name="home"),
    path('signup/',signup_page,name="signup"),
    path('logout/',logout,name="logout"),
    path('operator/',operator,name="operator"),
    path('profile/', profile_view, name='profile'),
    path('admin-profile/', AdminProfile_view, name="admin-profile"),


    path('grafika/',grafika,name="grafika"),
    path('zakaz-grafika/',ZakazGrafika,name="zakaz-grafika"),
    path('news/',news,name="news"),
    path('delete-news/', DeleteNewsView.as_view(), name="delete-news"),
    path('edit/<int:id>/', edit.as_view(), name="edit"),


    path('soups/',SoupFootInsert,name="soups"),
    path('delete-soups/', DeleteSoupFoot.as_view(), name="delete-soups"),
    path('soups-update/<int:id>',SoupsUpdate.as_view(),name="soups-update"),


    path('salads-foot-insert/',SaladsFootInsert,name="salads-foot-insert"),
    path('salads-foot-update/<int:id>/',SaladsFootUpdate.as_view(),name="salads-foot-update"),
    path('delete-salads/',DeleteSaladsFoot.as_view(),name="delete-salads"),


    path('DishesToOrder/',DishesToOrderInsert,name="DishesToOrder"),
    path('Dishes-to-order-update/<int:id>/',DishesOrderUpdate.as_view(),name="Dishes-to-order-update"),
    path('delete-dishes/',DeleteDishesOrderFoot.as_view(),name="delete-dishes"),


    path('Pizza-foot-insert/',PizzaFootInsert,name="Pizza-foot-insert"),
    path('Pizza-foot-update/<int:id>/',PizzaFootUpdate.as_view(),name="Pizza-foot-update"),
    path('delete-pizza/',DeletePizzaFoot.as_view(),name="delete-pizza"),


    path('beer-insert/',BeerInser,name = "beer"),
    path('bread-update/<int:id>/',BreadUpdate.as_view(),name="bread-update"),
    path('delete-bread/',DeleteBread.as_view(),name="delete-bread"),


    path('vynechka-foot-insert/',VynechkaFootInsert,name="vynechka-foot-insert"),
    path('vnechka-foot-update/<int:id>/>',VnechkaFootUpdate.as_view(),name="vnechka-update"),
    path('delete-vnechka/',DeleteVnechka.as_view(),name="delete-vnechka"),

    path('grill-foot/',GrillFootInsert,name="grill_insert"),
    path('grill-foot-update/<int:id>/',GrillFootUpdate.as_view(),name="grill_update"),
    path('delete-grill/',DeleteGrillFoot.as_view(),name="grill-delete"),


    path('home-foor/',HomeFootInsert,name="home_foot"),
    path('home-foot-update/<int:id>/',HomeFootUpdate.as_view(),name="home_foot_update"),
    path('delete-home/',DeleteHomeFoot.as_view(),name="home_foot_update"),

    path('tea-karna/',Tea_karnaInsert,name="tea-karna"),
    path('tea-karna-update/<int:id>/',TeaKarnaUpdate.as_view(),name="tea-karna-update"),
    path('delete-tea/',DeleteTeaKarna.as_view(),name="tea-delete"),


    path('cold-drinks/',ColdDrinksInsert,name="cold-drinks"),
    path('cold-drinks-update/<int:id>/',ColdDrinksUpdate.as_view(),name="cold-update"),
    path('delete-cold/',DeleteColdDrinks.as_view(),name="cold-delete"),


    path('vodka-drinks/',VodkaDrinksInsert,name="vodka-drinks"),
    path('vodka-drinks-update/<int:id>',VodkaDrinksUpdate.as_view(),name="vodka-update"),
    path('delete-vodka/',DeleteVodkaDrinks.as_view(),name="delete-vodka"),


    path('privo-drinks/',PivoDrinksInsert,name="privo-insert"),
    path('pivo-drinks-update/<int:id>/',PivoDrinksUpdate.as_view(),name="pivo-update"),
    path('delete-piva/',DeletePivaDrinks.as_view(),name="piva-delete"),


    path('kneva/',KnevaFootInsert,name="kneva-insert"),
    path('kneva-foot-update/<int:id>/',KnevaFootUpdate.as_view(),name="kneva-update"),
    path('delete-krneva/',DeleteKrnevaFoot.as_view(),name="krneva-delete"),

    path('zakaz-olish/',zakazOlish,name="zakaz-olish"),
    path('zakaz/',JamiZakaz,name="zalaz"),
    path('zakaz-table/',ZakazTable,name="zakaz_table"),
    path('filter/',ZakazTable,name="filter"),

]