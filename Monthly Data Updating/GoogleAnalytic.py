import pandas as pd
import re

csv_url = input("Input the link of the Google sheet: ")
csv_url = csv_url.replace("/edit?usp=sharing", "/export?format=csv")

df = pd.read_csv(csv_url, skiprows=9)
print("-"*50, "DF.HEAD", "-"*50)
print(df.head())

# paste the "Web" column from Excel here - Target Channels

inputs = '''
coingape
business2community
techopedia
CryptoNews
CoinCodeCap
nftevening
coinwire
coinedition
Kriptoparahaber.com
kryptoszene.de
Actufinance.fr
bitdegree
Finaria.it
99bitcoins.com
Cryptonaute.fr
Bitcoinmagazine.nl
Coincierge.de
traderfactor
InsideBitcoins.com
Crypto-news-flash.com
blockchainmagazine
zycrypto
Coingabbar
Techbullion.com
Techreport.com
Bsc.news
coindoo
Thecryptobasic
Bitcoinist.com
cryptopotato
blockchainreporter
Thenewscrypto
u.today
Coinpedia.org
cryptodaily.co.uk
cryptopolitan
cryptoslate
Readwrite.com
Valuewalk.com
Beincrypto
Coinspeaker
Hackernoon
'''

targets = inputs.split()
targets = [i.split(".")[0] if len(i.split(".")[0])>2 else i for i in targets]
sources = df["Session source / medium"]
matched = {t : [] for t in targets}

for t in targets:
  for s in sources:
    if re.search(t, re.sub(" ", "", s), re.IGNORECASE):
      matched[t].append(s)

for i in matched:
  if len(matched[i]) > 1:
    for a in matched[i]:
      if "paid_content" in a:
        matched[i] = [a]
        break
    else:
      matched[i] = [matched[i][1]]

# Special
matched["nftevening"] = ["NFTev / paid_content"]

newDF = pd.DataFrame()
newDF["sourceName"] = inputs.split()
newDF["matchedName"] = [i[0] if len(i) > 0 else "-" for i in matched.values()]
mergedDF = newDF.merge(df[["Session source / medium", "Sessions"]], left_on="matchedName", right_on="Session source / medium", how="left")
mergedDF.fillna(0, inplace=True)
mergedDF["Sessions"] = mergedDF["Sessions"].astype(int)
resultDF = mergedDF[["sourceName", "Sessions"]]

print("-"*50, "MERGEDDF", "-"*50)
print(mergedDF)
print("-"*50, "RESULTDF", "-"*50)
print(resultDF)
# notMatched - try manually with the abbreviation or a part of the name
print("-"*50, "CHECK", "-"*50)
print(mergedDF[mergedDF["matchedName"] == "-"]["sourceName"])
