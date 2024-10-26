# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
import requests
import json
from weather_utils import get_weather, process_weather_data
import re

def go():
    city = entry.get()
    try:
        if city:
            data = get_weather(city)
            if data['cod'] == 200:
                dic = process_weather_data(data)
            else:
                raise Exception("Invalid location")
        else:
            raise Exception("Invalid location")
    except requests.exceptions.ConnectionError:
        messagebox.showwarning("Alert", "Computer not Connected to internet")
        return
    except ValueError:
        messagebox.showwarning("Alert", "Server Error")
        return
    except Exception as e:
        messagebox.showwarning("Alert", str(e))
        return

    main = Toplevel()
    main.geometry('450x450+200+200')
    main.title(city)
    main.geometry(f"{main.winfo_screenwidth()}x{main.winfo_screenheight()}+0+0")
    main.resizable(width=False, height=False)
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()
    
    tmp = f"{dic['today']['temp']}°C"
    tmp_min = f"Min : {dic['today']['min']}°C"
    tmp_max = f"Max : {dic['today']['max']}°C"

    canvas = Canvas(main, width=screen_width, height=screen_height)
    canvas.pack()
    canvas.create_text(screen_width/2, screen_height*0.1, text=city, fill="white", font="Comic 60")
    canvas.create_text(screen_width/2, screen_height*0.2, text=tmp, fill="white", font="Sans 40")
    canvas.create_text(screen_width*0.2, screen_height*0.2, text=tmp_min, fill="white", font="Sans 30")
    canvas.create_text(screen_width*0.8, screen_height*0.2, text=tmp_max, fill="white", font="Sans 30")

def matches(fieldValue, acListEntry):
    pattern = re.compile(re.escape(fieldValue) + '.*', re.IGNORECASE)
    return re.match(pattern, acListEntry)

if __name__ == '__main__':
    autocompleteList = ["New York", "London", "Tokyo", "Delhi", "Mumbai"]
    
    win = Tk()
    win.geometry("320x180+600+400")
    win.resizable(width=False, height=False)
    win.title('Weather Reporter')
    
    entry = Entry(win, width=32)
    entry.insert(END, 'Enter City Here ...')
    entry.place(relx=0.5, rely=0.5, anchor=CENTER)

    button = Button(win, text="GO", command=go, width=10, height=2)
    button.place(relx=0.5, rely=0.7, anchor=CENTER)

    win.mainloop()
