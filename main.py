import requests
from bs4 import BeautifulSoup
print("\n Tool Download All Images in Web")

P = input("\nWebsite: ")

page = requests.get(P)
soup = BeautifulSoup(page.content,"html.parser")
wrapper = soup.find("body")

images = wrapper.find_all("img")
for image in images:
    Data = image["src"]
    print("\nData: ")
    print(Data)
    if ";" in Data:
        continue
    downloadPath = ".Img_Down"
    filetmp = Data.split('/')

    for files in filetmp:
        if ".png" in files or ".gif" in files or ".jpeg" in files or ".jpg" in files or ".webp" in files:
            filename = files
            break
    
 
    print(filename)
    response = requests.get(Data)

    file = open(downloadPath + filename, "wb")
    file.write(response.content)
    file.close()