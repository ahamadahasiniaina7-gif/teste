#creer liste vide avec dictionnaire la dedant (nom,age,ville) et afficher dans le tableau
from prettytable import PrettyTable
from colorama import Fore, Style, init
init(autoreset=True)
table = PrettyTable(["Nom", "Age", "Ville"])

table = PrettyTable()
table.field_names = [
    Fore.CYAN + "Nom" + Style.RESET_ALL,
    Fore.YELLOW + "Age" + Style.RESET_ALL,
    Fore.GREEN + "Ville" + Style.RESET_ALL
]
table.add_rows([
    Fore.BLUE + "Rakoto",
    Fore.GREEN + "50",
    "Tana"
])


table.horizontal_char = '_'
table.vertical_char = '|'
table.junction_char = '┼'

print(table)