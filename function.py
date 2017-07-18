#making the necessary imports
import requests
import urllib
import  Tkinter
import tkMessageBox
from PIL import Image


#This file has the necessary functions being used in other file

#global variable Access token and base url
Access_token='5697615882.a918ceb.8a12a664f5d84dff9d0b4802205e1d78'
base='https://api.instagram.com/v1/'



#sel method to display the details of own profile
def self():
    url=base+'users/self/?access_token='+Access_token
    print url
    self_info=requests.get(url).json()

    branch=Tkinter.Tk()
    branch.title('SELF DETAILS')
    branch.configure(background='red')
    if self_info['meta']['code'] == 200:
        if len(self_info['data']):
            Tkinter.Label(branch, font=('Helvetica', 20), text="The username : "+self_info['data']['username'],fg='blue').grid(row=0, column=0,pady=(10),padx=(10))
            #print 'Username: %s' % (self_info['data']['username'])
            Tkinter.Label(branch, font=(None, 20), text="No. of followers : " + str(self_info['data']['counts']['followed_by']),fg='blue').grid(row=1,column=0,pady=(10),padx=(10))

            #print 'No. of followers: %s' % (self_info['data']['counts']['followed_by'])
            Tkinter.Label(branch, font=(None, 20), text="Following : " + str(self_info['data']['counts']['follows']),fg='blue').grid(row=2,column=0,pady=(10),padx=(10))

            #print 'No. of people you are following: %s' % (self_info['data']['counts']['follows'])
            Tkinter.Label(branch, font=(None, 20), text="No. of posts : " + str(self_info['data']['counts']['media']),fg='blue').grid(row=3,column=0,pady=(10),padx=(10))

            #print 'No. of posts: %s' % (self_info['data']['counts']['media'])
        else:
            Tkinter.label(branch,text= 'User does not exist!',fg='blue').gird(row=3,column=0,pady=(10),padx=(10))
    else:
        Tkinter.label(branch, text='ERROR!!!',fg='blue').gird(row=3, column=0,pady=(10),padx=(10))
        print 'Status code other than 200 received!'
    branch.mainloop()

#method to display user's own media from the downloaded path using canvas and Tkinter
def display_self_media(i):
        branch = Tkinter.Toplevel()
        val = int(i) - 1
        print val
        branch.configure(background='black')
        canvas = Tkinter.Canvas(branch, width=1000, height=1000)
        path = 'selfmedia_%s_.jpg' % (str(val))
        canvas.pack()
        im = Image.open(path)
        im = im.convert('RGB')
        im.save(path + '.pgm')
        img = Tkinter.PhotoImage(file=path + ".pgm")
        canvas.create_image(40, 40, image=img, anchor='nw')
        branch.mainloop()


# method to download the user's self media and save it to the desired path
def get_self_media(i):
        url = (base + 'users/self/media/recent/?access_token=' + Access_token)
        val = int(i) - 1
        print val
        path = 'selfmedia_%s_.jpg' % (str(i))
        self_media = requests.get(url).json()
        if val >= len (self_media['data'] ):
            print "out of bound"
            tkMessageBox.showwarning("Error",'This media is not available')
        else:
            if self_media['data'][val]['images']:
                print 'url is ', self_media['data'][val]['images']['standard_resolution']['url']
                print 'media id is', self_media['data'][val]['id']
            #using urllib library to download the images
                urllib.urlretrieve(self_media['data'][val]['images']['standard_resolution']['url'], path)

                tkMessageBox.showwarning('succesfull', 'the image has been succesfully downloaded')

            else:
                print 'ERROR'

#method to get user's id  bases on the username of the user being passed as the parameter to the method
#this method performs function via instagram's Api endpoints
def get_user_id(username):
    if len(username)==0:
        tkMessageBox.showwarning('ERROR','Name can not be empty')

    url=(base+'users/search?q=%s&access_token=%s') %(username,Access_token)
    print url
    user_id=requests.get(url).json()
    if len(user_id['data'] ):
        user_info(user_id['data'][0]['id'])
        return user_id['data'][0]['id']

    else :
         tkMessageBox.showwarning("Error",'user does not exist')

#this method has user id as its parameter and on the basis of the user id being passed it uses the perticular endpoint to fetch user details

def user_info(user_id):
     url = (base+'users/%s/?access_token='+Access_token )%(user_id)
     print url
     user=requests.get(url).json()
     branch=Tkinter.Tk()
     branch.title('User details')
     branch.configure(background='black')
     if user['meta']['code']==200:
         if len(user['data'])>1:
             Tkinter.Label(branch, font=('Helvetica', 20), text="The username : " + user['data']['username'],fg='blue').grid(row=0, column=0, pady=(10), padx=(10))
             # print 'Username: %s' % (self_info['data']['username'])
             Tkinter.Label(branch, font=(None, 20),text="No. of followers : " + str(user['data']['counts']['followed_by']),fg='blue').grid(row=1, column=0, pady=(10), padx=(10))

             # print 'No. of followers: %s' % (self_info['data']['counts']['followed_by'])
             Tkinter.Label(branch, font=(None, 20), text="Following : " + str(user['data']['counts']['follows']),fg='blue').grid(row=2, column=0, pady=(10), padx=(10))

             # print 'No. of people you are following: %s' % (self_info['data']['counts']['follows'])
             Tkinter.Label(branch, font=(None, 20), text="No. of posts : " + str(user['data']['counts']['media']),fg='blue').grid(row=3, column=0, pady=(10), padx=(10))

             # print 'No. of posts: %s' % (self_info['data']['counts']['media'])
         else:
             Tkinter.label(branch, text='User does not exist!', fg='blue').gird(row=3, column=0, pady=(10), padx=(10))
     else :
            Tkinter.label(branch, text='ERROR!!!', fg='blue').gird(row=3, column=0, pady=(10), padx=(10))
            print 'Status code other than 200 received!'
     branch.mainloop()

#this method download the users media using instagram api endpoints and the urllib library
def get_user_media(username,i):
    if len(username)==0:
        tkMessageBox.showwarning('ERROR','Name can not be empty')

    url=(base+'users/search?q=%s&access_token=%s') %(username,Access_token)
    print url
    user_id=requests.get(url).json()
    val = int(i) - 1
    print val
    path = 'usermedia_%s_.jpg' % (str(i))
    if len(user_id['data'] ):
        use_id=user_id['data'][0]['id']
    url=(base+'users/%s/media/recent/?access_token=%s')%(use_id,Access_token)
    user_media=requests.get(url).json()
    if user_media['data'][0]['images']:
        print 'url is ', user_media['data'][val]['images']['standard_resolution']['url']
        urllib.urlretrieve(user_media['data'][val]['images']['standard_resolution']['url'], path)
        print 'the image has been succesfully downloaded'
        print 'user media id =',user_media['data'][0]['id']

#this method is used to display the media downloaded by the urllib library by the help of canvas

def display_umedia(i):
    branch = Tkinter.Toplevel()
    val = int(i) - 1
    print val
    branch.configure(background='black')
    canvas = Tkinter.Canvas(branch, width=1000, height=1000)
    path = 'usermedia_%s_.jpg' % (str(i))
    canvas.pack()
    im = Image.open(path)
    im = im.convert('RGB')
    im.save(path + '.pgm')
    img = Tkinter.PhotoImage(file=path + ".pgm")
    canvas.create_image(40, 40, image=img, anchor='nw')
    branch.mainloop()


# this methos puts a like on the user's post
#it has two parameters one for the username and other is the variable which helps in finding the media id of a particula media out of the whole list

def put_like(username,i):
    if len(username)==0:
        tkMessageBox.showwarning('ERROR','Name can not be empty')

    url=(base+'users/search?q=%s&access_token=%s') %(username,Access_token)
    print url
    user_id=requests.get(url).json()
    val = int(i) - 1
    print val

    if len(user_id['data']):
        use_id = user_id['data'][0]['id']
    url = (base + 'users/%s/media/recent/?access_token=%s') % (use_id, Access_token)
    user_media = requests.get(url).json()
    if user_media['data'][0]['images']:
        print 'url is ', user_media['data'][val]['images']['standard_resolution']['url']

        media_id=user_media['data'][val]['id']
        print 'user media id =', user_media['data'][0]['id']
        #here the media id is saved to the variable so that it can be used further for like endpoint

    url=(base+'media/%s/likes') %(media_id)
    #payloads are used to send additional data during post requests
    payload={"access_token":Access_token}
    print url
    post_like=requests.post(url,payload).json()
    print post_like
    if post_like['meta']['code']==200:
        tkMessageBox.showinfo('Succesfull','Succesfully liked the post')
    else :
        tkMessageBox.showinfo('Failed!!','Unsuccesfull in liking the post')

# this method works in similar way as the put like method
#only difference is that it uses a different enpoint

def post_comment(username,i,comment):

    if len(username)==0:
        tkMessageBox.showwarning('ERROR','Name can not be empty')
    if len(comment)==0:
        tkMessageBox.showwarning('ERROR', 'Comment can not be empty')
    url=(base+'users/search?q=%s&access_token=%s') %(username,Access_token)
    print url
    user_id=requests.get(url).json()
    val = int(i) - 1
    print val
    path = 'usermedia_%s_.jpg' % (str(i))
    if len(user_id['data']):
        use_id = user_id['data'][0]['id']
    url = (base + 'users/%s/media/recent/?access_token=%s') % (use_id, Access_token)
    user_media = requests.get(url).json()
    if user_media['data'][0]['images']:
        print 'url is ', user_media['data'][val]['images']['standard_resolution']['url']

        media_id=user_media['data'][val]['id']
        print 'user media id =', user_media['data'][0]['id']

    url=(base+'media/%s/comments') %(media_id)
    payloads={'access_token':Access_token,'text':comment}
    post_Cmmnt=requests.post(url,payloads).json()
    if post_Cmmnt['meta']['code']==200:
        tkMessageBox.showinfo('Succesfull', "Comment Posted!!!")
    else:
        tkMessageBox.showinfo('Unsuccesfull', "Comment Not Posted!!!")


#this method is used to get the list of comments on the user's post by using the appropriate endpoint
#it works in the same way as the like and comment method
def fetch_comments(username,i):
    if len(username) == 0:
        tkMessageBox.showwarning('ERROR', 'Name can not be empty')
    branch=Tkinter.Tk()
    branch.configure(background='black')
    url = (base + 'users/search?q=%s&access_token=%s') % (username, Access_token)
    print url
    user_id = requests.get(url).json()
    val = int(i) - 1
    print val

    if len(user_id['data']):
        use_id = user_id['data'][0]['id']
    url = (base + 'users/%s/media/recent/?access_token=%s') % (use_id, Access_token)
    user_media = requests.get(url).json()
    if user_media['data'][0]['images']:
        print 'url is ', user_media['data'][val]['images']['standard_resolution']['url']

        media_id = user_media['data'][val]['id']
        print 'user media id =', user_media['data'][0]['id']
    url=base+'media/%s/comments?access_token=%s' %(media_id,Access_token)
    comment_list=requests.get(url).json()
    print comment_list
    if comment_list['meta']['code']==200:
        if len(comment_list['data'])>0:
            for x in range(len(comment_list['data'])):
                 Tkinter.Label(branch,text=str(x+1)+' . ' + comment_list['data'][x]['from']['full_name']+' : '+comment_list['data'][x]['text'],fg='blue',font=(None,20)).grid(row=x,column=1)

        else :
            tkMessageBox.showerror('Alert','No comment Found')

    else :
        tkMessageBox.showerror('Error','Code other than 200 recieved')
    branch.mainloop()


#method to find the media with the minimun likes
#it downloads the image and then displays it
def min_likes(username):
    if len(username)==0:
        tkMessageBox.showwarning('ERROR','Name can not be empty')

    url=(base+'users/search?q=%s&access_token=%s') %(username,Access_token)
    print url
    user_id=requests.get(url).json()
    if len(user_id['data'] ):
            use_id=user_id['data'][0]['id']
    url=(base+'users/%s/media/recent/?access_token=%s')%(use_id,Access_token)
    user_media=requests.get(url).json()
    if user_media['meta']['code']:
        list=[]
        count=0
        for x in  range(len(user_media['data'])):
            count=user_media['data'][x]['likes']['count']
            list.append(count)
    else:
        tkMessageBox.showerror('Error','Code other than 200')
    list=sorted(list)
    print list
    for x in range(len(user_media['data'])):
        path='min_like%s.jpg' %(str(x))
        if list[0]==user_media['data'][x]['likes']['count']:
            urllib.urlretrieve(user_media['data'][x]['images']['standard_resolution']['url'], path)
            print 'the image has been succesfully downloaded'
            branch = Tkinter.Toplevel()
            branch.title('Media')
            branch.configure(background='black')
            canvas = Tkinter.Canvas(branch, width=500, height=500)

            canvas.pack()
            im = Image.open(path)
            im = im.convert('RGB')
            im.save(path + '.pgm')
            img = Tkinter.PhotoImage(file=path + ".pgm")
            canvas.create_image(40, 40, image=img, anchor='nw')
            branch.mainloop()
#this methos is similar to the min likes methos but with a slight change
#it find the media with the maximum likes
def max_likes(username):
                if len(username) == 0:
                    tkMessageBox.showwarning('ERROR', 'Name can not be empty')

                url = (base + 'users/search?q=%s&access_token=%s') % (username, Access_token)
                print url
                user_id = requests.get(url).json()
                if len(user_id['data']):
                    use_id = user_id['data'][0]['id']
                url = (base + 'users/%s/media/recent/?access_token=%s') % (use_id, Access_token)
                user_media = requests.get(url).json()
                if user_media['meta']['code']:
                    list = []
                    count = 0
                    for x in range(len(user_media['data'])):
                        count = user_media['data'][x]['likes']['count']
                        list.append(count)



                else:
                    tkMessageBox.showerror('Error', 'Code other than 200')
                list = sorted(list)
                print list
                for x in range(len(user_media['data'])):
                    path = 'min_like%s.jpg' % (str(x))
                    if max(list) == user_media['data'][x]['likes']['count']:
                        urllib.urlretrieve(user_media['data'][x]['images']['standard_resolution']['url'], path)
                        print 'the image has been succesfully downloaded'
                        branch = Tkinter.Toplevel()
                        branch.title('Media')
                        branch.configure(background='black')
                        canvas = Tkinter.Canvas(branch, width=500, height=500)

                        canvas.pack()
                        im = Image.open(path)
                        im = im.convert('RGB')
                        im.save(path + '.pgm')
                        img = Tkinter.PhotoImage(file=path + ".pgm")
                        canvas.create_image(40, 40, image=img, anchor='nw')
                        branch.mainloop()

#these are the functions that have been used