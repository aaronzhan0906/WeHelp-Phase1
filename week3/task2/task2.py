import ssl
import bs4
import urllib.request as req
import csv

ssl._create_default_https_context = ssl._create_unverified_context

def get_web_title(url):
    post_data = []

    request = req.Request(url, headers={
        "cookie": "over18=1;",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    
    post_root = root.find_all("div", class_="title")  
    like_dislike_count_root = root.find_all("div", class_="nrec")

    for artical_title in post_root:
        if artical_title.a is not None:
            post_data.append(artical_title.a.string)
            # if like_dislike_count_root[post_root.index(artical_title)].string is not None:
            

            page_link = "https://www.ptt.cc" + artical_title.a["href"]
            sub_request = req.Request(page_link, headers={
                "cookie": "over18=1;",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
            })
            with req.urlopen(sub_request) as sub_response:
                sub_data = sub_response.read().decode("utf-8")
            sub_webpage = bs4.BeautifulSoup(sub_data, "html.parser")

            get_publishtime = sub_webpage.find_all("span", class_="article-meta-value")
            if get_publishtime:
                post_data.append(get_publishtime[-1].string)
    
    # get the previous page url
    prepage = root.find("a", class_="btn wide", string="‹ 上頁")  
    new_url = "https://www.ptt.cc" + prepage["href"]
    return post_data, new_url

url = "https://www.ptt.cc/bbs/Lottery/index.html"
for i in range(3):
    post_data, url = get_web_title(url)
    print(post_data)  

# write the data to article.csv in [問題] 享受輸的感覺539,4,Fri Jul 14 23:34:43 2023
with open("article.csv", mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Like/Dislike", "Publish Time"])
    for data in post_data:
        writer.writerow(data)
