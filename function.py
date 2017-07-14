import requests
import json
import urllib
import  Tkinter
import tkMessageBox
from PIL import Image , ImageTk

Access_token='5697615882.a918ceb.8a12a664f5d84dff9d0b4802205e1d78'
base='https://api.instagram.com/v1/'


tkobj=Tkinter.Tk()
tkobj.title("INSTABOT")

def self():
    url=base+'users/self/?access_token='+Access_token
    print url
    self_info=requests.get(url).json()

    branch=Tkinter.Tk()
    if self_info['meta']['code'] == 200:
        if len(self_info['data']):
            Tkinter.Label(branch, font=(None, 20), text="The username : "+self_info['data']['username']).grid(row=0, column=0)
            #print 'Username: %s' % (self_info['data']['username'])
            Tkinter.Label(branch, font=(None, 20), text="No. of followers : " + str(self_info['data']['counts']['followed_by'])).grid(row=1,column=0)

            #print 'No. of followers: %s' % (self_info['data']['counts']['followed_by'])
            Tkinter.Label(branch, font=(None, 20), text="Following : " + str(self_info['data']['counts']['follows'])).grid(row=2,column=0)

            #print 'No. of people you are following: %s' % (self_info['data']['counts']['follows'])
            Tkinter.Label(branch, font=(None, 20), text="No. of posts : " + str(self_info['data']['counts']['media'])).grid(row=3,column=0)

            #print 'No. of posts: %s' % (self_info['data']['counts']['media'])
        else:
            Tkinter.label(branch,text= 'User does not exist!').gird(row=3,column=0)
    else:
        Tkinter.label(branch, text='ERROR!!!').gird(row=3, column=0)
        print 'Status code other than 200 received!'
    branch.mainloop()


def get_user_id(username):
    url=(base+'users/search?q=%s&access_token=%s') %(username,Access_token)
    print url
    user_id=requests.get(url).json()
    if len(user_id['data'][0]):
         return user_id['data'][0]['id']
    else :
        print 'user doesnot exist'

def user_info(user_id):
     url = (base+'users/%s/?access_token='+Access_token )%(user_id)
     print url
     user=requests.get(url).json()
     branch=Tkinter.Tk()
     if user['meta']['code']==200:
         if len(user['data']):
             Tkinter.Label(branch, font=(None, 20), text="The username : " + user['data']['username']).grid(row=0,column=0)

             #print 'Username: %s' % (user['data']['username'])
             Tkinter.Label(branch, font=(None, 20), text="No. of Followers : " + str(user['data']['counts']['followed_by'])).grid(row=1,column=0)

             #print 'No. of followers: %s' % (user['data']['counts']['followed_by'])
             Tkinter.Label(branch, font=(None, 20), text="Following : " + str(user['data']['counts']['follows'])).grid(row=2,column=0)

             #print 'No. of people you are following: %s' % (user['data']['counts']['follows'])
             Tkinter.Label(branch, font=(None, 20),text="Posts : " + str(user['data']['counts']['media'])).grid(row=3, column=0)

             #print 'No. of posts: %s' % (user['data']['counts']['media'])
         else:
             Tkinter.label(branch, text='User does not exist!').gird(row=3, column=0)
             print 'User does not exist!'
     else:
         Tkinter.label(branch, text='Status code other than 200 received!').gird(row=3, column=0)
         print 'Status code other than 200 received!'

def display_self_media():
    canvas = Tkinter.Canvas(tkobj, width=400, height=400)
    canvas.pack()
    im = Image.open('self_media.jpg')
    im = im.convert('RGB')
    im.save('Apple.pgm')
    img = Tkinter.PhotoImage(file="Apple.pgm")
    canvas.create_image(20, 20, image=img)



def get_self_media():
    url=(base+'users/self/media/recent/?access_token='+Access_token)

    self_media=requests.get(url).json()
    if self_media['data'][0]['images']:
        print 'url is ',self_media['data'][0]['images']['standard_resolution']['url']
        print 'media id is',self_media['data'][0]['id']

        urllib.urlretrieve(self_media['data'][0]['images']['standard_resolution']['url'], 'self_media.jpg')
        display_self_media()
        print 'the image has been succesfully downloaded'

    else:
        print 'ERROR'
def get_user_media(user_id):
    url=(base+'users/%s/media/recent/?access_token=%s')%(user_id,Access_token)
    user_media=requests.get(url).json()
    if user_media['data'][0]['images']:
        print 'url is ', user_media['data'][0]['images']['standard_resolution']['url']
        urllib.urlretrieve(user_media['data'][0]['images']['standard_resolution']['url'], "user_media.jpg")
        print 'the image has been succesfully downloaded'
        print 'user media id =',user_media['data'][0]['id']
        put_like(user_media['data'][0]['id'])



def getuname():
    uname=user_entername.get()
    user_id=get_user_id(uname)
    user_info(user_id)
def get_umedia():
    uname=user_entername.get()
    user_id=get_user_id(uname)
    get_user_media(user_id)
    canvas = Tkinter.Canvas(tkobj, width=400, height=400)
    canvas.pack()
    im = Image.open('user_media.jpg')
    im = im.convert('RGB')
    im.save('umedia.pgm')
    img = Tkinter.PhotoImage(file="umedia.pgm")
    canvas.create_image(20, 20, image=img)
def put_like(media_id):
    url=(base+'media/%s/likes') %(media_id)
    payload={"access_token":Access_token}
    print url
    post_like=requests.post(url,payload).json()
    print post_like
    if post_like['meta']['code']==200:
        print 'Succesfully liked the post'
    else :
        print 'Unsuccesfull in liking the post'

def post_comment():
    uname=user_entername.get()
    user_id=get_user_id(uname)
    url = (base + 'users/%s/media/recent/?access_token=%s') % (user_id, Access_token)
    user_media = requests.get(url).json()
    if user_media['data'][0]['images']:
        media_id=user_media['data'][0]['id']
    else:
        print "Error "
    print 'media id =',media_id
    comment_text=comment.get()
    print comment_text
    url=(base+'media/%s/comments') %(media_id)
    payloads={'access_token':Access_token,'text':comment_text}
    post_Cmmnt=requests.post(url,payloads).json()
    if post_Cmmnt['meta']['code']==200:
        print "comment posted"
    else:
        print "unsuccesfull try"



but=Tkinter.Button(tkobj,text='display My details',command=self).grid(row=1,column=0)
user_entername=Tkinter.StringVar()
Tkinter.Label(tkobj,text='Search for another user:').grid(row=2,column=0)
Enter_uname=Tkinter.Entry(tkobj,width=15,textvariable=user_entername).grid(row=3,column=0)
#user_id=get_user_id((user_entername.get()))
but_show_self_media=Tkinter.Button(tkobj,text='Show  my recent media',command=get_self_media).grid(row=1,column=2)
but_user=Tkinter.Button(tkobj,text='Show details',command=getuname).grid(row=3,column=1)
but_user_media=Tkinter.Button(tkobj,text="Show media",command=get_umedia).grid(row=3,column=4)
but_user_media_like=Tkinter.Button(tkobj,text='put a Like',command=get_umedia).grid(row=3,column=5)
comment=Tkinter.StringVar()
Tkinter.Label(tkobj,text='Enter comment here(enter the username too)').grid(row=4,column=0)
Enter_comment=Tkinter.Entry(tkobj,width=20,textvariable=comment).grid(row=4,column=1)
but_put_cmmnt=Tkinter.Button(tkobj,text='Post the comment',command=post_comment).grid(row=4,column=2)


tkobj.mainloop()