from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.views import View
from datetime import datetime, timedelta
from django.utils import timezone
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Sum
# Create your views here.


def Login_page(request):
    error_message = None
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if username.lower() == "admin":
                return redirect("home")
            elif username.lower() == "user":
                return redirect("operator")
            else:
                return redirect("operator")
        else:
            error_message = "Вероятно, вы ввели неверный логин или пароль, попробуйте еще раз."
    return render(request,"login.html", {"error_message": error_message})

@login_required(login_url="login")
def Home_page(request):
    today = timezone.now().date()  # Get the current date

    # Filter records for today and calculate today's total price
    today_grafikadata = OrderBaza.objects.filter(time_of_year__date=today)
    today_total_price = today_grafikadata.aggregate(total_price=Sum('price'))['total_price'] or 0

    # Calculate the overall total price from all records
    overall_total_price = OrderBaza.objects.aggregate(total_price=Sum('price'))['total_price'] or 0

    # Calculate today's total for cash ('Наличные')
    today_cash_total = \
    OrderBaza.objects.filter(time_of_year__date=today, payment_method='1').aggregate(total_price=Sum('price'))[
        'total_price'] or 0

    # Calculate today's total for card ('Пластик')
    today_card_total = \
    OrderBaza.objects.filter(time_of_year__date=today, payment_method='2').aggregate(total_price=Sum('price'))[
        'total_price'] or 0

    # Calculate overall total for cash ('Наличные')
    overall_cash_total = OrderBaza.objects.filter(payment_method='1').aggregate(total_price=Sum('price'))[
                             'total_price'] or 0

    # Calculate overall total for card ('Пластик')
    overall_card_total = OrderBaza.objects.filter(payment_method='2').aggregate(total_price=Sum('price'))[
                             'total_price'] or 0

    context = {
        "today_total_price": today_total_price,
        "overall_total_price": overall_total_price,
        "today_cash_total": today_cash_total,
        "today_card_total": today_card_total,
        "overall_cash_total": overall_cash_total,
        "overall_card_total": overall_card_total,
    }
    return render(request,"home.html",context)

@login_required(login_url="login")
def operator(request):
    return render(request,"operator.html")
@login_required(login_url="login")
def signup_page(request):
    error_message = None
    if request.POST:
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password != password2:
            error_message = "Пароли должны быть одинаковыми."
        else:
            my_user = User.objects.create_user(username=username, email=email, password=password)
            my_user.first_name = first_name  # first_name ni alohida o'rnatish
            return redirect("login")
    return render(request,"signup.html",{"error_message": error_message})
@login_required(login_url="login")
def logout(request):
    auth_logout(request)
    return redirect("login")
@login_required(login_url="login")
def grafika(request):
    today = timezone.now().date()  # Get the current date

    # Filter records for today and calculate today's total price
    today_grafikadata = OrderBaza.objects.filter(time_of_year__date=today)
    today_total_price = today_grafikadata.aggregate(total_price=Sum('price'))['total_price'] or 0

    # Calculate the overall total price from all records
    overall_total_price = OrderBaza.objects.aggregate(total_price=Sum('price'))['total_price'] or 0

    # Calculate today's total for cash ('Наличные')
    today_cash_total = OrderBaza.objects.filter(time_of_year__date=today, payment_method='1').aggregate(total_price=Sum('price'))['total_price'] or 0

    # Calculate today's total for card ('Пластик')
    today_card_total = OrderBaza.objects.filter(time_of_year__date=today, payment_method='2').aggregate(total_price=Sum('price'))['total_price'] or 0

    # Calculate overall total for cash ('Наличные')
    overall_cash_total = OrderBaza.objects.filter(payment_method='1').aggregate(total_price=Sum('price'))['total_price'] or 0

    # Calculate overall total for card ('Пластик')
    overall_card_total = OrderBaza.objects.filter(payment_method='2').aggregate(total_price=Sum('price'))['total_price'] or 0

    context = {
        "today_total_price": today_total_price,
        "overall_total_price": overall_total_price,
        "today_cash_total": today_cash_total,
        "today_card_total": today_card_total,
        "overall_cash_total": overall_cash_total,
        "overall_card_total": overall_card_total,
    }
    return render(request, "grafika.html", context)

@login_required(login_url="login")
def ZakazGrafika(request):
    today = timezone.now().date()  # Get the current date

    # Filter records for today and calculate today's total price
    today_grafikadata = OrderBaza.objects.filter(time_of_year__date=today)
    today_total_price = today_grafikadata.aggregate(total_price=Sum('price'))['total_price'] or 0

    # Calculate the overall total price from all records
    overall_total_price = OrderBaza.objects.aggregate(total_price=Sum('price'))['total_price'] or 0

    # Calculate today's total for cash ('Наличные')
    today_cash_total = \
        OrderBaza.objects.filter(time_of_year__date=today, payment_method='1').aggregate(total_price=Sum('price'))[
            'total_price'] or 0

    # Calculate today's total for card ('Пластик')
    today_card_total = \
        OrderBaza.objects.filter(time_of_year__date=today, payment_method='2').aggregate(total_price=Sum('price'))[
            'total_price'] or 0

    # Calculate overall total for cash ('Наличные')
    overall_cash_total = OrderBaza.objects.filter(payment_method='1').aggregate(total_price=Sum('price'))[
                             'total_price'] or 0

    # Calculate overall total for card ('Пластик')
    overall_card_total = OrderBaza.objects.filter(payment_method='2').aggregate(total_price=Sum('price'))[
                             'total_price'] or 0

    context = {
        "today_total_price": today_total_price,
        "overall_total_price": overall_total_price,
        "today_cash_total": today_cash_total,
        "today_card_total": today_card_total,
        "overall_cash_total": overall_cash_total,
        "overall_card_total": overall_card_total,
    }
    return render(request,"zakaz-grafika.html",context)

@login_required(login_url="login")
def news(request):
    if request.method == 'POST':
        fm = OfficeForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("news")
    else:
        fm = OfficeForm()
    data = office.objects.all()
    context = {
        "form": fm,
        "Modeldata": data,
    }

    return render(request, "news.html", context)

# class NewsView(View):
#     template_name = 'news.html'
#
#     # GET so'rovni qayta ishlash
#     def get(self, request):
#         fm = OfficeForm()
#         data = office.objects.all()
#         context = {
#             "form": fm,
#             "Modeldata": data,
#         }
#         return render(request, self.template_name, context)
#
#     # POST so'rovni qayta ishlash
#     def post(self, request):
#         fm = OfficeForm(request.POST)
#         if fm.is_valid():
#             fm.save()
#             return redirect('news')
#         data = office.objects.all()
#         context = {
#             "form": fm,
#             "Modeldata": data,
#         }
#         return render(request, self.template_name, context)

# def delete_news(request, id):
#     if request.method == 'POST':
#         newsdata = office.objects.get(id=id)
#         newsdata.delete()
#     return redirect("news")

class DeleteNewsView(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        newsdata = office.objects.get(id=id)
        newsdata.delete()
        return redirect("news")

class edit(View):
    def get(self,request,id):
        data = office.objects.get(id=id)
        fm = OfficeForm(instance=data)
        return render(request,"news-update.html",{'form':fm})

    def post(self,request,id):
        data = office.objects.get(id=id)
        fm = OfficeForm(request.POST,instance=data)
        if fm.is_valid():
            fm.save()
            return redirect("news")

@login_required(login_url="login")
def SoupFootInsert(request):
    if request.method == 'POST':
        fm = SoupsFootForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("soups")
    else:
        fm = SoupsFootForm()

    data = Soups_foot.objects.all()
    total_price = sum(item.price for item in data)
    context = {
        "Soupform": fm,
        "Soupdata": data,
        "total_price": total_price,
    }
    return render(request, "Soups_foot.html", context)

class DeleteSoupFoot(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        soupdata = Soups_foot.objects.get(id=id)
        soupdata.delete()
        return redirect("soups")

class SoupsUpdate(View):
    def get(self,request,id):
        soupdata = Soups_foot.objects.get(id=id)
        soupsfm = SoupsFootForm(instance=soupdata)
        return render(request,"Soups_footUpdate.html",{'Soupsform':soupsfm})

    def post(self,request,id):
        soupdata = Soups_foot.objects.get(id=id)
        soupsfm = SoupsFootForm(request.POST,instance=soupdata)
        if soupsfm.is_valid():
            soupsfm.save()
            return redirect("soups")


@login_required(login_url="login")
def SaladsFootInsert(request):
    if request.method == 'POST':
        saladsForm = SaladsFootForm(request.POST)
        if saladsForm.is_valid():
            saladsForm.save()
            return redirect("salads-foot-insert")
    else:
        saladsForm = SaladsFootForm()

    saladsdata = Salads_foot.objects.all()
    total_price = sum(item.price for item in saladsdata)
    context = {
        "saladsForm": saladsForm,
        "saladsdata": saladsdata,
        "total_price": total_price,
    }
    return render(request, "Salads_foot.html", context)

class SaladsFootUpdate(View):
    def get(self,request,id):
        saladdata = Salads_foot.objects.get(id=id)
        saladsfm = SaladsFootForm(instance=saladdata)
        return render(request,"SaladsFootUpdate.html",{'saladsfm':saladsfm})

    def post(self,request,id):
        saladdata = Salads_foot.objects.get(id=id)
        saladsfm = SaladsFootForm(request.POST,instance=saladdata)
        if saladsfm.is_valid():
            saladsfm.save()
            return redirect("salads-foot-insert")

class DeleteSaladsFoot(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        saladdata = Salads_foot.objects.get(id=id)
        saladdata.delete()
        return redirect("salads-foot-insert")

@login_required(login_url="login")
def DishesToOrderInsert(request):
    if request.method == 'POST':
        DishesOrderForm = DishesToOrderForm(request.POST)
        if DishesOrderForm.is_valid():
            DishesOrderForm.save()
            return redirect("DishesToOrder")
    else:
        DishesOrderForm = DishesToOrderForm()

    Dishesdata = Dishes_to_order.objects.all()
    total_price = sum(item.price for item in Dishesdata)
    context = {
        "dishesform": DishesOrderForm,
        "Dishesdata": Dishesdata,
        "total_price": total_price,
    }
    return render(request, "DishesToOrder.html", context)


class DishesOrderUpdate(View):
    def get(self,request,id):
        Dishesdata = Dishes_to_order.objects.get(id=id)
        Dishesfm = DishesToOrderForm(instance=Dishesdata)
        return render(request,"DishesToOrderUpdate.html",{'Dishesfm':Dishesfm})

    def post(self,request,id):
        Dishesdata = Dishes_to_order.objects.get(id=id)
        Dishesfm = DishesToOrderForm(request.POST,instance=Dishesdata)
        if Dishesfm.is_valid():
            Dishesfm.save()
            return redirect("DishesToOrder")

class DeleteDishesOrderFoot(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        Dishesdata = Dishes_to_order.objects.get(id=id)
        Dishesdata.delete()
        return redirect("DishesToOrder")

@login_required(login_url="login")
def PizzaFootInsert(request):
    if request.method == 'POST':
        fm = PizzaFootForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("Pizza-foot-insert")
    else:
        fm = PizzaFootForm()

    data = Pizza_foot.objects.all()
    total_price = sum(item.price for item in data)
    context = {
        "fm": fm,
        "data": data,
        "total_price": total_price,
    }
    return render(request, "PizzaFoot.html", context)

class PizzaFootUpdate(View):
    def get(self,request,id):
        data = Pizza_foot.objects.get(id=id)
        fm = PizzaFootForm(instance=data)
        return render(request,"PizzaFootUpdate.html",{'fm':fm})

    def post(self,request,id):
        data = Pizza_foot.objects.get(id=id)
        fm = PizzaFootForm(request.POST,instance=data)
        if fm.is_valid():
            fm.save()
            return redirect("Pizza-foot-insert")


class DeletePizzaFoot(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        data = Pizza_foot.objects.get(id=id)
        data.delete()
        return redirect("Pizza-foot-insert")

@login_required(login_url="login")
def BeerInser(request):
    if request.method == 'POST':
        beerforms = BeerForm(request.POST)
        if beerforms.is_valid():
            beerforms.save()
            return redirect("beer")
    else:
        beerforms = BeerForm()

    Beerdata = Breadbaza.objects.all()
    total_price = sum(item.price for item in Beerdata)
    context = {
        "beerforms": beerforms,
        "Beerdata": Beerdata,
        "total_price": total_price,
    }
    return render(request, "Bread.html", context)

class BreadUpdate(View):
    def get(self,request,id):
        Breaddata = Breadbaza.objects.get(id=id)
        breadfm = BeerForm(instance=Breaddata)
        return render(request,"BreadUpdate.html",{'breadfm':breadfm})

    def post(self,request,id):
        Breaddata = Breadbaza.objects.get(id=id)
        breadfm = BeerForm(request.POST,instance=Breaddata)
        if breadfm.is_valid():
            breadfm.save()
            return redirect("beer")

class DeleteBread(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        breaddata = Breadbaza.objects.get(id=id)
        breaddata.delete()
        return redirect("beer")
@login_required(login_url="login")
def VynechkaFootInsert(request):
    if request.method == 'POST':
        vnechikaform = VnechniyFootForm(request.POST)
        if vnechikaform.is_valid():
            vnechikaform.save()
            return redirect("vynechka-foot-insert")
    else:
        vnechikaform = VnechniyFootForm()

    vnechkadata = Vynechka_foot.objects.all()
    total_price = sum(item.price for item in vnechkadata)
    context = {
        "vnechikaform": vnechikaform,
        "vnechkadata": vnechkadata,
        "total_price": total_price,
    }
    return render(request,"VynechkaFoot.html",context)


class VnechkaFootUpdate(View):
    def get(self,request,id):
        vnechkadata = Vynechka_foot.objects.get(id=id)
        vnechkafm = VnechniyFootForm(instance=vnechkadata)
        return render(request,"Vnechka-foot-update.html",{'vnechkafm':vnechkafm})

    def post(self,request,id):
        vnechkadata = Vynechka_foot.objects.get(id=id)
        vnechkafm = VnechniyFootForm(request.POST,instance=vnechkadata)
        if vnechkafm.is_valid():
            vnechkafm.save()
            return redirect("vynechka-foot-insert")

class DeleteVnechka(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        vnechkadata = Vynechka_foot.objects.get(id=id)
        vnechkadata.delete()
        return redirect("vynechka-foot-insert")

@login_required(login_url="login")
def GrillFootInsert(request):
    if request.method == 'POST':
        grillform = GrillFootForm(request.POST)
        if grillform.is_valid():
            grillform.save()
            return redirect("grill_insert")
    else:
        grillform = GrillFootForm()

    grilldata = Giril_foot.objects.all()
    total_price = sum(item.price for item in grilldata)
    context = {
        "grillform": grillform,
        "grilldata": grilldata,
        "total_price": total_price,
    }
    return render(request,"giril-foot.html",context)

class GrillFootUpdate(View):
    def get(self,request,id):
        grilldata = Giril_foot.objects.get(id=id)
        grillfm = GrillFootForm(instance=grilldata)
        return render(request,"grill-foot-update.html",{'grillfm':grillfm})

    def post(self,request,id):
        grilldata = Giril_foot.objects.get(id=id)
        grillfm = GrillFootForm(request.POST,instance=grilldata)
        if grillfm.is_valid():
            grillfm.save()
            return redirect("grill_insert")


class DeleteGrillFoot(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        grilldata = Giril_foot.objects.get(id=id)
        grilldata.delete()
        return redirect("grill_insert")

@login_required(login_url="login")
def HomeFootInsert(request):
    if request.method == 'POST':
        homefooform = HomeFootForm(request.POST)
        if homefooform.is_valid():
            homefooform.save()
            return redirect("home_foot")
    else:
        homefooform = HomeFootForm()

    homedata = Home_foot.objects.all()
    total_price = sum(item.price for item in homedata)
    context = {
        "homefooform": homefooform,
        "homedata": homedata,
        "total_price": total_price,
    }
    return render(request,"Home_foot.html",context)

class HomeFootUpdate(View):
    def get(self,request,id):
        homedata = Home_foot.objects.get(id=id)
        homefootfm = HomeFootForm(instance=homedata)
        return render(request,"Home-foot-update.html",{'homefootfm':homefootfm})

    def post(self,request,id):
        homedata = Home_foot.objects.get(id=id)
        homefootfm = HomeFootForm(request.POST,instance=homedata)
        if homefootfm.is_valid():
            homefootfm.save()
            return redirect("home_foot")

class DeleteHomeFoot(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        homedata = Home_foot.objects.get(id=id)
        homedata.delete()
        return redirect("home_foot")

@login_required(login_url="login")
def Tea_karnaInsert(request):
    if request.method == 'POST':
        TeaKarnaform = TeaKarnaFootForm(request.POST)
        if TeaKarnaform.is_valid():
            TeaKarnaform.save()
            return redirect("tea-karna")
    else:
        TeaKarnaform = TeaKarnaFootForm()

    teakarnadata = Tea_Karna_foot.objects.all()
    total_price = sum(item.price for item in teakarnadata)
    context = {
        "TeaKarnaform": TeaKarnaform,
        "teakarnadata": teakarnadata,
        "total_price": total_price,
    }
    return render(request,"Tea_Karna_foot.html",context)


class TeaKarnaUpdate(View):
    def get(self,request,id):
        karnadata = Tea_Karna_foot.objects.get(id=id)
        teakarnafm = TeaKarnaFootForm(instance=karnadata)
        return render(request,"tea-karna-update.html",{'teakarnafm':teakarnafm})

    def post(self,request,id):
        karnadata = Tea_Karna_foot.objects.get(id=id)
        teakarnafm = TeaKarnaFootForm(request.POST,instance=karnadata)
        if teakarnafm.is_valid():
            teakarnafm.save()
            return redirect("tea-karna")

class DeleteTeaKarna(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        teakarnadata = Tea_Karna_foot.objects.get(id=id)
        teakarnadata.delete()
        return redirect("tea-karna")

@login_required(login_url="login")
def ColdDrinksInsert(request):
    if request.method == 'POST':
        colddriksform = ColdDrunksForm(request.POST)
        if colddriksform.is_valid():
            colddriksform.save()
            return redirect("cold-drinks")
    else:
        colddriksform = ColdDrunksForm()

    colddrinksdata = Cold_drinks.objects.all()
    total_price = sum(item.price for item in colddrinksdata)
    context = {
        "colddriksform": colddriksform,
        "colddrinksdata": colddrinksdata,
        "total_price": total_price,
    }
    return render(request,"Cold-drinks.html",context)


class ColdDrinksUpdate(View):
    def get(self,request,id):
        colddata = Cold_drinks.objects.get(id=id)
        colddrinksfm = ColdDrunksForm(instance=colddata)
        return render(request,"cold-drinks-update.html",{'colddrinksfm':colddrinksfm})

    def post(self,request,id):
        colddata = Cold_drinks.objects.get(id=id)
        colddrinksfm = ColdDrunksForm(request.POST,instance=colddata)
        if colddrinksfm.is_valid():
            colddrinksfm.save()
            return redirect("cold-drinks")

class DeleteColdDrinks(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        colddrinksdata = Cold_drinks.objects.get(id=id)
        colddrinksdata.delete()
        return redirect("cold-drinks")

@login_required(login_url="login")
def VodkaDrinksInsert(request):
    if request.method == 'POST':
        vodkadrinksform = VodkaDrinksForm(request.POST)
        if vodkadrinksform.is_valid():
            vodkadrinksform.save()
            return redirect("vodka-drinks")
    else:
        vodkadrinksform = VodkaDrinksForm()

    vodkadrinksdata = Vodka_drinks.objects.all()
    total_price = sum(item.price for item in vodkadrinksdata)
    context = {
        "vodkadrinksform": vodkadrinksform,
        "vodkadrinksdata": vodkadrinksdata,
        "total_price": total_price,
    }
    return render(request,"Vodka-drinks.html",context)

class VodkaDrinksUpdate(View):
    def get(self,request,id):
        vodkadata = Vodka_drinks.objects.get(id=id)
        vodkadriksfm = VodkaDrinksForm(instance=vodkadata)
        return render(request,"Vodka-driks-update.html",{'vodkadriksfm':vodkadriksfm})

    def post(self,request,id):
        vodkadata = Vodka_drinks.objects.get(id=id)
        vodkadriksfm = VodkaDrinksForm(request.POST,instance=vodkadata)
        if vodkadriksfm.is_valid():
            vodkadriksfm.save()
            return redirect("vodka-drinks")


class DeleteVodkaDrinks(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        vodkadrinksdata = Vodka_drinks.objects.get(id=id)
        vodkadrinksdata.delete()
        return redirect("vodka-drinks")
@login_required(login_url="login")
def PivoDrinksInsert(request):
    if request.method == 'POST':
        pivodrinksform = PivoDrinksForm(request.POST)
        if pivodrinksform.is_valid():
            pivodrinksform.save()
            return redirect("privo-insert")
    else:
        pivodrinksform = PivoDrinksForm()

    pivodrinksdata = Beer_drinks.objects.all()
    total_price = sum(item.price for item in pivodrinksdata)
    context = {
        "pivodrinksform": pivodrinksform,
        "pivodrinksdata": pivodrinksdata,
        "total_price": total_price,
    }
    return render(request,"Privo-drinks.html",context)

class PivoDrinksUpdate(View):
    def get(self,request,id):
        pivodrinksdata = Beer_drinks.objects.get(id=id)
        pivodrinksfm = PivoDrinksForm(instance=pivodrinksdata)
        return render(request,"Pivo-drinks-update.html",{'pivodrinksfm':pivodrinksfm})

    def post(self,request,id):
        pivodrinksdata = Beer_drinks.objects.get(id=id)
        pivodrinksfm = PivoDrinksForm(request.POST,instance=pivodrinksdata)
        if pivodrinksfm.is_valid():
            pivodrinksfm.save()
            return redirect("privo-insert")

class DeletePivaDrinks(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        pivadrinksdata = Beer_drinks.objects.get(id=id)
        pivadrinksdata.delete()
        return redirect("privo-insert")

@login_required(login_url="login")
def KnevaFootInsert(request):
    if request.method == 'POST':
        knevaform = KnevaFootForm(request.POST)
        if knevaform.is_valid():
            knevaform.save()
            return redirect("kneva-insert")
    else:
        knevaform = KnevaFootForm()

    knevadata = Knivu_foot.objects.all()
    # Calculate total
    total_price = sum(item.price for item in knevadata)
    context = {
        "knevaform": knevaform,
        "knevadata": knevadata,
        "total_price": total_price,
    }
    return render(request,"Kineva.html",context)


class KnevaFootUpdate(View):
    def get(self,request,id):
        knevadata = Knivu_foot.objects.get(id=id)
        knevafootfm = KnevaFootForm(instance=knevadata)
        return render(request,"Kineva-update.html",{'knevafootfm':knevafootfm})

    def post(self,request,id):
        knevadata = Knivu_foot.objects.get(id=id)
        knevafootfm = KnevaFootForm(request.POST,instance=knevadata)
        if knevafootfm.is_valid():
            knevafootfm.save()
            return redirect("kneva-insert")


class DeleteKrnevaFoot(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        krnevafootdata = Knivu_foot.objects.get(id=id)
        krnevafootdata.delete()
        return redirect("kneva-insert")
@login_required(login_url="login")
def zakazOlish(request):
    kabinadata = office.objects.all()
    context = {
        'kabinadata': kabinadata,
        'soups': Soups_foot.objects.all(),
        'salads': Salads_foot.objects.all(),
        'dishes': Dishes_to_order.objects.all(),
        'pizzas': Pizza_foot.objects.all(),
        'breads': Bread.objects.all(),
        'breadbazas': Breadbaza.objects.all(),
        'vynechkas': Vynechka_foot.objects.all(),
        'girils': Giril_foot.objects.all(),
        'homes': Home_foot.objects.all(),
        'tea_karnas': Tea_Karna_foot.objects.all(),
        'cold_drinks': Cold_drinks.objects.all(),
        'vodka_drinks': Vodka_drinks.objects.all(),
        'beer_drinks': Beer_drinks.objects.all(),
        'knivu': Knivu_foot.objects.all(),
    }
    return render(request,"zakaz-olish.html",context)

@login_required(login_url="login")
def JamiZakaz(request):
    if request.method == "POST":
        payment_method = request.POST.get("money")
        kabina_id = request.POST.get("kabina")
        stol_id = request.POST.get("stol")
        tip_id = request.POST.get("tip")
        soup_id = request.POST.get("soups")
        salad_id = request.POST.get("salads")
        dish_id = request.POST.get("dishes")
        pizza_id = request.POST.get("pizzas")
        bread_id = request.POST.get("breads")
        vynechka_id = request.POST.get("vynechkas")
        giril_id = request.POST.get("girils")
        home_id = request.POST.get("homes")
        tea_karna_id = request.POST.get("tea_karnas")
        cold_drink_id = request.POST.get("cold_drinks")
        vodka_drink_id = request.POST.get("vodka_drinks")
        beer_drink_id = request.POST.get("beer_drinks")
        knivu_id = request.POST.get("knivu")

        payment_method_display = dict(OrderBaza.PAYMENT_CHOICES).get(payment_method, "Unknown")
        total_price = 0
        items = []


        if kabina_id:
            item = office.objects.get(id=kabina_id)
            items.append({'name': item.kobina, 'price': 0})

        if stol_id:
            item = office.objects.get(id=kabina_id)
            items.append({'name': item.stol, 'price': 0})

        if tip_id:
            item = office.objects.get(id=kabina_id)
            items.append({'name': item.turi, 'price': 0})

        if soup_id:
            item = Soups_foot.objects.get(id=soup_id)
            total_price += item.price
            items.append({'name': item.name, 'price': item.price,'payment_method_display': payment_method_display})

        if salad_id:
            item = Salads_foot.objects.get(id=salad_id)
            total_price += item.price
            items.append({'name': item.name, 'price': item.price, 'payment_method_display': payment_method_display})

        if dish_id:
            item = Dishes_to_order.objects.get(id=dish_id)
            total_price += item.price
            items.append({'name': item.name, 'price': item.price, 'payment_method_display': payment_method_display})

        if pizza_id:
            item = Pizza_foot.objects.get(id=pizza_id)
            total_price += item.price
            items.append({'name': item.name, 'price': item.price, 'payment_method_display': payment_method_display})

        if bread_id:
            item = Breadbaza.objects.get(id=bread_id)
            total_price += item.price
            items.append({'name': item.name, 'price': item.price, 'payment_method_display': payment_method_display})

        if vynechka_id:
            item = Vynechka_foot.objects.get(id=vynechka_id)
            total_price += item.price
            items.append({'name': item.name, 'price': item.price, 'payment_method_display': payment_method_display})

        if giril_id:
            item = Giril_foot.objects.get(id=giril_id)
            total_price += item.price
            items.append({'name': item.name, 'price': item.price, 'payment_method_display': payment_method_display})

        if home_id:
            item = Home_foot.objects.get(id=home_id)
            total_price += item.price
            items.append({'name': item.name, 'price': item.price, 'payment_method_display': payment_method_display})

        if tea_karna_id:
            item = Tea_Karna_foot.objects.get(id=tea_karna_id)
            total_price += item.price
            items.append({'name': item.name, 'price': item.price, 'payment_method_display': payment_method_display})

        if cold_drink_id:
            item = Cold_drinks.objects.get(id=cold_drink_id)
            total_price += item.price
            items.append({'name': item.name, 'price': item.price, 'payment_method_display': payment_method_display})

        if vodka_drink_id:
            item = Vodka_drinks.objects.get(id=vodka_drink_id)
            total_price += item.price
            items.append({'name': item.name, 'price': item.price, 'payment_method_display': payment_method_display})

        if beer_drink_id:
            item = Beer_drinks.objects.get(id=beer_drink_id)
            total_price += item.price
            items.append({'name': item.name, 'price': item.price, 'payment_method_display': payment_method_display})

        if knivu_id:
            item = Knivu_foot.objects.get(id=knivu_id)
            total_price += item.price
            items.append({'name': item.name, 'price': item.price, 'payment_method_display': payment_method_display})

        for item in items:
            order_entry = OrderBaza(
                name=item['name'],
                price=item['price'],
                piece=1,  # Set this to the actual quantity if available
                time_of_year=timezone.now(),
                payment_method=payment_method,
            )
            order_entry.save()
        context = {
            "items": items,
            "total_price": total_price,
        }


    return render(request,"zakaz-olish.html",context)

@login_required(login_url="login")
def ZakazTable(request):
    filter_by = request.GET.get('filter_by', 'all')

    Orderdata = OrderBaza.objects.all().order_by('id')
    today = timezone.now().date()

    if filter_by == 'day':
        Orderdata = Orderdata.filter(time_of_year__gte=today)
    elif filter_by == 'week':
        start_of_week = today - timedelta(days=today.weekday())  # Get the start of the week (Monday)
        Orderdata = Orderdata.filter(time_of_year__gte=start_of_week)
    elif filter_by == 'month':
        start_of_month = today.replace(day=1)  # Get the start of the current month
        Orderdata = Orderdata.filter(time_of_year__gte=start_of_month)

    total_price = sum(i.price for i in Orderdata)
    total_piece = sum(y.piece for y in Orderdata)

    paginator = Paginator(Orderdata, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "Orderdata": Orderdata,
        "total_price": total_price,
        "total_piece": total_piece,
        "page_obj": page_obj,
        "selected_filter": filter_by,
    }
    return render(request,"operator-zakaz-table.html",context)

@login_required(login_url="login")
def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to a success page or profile page
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'profile.html', {'form': form, 'username': request.user.username})


@login_required(login_url="login")
def AdminProfile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('admin-profile')  # Redirect to a success page or profile page
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'Adminprofile.html', {'form': form, 'username': request.user.username})


