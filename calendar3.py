import calendar
import tkinter as tk

def afficher_calendrier():
    annee = int(annee_entry.get())
    mois = int(mois_entry.get())
    
    cal = calendar.month(annee, mois)
    resultat.config(text=cal)

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calendrier")

# Créer des étiquettes et des champs de saisie pour l'année et le mois
annee_label = tk.Label(fenetre, text="Année:")
annee_label.pack()
annee_entry = tk.Entry(fenetre)
annee_entry.pack()

mois_label = tk.Label(fenetre, text="Mois:")
mois_label.pack()
mois_entry = tk.Entry(fenetre)
mois_entry.pack()

# Bouton pour afficher le calendrier
afficher_bouton = tk.Button(fenetre, text="Afficher Calendrier", command=afficher_calendrier)
afficher_bouton.pack()

# Étiquette pour afficher le calendrier
resultat = tk.Label(fenetre, text="", justify="left")
resultat.pack()

# Lancer la boucle principale de l'interface utilisateur
fenetre.mainloop()