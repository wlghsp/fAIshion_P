import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_image(images,count):
    idx = 0
    for image in images:
        if image.select_one("div.icon_group > ul > li")["title"] != '여성':
            image_url = image.select_one("div.li_inner > div.list_img > a > img")["data-original"]
            with urlopen("http:" + image_url) as file:
                with open("C:/Users/kojaejeung/Desktop/패션추천시스템프로젝트/shirt_images/shirt" + str(count) + '_' + str(idx) +".jpg", 'wb') as h:
                    img = file.read()
                    h.write(img)
            idx = int(idx) + 1
    print(count,'done')

 
def main():
    temp = ""
    count = 0
    for num in range(1,3):
        # 블레이저
        blazer_URL = f"https://store.musinsa.com/app/items/lists/002003/?page={num}"
        # 셔츠
        shirt_URL = f"https://store.musinsa.com/app/items/lists/001002/?page={num}"
        # 후드티

        # 맨투맨

        # 티셔츠

        # 위에 맞는 url명을 requests.get(요기에 넣어주시면 됩니다.)
        response = requests.get(shirt_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.select("#searchList > li")

        if temp == images:
            break
        temp = images
        # print(len(images))
        get_image(images,count)
        count += 1

main()