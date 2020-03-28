
import requests
from bs4 import BeautifulSoup

def get_page (url):
    try:
        page = requests.get(url)
        if page.status_code==200:
            soup = BeautifulSoup(page.text,"lxml")
            return soup
        else:
            print("error finding page",e)
    except Exception as e:
        print("error->",e)

def search_snapdeal(search_term='mobile',start_pos=0):
    url=f"https://www.snapdeal.com/acors/json/product/get/search/1/{start_pos}/20?q=&sort=dhtl&brandPageUrl=&keyword={search_term}&k3=true|k5=0|k6=0|k8=0&pincode=&vc=&webpageName=searchResult&campaignId=&brandName=&isMC=false&clickSrc=unknown&showAds=true&cartId=&page=srp"
    soup=get_page(url)
    if soup:
        print("download page")
        return soup
    else:
        print("what is happening here")    

# amazon

# flipkart 

# extract data from snapdeal
# extract data from amazon
# extract data from flipkart
soup = search_snapdeal()

container=soup.find_all('div', attrs={'class':'product-tuple-listing'})

print(len(container))



