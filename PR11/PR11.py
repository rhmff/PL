import requests
from tkinter import *


def click():
    rep = txt.get()
    r = requests.get(f'https://api.github.com/repos/{rep}/{rep}')

    with open('C:\\Users\\all\\Downloads\\Telegram Desktop\\444.txt', 'a+') as f:
        if 'company' in r.json():
            f.write(f"'company': '{r.json()['company']}'\n")
        else:
            f.write("'company':")
            f.write('None\n')
        if 'created_at' in r.json():
            f.write(f"'created_at': '{r.json()['created_at']}'\n")
        else:
            f.write("'created_at: None'\n")
        if 'email' in r.json():
            f.write(f"'email': '{r.json()['email']}'\n")
        else:
            f.write("'email':")
            f.write('None\n')
        if 'id' in r.json():
            f.write(f"'id': '{r.json()['id']}'\n")
        else:
            f.write("'id: None'\n")
        if 'name' in r.json():
            f.write(f"'name': '{r.json()['name']}'\n")
        else:
            f.write("'name: None'\n")
        if 'url' in r.json():
            f.write(f"'url': '{r.json()['url']}'\n")
        else:
            f.write("'url: None'\n")


window = Tk()
window.title('Ткаченко Даниил группа УБ-22')
window.geometry('240x60')
lbl = Label(window, text='Название репозитория', font=('Calibri', 12))
lbl.grid(column=35, row=0)
btn = Button(window, text='Поиск', command=click)
btn.grid(column=35, row=10)
txt = Entry(window, width=10)
txt.grid(column=45, row=0)
window.mainloop()