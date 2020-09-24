import pandas as pd

class Artist:
    def __init__(self, name, info, flyer, discography):
        self.name = name
        self.info = info
        self.flyer = flyer
        self.discography = discography
    

def _get_flyer(search):
    # Creamos un dataframe y filtramos
    df = pd.DataFrame(search.json()['artists']['items'])
    flyer = df.sort_values(by='popularity', ascending=False)
    return flyer.iloc[0]