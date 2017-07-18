import Tkinter
import ttk
from function import  self ,get_self_media ,display_self_media , get_user_id ,get_user_media , display_umedia , fetch_comments,put_like ,post_comment
from maintool import tag_media
master=Tkinter.Tk()
master.title('InstaBot')
master.configure(background='black')
#----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*
self_frame=Tkinter.LabelFrame(master,text="Self",fg='blue',font=(None,20))
self_frame.configure(background='black')
self_frame.grid(row=7,column=0,padx=(30,30),pady=(10),)
self_det_but=Tkinter.Button(self_frame,text="Show My Details",fg='red',command=self).grid(column=1,row=2,padx=(10),pady=(10))
i1=Tkinter.StringVar()
Tkinter.Label(self_frame,text='Choose media number:',fg='red').grid(row=1,column=2)
media_no=ttk.Combobox(self_frame,width=12,textvariable=i1)
media_no['values']=(1,2,3,4,5,6,7,8,9)
media_no.set(0)
media_no.grid(row=2,column=2,pady=(10))
downld_self_media=Tkinter.Button(self_frame,text='Download',fg='red',command=lambda  :get_self_media(media_no.get())).grid(row=2,column=3,pady=(10))
show_self_media=Tkinter.Button(self_frame,text='Show media',fg='red',command=lambda  : display_self_media(media_no.get()) ).grid(row=2,column=4,padx=(10),pady=(10))

#----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*
#----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*----*-----*

user_frame=Tkinter.LabelFrame(master,text="User",fg='red',font=(None,20))
user_frame.configure(background='black')
user_frame.grid(row=9,column=0,padx=(10,10))
username=Tkinter.StringVar()
username.set('tourism._nepal')

Tkinter.Label(user_frame,text='Enter Username :',fg='green').grid(row=8,column=0)
enter_user=Tkinter.Entry(user_frame,width=15,textvariable=username).grid(row=9,column=0)
user_det_but=Tkinter.Button(user_frame,text="Show Details",fg='green',command= lambda  : get_user_id(username.get())).grid(column=1,row=9,padx=(10))
i2=Tkinter.StringVar()
Tkinter.Label(user_frame,text='Choose media number:',fg='green').grid(row=8,column=2)
media_no2=ttk.Combobox(user_frame,width=12,textvariable=i2)
media_no2['values']=(1,2,3,4,5,6,7,8,9)
media_no2.set(1)
media_no2.grid(row=9,column=2,pady=(10))
downld_user_media=Tkinter.Button(user_frame,text='Download',fg='green',command=lambda: get_user_media(username.get(),media_no2.get())).grid(row=9,column=3,pady=(10))
show_user_media=Tkinter.Button(user_frame,text='Show media',fg='green',command=lambda : display_umedia(media_no2.get())).grid(row=9,column=4,padx=(10,10),pady=(10))
commenttext=Tkinter.StringVar()
fetch_comment=Tkinter.Button(user_frame,text='Fetch Comments',fg='green',command=lambda : fetch_comments(username.get(),media_no2.get())).grid(row=10,column=0,pady=(10),padx=(10))
Tkinter.Label(user_frame,text='Post a Comment :',fg='green').grid(row=10,column=1, padx=(10,10),pady=(10))
enter_commnt=Tkinter.Entry(user_frame,width=15,fg='green',textvariable=commenttext).grid(row=10,column=2,padx=(10,10),pady=(10))
cmmnt_but=Tkinter.Button(user_frame,text='Post Comment',fg='green',command= lambda : post_comment(username.get(),media_no2.get(),commenttext.get())).grid(row=10,column=3,padx=(10,10),pady=(10))
like_but =Tkinter.Button(user_frame,text='Like!!!',fg='green',command=lambda: put_like(username.get(),media_no2.get())).grid(row=10,column=4,padx=(10,10),pady=(10))

#*-----*----*-----*----*-----*----*-----*--*-----*----*-----*----*-----*----*-----*--*-----*----*-----*----*-----*----*-----*--*-----*----*-----*----*-----*----*-----*--*-----*----*-----*----*-----*----*-----*--*-----*----*-----*----*-----*----*-----*--
#*-----*----*-----*----*-----*----*-----*--*-----*----*-----*----*-----*----*-----*--*-----*----*-----*----*-----*----*-----*--*-----*----*-----*----*-----*----*-----*--*-----*----*-----*----*-----*----*-----*--*-----*----*-----*----*-----*----*-----*--
main_frame=Tkinter.LabelFrame(master,text='Targeted Marketing tool',fg='green',font=(None,20))
main_frame.configure(background='black')
main_frame.grid(row=15,column=0,pady=(10))
commnt=Tkinter.StringVar()
tagname=Tkinter.StringVar()

#Tkinter.Label(main_frame,text='Enter the Username :',fg='blue').grid(row=16,column=0,padx=(10,10))
#enter_uname=Tkinter.Entry(main_frame,width=15,fg='blue').grid(row=17,column=0,padx=(10,10),pady=(10))
Tkinter.Label(main_frame,text='Enter the Tag name you want to search :',fg='blue').grid(row=17,column=0,pady=(10))
enter_tag=Tkinter.Entry(main_frame,width=20,fg='blue',textvariable=tagname).grid(row=17,column=1,pady=(10))
Tkinter.Label(main_frame,text='Enter the comment you want to post :',fg='blue').grid(row=18,column=0,padx=(10),pady=(10))
enter_comment=Tkinter.Entry(main_frame,width=25,fg='blue',textvariable=commnt).grid(row=18,column=1,padx=(10),pady=(10))
start=Tkinter.Button(main_frame,text='Start',font=(None,15),fg='blue',command=lambda : tag_media(tagname.get(),commnt.get())).grid(row=19,column=0,pady=(10),padx=(100,130))
#*-----*----*-----*----*-----*----*-----*--*-----*----*-----*----*-----*----*-----*--*-----*----*-----*----*-----*----*-----*--*-----*----*-----*----*-----*----*-----*--*-----*----*-----*----*-----*----*-----*--*-----*----*-----*----*-----*----*-----*--*-----*----*-----*----*-----*----*-----*--
#*-----*----*-----*----*-----*----*-----*--*-----*----*-----*----*-----*----*-----*--*-----*----*-----*----*-----*----*-----*--*-----*----*-----*----*-----*----*-----*--


master.mainloop()