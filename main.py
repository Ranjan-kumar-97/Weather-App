import tkinter as tk                                        #import tkinter to make GUI
import requests                                             #import request to fetch data from URL
import os                                                   #import os to make enviernment variable
from PIL import Image,ImageTk                               #import Pillow from image to add backgrounf inage in frame

os.environ["key"]='72f37571bd15b8978674b1fd3b70dfdc'        #making key as environment varibale

def form_response(weather):                                 #function to assign data fetched from Open weather API in varibales to print weather data
    try: 
        city=weather['name']                                #Assign place name in city variable
        condition=weather['weather'][0]['description']      #Assign weather description in condition variable
        temp=weather['main']['temp']                        #Assign tampratre in fahrenheit in temp varibale
        feel_temp=weather['main']['feels_like']             #Assign feel like temprature in feel_temp varibale
        humidity=weather['main']['humidity']                #Assign Humidity in humodity varibale
        wind_speed=weather['wind']['speed']                 #assign speed of wind in wind_speed varibale
        final_str=" Place : %s \n Condition : %s \n Temprature(f) : %s* \n Feels Like Temprature(f) : %s* \n Humidity(G.m3) : %s \n Wind Speed(km/hr) : %s " %(city,condition,temp,feel_temp,humidity,wind_speed) #Assign all data in final_string varible to print all data 
    except:                                                 #if any error occures in data fetching then this part will be printed
        final_str="There is a Problem in Fetching Data" 
    return final_str



def get_weather(city):                                      #funcrion to fetch data from Open weather API with URL and Key
    weather_key=os.environ["key"]                           #Assing environment varibale key in weather_key varibale
    url='https://api.openweathermap.org/data/2.5/weather'   #URL of oepn weather API
    params={'APPID':weather_key,'q':city,'units':'imperial'}#Parameters to fetch wether data of specified place
    response=requests.get(url,params)                       #fetching data and assign in response varibale
    weather=response.json()                                 #Assign dfeched data (json file) in weather varibale
    result['text']=form_response(weather)                   





root=tk.Tk() 

root.title("Mausam")                                        #GUI title as Mausan
root.geometry("600x500")

img=Image.open("./weather_bg.png")                          #Backdround Image of GUI
img=img.resize((600,500),Image.ANTIALIAS)
img_photo=ImageTk.PhotoImage(img)
bg_lbl=tk.Label(root,image=img_photo)
bg_lbl.place(x=0,y=0,width=600,height=500)

head_title=tk.Label(bg_lbl,text="Enter City/ State/ Country (Including Over 2L Places!)",fg="red",bg="white",font=("Times new roman", 16,'bold'))
head_title.place(x=30,y=20)

frame_one=tk.Frame(bg_lbl,bg="SkyBlue",bd=5)                #First frame to search pace and Button
frame_one.place(x=30, y=60, width=530, height=65)

txt_box=tk.Entry(frame_one,font=("Times new roman", 25),width=24,) #Text box to search city
txt_box.grid(row=0,column=0,sticky='W')

btn=tk.Button(frame_one,text="Check",fg="Green",font=("Times new roman", 20,"bold"),command=lambda:get_weather(txt_box.get()))
btn.grid(row=0,column=3,padx=10)                            #Button to check weather

frame_two=tk.Frame(bg_lbl,bg="SkyBlue",bd=5)                #Frame two to show result
frame_two.place(x=30, y=130, width=530, height=350)

result=tk.Label(frame_two,font=("Times new roman", 20,"bold"),justify='left', anchor='nw') #Lable to show weather data
result.place(relwidth=1,relheight=1)


root.mainloop()