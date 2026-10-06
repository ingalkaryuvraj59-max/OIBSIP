import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "1664eea894aa91c37c8d777d25e206a0"


def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showwarning("Warning", "Please enter city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if data.get("cod") != 200:
            result_label.config(text="City not found or API inactive")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        condition = data["weather"][0]["description"]
        wind = data["wind"]["speed"]

        result = (
            f"📍 City: {city}\n\n"
            f"🌡 Temperature: {temp}°C\n\n"
            f"💧 Humidity: {humidity}%\n\n"
            f"🌬 Wind Speed: {wind} m/s\n\n"
            f"📊 Pressure: {pressure} hPa\n\n"
            f"☁ Condition: {condition}"
        )

        result_label.config(text=result)

    except Exception as e:
     result_label.config(text=f"Error: {e}")
     print("ERROR:", e)


# Main Window
root = tk.Tk()
root.title("Weather App")
root.geometry("450x600")
root.config(bg="#87CEEB")
root.resizable(False, False)

# Heading
heading = tk.Label(
    root,
    text="☁ Chek  Weather..",
    font=("Arial", 24, "bold"),
    bg="#0C2A95",
    fg="white"
)
heading.pack(pady=20)

# Input Box
city_entry = tk.Entry(
    root,
    font=("Arial", 16),
    width=20,
    justify="center",
    bd=6
)
city_entry.pack(pady=15)

# Button
search_btn = tk.Button(
    root,
    text="Get Weather",
    font=("Arial", 14, "bold"),
    bg="#0EE211",
    fg="white",
    padx=15,
    pady=6,
    command=get_weather
)
search_btn.pack(pady=10)

# Result Box
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    bg="gray",
    fg="black",
    width=30,
    height=12,
    relief="ridge",
    bd=3,
    justify="left",
    anchor="nw",
    padx=10,
    pady=10
)
result_label.pack(pady=20)

# Footer
footer = tk.Label(
    root,
    text="Made by Uv Applicarion...",
    font=("Arial", 10),
    bg="#436876",
    fg="white"
)
footer.pack(side="bottom", pady=11)

root.mainloop()

# Program write by Yuvraj Ingalkar