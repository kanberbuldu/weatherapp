import requests
from tkinter import *
from tkinter import messagebox

#Window option
window = Tk()
window.title("Weather App")
window.geometry("280x200")
FONT = ("Arial", 12, "bold")

def clear_label(weather_label=""):
    weather_label.after(1000, weather_label.destroy())


def show_weather():
    api_key = "f5eccd1935e67301b2a710abbce7876b"
    weather_location = enter_city.get()
    if weather_location == "":
        messagebox.showinfo(title='info', message="Enter City")
    else:
        # weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={
        # weather_location}&lang=tr&units=Metric&appid={api_key}")
        weather_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q= {weather_location}&lang=tr"
                                    f"&units=Metric&appid={api_key}")
        print(weather_data.json())

        try:
            weather_status = weather_data.json()['weather'][0]['description']
            weather_temp = weather_data.json()["main"]["temp"]
            weather_temp = int(weather_temp)
            result = f"{weather_location}: {weather_temp}\u00b0C\n{weather_status}".title()
            weather_label = Label(text=result, font=FONT)
            weather_label.place(x=10, y=70)

        except:
            messagebox.showerror(title="İnfo", message="City not found")

        finally:
            enter_city.delete(0, END)


button_show = Button(text="Show Weather", command=show_weather)
button_show.place(x=20, y=150)

clear_button = Button(text="Clear", command=clear_label)
clear_button.place(x=110, y=150)

weather_text = Label(text="City Name", font=FONT)
weather_text.place(x=20, y=2)

enter_city = Entry()
enter_city.place(x=10, y=30)

mainloop()
