from tkinter import *
import requests

API_KEY = "YOUR API KEY IN OpenWeather"

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"


# ---------------------------------------------------FUNCTIONALITY-----------------------------------------------------#

def get_weather():
    params = {
        "q": entry.get(),
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(url=API_ENDPOINT, params=params)
    response.raise_for_status()
    data = response.json()

    city_name = entry.get()
    if city_name == data["name"]:
        temperature = data["main"]["temp"]
        condition = data["weather"][0]["description"]

        label.config(text=city_name)
        temp_label.config(text=f"{temperature}°C")

        condition_label.config(text=condition)

    else:
        temp_label.config(text="City Not Found")


# ----------------------------------------------------UI SETUP---------------------------------------------------------#

window = Tk()
window.title("Weather App")
window.config(padx=50, pady=50)

label = Label(text="Enter city name:", font=("Helvetica", 20, "italic"))
label.grid(column=1, row=0)

temp_label = Label(text="", font=("Helvetica", 18))
temp_label.grid(column=1, row=3)

canva = Canvas(width=260, height=260)
logo = PhotoImage(file="weather-icon-png.png")
canva.create_image(130, 130, image=logo)
canva.grid(column=1, row=4)

condition_label = Label(text="", font=("Helvetica", 18))
condition_label.grid(column=1, row=5)

entry = Entry(width=42)
entry.grid(column=1, row=1)

button = Button(text="Get Weather", width=35, command=get_weather)

button.grid(column=1, row=2)

window.mainloop()
