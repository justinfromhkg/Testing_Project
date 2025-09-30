import requests
from bs4 import BeautifulSoup
import time

for page in range(1, 6):
    url = f"https://nocturnespider.baicizhan.com/practise/42/PAGE/{page}.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10146) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    titles = soup.find_all(class_="sojob-item-main clearfix")
    for item in titles:
        finance_tag = item.find(class_="field-financing")
        if finance_tag:
            finance_span = finance_tag.find("span")
            if finance_span and finance_span.string == "已上市":
                name_tag = item.find(class_="company-name")
                job_tag = item.find("h3")
                if name_tag and job_tag:
                    name_a = name_tag.find("a")
                    job_a = job_tag.find("a")
                    if name_a and job_a:
                        name = name_a.string.strip()
                        job = job_tag.text.strip()
                        job_url = job_a.attrs.get("href", "")
                        print(f"{name},{job},{job_url}")
                        with open(r"C:\Users\liaoj\Desktop\工作数据.txt", "a", encoding="utf-8") as f:
                            f.write(name + "," + job + "," + job_url + "\n")
    time.sleep(2)