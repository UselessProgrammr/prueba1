# propiedades = {"Bow": {"Crit Chance": "105%",
#                         "Base Damage": 1542,
#                         "Status": "45%"
#                         },
#             "Dagger": {"Crit Chance": "200%",
#                             "Base damage": 1300,
#                             "Status": "100%"}
#                         }

# secciones = [ ["Maria", "Andres", "Pedro"] , ["Stefan", "Gabriel","Julia","Manuel"] ]
# txt_final = "El estudiante es: {}"

# for i in range(len(secciones)):
#     for j in range(len(secciones[i])):
#         print(txt_final.format(secciones[i][j]))

dict = {}

ciclo = True

while ciclo == True:

    user1 = input("\nAgrega algo:\n")
    user2 = input("\nAgrega otra cosa dentro de el otro algo\n")
    user3 = input("\nAgrega algo como valor de la otra cosa\n")

    dict.update({user1: {user2 : user3}})

    siguiente = input("\nDesea agregar algo mas?\nEscriba si o no\n\n")
    if siguiente == "si":
        ciclo = True
    if siguiente == "no":
        ciclo = False
        print(dict)

