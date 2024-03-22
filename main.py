import random
import string
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk

def generate_password(length, complexity):
    if complexity == "faible":
        characters = string.ascii_letters + string.digits
    elif complexity == "moyenne":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "forte":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
    else:
        raise ValueError("Complexité invalide. Choisissez parmi 'faible', 'moyenne' ou 'forte'.")

    return ''.join(random.choice(characters) for _ in range(length))

def generate_button_clicked():
    length = int(length_entry.get())
    complexity = complexity_var.get()
    password = generate_password(length, complexity)
    password_var.set(password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copié", "Mot de passe copié dans le presse-papiers !")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Générateur de mots de passe")

# Cadre pour les paramètres
parameter_frame = tk.Frame(root)
parameter_frame.pack(pady=10)

# Label et entrée pour la longueur
length_label = tk.Label(parameter_frame, text="Longueur du mot de passe :")
length_label.grid(row=0, column=0)
length_entry = tk.Entry(parameter_frame)
length_entry.grid(row=0, column=1)

# Label et menu déroulant pour la complexité
complexity_label = tk.Label(parameter_frame, text="Complexité :")
complexity_label.grid(row=1, column=0)
complexity_var = tk.StringVar(root)
complexity_var.set("faible")  # Défaut
complexity_dropdown = tk.OptionMenu(parameter_frame, complexity_var, "faible", "moyenne", "forte")
complexity_dropdown.grid(row=1, column=1)

# Bouton de génération de mot de passe
generate_button = tk.Button(root, text="Générer mot de passe", command=generate_button_clicked)
generate_button.pack(pady=5)

# Bouton de copie de mot de passe
copy_button = tk.Button(root, text="Copier mot de passe", command=copy_password)
copy_button.pack(pady=5)

# Affichage du mot de passe généré
password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var, font=("Helvetica", 12))
password_label.pack(pady=10)

# Exécution de la boucle principale
root.mainloop()
