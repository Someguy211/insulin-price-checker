from bs4 import BeautifulSoup
import requests
url = "https://insulin.store/humalog/insulin-humalog-vial-10-ml/"

headers =  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
page = requests.get(url, headers = headers)
response = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
price = soup.find(id = "total_price").get_text()
print ("$",price)


urltwopricetwo = "https://www.google.com/shopping/product/15737249068825768559?sca_esv=568362559&rlz=1C1RXMK_enUS1019US1019&sxsrf=AM9HkKnMowcYgahQP1MSqbnGotANaqMYUw:1695693401253&q=humalog+insulin&biw=1920&bih=969&dpr=1&prds=eto:12803139871616740394_0,pid:7640690421513193980&sa=X&ved=0ahUKEwjjzsW3l8eBAxVEkokEHUjSCRkQ8wIIgAw"
page = requests.get(urltwopricetwo, headers = headers)
response = requests.get(urltwopricetwo)
soup = BeautifulSoup(page.content, 'html.parser')
pricetwo = soup.find('span', class_='g9WBQb').get_text()
print (pricetwo)

urlthreepricethree = "https://canadianinsulin.com/product/humalog-vial-100-units-ml/"
page = requests.get(urlthreepricethree, headers = headers)
response = requests.get(urlthreepricethree)
soup = BeautifulSoup(page.content, 'html.parser')
pricethree = soup.find('p', class_='price').get_text()
print (pricethree)

urlfourpricefour = "https://www.google.com/shopping/product/1?q=humalog+insulin&prds=epd:2221974124496111182,eto:2221974124496111182_0,pid:2221974124496111182&sa=X&ved=0ahUKEwjb57KgmMeBAxWVhIkEHcfxAFkQ9pwGCAU"
page = requests.get(urlfourpricefour, headers = headers)
response = requests.get(urlfourpricefour)
soup = BeautifulSoup(page.content, 'html.parser')
pricefour = soup.find('span', class_='g9WBQb').get_text()
print (pricefour) 

urlfivepricefive = "https://www.google.com/shopping/product/1?q=humalog+insulin+buy+online&prds=epd:6098527067727738182,eto:6098527067727738182_0,pid:6098527067727738182&sa=X&ved=0ahUKEwj78aXLmMeBAxWJkIkEHdlMAQwQ9pwGCAU"
page = requests.get(urlfivepricefive, headers = headers)
response = requests.get(urlfivepricefive)
soup = BeautifulSoup(page.content, 'html.parser')
pricefive = soup.find('span', class_='g9WBQb').get_text()
print (pricefive)

def bestprice():
    lowestprice = [price, pricetwo, pricethree, pricefour, pricefive]
    lowest_value = min(lowestprice)
    print(lowestprice)

