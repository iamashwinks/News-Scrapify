from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://news.google.com/search?q="
search = input("Enter the search string: ")

str = search.replace(" ","%20")
src = str + "&hl=en-IN&gl=IN&ceid=IN%3Aen"

uClient = uReq(my_url + src)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

news = page_soup.findAll("a",{"class": "VDXfz"})
about = page_soup.findAll("div",{"class": "a5SXAc iYiEmb"})

for ab in about:
    print(ab.span.text)
    
for n, a in zip(news, about):
    ref = n["href"]
    title = n.text
    source = a.span.text
    news_time = a.find("span",{"class": "oM4Eqe"})
    time = news_time.span.text
    print(ref)
    print(title)
    print(source)
    print(time)

