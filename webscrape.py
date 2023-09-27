from bs4 import BeautifulSoup
import requests
url = "https://insulin.store/humalog/insulin-humalog-vial-10-ml/"

headers =  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
page = requests.get(url, headers = headers)
response = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
price = float(soup.find(id="total_price").get_text().strip('$'))
print ("$",price)


urltwo = "https://www.google.com/shopping/product/15737249068825768559?sca_esv=568362559&rlz=1C1RXMK_enUS1019US1019&sxsrf=AM9HkKnMowcYgahQP1MSqbnGotANaqMYUw:1695693401253&q=humalog+insulin&biw=1920&bih=969&dpr=1&prds=eto:12803139871616740394_0,pid:7640690421513193980&sa=X&ved=0ahUKEwjjzsW3l8eBAxVEkokEHUjSCRkQ8wIIgAw"
page = requests.get(urltwo, headers = headers)
response = requests.get(urltwo)
soup = BeautifulSoup(page.content, 'html.parser')
pricetwo = float(soup.find('span', class_='g9WBQb').get_text().strip('$'))
print (pricetwo)

urlthree = "https://canadianinsulin.com/product/humalog-vial-100-units-ml/"
page = requests.get(urlthree, headers = headers)
response = requests.get(urlthree)
soup = BeautifulSoup(page.content, 'html.parser')
pricethree = float(soup.find('p', class_='price').get_text().strip('$'))
print (pricethree)

urlfour = "https://www.google.com/shopping/product/1?q=humalog+insulin&prds=epd:2221974124496111182,eto:2221974124496111182_0,pid:2221974124496111182&sa=X&ved=0ahUKEwjb57KgmMeBAxWVhIkEHcfxAFkQ9pwGCAU"
page = requests.get(urlfour, headers = headers)
response = requests.get(urlfour)
soup = BeautifulSoup(page.content, 'html.parser')
pricefour = float(soup.find('span', class_='g9WBQb').get_text().strip('$'))
print (pricefour) 

urlfive = "https://www.google.com/shopping/product/1?q=humalog+insulin+buy+online&prds=epd:6098527067727738182,eto:6098527067727738182_0,pid:6098527067727738182&sa=X&ved=0ahUKEwj78aXLmMeBAxWJkIkEHdlMAQwQ9pwGCAU"
page = requests.get(urlfive, headers = headers)
response = requests.get(urlfive)
soup = BeautifulSoup(page.content, 'html.parser')
pricefive = float(soup.find('span', class_='g9WBQb').get_text().strip('$'))
print (pricefive)

lowestprice = min(price, pricetwo, pricethree, pricefour, pricefive)
print("Here is the lowest price! " + str(lowestprice))


if(price == lowestprice):
    print (url)
elif(pricetwo == lowestprice):
    print(urltwo)
elif(pricethree == lowestprice):
    print(urlthree)
elif(pricefour == lowestprice):
    print(urlfour)
elif(pricefive == lowestprice):
    print(urlfive)
    
