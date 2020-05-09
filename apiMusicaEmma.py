import json
import requests
import os

#PONER TRY Y EXCEPT
#
#
#


# https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/

def tipoPelicula():
    buscarPelicula= input("Introduce una pelicula para saber su tipo: ")
    #Kimi no Na wa
    apiPeli= "https://api.jikan.moe/v3/search/anime?q=%s&limit=16"%buscarPelicula
    resp= requests.get(apiPeli) #para hacer solicitudes a HTTP
    #json.loads () espera una cadena JSON (válida)
    #mientras que json.load () espera un archivo (objeto de archivo)
    peliculas= json.loads(resp.content)
    pelicula= peliculas.get('results')
    encontrarP= pelicula[0]
    tipoPelicula= encontrarP['type']
    print(tipoPelicula)

def sinopsisPelicula():
    buscarPelicula= input("Introduce una pelicula para obtener su sinopsis: ")
    apiPeli= "https://api.jikan.moe/v3/search/anime?q=%s&limit=16"%buscarPelicula
    resp= requests.get(apiPeli) #para hacer solicitudes a HTTP
    #json.loads () espera una cadena JSON (válida)
    #mientras que json.load () espera un archivo (objeto de archivo)
    peliculas= json.loads(resp.content)
    pelicula= peliculas.get('results')
    encontrarP= pelicula[0]
    sinopsisPelicula= encontrarP['synopsis']
    print(sinopsisPelicula)


sinopsisPelicula()