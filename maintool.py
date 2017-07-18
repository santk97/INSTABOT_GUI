
import requests
import tkMessageBox


def tag_media(tag,comment):

    Access_token = '5697615882.a918ceb.8a12a664f5d84dff9d0b4802205e1d78'
    base = 'https://api.instagram.com/v1/'
    #comment_text = raw_input('enter the comment you want to make ')
    #tag=raw_input('enetr the tag you are searching for ')
    url = base +'tags/%s/media/recent?access_token=%s' %(tag,Access_token)
    print url

    media =requests.get(url).json()
    if media['data'][0]['images']:

        rang=len(media['data'])
        tkMessageBox.showinfo('Media Found','Total  media with the  tag '+str(rang))
        for i in range(rang):

            print media['data'][i]['images']['standard_resolution']['url']

            media_id=media['data'][i]['id']
            url = (base + 'media/%s/comments') % (media_id)
            payloads = {'access_token': Access_token, 'text': comment}
            post_Cmmnt = requests.post(url, payloads).json()
            if post_Cmmnt['meta']['code'] == 200:
                tkMessageBox.showinfo('Succesfull','Comment posted on image '+str(i+1))
            else:
                tkMessageBox.showinfo("Unsuccesfull","Could not post the comment")
            i+=1
    else:
        tkMessageBox.showerror('Error','No media Found with the tag')



