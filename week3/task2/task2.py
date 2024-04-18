import ssl
import bs4
import urllib.request as req
import csv

ssl._create_default_https_context = ssl._create_unverified_context

def get_web_title(url):
    with open("article.csv", mode="w", newline='') as file:
        writer = csv.writer(file)  

        # 遍歷所有頁面
        for _ in range(3):
            request = req.Request(url, headers={
                "cookie": "over18=1;",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
            })
            with req.urlopen(request) as response:
                data = response.read().decode("utf-8")
            root = bs4.BeautifulSoup(data, "html.parser")
            
            post_root = root.find_all("div", class_="title")  
        
            for artical_title in post_root:
                if artical_title.a is not None:
                    # get the title of the article
                    ArticleTitle = artical_title.a.string
                
                    # get the like and dislike of the article
                    nrec_div = artical_title.parent.find("div", class_="nrec")
                    span_element = nrec_div.find("span", class_="hl")
                    if span_element:
                        LikeDislikeCount = span_element.string
                    else:
                        LikeDislikeCount = "0"
            
                    # get the publish time of the article
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
                        PublishTime = get_publishtime[-1].string

                    writer.writerow([ArticleTitle, LikeDislikeCount, PublishTime])
            
            # get the previous page url for next iteration
            prepage = root.find("a", class_="btn wide", string="‹ 上頁")  
            if prepage:
                url = "https://www.ptt.cc" + prepage["href"]
            else:
                break

url = "https://www.ptt.cc/bbs/Lottery/index.html"
get_web_title(url)

