from tkinter import *
from tkcalendar import Calendar
from datetime import date
import time

t = time.localtime()


root = Tk()
root.title('Jahresrechner DA-Discord')
root.geometry("500x400")



cal = Calendar(root, selectmode='day',
               year=t.tm_year, month=t.tm_mon,
               day=t.tm_mday)

cal.pack(pady=20)



def calc():
    dateinp = str(cal.get_date())
    dateinp = dateinp.split('/')
    year_inp = f"20{int(dateinp[2])}"
    month_inp = dateinp[0]
    day_inp = dateinp[1]
    date_input = date(int(year_inp), int(month_inp), int(day_inp))
    date_today = date.today()
    delta = date_today - date_input
    calyear = (((int(delta.days) / 30.5) / 6) + 1)
    calyear = str(calyear).split('.')
    year.config(text=f"Der User ist am {day_inp}.{month_inp}.{year_inp} gejoint und bekommt deshalb die Jahr {calyear[0]} Rolle")



# Add Button and Label
Button(root, text="Schuljahr ausrechnen",
       command=calc).pack(pady=20)

year = Label(root, text="")
year.pack(pady=20)

# Execute Tkinter
root.mainloop()