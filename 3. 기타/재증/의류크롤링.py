import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_url(images_url,count):
    url_list = []
    main_url = "https://store.musinsa.com"

    for image_url in images_url:
        if image_url.select_one("div.icon_group > ul > li")["title"] != '여성':
            image_url = image_url.select_one("div.li_inner > div.list_img > a ")["href"]
            url_list.append(main_url+image_url)

    return get_image(url_list,count)

def get_image(url_list,count):
    idx = 0

    for url in url_list:
        response = requests.get(url)
        # print(response)
        soup = BeautifulSoup(response.text, 'html.parser')
        image_url = soup.select_one("#bigimg")["src"]
        
        with urlopen("http:"+image_url) as file:
            with open("C:/Users/kojaejeung/Desktop/패션추천시스템프로젝트/man_to_man_images/man_to_man"+str(count)+'_'+str(idx)+".jpg", "wb") as h:
                img = file.read()
                h.write(img)
        idx += 1

    print(count,"done")
 
def main():
    temp = ""
    count = 0
    for num in range(1,100):
        blazer_URL = f"https://store.musinsa.com/app/items/lists/002003/?page={num}"
        shirt_URL = f"https://store.musinsa.com/app/items/lists/001002/?page={num}"
        hood_t_URL = f"https://store.musinsa.com/app/items/lists/001004/?page={num}"
        man_to_man_URL = f"https://store.musinsa.com/app/items/lists/001005/?page={num}"
        t_shirt_URL = f"https://store.musinsa.com/app/items/lists/001001/?page={num}"

        # 위에 맞는 url명을 requests.get(요기에 넣어주시면 됩니다.)
        response = requests.get(man_to_man_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        images_url = soup.select("#searchList > li")

        if temp == images_url:
            break
        temp = images_url

        get_url(images_url, count)
        count += 1

main()

# "https://store.musinsa.com" + "/app/product/detail/1539678/0"