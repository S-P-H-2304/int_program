nombre = input("¿Cuál es tu nombre? ")
print("Hola,", nombre)
year = int(input("¿En qué año naciste? "))
edad = 2024 - year
if year >= 1930 and year <= 1948:
    print(nombre,"tienes",edad,"años", "y perteneces a la generación Niños de la Posguerra")
elif year >= 1949 and year <= 1968:
    print(nombre,"tienes",edad,"años", "y perteneces a la generación Baby Boomer")
elif year >= 1969 and year <= 1980:
    print(nombre,"tienes",edad,"años", "y perteneces a la generación X")
elif year >= 1981 and year <= 1993:
    print(nombre,"tienes",edad,"años", "y perteneces a la generación de los Millenials")
elif year >= 1994 and year <= 2010:
    print(nombre,"tienes",edad,"años", "y perteneces a la generación Z")
elif year >= 2011:
    print(nombre,"tienes",edad,"años", "y perteneces a la generación Alfa")   