from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2018/0/0/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
connection = urlopen(url)
raw_data = connection.read()
text = raw_data.decode("utf-8")

soup = BeautifulSoup(text, "html.parser")
table_news = soup.find("table", id="tableContent")

tr_list = table_news.find_all("tr")
print (tr_list)
news_items = [ ]


for tr in tr_list:
    for td in tr:
        td = tr.td
        title = td.find("td", "b_r_c")
        print(title)
    # title = a.text
    # link = url + a["href"]
    # img = a.img
    # image_link = url + img['src']
    # items = {
    #     "Trước Sau": title,
    #     "2014": year1,
    #     "2015": year2,
    #     "2016": year3,
    #     "2017": year4,
    #     "Tăng trưởng": speed
    # }
#     news_items.append(items)

# pyexcel.save_as(records=news_items, dest_file_name="cafes.xlsx")