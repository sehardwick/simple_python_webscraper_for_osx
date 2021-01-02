

#imports
from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

#set colors for print statements
class colors:
    blue = '\033[94m'
    red = '\033[91m'
    end = '\033[0m'

#define search funcion
def StartSearch():


    search = input("Search for: ")
    print("")
    params = {"q": search}
    parent_dir_name = "./scraped_images/"
    dir_name = parent_dir_name + search.replace(" ", "_").lower()

#create parent directory "scraped_images" if it doesn't already exist
    if not os.path.isdir(parent_dir_name):
        os.makedirs(parent_dir_name)

#create directory for images if it doesn't exist in osX
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    r = requests.get("http://www.bing.com/images/search", params=params)

    soup = BeautifulSoup(r.text, features="html.parser")
    links = soup.findAll("a", {"class": "thumb"})

    for item in links:
        img_obj = requests.get(item.attrs["href"])
        title = item.attrs["href"].split("/")[-1]
#test for server request delay
        try:
#test for access to image
            try:
    #image is accessible and can be dowloaded/saved
                img = Image.open(BytesIO(img_obj.content))
                img.save("./" + dir_name + "/" + title, img.format)
                print("Saved " + colors.blue + title + colors.end + " to " + colors.red + search +
                      colors.end + " folder")
                print("")
    #image cannot be accessed
            except:
                print("Could not save image " + colors.red + title + colors.end)
                print("")
    #timeout exception
        except:
            print("Could not request image " + colors.red + title + colors.end)
            print("")
    print("")

#iterate the search function
    StartSearch()

#begin search
StartSearch()
