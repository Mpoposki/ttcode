from s4gpy.s4gpy import S4GAPI
import re

#first register with your vod-prime.space credentials
api=S4GAPI("poposki.matthieu@gmail.com","%q^b*2xJASdQ&kTm4SBG2X")
regex = r"\s(.*)"
direct_video_id=[]


def direct_api():
    for s in api.get_direct_api().get_direct_schedule(): 
        try:
            imdb_data=s.content().imdb_id()
            genres="+".join([g["genre"] for g in imdb_data.data.genres])
        except AttributeError: #in case platform.vod-prime.space fucks up things
            print(f"{s.airing_time};{s.video_id};UNKNOWN;UNKNOWN")
            continue
        # print(f"{s.airing_time_human};{s.video_id};{imdb_data.data.title};f{genres}")
        value = re.search(regex, s.airing_time_human)
        value = value.group(1).split(':')
        if value[0]>="19" and value[1]<="23" :
            direct_video_id.append({s.video_id})
            print(direct_video_id)

       

# https://hapi.vod-prime.space/api/netflix/thumbnails?limit=9999&date_from=2020/10/01&date_to=now&sorted_by=count




direct_api()   
