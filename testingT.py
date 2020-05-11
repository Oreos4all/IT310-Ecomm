#straight from the documentation
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4.diagnose import diagnose
from bs4 import BeautifulSoup
import re

#Amazon stuff
#AT = "C:/Users/JoJo/Desktop/Class stuff/it310/ArtOfWarTest.html"
AT = "C:/Users/JoJo/Desktop/Class stuff/it310/Webscrapping/ccbbAMZN.html"
page = open(AT, encoding= "utf8")

#Ebay stuff
#BT = "C:/Users/JoJo/Desktop/Class stuff/it310/EbayAOW.html"
BT = "C:/Users/JoJo/Desktop/Class stuff/it310/BigEbay.html"
page2 = open(BT, encoding= "utf8")

#set up soup
soup = BeautifulSoup(page.read(), features="lxml")
soup2 = BeautifulSoup(page2.read(), features="lxml")

#For Amazon
# title section
bookTitle = soup.find('div', {"class" : "a-section a-spacing-none"})
soupTitle = 'Title:'

for i in bookTitle.findAll('span'):
    soupTitle = soupTitle + " " + i.get_text().strip()  
#this print statment is so we can see what's being printed
#will change to full file print stament later >;3c or not its just for debugging really so i might remove in push to submission

print (soupTitle)

# now for the price section...
#('div', {"class" : "inlineBlock-display"})
bookPrice = soup.find('div', {"class" : "a-color-price"})
soupPrice = 'Price: '

for i in bookPrice.findAll('span'):
    soupPrice = soupPrice + i.get_text()
print(soupPrice)

#scrapping information
#webURL = "https://www.amazon.com/Art-War-Sun-Tzu/dp/1545211957/ref=sr_1_10?dchild=1&keywords=The+Art+Of+War&qid=1588799654&sr=8-10"
webURL = "https://www.amazon.com/Chicka-Boom-Bill-Martin-Jr-ebook/dp/B0066U1SJU/ref=msx_wsirn_kids_v1_18?_encoding=UTF8&pd_rd_i=B0066U1SJU&pd_rd_r=cbf0a9a2-4dce-499e-b64f-89db1b91db61&pd_rd_w=xZju1&pd_rd_wg=52DUV&pf_rd_p=34771393-4268-4bbe-b7ca-a2ad72c8692b&pf_rd_r=QW7CX84B9M54AB782TWR&psc=1&refRID=QW7CX84B9M54AB782TWR"
sInfo = 'Website scrapped from ' + "Amazon: " + webURL

print(sInfo)



#lets do...hmm 
#https://www.ebay.com/p/237754240
bookTitle2 = soup2.find('div', {"class" : "product-info no-product-picture"})
soupTitle2 = 'Title: '

for i in bookTitle2.find('h1'):
    soupTitle2 = soupTitle2 + i

print(soupTitle2)

# now for price...
bookPrice2 = soup2.find('div', {"class" : "item-price-logistics-wrapper"})
soupPrice2 = 'Price: '

for i in bookPrice2.findAll('span'):
    soupPrice2 = soupPrice2 + i.get_text()
print(soupPrice2)

#Hit em' with that INFO
#webURL2 = "https://www.ebay.com/p/237754240"
webURL2 = "https://www.ebay.com/p/244721?iid=383499440480"
sInfo2 = 'Website scrapped from ' + "Ebay: " + webURL2

print(sInfo2)


with open('testingW', 'w') as file:
    #AMZN

    file.write(soupTitle + '\n')
    file.write(soupPrice + '\n')
    file.write(sInfo + '\n\n')

    #NJIT
    file.write(soupTitle2 + '\n')
    file.write(soupPrice2 + '\n')
    file.write(sInfo2 + '\n')
