import requests
import pandas as pd
import base64

def usr_get_token(client_id, client_secret):
    encoded = base64.b64encode(bytes(client_id + ':' + client_id_secret, 'utf-8'))
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

def main(url_artist, usr_token):
    # Token de artista
    pass

if __name__ == '__main__':
    url_base = 'https://api.spotify.com/v1'
    
    client_id = input('Registre su client id de desarrollador: ')
    client_secret = input('Registre su client id secreta: ')
    usr_token = usr_get_token(client_id, client_secret)

    artist_id = input('Pegue aquí el ID del artista: ')
    ep_artist = f'/artist/{artist_id}' # Artist endpoint
    url_armada = url_base + ep_artist
    main(url_artist = url_armada, usr_token)