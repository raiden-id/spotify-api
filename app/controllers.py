
from flask import jsonify
from app.helpers import Search_video, get_download_data
from app import app

import json
baseurl = app.config['BASE_URL']

def spotify_id(q):
  basedata = q
  res = get_download_data(basedata)
  return jsonify({'author':'Konan','results':res})

def search_data(data):
  basedata = baseurl + data
  #results = Stream_video(basedata)
  #return jsonify({'author':'Konan','results':results})
  
  
   # else: return jsonify({'author':'konan','status':False})

