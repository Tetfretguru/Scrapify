@property
def url_base():
    url_base = 'https://api.spotify.com/v1'
    return url_base

@property
def url_search():
    url_search = 'https://api.spotify.com/v1/search'
    return url_search

def mk_header(token):
    header = {'Authorization':f'Bearer {token}'}
    return header