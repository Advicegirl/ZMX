import pandas as pd
import re

toMatched = '''
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
TheCoinRepublic
TheMarketPeriodical.com
Bitcoinworld
BitcoinInsider
coin-update.de
Trend-online.com
TheCryptoUpdates
Cryptowisser
AmbCrypto
CoinGape
forklog.com
de.cointelegraph.com
cryptoninjas.net
FinanceFeeds
EstrategiasdeInversión'''

file_path = input("Input the path of the file: ")
df = pd.read_excel(file_path)

header = ["Channels", "PV"]
df.columns = header

targets = toMatched.split()
targets = [i.split(".")[0] if len(i.split(".")[0])>2 else i for i in targets]
sources = df["Channels"]
matched = {t : [] for t in targets}

for t in targets:
  t = re.sub(r"[^a-zA-Z0-9ó]", "", str(t))
  for s in sources:
    parsed = re.sub(r"[^a-zA-Z0-9]", "", str(s))
    if re.search(t, parsed, re.IGNORECASE):
      matched[t].append(s)

matchedDF = pd.DataFrame()
matchedDF["Channels"] = matched.keys()
matchedDF["Matched"] = [i[0] if len(i) == 1 else "-" for i in matched.values()]

final = matchedDF.merge(df, left_on="Matched", right_on="Channels", how="left", suffixes=('_matched', '_original'))
final["PV"].fillna(0, inplace=True)
final["PV"] = final["PV"].astype(int)

remained = df[~df["Channels"].isin(final["Channels_original"])].sort_values("Channels")

print("-"*50, "MATCHEDDF", "-"*50)
print(final)
print("-"*50, "RESULTDF", "-"*50)
print(final["PV"].to_string(index=False))
# notMatched - try manually with the abbreviation or a part of the name
print("-"*50, "CHECK", "-"*50)
print("-"*25, "CHANNELS LEFT BLANK", "-"*25)
print(final[final["Matched"] == "-"].sort_values("Channels_matched")["Channels_matched"])
print("-"*25, "CHANNELS LEFT FROM ORIGINAL", "-"*25)
print(remained["Channels"])

matchedDF.to_excel("matched.xlsx", index=False)
final.to_excel("matched_final.xlsx", index=False)
