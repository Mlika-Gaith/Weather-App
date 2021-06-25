import tkinter as tk
import requests
from math import *
from PIL import Image, ImageTk

HEIGHT = 500
WIDTH = 600


# b6aea90e84f94062c9ebcfa23711dc94
# api.openweathermap.org/data/2.5/forecast?q={city name},{state code},{country code}&appid={API key}

def format_response(weather):
    try:
        city = weather['name']
        country = weather['sys']['country']
        weatherType = weather['weather'][0]['main']
        weatherDesc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        feels_like = weather['main']['feels_like']
        humidity = weather['main']['humidity']
        final_str = 'City : ' + str(city) + '\nCountry : ' + str(country) + '\nWeather : ' + str(
            weatherType) + '\nWeather Description : ' + str(weatherDesc) + '\nTemperature : ' + str(
            ceil(temp)) + ' °C\nFeels Like : ' + str(ceil(feels_like)) + ' °C\nHumidity : ' + str(humidity)
    except:
        final_str = "There was a Problem retrieving infomation"
    return final_str


def get_weather(city):
    weather_key = 'b6aea90e84f94062c9ebcfa23711dc94'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather_json = response.json()
    lower_label['text'] = format_response(weather_json)
    icon_name = weather_json['weather'][0]['icon']
    open_image(icon_name)



def open_image(icon_name):
    size = int(lower_frame.winfo_height() * 0.25)
    img = ImageTk.PhotoImage(Image.open('./img/' + icon_name + '.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0, 0, anchor='nw', image=img)
    weather_icon.image = img


root = tk.Tk()
root.title("Weather APP")
root.iconbitmap('cloudy.ico')

canva = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canva.pack()

background_image = tk.PhotoImage(file="landscape.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1, rely=0.5)

frame = tk.Frame(root, bg="#c9184a", bd=4, relief="flat")
frame.place(relheight=0.1, relwidth=0.75, relx=0.5, rely=0.1, anchor='n')

entry = tk.Entry(frame, bd=1, relief="flat", font=('Bahnschrift SemiBold SemiConden', 11))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", bd=1, relief="flat", command=lambda: get_weather(entry.get()),
                   font=('Bahnschrift SemiBold SemiConden', 13), bg='#ff8fa3', fg='black')
button.place(relx=0.69, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg="#c9184a", bd=10, relief="flat")
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

lower_label = tk.Label(lower_frame, font=('Bahnschrift SemiBold SemiConden', 13), anchor='nw', justify='left', bd=8)
lower_label.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(lower_label, bd=0)
weather_icon.place(relx=0.75, rely=0, relwidth=1, relheight=0.5)

if __name__ == '__main__':
    root.mainloop()
