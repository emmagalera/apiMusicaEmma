import json
import requests
import os

#https://jikan.moe/
try:
    def tipo():
        buscarAnime= input("Introduce el nombre de un Anime: ")
        apiAnime= "https://api.jikan.moe/v3/search/anime?q=%s&limit=16"%buscarAnime
        resp= requests.get(apiAnime) #para hacer solicitudes a HTTP
        if resp.status_code==200:
            #json.loads () espera una cadena JSON (válida)
            #mientras que json.load () espera un archivo (objeto de archivo)
            animes= json.loads(resp.content)
            #diccionario
            anime= animes.get('results')
            #lista
            consultaAnime= anime[0]
            resultadoConsulta= consultaAnime['type']
            print("\nEl tipo de anime, %s, es: %s\n"%(buscarAnime,resultadoConsulta))


    def sinopsis():
        buscarAnime= input("Introduce el nombre de un Anime: ")
        apiAnime= "https://api.jikan.moe/v3/search/anime?q=%s&limit=16"%buscarAnime
        resp= requests.get(apiAnime) #para hacer solicitudes a HTTP
        if resp.status_code==200:
            #json.loads () espera una cadena JSON (válida)
            #mientras que json.load () espera un archivo (objeto de archivo)
            animes= json.loads(resp.content)
            #diccionario
            anime= animes.get('results')
            #lista
            consultaAnime= anime[0]
            resultadoConsulta= consultaAnime['synopsis']
            print("\nLa sinopsis del anime %s es:"%buscarAnime)
            print("\n",resultadoConsulta,"\n")


    def puntos():
        buscarAnime= input("Introduce el nombre de un Anime: ")
        apiAnime= "https://api.jikan.moe/v3/search/anime?q=%s&limit=16"%buscarAnime
        resp= requests.get(apiAnime) #para hacer solicitudes a HTTP
        if resp.status_code==200:
            #json.loads () espera una cadena JSON (válida)
            #mientras que json.load () espera un archivo (objeto de archivo)
            animes= json.loads(resp.content)
            #diccionario
            anime= animes.get('results')
            #lista
            consultaAnime= anime[0]
            resultadoConsulta= consultaAnime['score']
            print("\nEl puntaje de %s es: %s"%(buscarAnime,resultadoConsulta))
    

    def imagen():
        buscarAnime= input("Introduce el nombre de un Anime: ")
        apiAnime= "https://api.jikan.moe/v3/search/anime?q=%s&limit=16"%buscarAnime
        resp= requests.get(apiAnime) #para hacer solicitudes a HTTP
        if resp.status_code==200:
            #json.loads () espera una cadena JSON (válida)
            #mientras que json.load () espera un archivo (objeto de archivo)
            animes= json.loads(resp.content)
            #diccionario
            anime= animes.get('results')
            #lista
            consultaAnime= anime[0]
            resultadoConsulta= consultaAnime['image_url']
            print("\nLa url de la cartelera de %s es: "%buscarAnime)
            print(resultadoConsulta)

    def episodiosCantidad():
        buscarAnime= input("Introduce el nombre de un Anime: ")
        apiAnime= "https://api.jikan.moe/v3/search/anime?q=%s&limit=16"%buscarAnime
        resp= requests.get(apiAnime) #para hacer solicitudes a HTTP
        if resp.status_code==200:
            #json.loads () espera una cadena JSON (válida)
            #mientras que json.load () espera un archivo (objeto de archivo)
            animes= json.loads(resp.content)
            #diccionario
            anime= animes.get('results')
            #lista
            consultaAnime= anime[0]
            resultadoConsulta= consultaAnime['episodes']
            print("\n%s tiene: %s episodios"%(buscarAnime,resultadoConsulta))

    def menu():
        os.system('cls')
        print("Series y Peliculas Animes: ")
        print("1- Obetener el tipo de un Anime.")
        print("2- Obtener la sinopsis de un Anime.") 
        print("3- Obetener el puntaje de un Anime.")
        print("4- Introduce una Anime para obtener la imgen de su cartelera.")
        print("5- Introduce una Anime para obtener cuantos episodios tiene.")
        print("6- Salir.")
        print("\nEjemplos de animes que buscar: Naruto, Kimi no Na wa, Tokyo Ghoul....")
        
    while True: 
        menu()
        opcion= int(input("\nIntroduce una opción: "))
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
except ValueError:
    print("Error, porfavor intentelo de nuevo")
except Exception as e: # 
    print("Ha ocurrido un error no previsto", type(e).__name__ )


