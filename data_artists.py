import pandas as pd

class Artist:
    def __init__(self, name, info, flyer, discography):
        self.name = name
        self.info = info
        self.flyer = flyer
        self.discography = discography
    
    def create_discography_df(self, name, discography):
        return pd.DataFrame(discography)
        

def export_csv(name, df):
    return df.to_csv(f'{name}_discography.csv')

def export_excel(name, df):
    pass
    

def _get_flyer(search):
    # Creamos un dataframe y filtramos
    df = pd.DataFrame(search['artists']['items'])
    flyer = df.sort_values(by='popularity', ascending=False)
    return flyer.iloc[0]

def _df_detail(df):
    i = 0
    while i < len(df):
        print(df.iloc[i], '\n')
        i += 1