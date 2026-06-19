from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Produit", "Prix", "Stock"]
table.align["Produit"] = "r"
table.align["Prix"] = "r"
table.align["Stock"] = "r"

table.add_row(["Clavier", 29.99, 15])
table.add_row(["Souris", 15.50, 42])
table.add_row(["Ecran 4k", 199.99, 8])


table.horizontal_char = '_'
table.vertical_char = '|'
table.junction_char = '┼'

print(table)
