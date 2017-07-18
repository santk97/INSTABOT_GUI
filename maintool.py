
import requests
import tkMessageBox

#this file has the method of the main marketing tool
#this method performs a search for  hashtag throughout the data , using one of the instagram's endpoint Api
def tag_media(tag,comment):

    Access_token = '5697615882.a918ceb.8a12a664f5d84dff9d0b4802205e1d78'
    base = 'https://api.instagram.com/v1/'
   #search for tags using the endpoint
    url = base +'tags/%s/media/recent?access_token=%s' %(tag,Access_token)
    print url

    media =requests.get(url).json()
    if media['data'][0]['images']:

        rang=len(media['data'])
        tkMessageBox.showinfo('Media Found','Total  media with the  tag  : '+str(rang))
        for i in range(rang):

            print media['data'][i]['images']['standard_resolution']['url']
    #post comments on the media found in the results using another endpoint
            media_id=media['data'][i]['id']
            url = (base + 'media/%s/comments') % (media_id)
            payloads = {'access_token': Access_token, 'text': comment}
            post_Cmmnt = requests.post(url, payloads).json()
            if post_Cmmnt['meta']['code'] == 200:
                print 'succesfull'
                #tkMessageBox.showinfo('Succesfull','Comment posted on image :  '+str(i+1))
            else:
                tkMessageBox.showinfo("Unsuccesfull","Could not post the comment")
            i+=1
            if i==rang:
                tkMessageBox.showinfo("Succesfull","Succesfully commented on all posts")
    else:
        tkMessageBox.showerror('Error','No media Found with the tag')



