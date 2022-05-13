from PIL import Image
import requests
from io import BytesIO
from bs4 import BeautifulSoup


def spoon(enchant_name):
    base_url = f'https://na.mabibase.com/enchants/search?q=localName%2C%22{enchant_name}%22&page=0#enchant_preview-31631'
    response = requests.get(base_url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    img = Image.open(BytesIO(response.content))
    print(img)
            
# from selenium import webdriver
# import webbrowser
# def spoon(enchant_name):
#     driver = webdriver.Chrome()
#     driver.get(f'https://na.mabibase.com/enchants/search?q=localName%2C%22{enchant_name}%22&page=0')
#     button = driver.find_elements_by_class_name('button')
#     return 
    
spoon('meteoroid')