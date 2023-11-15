from flask import jsonify
from bs4 import BeautifulSoup
import requests, re


def get_download_data(data):
  url = 'https://spotifymate.com/'
  ses = requests.Session()
  r = ses.get(url)
  bs = BeautifulSoup(r.text, 'html.parser')
  
  input_elements = bs.find_all('input')
  for input_element in input_elements:
    input_name = input_element.get('name')
    input_value = input_element.get('value')
  
  url = f"https://open.spotify.com/track/{data}?si=ozr18HYkRP-jMDvqKjTEaQ&utm_source=copy-link"
  data = {
    "url": url, 
    f"{input_name}":f"{input_value}"
  }
  
  rpos = ses.post("https://spotifymate.com/action",data=data).text
  
  rgx = re.findall(r'href="(.*?)"', rpos)[0]
  
  
  return rgx
  
  
def Search_video(data):
  return None
  