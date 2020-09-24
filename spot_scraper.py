import requests
import pandas as pd
import base64
import api_urls as apiu
import data_artists as da

def _get_artist_discography(url_artist, usr_token):
    pass

def  _artist_search(url_search, artist_name, header):
    search_params = {'q':f'{artist_name}', 'type':'artist', 'market':'UY'}
    search = requests.get(url_search,headers=header,params=search_params)
    if search.status_code == 200:
        print('Búsqueda realizada con éxito.')
        return search.json()
    else:
        print('No se pudo realizar búsqueda.')
        return None

def _get_artist_info(url_artist, usr_token):
   
    header = {'Authorization':f'Bearer {usr_token}'}
    artist_request = requests.get(url_artist, headers=header)
    if artist_request.status_code == 200:
        print('Artista encontrado')
        return artist_request.json()
    else:
        print('No se pudo encontrar artista con ese id')
        return None

def _get_artist_name(url_artist, usr_token):
   
    header = {'Authorization':f'Bearer {usr_token}'}
    artist_request = requests.get(url_artist, headers=header)
    if artist_request.status_code == 200:
        print('Artista encontrado')
        return artist_request.json()['name']
    else:
        print('No se pudo encontrar artista con ese id')
        return None

def usr_get_token(client_id, client_secret):
    encoded = base64.b64encode(bytes(client_id + ':' + client_secret, 'utf-8'))
    params = {'grant_type':'client_credentials'}
    header = {'Authorization': 'Basic ' + str(encoded, 'utf-8')}
    r = requests.post('https://accounts.spotify.com/api/token', headers=header, data=params)
    if r.status_code != 200:
        print('Error en request')
        print(r.json())
        return None
    else:
        print('Token válido por {} segundos.'.format(r.json()['expires_in']))
        return r.json()['access_token']

def main(url_artist, usr_token, url_search):
    # Nombre de artista e info
    artist_name = _get_artist_name(url_artist, usr_token)
    artist_info = _get_artist_info(url_artist, usr_token)

    # Búsqueda de artista por mercado, devolverá todas las coincidencias con los nombres
    artist_search_res = _artist_search(url_search,artist_name, header = apiu.mk_header(token=usr_token))
    flyer = da._get_flyer(search = artist_search_res)

    discography = _get_artist_discography(url_artist, usr_token)

    # Creamos un objeto con los datos del artista elegido
    artista = da.Artist(name = artist_name, info = artist_info, flyer = flyer, discography = discography)


    

if __name__ == '__main__':
    url_base = apiu.url_base
    url_search = apiu.url_search

    client_id = input('Registre su client id de desarrollador: ')
    client_secret = input('Registre su client id secreta: ')
    usr_token = usr_get_token(client_id, client_secret)

    artist_id = input('Pegue aquí el ID del artista: ')
    ep_artist = f'/artist/{artist_id}' # Artist endpoint
    url_artist = url_base + ep_artist
    main(url_artist, usr_token, url_search)