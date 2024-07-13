import tkinter as tk
import requests
from tkinter import messagebox


def getWeather():
    global city,api
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06c921750b9a82d8f5d1294e1586276f"
    global condition,temp,min_temp,max_temp,pressure,humidity,wind,lat,lon
    json_data = requests.get(api).json()
    condition=json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    lat = json_data['coord']['lat']
    lon = json_data['coord']['lon']



def coord():
  info0 = "Lattitude:"+str(lat) + "\n" +"Longitude"+ str(lon)
  label1.config(text=info0, bg="lightgreen")

def temp1():
  info1 =  condition + "\n" + str(temp) + "°C"
  label1.config(text=info1, bg="lightgreen")

def minmax():
    info2="minimum temp"+str(min_temp)+ "°C"+"\n"+"maximum temp"+str(max_temp)+ "°C"
    label1.config(text=info2, bg="lightgreen")

def press():
    info3="Pressure: " + str(pressure)
    label1.config(text=info3, bg="lightblue")

def humid():
        info4 = "Humidity: " + str( humidity)
        label1.config(text=info4, bg="lightgreen")

def winds():
    info5 = "Wind Speed: " + str(wind)
    label1.config(text=info5,bg="lightgreen")

def CLOSE():
    if messagebox.askyesno(title="quit?",message="do you really want to quit?"):
      root.destroy()



root = tk.Tk()
root.geometry("600x400")
root.configure(bg="beige")
root.title("Weather App")
f = ("Arial", 15, "bold")
t = ("Arial", 25, "bold")


label0= tk.Label(root,text="City Name", font="Helvetica")
label0.place(x=30)
textField = tk.Entry(root, font=t,width=50)
textField.focus()
textField.pack(pady=30,padx=25)





buttonframe1 =tk.Frame(root)
buttonframe1.columnconfigure(0,weight=1)
buttonframe1.columnconfigure(1,weight=1)
btn0=tk.Button(buttonframe1,text="Enter",  font=("Helvetica", 14),fg="white", bg="lightblue",command = getWeather,border="3")
btn0.grid(row=0,column=0,sticky=tk.W+tk.E)
btn01 = tk.Button(buttonframe1, text="Clear", font=("Helvetica", 14),fg="white", bg="lightblue")
btn01.grid(row=0,column=1,sticky=tk.W+tk.E)
buttonframe1.pack(fill="x",padx=50)
btn01.config(command=lambda: textField.delete(0, tk.END))


buttonframe =tk.Frame(root)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)

btn1=tk.Button(buttonframe,text="Temperature",font=f,command=temp1,fg="white", bg="black")
btn1.grid(row=0,column=0,sticky=tk.W+tk.E)
btn2=tk.Button(buttonframe,text="Minimum and Maximum Temp",font=f,command=minmax,fg="white", bg="black")
btn2.grid(row=0,column=1,sticky=tk.W+tk.E)
btn3=tk.Button(buttonframe,text="Pressure",font=f,command=press,fg="white", bg="black")
btn3.grid(row=0,column=2,sticky=tk.W+tk.E)
btn4=tk.Button(buttonframe,text="Humidity",font=f,command=humid,fg="white", bg="black")
btn4.grid(row=1,column=0,sticky=tk.W+tk.E)
btn5=tk.Button(buttonframe,text="Wind Speed",font=f,command=winds,fg="white", bg="black")
btn5.grid(row=1,column=1,sticky=tk.W+tk.E)
btn6=tk.Button(buttonframe,text="Coordinate",font=f,command=coord,fg="white", bg="black")
btn6.grid(row=1,column=2,sticky=tk.W+tk.E)
buttonframe.pack(fill="x",padx=35, pady=20)#can also use .place(x coord,y coord,height,weight)=to place manually





label1 = tk.Label(root, font=t)
label1.pack(pady=20)


root.protocol("WM_DELETE_WINDOW",CLOSE)
root.mainloop()
