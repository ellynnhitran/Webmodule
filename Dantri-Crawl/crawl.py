# 1. Download dantri page
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://dantri.com.vn"
connection = urlopen(url)
raw_data = connection.read()
text = raw_data.decode("utf-8")

# with open (" ")
# f = open("dantri.html", "wb")
# f.write(raw_data)
# f.close()

soup = BeautifulSoup(text, "html.parser")
# print(soup.prettify())

# 2 Find the ROI
ul_news = soup.find("ul", "ul1 ulnew") # find one
# print(ul_news.prettify())


# 3 Extract data
li_list = ul_news.find_all("li")
# print(li_list)

# list_of_dictionaries
news_items = []

for li in li_list:
    a = li.h4.a 
    link = url + a["href"]
    title = a.text 
    item = {
        "Title": title,
        "Link": link
    }
    news_items.append(item)
print(news_items)

# 4 Save data
pyexcel.save_as(records=news_items, dest_file_name="dantri.xlsx")

