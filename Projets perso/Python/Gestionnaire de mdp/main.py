#-----------------------------------IMPORTS-----------------------------#
from tkinter import *
from tkinter import messagebox
import random
import tkinter
import pyperclip
#-----------------------------------GÉNÉRER MDP-----------------------------#
def generer_mdp() :
    lettres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    nombres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symboles = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    mdp_lettres = [random.choice(lettres) for _ in range(nr_letters)]
    mdp_symboles = [random.choice(symboles) for _ in range(nr_symbols)]
    mdp_nombres = [random.choice(nombres) for _ in range(nr_numbers)]

    list_mdp = mdp_lettres + mdp_nombres + mdp_symboles
    random.shuffle(list_mdp)

    mdp = "".join(list_mdp)

    case_mdp.insert(0, mdp)

    pyperclip.copy(mdp)

#-----------------------------------ENREGISTER MDP-----------------------------#
def enregistrer():

    siteWeb = case_siteWeb.get()
    nomSiteWeb = case_nomSiteWeb.get()
    email = case_email.get()
    mdp = case_mdp.get()

    if len(siteWeb) == 0 or len(nomSiteWeb) == 0 or len(mdp) == 0:
        messagebox.showinfo(title="Oups", message="Veuillez remplir toutes les cases!")
    else: 
        is_ok = messagebox.askokcancel(title=nomSiteWeb, message=f"Les informations rentrées sont : \n\nURL: {siteWeb}\nSite web: {nomSiteWeb}\nEmail: {email} \nMot de passe: {mdp} \n\nAppuyez sur Ok pour enregister ces informations dans un fichier texte nommé \"infos.txt\"." )

        if is_ok:
            with open("infos.txt", "a") as fichier_infos:
                fichier_infos.write(f"URL : {siteWeb}\nSite web : {nomSiteWeb}\nEmail : {email}\nMot de passe : {mdp}\n\n")
                case_siteWeb.delete(0, END)
                case_mdp.delete(0, END)
                messagebox.showinfo(title="Succès", message="Les informations ont bien été enregistrées!")
        else :
            messagebox.showinfo(title="Succès", message="Les informations n'ont pas été enregistrées.")

#-----------------------------------UI SETUP-----------------------------#
window = Tk()
window.title = ("Mot de passe")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Nomage des cases
siteWeb = Label(text="URL :")
siteWeb.grid(row=1, column=0)
nomSiteWeb = Label(text="Site :")
nomSiteWeb.grid(row=2, column=0)
email = Label(text="Email :")
email.grid(row=3, column=0)
mdp = Label(text="Mot de passe :")
mdp.grid(row=4, column=0)

# Cases
case_siteWeb = Entry(width=53)
case_siteWeb.grid(row=1, column=1, columnspan=2)
case_siteWeb.focus()
case_nomSiteWeb = Entry(width=53)
case_nomSiteWeb.grid(row=2, column=1, columnspan=2)
case_email = Entry(width=53)
case_email.grid(row=3, column=1, columnspan=2)
case_email.insert(0, "exemple@gmail.com")
case_mdp = Entry(width=35)
case_mdp.grid(row=4, column=1)

# Boutons
generer_mdp = Button(text="Générer", width=14, command=generer_mdp)
generer_mdp.grid(row=4, column=2)
bouton_ajouter = Button(text="Ajouter", width=36, command=enregistrer)
bouton_ajouter.grid(row=5, column=1, columnspan=2)

# Fenêtre
window.mainloop()