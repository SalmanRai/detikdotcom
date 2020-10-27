from bs4 import BeautifulSoup
import requests
print('NOTE : INI GRAB SAMPE 100 PAGE')
print("SILAHKAN UBAH SESUAI KEINGINAN DI CODINGANNYA")

key : input("Masukan keywords :")

url = 'https://www.detik.com/search/searchall?query={key}&siteid=2&sortby=time&page='
batasHalaman = 100
 
for pages in range(1, batasHalaman+1):
 
    source = requests.get(url+str(pages)).text
    soup = BeautifulSoup(source, 'html.parser')
 
    for article in soup.find_all('article'):
        headline = article.find('h2',class_= 'title').text
        print(headline)
 
        tanggal = article.find('span',class_='date').text 
        print(tanggal)
 
        snippet = article.find('p').text
        print(snippet)
        print("DONE, THANK YOU!!!")