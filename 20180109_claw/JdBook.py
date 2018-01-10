from urllib.request import  urlopen
from bs4 import  BeautifulSoup



html = urlopen("http://search.jd.com/Search?keyword=Python&enc=utf-8&book=y&wq=Python&pvid=33xo9lni.p4a1qb")

data = BeautifulSoup(html.read(), "html.parser")
bookNamelist =  data.find_all("div",{"class","p-name"})
for book in  bookNamelist:
    print(book.getText())


