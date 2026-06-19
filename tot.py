from prettytable import PrettyTable
from colorama import Fore, init
from dotenv import load_dotenv
from openpyxl import workbook
import os
import matplotlib

matplotlib.use("TkAgg")

load_dotenv()
APP_NAME = os.getenv("APP_NAME")
ADMIN = os.getenv("DB_USER")

todos = {}
next_id = 1

def afficher_menu():
    print(f"\n{Fore.CYAN} ====== {APP_NAME}======")
    print("1. Ajouter une tache")
    print("2. Voir les taches")
    print("3. Supprimer une tache")
    print("4. Quitter une tache")
    print("5. terminé une tache")
    print("6. afficher_diagramme")

def ajouter_tache():
    #id:1, titre: "cours python", status: "Termine"
    global next_id

    titre = input("Entrer le tittre: ")

    todos[next_id] = {
        "titre": titre,
        "status": "non terminé"
    }

    print(Fore.GREEN + "tache ajouter avec succès")
    next_id +=1

def afficher_tache():
    if not todos:
        print(Fore.YELLOW + "aucune tache trouvée")
        return
    table = PrettyTable()
    table.field_names = ["ID", "Titre", "Status"]

    for id_tache, tache in todos.items():
        table.add_row([id_tache,["title"], tache["status"]])


    print(table)

def termine():
    try:
        id_tache = int(input("Entrer l'ID à terminer : "))

        if id_tache not in todos:
            raise KeyError("Tâche introuvable")

        todos[id_tache] ["status"] = "Terminé"

        print(Fore.GREEN + "Tâche terminée.")

    except ValueError:
        print(Fore.RED + "Veuillez entrer un ID valide.")
    except KeyError as e:
        print(Fore.RED + str(e))

def supprimer_tache():
    try:
        id_tache = int(input("Entrer l'ID à supprimer: "))
        if id_tache not in todos:
            raise KeyError("Tache introuvable")
        del todos[id_tache]

        print(Fore.GREEN + "Tache supprimer.")
    
    except ValueError:
        print(Fore.RED + "Veuiller entrer l'ID à supprimer")
    except KeyError  as e:
        print(Fore.RED + str(e))

from matplotlib import pyplot as plt
def diagramme_taches():
    #verifier si aucune tache
    if not todos:
        print("Aucune tache.")
        return
    #variable pour stcker les taches non terminées et terminée
    terminees = 0
    non_terminer = 0
    #recuperer les valeurs du status dans le ditionnaire todos{}
    for tache in todos.values():

        if tache["status"] == "Terminé":
            terminees += 1
        else:
            non_terminer += 1
    #labels du diagramme
    labels = [
        "terminees",
        "non_terminer"
    ]
    valeurs = [
        terminees,
        non_terminer
    ]
    #diagramme circulaire avec: valeurs en % et labels
    plt.pie(
        valeurs,
        labels=labels,
        autopct="%1.1f%%"
    )
    #titre du diagramme
    plt.title("Répartition des taches")
    #enregistrer le diagramme en image png
    plt.savefig("diagramme_taches.png")
    #afficher le diagramme sur l'interface graphique
    plt.show()        
def main():
    print(Fore.GREEN + f"Bienvenue {ADMIN}")

    while True:
        afficher_menu()

        try:
            choix = int(input("Votre choix"))

            if choix == 1:
                ajouter_tache()
            elif choix == 2:
                afficher_tache()
            elif choix == 3:
                supprimer_tache()
            elif choix == 6:
                diagramme_taches()
            elif choix == 5:
                termine()
            elif choix == 4:
                print(Fore.CYAN + "Au revoir")
                break
            else:
                print(Fore.RED + "choix invalide")
        except ValueError:
            print(Fore.RED + "Entrer un nombre valide")

if __name__ == "__main__":
    main()



