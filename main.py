from prettytable import PrettyTable
from colorama import Fore, Style, init
init(autoreset=True)

# Créer un tableau coloré
table = PrettyTable()
table.field_names = [
    Fore.CYAN + "ID" + Style.RESET_ALL,
    Fore.YELLOW + "Statut" + Style.RESET_ALL,
    Fore.GREEN + "Tâche" + Style.RESET_ALL
]

# Ajouter des lignes colorées
table.add_row([
    Fore.BLUE + "1",
    Fore.GREEN + "✓ Terminé",
    "Acheter du pain"
])
table.add_row([
    Fore.BLUE + "2",
    Fore.RED + "✗ En cours",
    "Faire l'exercice Python"
])

print(table)