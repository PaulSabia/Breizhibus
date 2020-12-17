import tkinter as tk
from tkinter import ttk
from connecteur import MySQL
from functools import partial
from PIL import Image, ImageTk


bdd = MySQL()

class Interface(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Breizhibus')
        self.geometry('720x540')
        self.minsize(740, 540)
        self.maxsize(740, 540)
        self.configure(bg='#A9DFBF')

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo) :
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#A9DFBF')

        titre = tk.Label(self, text='Breizhibus')
        titre.configure(font=('Helvetica',50), bg='#A9DFBF')
        titre.pack(pady=20)

        label = tk.Label(self, text='Bienvenu sur nos lignes')
        label.configure(font=('Helvetica',12), bg='#A9DFBF')
        label.pack()

        frame_bouton = tk.Frame(self, bg='#A9DFBF')
        frame_bouton.pack(side='bottom')

        bouton = tk.Button(frame_bouton, text='Les Arrêts', command=lambda : controller.show_frame(PageOne))
        bouton.configure(width=25, font=('Helvetica', 12), bg='#D4EFDF')
        bouton.grid(row=0, column=0, padx=50, pady=50)

        bouton2 = tk.Button(frame_bouton, text='Gestion des bus', command=lambda : controller.show_frame(PageTwo))
        bouton2.configure(width=25, font=('Helvetica', 12), bg='#D4EFDF')
        bouton2.grid(row=0, column=1, padx=50, pady=50)

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#A9DFBF')

        frame_bouton = tk.Frame(self, bg='#A9DFBF')
        frame_bouton.pack(side='top', pady=20)

        bouton = tk.Button(frame_bouton, text='Accueil', command=lambda : controller.show_frame(StartPage))
        bouton.configure(width=25, font=('Helvetica', 12), bg='#D4EFDF')
        bouton.grid(row=0, column=0, padx=50)

        bouton2 = tk.Button(frame_bouton, text='Gestion des bus', command=lambda : controller.show_frame(PageTwo))
        bouton2.configure(width=25, font=('Helvetica', 12), bg='#D4EFDF')
        bouton2.grid(row=0, column=1, padx=50)

        label = tk.Label(self, text='Rechercher un arrêt')
        label.configure(font=('Helvetica',20), bg='#A9DFBF')
        label.pack(pady=10)

        self.affiche_arret_bus()

    #Selection d'une ligne
    def affiche_arret_bus(self):
        liste_ligne = bdd.recup_lignes()
        self.menu_ligne = ttk.Combobox(self, values=liste_ligne, state='readonly', font=('Helvetica', 12))
        self.menu_ligne.bind('<<ComboboxSelected>>', self.affiche_arret)
        self.menu_ligne.pack(pady=20)

        self.frame_arret = tk.Frame(self, bg='#A9DFBF')
        self.frame_arret.pack(pady=20)

    #Affichage des arrêts après selection
    def affiche_arret(self, *args):
        for widget in self.frame_arret.winfo_children():
            widget.destroy()
        label_numero = tk.Label(self.frame_arret, text='N°', font=('Helvetica',15), width=10, bg='#A9DFBF')
        label_numero.grid(row = 0, column=0)
        label_nom = tk.Label(self.frame_arret, text='Nom', font=('Helvetica',15), width=15, bg='#A9DFBF')
        label_nom.grid(row = 0, column=1)
        label_adresse = tk.Label(self.frame_arret, text='Adresse', font=('Helvetica',15), width=15, bg='#A9DFBF')
        label_adresse.grid(row = 0, column=2)

        choix = self.menu_ligne.get()
        id_ligne = choix[0]
        liste_arret = bdd.recup_arrets(id_ligne)
        for i, arret in enumerate(liste_arret, 1):
            label_arret_num = tk.Label(self.frame_arret, text=arret[0], font=('Helvetica',12), width=10, bg='#A9DFBF')
            label_arret_num.grid(row = i, column=0)
            label_arret_nom = tk.Label(self.frame_arret, text=arret[1], font=('Helvetica',12), width=15, bg='#A9DFBF')
            label_arret_nom.grid(row = i, column=1)
            label_arret_addr = tk.Label(self.frame_arret, text=arret[2], font=('Helvetica',12), width=15, bg='#A9DFBF')
            label_arret_addr.grid(row = i, column=2)

        commande = partial(self.affiche_bus, id_ligne)
        bouton_bus = tk.Button(self.frame_arret, text='Afficher les bus', command=commande, font=('Helvetica',12), bg='#D4EFDF')
        bouton_bus.grid(row = i+1, columnspan=3, pady=20)

        self.frame_bus = tk.Label(self.frame_arret, bg='#A9DFBF')
        self.frame_bus.grid(columnspan=3)

    #Affichage des bus si appui sur 'bouton_bus' 
    def affiche_bus(self, id_ligne):
        label_numero = tk.Label(self.frame_bus, text='N°', font=('Helvetica',15), width=10, bg='#A9DFBF')
        label_numero.grid(row = 0, column=0)
        label_nom = tk.Label(self.frame_bus, text='Immatriculation', font=('Helvetica',15), width=15, bg='#A9DFBF')
        label_nom.grid(row = 0, column=1)
        label_adresse = tk.Label(self.frame_bus, text='Nombre de places', font=('Helvetica',15), width=15, bg='#A9DFBF')
        label_adresse.grid(row = 0, column=2)

        liste_bus = bdd.recup_bus(id_ligne)
        for i, bus in enumerate(liste_bus, 1):
            label_bus_num = tk.Label(self.frame_bus, text=bus[1], font=('Helvetica',12), width=10, bg='#A9DFBF')
            label_bus_num.grid(row = i, column=0)
            label_bus_nom = tk.Label(self.frame_bus, text=bus[2], font=('Helvetica',12), width=15, bg='#A9DFBF')
            label_bus_nom.grid(row = i, column=1)
            label_bus_addr = tk.Label(self.frame_bus, text=bus[3], font=('Helvetica',12), width=15, bg='#A9DFBF')
            label_bus_addr.grid(row = i, column=2)


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#A9DFBF')

        frame_bouton = tk.Frame(self, bg='#A9DFBF')
        frame_bouton.pack(side='top', pady=20)

        bouton = tk.Button(frame_bouton, text='Accueil', command=lambda : controller.show_frame(StartPage))
        bouton.configure(width=25, font=('Helvetica', 12), bg='#D4EFDF')
        bouton.grid(row=0, column=0, padx=50)
        bouton2 = tk.Button(frame_bouton, text='Les Arrêts', command=lambda : controller.show_frame(PageOne))
        bouton2.configure(width=25, font=('Helvetica', 12), bg='#D4EFDF')
        bouton2.grid(row=0, column=1, padx=50)

        label = tk.Label(self, text='Espace Administrateur', bg='#A9DFBF', font=('Helvetica',20))
        label.pack(pady=20)

        self.frame_bus = tk.Frame(self, bg='#A9DFBF')
        self.frame_bus.pack(pady=50)

        self.affiche_bus()

        # bouton_nouveau = tk.Button(self, text='Ajouter', command=self.entry_ajout_bus)
        # bouton_nouveau.pack()

        frame_bouton2 = tk.Frame(self, bg='#A9DFBF')
        frame_bouton2.pack()

        bouton_modif = tk.Button(frame_bouton2, text='Ajouter / Modifier', command=self.entry_modif_bus, bg='#D4EFDF', font=('Helvetica',10), width=15)
        bouton_modif.grid(row=0, column=0, padx=25)

        bouton_suppr = tk.Button(frame_bouton2, text='Supprimer', command=self.entry_suppr_bus, bg='#D4EFDF', font=('Helvetica',10), width=15)
        bouton_suppr.grid(row=0, column=1)

        self.frame_modif = tk.Frame(self, bg='#A9DFBF')
        self.frame_modif.pack(pady=20, padx=25)

    #Pour nettoyer la frame de modification:
    def clean_frame_modif(self):
        for widget in self.frame_modif.winfo_children():
            widget.destroy()

    #Pour update l'affichage des bus
    def update_affichage_bus(self):
        for widget in self.frame_modif.winfo_children():
            widget.destroy()
        for widget in self.frame_bus.winfo_children():
            widget.destroy()  
        self.affiche_bus()


    #Affichage des bus : 
    def affiche_bus(self):
        self.liste_bus = bdd.recup_bus2()

        label_numero = tk.Label(self.frame_bus, text='Numero', bg='#A9DFBF', font=('Helvetica',12), width=15)
        label_numero.grid(row = 0, column=0)
        label_immat = tk.Label(self.frame_bus, text='Immatriculation', bg='#A9DFBF', font=('Helvetica',12), width=15)
        label_immat.grid(row = 0, column=1)
        label_nbr = tk.Label(self.frame_bus, text='Nombre de place', bg='#A9DFBF', font=('Helvetica',12), width=15)
        label_nbr.grid(row = 0, column=2)
        label_ligne = tk.Label(self.frame_bus, text='Ligne', bg='#A9DFBF', font=('Helvetica',12), width=15)
        label_ligne.grid(row = 0, column=3)

        for i, bus in enumerate(self.liste_bus, 1):
            label_numero = tk.Label(self.frame_bus, text=bus[0], bg='#A9DFBF', font=('Helvetica',10))
            label_numero.grid(row = i, column=0)
            label_immat = tk.Label(self.frame_bus, text=bus[1], bg='#A9DFBF', font=('Helvetica',10))
            label_immat.grid(row = i, column=1)
            label_nbr = tk.Label(self.frame_bus, text=bus[2], bg='#A9DFBF', font=('Helvetica',10))
            label_nbr.grid(row = i, column=2)
            label_ligne = tk.Label(self.frame_bus, text=bus[3], bg='#A9DFBF', font=('Helvetica',10))
            label_ligne.grid(row = i, column=3)


    # #Ajouter nouveau bus :
    # def entry_ajout_bus(self):
    #     self.clean_frame_modif()
    #     label_numero = tk.Label(self.frame_modif, text='Numero')
    #     label_numero.grid(row = 0, column=0)
    #     label_immat = tk.Label(self.frame_modif, text='Immatriculation')
    #     label_immat.grid(row = 0, column=1)
    #     label_nbr = tk.Label(self.frame_modif, text='Nombre de place')
    #     label_nbr.grid(row = 0, column=2)
    #     label_ligne = tk.Label(self.frame_modif, text='Ligne')
    #     label_ligne.grid(row = 0, column=3)

    #     self.entry_numero = tk.Entry(self.frame_modif)
    #     self.entry_numero.grid(row=2, column=0)
    #     self.entry_immat = tk.Entry(self.frame_modif)
    #     self.entry_immat.grid(row=2, column=1)
    #     self.entry_nbr = tk.Entry(self.frame_modif)
    #     self.entry_nbr.grid(row=2, column=2)
    #     self.entry_ligne = tk.Entry(self.frame_modif)
    #     self.entry_ligne.grid(row=2, column=3)

    #     bouton_valider = tk.Button(self.frame_modif, text='OK', command=self.ajouter_bus)
    #     bouton_valider.grid(row=2, column=4)

    # def ajouter_bus(self):
    #     numero = self.entry_numero.get()
    #     immat = self.entry_immat.get()
    #     nbr = self.entry_nbr.get()
    #     ligne = self.entry_ligne.get()

    #     if numero or immat or nbr or ligne != '':
    #         inserer = bdd.inserer_bus(numero, immat, nbr, ligne)
    #         if inserer == None:
    #             pass
    #         else:
    #             self.update_affichage_bus()
    #     else:
    #         pass


    #Affichage pour Ajouter/Modifier bus :
    def entry_modif_bus(self):
        self.clean_frame_modif()
        label_numero = tk.Label(self.frame_modif, text='Numero', bg='#A9DFBF')
        label_numero.grid(row = 0, column=0)
        label_immat = tk.Label(self.frame_modif, text='Immatriculation', bg='#A9DFBF')
        label_immat.grid(row = 0, column=1)
        label_nbr = tk.Label(self.frame_modif, text='Nombre de place', bg='#A9DFBF')
        label_nbr.grid(row = 0, column=2)
        label_ligne = tk.Label(self.frame_modif, text='Ligne', bg='#A9DFBF')
        label_ligne.grid(row = 0, column=3)

        liste_numero_bus = []
        for bus in self.liste_bus:
            liste_numero_bus.append(bus[0])

        self.choix_bus = ttk.Combobox(self.frame_modif, values=liste_numero_bus)
        self.choix_bus.bind('<<ComboboxSelected>>', self.selection_bus)
        self.choix_bus.grid(row=1, column=0)
        self.entry_immat = tk.Entry(self.frame_modif)
        self.entry_immat.grid(row=1, column=1)
        self.entry_nbr = tk.Entry(self.frame_modif)
        self.entry_nbr.grid(row=1, column=2)
        self.entry_ligne = tk.Entry(self.frame_modif)
        self.entry_ligne.grid(row=1, column=3)

        bouton_valider = tk.Button(self.frame_modif, text='OK', command=self.modifier_bus, bg='#D4EFDF')
        bouton_valider.grid(row=1, column=4)

    #Nettoyage + Auto-complétion des champs lorsque l'on selectionne un bus pour modification
    def selection_bus(self, *args):
        self.entry_immat.delete(0, 'end')
        self.entry_nbr.delete(0, 'end')
        self.entry_ligne.delete(0, 'end')

        choix_bus = self.choix_bus.get()
        self.bus = bdd.recup_bus3(choix_bus)
        self.entry_immat.insert(0, self.bus[0][2])
        self.entry_nbr.insert(0, self.bus[0][3])
        self.entry_ligne.insert(0, self.bus[0][4])

    #Commande ajouter/modifier bus
    def modifier_bus(self):
        try :
            ident = self.bus[0][0] 
        except:
            ident = 'NULL'
        numero = self.choix_bus.get()
        immat = self.entry_immat.get()
        nbr_place = self.entry_nbr.get()
        ligne = self.entry_ligne.get()
        bdd.modifier_bus(ident, numero, immat, nbr_place, ligne)
        self.update_affichage_bus()


    #Affichage pour la suppression de bus:
    def entry_suppr_bus(self):
        self.clean_frame_modif()
        liste_numero_bus = []
        for bus in self.liste_bus:
            liste_numero_bus.append(bus[0])
        self.choix_bus = ttk.Combobox(self.frame_modif, values=liste_numero_bus, state='readonly')
        self.choix_bus.grid()

        bouton_valider = tk.Button(self.frame_modif,  text='OK', command=self.suppr_bus, bg='#D4EFDF')
        bouton_valider.grid()

    #Commande Supprimer :
    def suppr_bus(self):
        choix = self.choix_bus.get()
        if choix != '':
            bus = self.choix_bus.get()
            bdd.suppr_bus(bus)
            self.update_affichage_bus()

