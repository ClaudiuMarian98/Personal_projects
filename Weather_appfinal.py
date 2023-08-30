from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
import datetime as dt
import pytz
from PIL import Image, ImageTk
import tkinter as tk
import requests







class SearchPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Search Page")
        self.geometry("523x700+100+200")
        self.resizable(False,False)


        self.background_image = Image.open("C:\\Users\\gabi1\\Downloads\\haibaietii.jpg")  
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)



      #search bar



        self.textfield=tk.Entry(self,justify="center",width=17, font=("poppins",25,"bold"),bg="#c0c0c0",border=0,fg="black")
        self.textfield.place(x=100,y=480)


        


        
  
  
      #search button
        
        self.search_button = tk.Button(self, text="Search",width=25,height=3,cursor="hand2", command=self.show_weather_page)
        self.search_button.place(x=162,y=570)


    def show_weather_page(self):
        location = self.textfield.get()
        WeatherPage(self, location)

class WeatherPage(tk.Toplevel):
    def __init__(self, master=None, location=""):
        super().__init__(master)
        self.title("Weather Information")
        self.geometry("523x700+100+200")
        self.resizable(False,False)
        self.configure(bg="#86d4eb")


        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        API_KEY = "6bdd9c7f13fa1b8b66be51d0f93a1c48"
        

        url_final= base_url + "appid=" + API_KEY + "&q=" + location


        response = requests.get(url_final).json()

        def kelvin_to_celsius(kelvin):
            celsius=kelvin-273.15
            return celsius

        temp_kelvin=response['main']['temp']
        temp_celsius=kelvin_to_celsius(temp_kelvin)
        feels_like_kelvin=response['main']['feels_like']
        feels_like_celsius=kelvin_to_celsius(feels_like_kelvin)
        wind_speed=response['wind']['speed']
        humidity=response['main']['humidity']
        description=response['weather'][0]['description']
        sunrise_time=dt.datetime.utcfromtimestamp(response['sys']['sunrise']+response['timezone'])
        sunset_time=dt.datetime.utcfromtimestamp(response['sys']['sunset']+response['timezone'])
        High=kelvin_to_celsius(response['main']['temp_max'])
        Low=kelvin_to_celsius(response['main']['temp_min'])
        

        self.weather_label = tk.Label(self, text=f"{location}",anchor="center",justify="center",width="19",font=("poppins",34),bg="#86d4eb",fg="white")
        self.weather_label.place(x=0,y=140)

        self.degrees_label=tk.Label(self,text=f"{temp_celsius:.2f}\u00b0",width="11",anchor="center",justify="center",font=("poppins",60),bg="#86d4eb",fg="white")
        self.degrees_label.place(x=0,y=190)

        self.description_label=tk.Label(self, text=f"{description}",anchor="center",justify="center",width="40",font=("poppins",16),bg="#86d4eb",fg="white")
        self.description_label.place(x=0,y=285)

        #highlow
        self.highlow_label=tk.Label(self, text=f"H:{High:.2f}   L:{Low:.2f}",anchor="center",justify="center",width="40",font=("poppins",16),bg="#86d4eb",fg="white")
        self.highlow_label.place(x=0,y=315)




        #windspeed

        self.windspeed_label=tk.Label(self, text=f"Windspeed:             {wind_speed} ms",anchor="w",justify="center",width="40",font=("poppins",16),bg="#86d4eb",fg="white")
        self.windspeed_label.place(x=0,y=450)

        #humidity
        self.humidity_label=tk.Label(self, text=f"Humidity:                  {humidity} %",anchor="w",justify="center",width="40",font=("poppins",16),bg="#86d4eb",fg="white")
        self.humidity_label.place(x=0,y=480)

        #sunrise
        self.sunrise_label=tk.Label(self, text=f"Sunrise:                  {sunrise_time}",anchor="w",justify="center",width="40",font=("poppins",16),bg="#86d4eb",fg="white")
        self.sunrise_label.place(x=0,y=510)

        #sunset
        self.sunset_label=tk.Label(self, text=f"Sunset:                   {sunset_time}",anchor="w",justify="center",width="40",font=("poppins",16),bg="#86d4eb",fg="white")
        self.sunset_label.place(x=0,y=540)


       



        self.back_button = tk.Button(self, text="Back", command=self.destroy)

    

if __name__ == "__main__":
    app = SearchPage()
    app.mainloop()
