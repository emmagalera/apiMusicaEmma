import json
import requests
import os

#PONER TRY Y EXCEPT
#
#
#




def tipo():
    buscarAnime= input("Introduce una pelicula para saber su tipo: ")
    #Kimi no Na wa
    apiAnime= "https://api.jikan.moe/v3/search/anime?q=%s&limit=16"%buscarAnime
    resp= requests.get(apiAnime) #para hacer solicitudes a HTTP
    #json.loads () espera una cadena JSON (válida)
    #mientras que json.load () espera un archivo (objeto de archivo)
    animes= json.loads(resp.content)
    #diccionario
    anime= animes.get('results')
    #lista
    consultaAnime= anime[0]
    resultadoConsulta= consultaAnime['type']
    print(resultadoConsulta)

def sinopsis():
    buscarAnime= input("Introduce una pelicula para saber su tipo: ")
    #Kimi no Na wa
    apiAnime= "https://api.jikan.moe/v3/search/anime?q=%s&limit=16"%buscarAnime
    resp= requests.get(apiAnime) #para hacer solicitudes a HTTP
    #json.loads () espera una cadena JSON (válida)
    #mientras que json.load () espera un archivo (objeto de archivo)
    animes= json.loads(resp.content)
    #diccionario
    anime= animes.get('results')
    #lista
    consultaAnime= anime[0]
    resultadoConsulta= consultaAnime['synopsis']
    print(resultadoConsulta)


def puntos():
    buscarAnime= input("Introduce una pelicula para saber su tipo: ")
    #Kimi no Na wa
    apiAnime= "https://api.jikan.moe/v3/search/anime?q=%s&limit=16"%buscarAnime
    resp= requests.get(apiAnime) #para hacer solicitudes a HTTP
    #json.loads () espera una cadena JSON (válida)
    #mientras que json.load () espera un archivo (objeto de archivo)
    animes= json.loads(resp.content)
    #diccionario
    anime= animes.get('results')
    #lista
    consultaAnime= anime[0]
    resultadoConsulta= consultaAnime['score']
    print(resultadoConsulta)

def imagen():
    buscarAnime= input("Introduce una pelicula para saber su tipo: ")
    #Kimi no Na wa
    apiAnime= "https://api.jikan.moe/v3/search/anime?q=%s&limit=16"%buscarAnime
    resp= requests.get(apiAnime) #para hacer solicitudes a HTTP
    #json.loads () espera una cadena JSON (válida)
    #mientras que json.load () espera un archivo (objeto de archivo)
    animes= json.loads(resp.content)
    #diccionario
    anime= animes.get('results')
    #lista
    consultaAnime= anime[0]
    resultadoConsulta= consultaAnime['image_url']
    print(resultadoConsulta)

def episodiosCantidad():
    buscarAnime= input("Introduce una pelicula para saber su tipo: ")
    #Kimi no Na wa
    apiAnime= "https://api.jikan.moe/v3/search/anime?q=%s&limit=16"%buscarAnime
    resp= requests.get(apiAnime) #para hacer solicitudes a HTTP
    #json.loads () espera una cadena JSON (válida)
    #mientras que json.load () espera un archivo (objeto de archivo)
    animes= json.loads(resp.content)
    #diccionario
    anime= animes.get('results')
    #lista
    consultaAnime= anime[0]
    resultadoConsulta= consultaAnime['episodes']
    print(resultadoConsulta)

def menu():
    print("Series y Peliculas Animes: ")
    print("1- Obetener el tipo de un Anime.")
    print("2- Obtener la sinopsis de un Anime.") 
    print("3- Obetener el tipo de un Anime.")
    print("4- Introduce una Anime para obtener la imgen de su cartelera.")
    print("5- Introduce una Anime para obtener cuantos episodios tiene.")
    print("6- Salir.")
    
while True: 
    menu()
    opcion= int(input("Introduce una opción: "))
    if opcion==1:
        tipo()
        input("Introduce cualquier letra para continuar:")
    elif opcion==2:
        sinopsis()
        input("Introduce cualquier letra para continuar:")
    elif opcion==3:
        puntos()
        input("Introduce cualquier letra para continuar:")
    elif opcion==4:
        imagen()
        input("Introduce cualquier letra para continuar:")
    elif opcion==5:
        episodiosCantidad()
        input("Introduce cualquier letra para continuar:")
    elif opcion==6:
        break


