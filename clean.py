import regex as re
import pandas as pd

def cleanTxt(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)
    text = re.sub(r'#', '', text)
    text = re.sub(r'RT[\s]+', '', text)
    text = re.sub(r'https?:\/\/\S+', '', text)

    return text

dfData=pd.read_excel("excel-data-twit/serumKolesterol.xlsx")

df=pd.DataFrame()
df['Twitler'] = dfData['tweet'].apply(cleanTxt)
df.to_excel("clean-data/serumKolesterol-clean.xlsx")
