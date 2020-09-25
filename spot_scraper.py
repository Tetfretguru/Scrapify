import requests
import pandas as pd
import base64
import api_urls as apiu
import data_artists as da

def _get_artist_discography(url_artist, usr_token, artist_id):
    header = apiu.mk_header(usr_token)
    ep_albums = f'/artists/{artist_id}/albums'
    url_base = 'https://api.spotify.com/v1'
    url_albums = url_base+ep_albums
    params = {'country': 'UY'}
    albums_art = requests.get(url_albums, headers=header,params=params)
    if albums_art.status_code == 200:
        print('Discografía encontrada')
        return albums_art.json()['items']
    else:
        return None
    


def _artist_search(url_search, artist_name, header):
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

def main(url_artist, usr_token, url_search, artist_id):
    # Nombre de artista e info
    artist_name = _get_artist_name(url_artist, usr_token)
    artist_info = _get_artist_info(url_artist, usr_token)

    # Búsqueda de artista por mercado, devolverá todas las coincidencias con los nombres
    artist_search_res = _artist_search(url_search,artist_name, header = apiu.mk_header(token=usr_token))

    flyer = da._get_flyer(search = artist_search_res)

    discography = _get_artist_discography(url_artist, usr_token, artist_id)

    # Creamos un objeto con los datos del artista elegido
    artista = da.Artist(name = artist_name, info = artist_info, flyer = flyer, discography = discography)

    # Cerear dataframe de la discografía
    df_discography = artista.create_discography_df(name=artista.name, discography=artista.discography)

    # Ver contenido de la discografía
    action = input(f'¿Desea ver el detalle de la discografía de {artista.name}?: (s/n)')
    if action == 's':
        da._df_detail(df=df_discography)
        print('Scraper finalizado')
        return da.export_csv(name=artista.name, df = df_discography)
    else:
        print('Scraper finalizado')
        return da.export_csv(name=artista.name, df = df_discography)



    

if __name__ == '__main__':
    url_base = apiu.url_base()
    url_search = apiu.url_search()

    client_id = input('Registre su client id de desarrollador: ')
    client_secret = input('Registre su client id secreta: ')
    usr_token = usr_get_token(client_id, client_secret)

    artist_id = input('Pegue aquí el ID del artista: ')
    ep_artist = f'/artists/{artist_id}' # Artist endpoint
    url_artist = url_base + ep_artist
    main(url_artist, usr_token, url_search, artist_id)