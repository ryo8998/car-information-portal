from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse, Http404
from django.template.response import TemplateResponse
from django.shortcuts import render
from carinfo.forms import SubmitForm
import requests
import datetime
import json

CAR_MAKERS = ["ASTON_MARTIN","TESLA","JAGUAR","MASERATI","LAND_ROVER","ROLLS_ROYCE","TOYOTA","MERCEDES_BENZ","BMW","BUGATTI"]
HEADERS = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

# Create your views here.
class IndexView(View):
    def get(self,request):
        return render(request,"carinfo/index.html",
        {"car_makers":CAR_MAKERS,"form":SubmitForm()})
    def post(self,request):
        car_maker = request.POST.get("car_maker")
        car_model = request.POST.get("car_model")
        begin_year = int(request.POST.get("begin_year"))
        end_year = int(request.POST.get("end_year"))

        results = []
        for year in range(begin_year,end_year+1):
            url = "https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getTrims&make={}&model={}&year={}".format(car_maker,car_model,year)
            print(url)
            data = fetchAPI(url)
            results += data["Trims"]
        form = SubmitForm(initial={
            "car_maker":car_maker,
            "car_model":car_model,
            "begin_year":begin_year,
            "end_year":end_year
        })
        if len(results) == 0: raise Http404("No result")

        return render(request,"carinfo/search_result.html",
        {"trims":results,
        "form":form }
        )

class ModelListView(View):
    def get(self,request,carmaker):
        url = "https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getModels&make={}&year={}".format(carmaker,datetime.datetime.now().year)
        data = fetchAPI(url)
        models = data["Models"]
        # has_this_year_model =  True if len(models) else False
        choices = {(model["model_name"],model["model_name"]) for model in models}
        form = SubmitForm(initial={"car_maker":carmaker})
        form.fields['car_model'].choices = choices
        return render(request,"carinfo/list.html",{
            "maker":carmaker,
            "models":models,
            "form":form,
            "message":"No Model Debuted in {}".format(datetime.datetime.now().year),
            "year":datetime.datetime.now().year
            })

class SearchResultView(View):
    def post(self,request):
        car_maker = request.POST.get("car_maker")
        car_model = request.POST.get("car_model")
        begin_year = int(request.POST.get("begin_year"))
        end_year = int(request.POST.get("end_year"))

        results = []
        for year in range(begin_year,end_year+1):
            url = "https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getTrims&make={}&model={}&year={}".format(car_maker,car_model,year)
            data = fetchAPI(url)
            results += data["Trims"]
        form = SubmitForm(initial={
            "car_maker":car_maker,
            "car_model":car_model,
            "begin_year":begin_year,
            "end_year":end_year
        })
        if len(results) == 0:
            raise Http404("No result")
        return render(request,"carinfo/search_result.html",
        {"trims":results,
        "form":form }
        )


def fetchAPI(url):
    response = requests.get(url,headers=HEADERS)
    response = response.text[2:-2]
    return json.loads(response)
