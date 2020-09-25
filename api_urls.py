def url_base():
    return 'https://api.spotify.com/v1'
    

def url_search():
    url_search = 'https://api.spotify.com/v1/search'
    return url_search

def mk_header(token):
    header = {'Authorization':f'Bearer {token}'}
    return header