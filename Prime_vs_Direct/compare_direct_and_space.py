from s4gpy.s4gpy import S4GAPI
import re
import config
import urllib
import requests
import json
import os


#first register with your vod-prime.space credentials
api=S4GAPI(config.user,config.password)
regex1 = r"\s(.*)"
regex2 = r"^.*?\{[^\d]*(\d+)[^\d]*}.*$"
direct_video_id=[]


def direct_api():
    for s in api.get_direct_api().get_direct_schedule(): 
        try:
            imdb_data=s.content().imdb_id()
            value = re.search(regex1, s.airing_time_human)
            value = value.group(1).split(':')
            if value[0]>="19" and value[0]<="23" :
                direct_video_id.append(str(s.video_id))
        except AttributeError: #in case platform.vod-prime.space fucks up things
            print(f"{s.airing_time};{s.video_id};UNKNOWN;UNKNOWN")
            continue
    return direct_video_id

def netflix_rec(direct_video_id):
    with open('total_extract.json') as json_data:
        data_dict = json.load(json_data)
        direct_video_id = list(dict.fromkeys(direct_video_id))
        count = 0
    for reco_video_id in data_dict:
        count += 1
        if reco_video_id in direct_video_id:
            print(f"Content ID : {reco_video_id} is recommended by Netflix {data_dict[reco_video_id]['count']} times")
    print (f'Number total of items {count} ')


# https://hapi.vod-prime.space/api/netflix/thumbnails?limit=9999&date_from=2020/10/01&date_to=now&sorted_by=count
# direct_api()
netflix_rec(direct_api())
# netflix_rec(direct_video_id)
