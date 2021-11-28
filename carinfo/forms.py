from django import forms
import datetime


CAR_MAKERS = [("CAR MAKER","CAR MAKER"),
("ASTON MARTIN","ASTON MARTIN"),
("TESLA","TESLA"),
("JAGUAR","JAGUAR"),
("MASERATI","MASERATI"),
("LAND ROVER","LAND ROVER"),
("ROLLS ROYCE","ROLLS ROYCE"),
("TOYOTA","TOYOTA"),
("MERCEDES-BENZ","MERCEDES-BENZ"),
("BMW","BMW"),
("BUGATTI","BUGATTI")]

CAR_MODELS = [("CAR MODEL","CAR MODEL")]

MIN_YEAR = 2000
MAX_YEAR = datetime.datetime.now().year
BEGIN_YEAR_CHOICE = [("Begin Year","Begin Year")] + [(i,i) for i in range(MIN_YEAR,MAX_YEAR+1)]
END_YEAR_CHOICE = [("End Year","End Year")] + [(i,i) for i in range(MIN_YEAR,MAX_YEAR+1)]


class SubmitForm(forms.Form):
    car_maker = forms.fields.ChoiceField(label="Car Maker",choices=CAR_MAKERS)
    car_model = forms.fields.ChoiceField(label="Car Model",choices=CAR_MODELS)
    begin_year  = forms.fields.ChoiceField(label="Begin Year",choices=BEGIN_YEAR_CHOICE)
    end_year  = forms.fields.ChoiceField(label="End Year",choices=END_YEAR_CHOICE)

