import urllib
import requests

def tag_media():
    Access_token = '5697615882.a918ceb.8a12a664f5d84dff9d0b4802205e1d78'
    base = 'https://api.instagram.com/v1/'
    url = base +'tags/ADVENTURES/media/recent?access_token=%s' %(Access_token)
    print url
    media =requests.get(url).json()
    if media['data'][0]['images']:
        i=0
        rang=len(media['data'])
        print rang
        for i in range(rang):

            print media['data'][i]['images']['standard_resolution']['url']
            i+=1
    else:
        print 'No media error'


tag_media()
