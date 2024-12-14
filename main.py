from utils.extractHtml import getHtml
import pandas as pd

flipUrl='https://www.flipkart.com/search?q=laptops&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_4_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_4_0_na_na_na&as-pos=4&as-type=TRENDING&suggestionId=laptops&requestId=64520a9a-60ac-4332-abdb-b5a88c5c80f1'
 
flipHeader= {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-full-version": "\"131.0.6778.110\"",
    "sec-ch-ua-full-version-list": "\"Google Chrome\";v=\"131.0.6778.110\", \"Chromium\";v=\"131.0.6778.110\", \"Not_A Brand\";v=\"24.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"15.0.0\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1"
  }

if __name__=='__main__':
    flipData= getHtml(websiteUrl=flipUrl,showBrowser=True,screenshotName='lp1')
    allData=[]
    alltiles=[t.text() for t in flipData.css ('div[class="KzDIhZ"]')]
    print(alltiles)
    allRating=[r.text() for r in flipData.css ('div[class="XQDdHH"]')]
    print(allRating)
    allPrice=[p.text() for p in flipData.css ('div[class="Nx9bqj_4b5DiR"]')]
    print(allPrice)
    flipData={
        'tiles':alltiles,
        'ratings':allRating,
        'price':allPrice
    }
    allData.append(flipData)
flipData=pd.DataFrame(allData)
flipData.to_csv('flipData.csv')