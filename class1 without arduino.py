import astropy.units as u
import matplotlib.pyplot as plt
import threading
import tkinter

from pyongc.ongc import listObjects
from pyongc.ongc import Dso
from astropy.coordinates import AltAz, EarthLocation, SkyCoord
from astropy.time import Time
from astropy.visualization import astropy_mpl_style, quantity_support
from datetime import datetime
from PIL import ImageTk, Image


def button_action(name, normal):
    global Name
    Name = name
    normal = str(normal)

    image = Image.open("photos/" + normal+".jpg").resize((500,500))
    photo = ImageTk.PhotoImage(image=image)

    label = tkinter.Label(root, image=photo)
    label.image = photo
    label.grid(row =12,column=12)

    x=normal
    


def updating():
    plt.style.use(astropy_mpl_style)
    quantity_support()
    
    if Name == "Moon":
        coord = "22h41m14s -13d40m06s"

    elif Name =="Sun":
        coord = "12h14m41s -01d35m31s"

    elif Name == "North Star":
        north = Dso("ngc188")
        coord = north.ra + north.dec

    elif Name =="Mercury":
        coord = "11h16m21s +06d24m45s"
    
    elif Name =="Venus":
        coord = "09h29m07s +11d09m43s"

    elif Name =="Mars":
        coord = "13h14m51s -07d29m43s"

    elif Name =="Jupiter":
        coord = "02h50m45s +14d55m34s"

    elif Name =="Saturn":
        coord = "22h17m19s -12d33m09s"

    elif Name =="Uranus":
        coord = "03h21m38s +18d08m33s"

    elif Name =="Neptune":
        coord = "23h47m33s -02d44m25s"

    else:

        constellation = Name
        print(constellation)
        objectList = listObjects(catalog="NGC", constellation=[str(constellation), ])
        s = objectList[0]

        dec = s.dec
        ra = s.ra
        coord = ra + dec

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.date()
    timed = Time(str(current_date) + " " + current_time) - utcoffest
    consti = SkyCoord(coord, unit=(u.hourangle,u.deg))
    altaz = consti.transform_to(AltAz(obstime=timed,location=bear_mountain))
    altCommand = str(altaz.alt).partition("d")[0]

    azCommand = str(altaz.az).partition("d")[0]

    print(altCommand)

    print(azCommand)
    threading.Timer(2, updating).start()

def moon():
    global Name
    Name = "Moon"

def sun():
    global Name
    Name = "Sun"

def north_Star():
    global Name
    Name = "North Star"

def mercury():
    global Name
    Name = "Mercury"  

def venus():
    global Name
    Name = "Venus"

def mars():
    global Name
    Name = "Mars"

def jupiter():
    global Name
    Name = "Jupiter"

def saturn():
    global Name
    Name = "Saturn"

def uranus():
    global Name
    Name = "Uranus"

def neptune():
    global Name
    Name = "Neptune"

Name = "Moon"

root = tkinter.Tk()
root.geometry("1920x1080")

root.title("Astral-Pointer")

with open('consti.txt', 'r') as file:
    button_name = file.read().split(", ")
number = len(button_name)

rootList = []

utcoffest = +5.5*u.hour
print(utcoffest)

bear_mountain = EarthLocation(lat=26.2303*u.deg, lon= 78.1689*u.deg, height= 1033*u.m)

for i in range(number):
    plt.style.use(astropy_mpl_style)
    quantity_support()
    name = str(button_name[i]).split(":")
    iau, normal = name[0],name[1]
    objectList = listObjects(catalog="NGC", constellation=[iau,])
    s = objectList[0]

    dec = s.dec
    ra = s.ra
    coord = ra + dec

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.date()
    timed = Time(str(current_date) + " " + current_time) - utcoffest
    consti = SkyCoord(coord, unit=(u.hourangle,u.deg))

    altaz = consti.transform_to(AltAz(obstime=timed,location=bear_mountain))

    out = float(str(altaz.alt.to_string(unit=u.rad,)).replace(" rad", ""))

    if out > -0.785398 and out< 0.785398:
        print(normal)
        rootList.append(objectList)

    else:
        print("Noooooooooooooooooooo")


rootnum = len(rootList)
columns=6
label = tkinter.Label(text="Please choose the constellation:- ").grid(row=0, column=0)
others = tkinter.Label(text="Others:-").grid(row=0,column =9)
nStarBtn = tkinter.Button(root, text = "North Star", command=lambda : north_Star()).grid(row=1, column=11, padx=40, pady=10)
moonBtn = tkinter.Button(root, text="Moon", command=lambda : moon()).grid(row = 1, column=10, padx=40, pady=10)
SunBtn = tkinter.Button(root, text = "Sun", command=lambda : sun()).grid(row=2, column=10, padx=40, pady=10)
Mercury = tkinter.Button(root, text = "Mercury", command=lambda : mercury()).grid(row=3, column=10, padx=40, pady=10)
Venus = tkinter.Button(root, text = "Venus", command=lambda : venus()).grid(row=4, column=10, padx=40, pady=10)
Mars = tkinter.Button(root, text = "Mars", command=lambda : mars()).grid(row=5, column=10, padx=40, pady=10)
Jupiter = tkinter.Button(root, text = "Jupiter", command=lambda : jupiter()).grid(row=6, column=10, padx=40, pady=10)
Saturn = tkinter.Button(root, text = "Saturn", command=lambda : saturn()).grid(row=7, column=10, padx=40, pady=10)
Uranus = tkinter.Button(root, text = "Uranus", command=lambda : uranus()).grid(row=8, column=10, padx=40, pady=10)
Neptune = tkinter.Button(root, text = "Neptune", command=lambda : neptune()).grid(row=9, column=10, padx=40, pady=10)

for i in range(rootnum):
    row = i //columns
    col = i%columns
    name = str(button_name[i]).split(":")
    iau, normal = name[0],name[1]
    button = tkinter.Button(root, text=normal, command= lambda btn = iau: button_action(btn, normal)).grid(row=row+1, column=col, padx=40, pady=10)


updating()

root.mainloop()