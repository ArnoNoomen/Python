import json
import re
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty,NumericProperty,StringProperty
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.list import MDList, TwoLineListItem, ThreeLineListItem
from kivy.uix.label import Label

from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.storage.jsonstore import JsonStore
from html.parser import HTMLParser
from datetime import datetime
from kivy.graphics import Line
from kivy.graphics import Point

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    search_results = ObjectProperty()
    cities = StringProperty()
    popup = None

    def search_location(self):
        search_template = "http://api.openweathermap.org/data/2.5/" +"find?q={}&type=like&appid=e1c649083a337011ceb4d6b1958ba87c"
        search_url = search_template.format(self.search_input.text)
        request = UrlRequest(search_url,self.found_location,on_error= self.failed)
        self.popup = Popup(title='Request Sent',content=Label(text='Loading...'),size_hint=(None, None), size=(400, 400),auto_dismiss=True)
        self.popup.open()
        print(request.on_success)

    #if request failed then close current popup & open new popup & display error    
    def failed(self,request,data):
        self.popup.dismiss()
        self.popup = Popup(title='Request Failed!',content=Label(text='Connection error....try agian later'),size_hint=(None, None), size=(400, 400),auto_dismiss=True)
        self.popup.open()

    #if request succeeded then get response and add it to arraylist
    def found_location(self,request,data):
        data = json.loads(data.decode()) if not isinstance(data,dict) else data
        cities = ["{} ({})".format(d['name'],d['sys']['country'])for d in data['list']]
        if len(cities) == 0 :
            self.cities = "No Cities Found!"
            
        self.search_results.item_strings = cities   
        self.search_results.adapter.data.clear()
        self.search_results.adapter.data.extend(cities)
        self.search_results._trigger_reset_populate()
        self.popup.dismiss()
        print(cities)

class LocationButton(MDList):
    pass

class CurrentWeather(BoxLayout):
    location = StringProperty()
    conditions = StringProperty()
    temp = NumericProperty()
    temp_max =  NumericProperty()
    temp_min =  NumericProperty()
    conditions_image = StringProperty()

    def update_weather(self):
        ##regular expression to remover () from string ex: London (GB) we only want London with out (GB)
        m = re.match('[A-Za-z]+',self.location)
        print(self.location)
        print(m.group())
        fixed_location_format = m.group()
        weather_template = "http://api.openweathermap.org/data/2.5/" +"weather?q={}&units=metric&appid=e1c649083a337011ceb4d6b1958ba87c"
        weather_url = weather_template.format(fixed_location_format)
        request = UrlRequest(weather_url,self.found_weather)
        
    def found_weather(self,request,data):
        data = json.loads(data.decode()) if not isinstance(data,dict) else data 
        print(data)
        self.conditions = data['weather'][0]['description']
        self.conditions_image = "http://openweathermap.org/img/w/{}.png".format(data['weather'][0]['icon'])
        self.temp = data['main']['temp']
        self.temp_max = data['main']['temp_max']
        self.temp_min= data['main']['temp_min']
        print(self.conditions)


class WeatherRoot(BoxLayout):
    current_weather = ObjectProperty()
    locations = ObjectProperty()
    location_list = ObjectProperty()
    forecast = ObjectProperty()

    def __init__(self,**kwargs):
        super(WeatherRoot,self).__init__(**kwargs)
        self.store = JsonStore("weather_store.json")
        if self.store.exists("locations"):
           current_location = self.store.get("locations")["current_location"]
           self.show_current_weather(current_location)

    def show_current_weather(self,location):
        self.clear_widgets()

        # if self.current_weather is None:
        #     self.current_weather = CurrentWeather()
        # if self.locations is None:
        #     self.locations = Factory.Locations()
        #     if(self.store.exists("locations")):
        #         locations = self.store.get("locations")['locations']
        #         self.locations.location_list.adapter.data.extend(locations)
        
        # #if there is a location       
        # if location is not None:    
        #     self.current_weather.location = location
        #     #if location not in the location history list then add it
        #     if location not in self.locations.location_list.adapter.data:
        #         self.locations.location_list.adapter.data.append(location)
        #         self.locations.location_list._trigger_reset_populate()
        #         self.store.put("locations",locations=self.locations.location_list.adapter.data,current_location=location)   
        # else:
        #     self.current_weather.location = "New York"
        #     self.current_weather.update_weather()

                
        # self.current_weather.update_weather()     
        # self.add_widget(self.current_weather)

        
    def show_locations(self):
        self.clear_widgets()
        self.add_widget(self.locations)

    def show_add_location_form(self):
        self.clear_widgets()
        self.current_weather.conditions = ""
        self.current_weather.temp = 00
        self.current_weather.temp_max = 00
        self.current_weather.temp_min = 00
        self.add_widget(AddLocationForm())

    def clear_location_list(self):
        self.locations.location_list.adapter.data = []
        self.show_locations()
        self.store.put("locations",locations=[],current_location="")

    def show_forecast(self,location=None):
        self.clear_widgets()

        if self.forecast is None:
            self.forecast = Factory.Forecast()
        if location is not None:
            self.forecase.location = location

        self.forecast.update_weather()
        self.add_widget(self.forecast)      

class Forecast(BoxLayout):
    location = StringProperty("New York")
    forecast_container = ObjectProperty()

    def update_weather(self):   
        weather_template = "http://api.openweathermap.org/data/2.5/forecast/daily?q={}&units=metric&cnt=3&appid=e1c649083a337011ceb4d6b1958ba87c"
        weather_url = weather_template.format(self.location)
        request = UrlRequest(weather_url,self.found_forecast)

    def found_forecast(self,request,data):
        data = json.loads(data.decode()) if not isinstance(data,dict) else data
        self.forecast_container.clear_widgets()
        for day in data['list']:
            label = Factory.ForecastLabel()
            label.conditions = day['weather'][0]['description']
            label.conditions_image = "http://openweathermap.org/img/w/{}.png".format(day['weather'][0]['icon'])
            label.temp_max = day['temp']['max']
            label.temp_min = day['temp']['min']
            label.date = datetime.fromtimestamp(day['dt']).strftime(" %a %b %d")
            self.forecast_container.add_widget(label)
            print(data)

class WeatherApp(App):
    pass
   
if __name__ == '__main__':  
    WeatherApp().run()
  
    
