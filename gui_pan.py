from tkinter import *
from tkinter.filedialog import *
import urllib.request
import urllib.parse#用于对url中的中文字符的解码
def download():
    b = b'/:?=.\/'#对url中的特定的符号不解码
    file=urllib.parse.quote(ent.get(),b)
    file=urllib.request.urlopen(file).read()
    filename=asksaveasfilename()
    with open(filename,'wb') as fn :
        fn.write(file)
def upload():
    filename=askopenfilename()
    url='http://127.0.0.1:5000/upload'
    data='''------WebKitFormBoundarytED18J4GyGmsQyPw
Content-Disposition: form-data; name="file"; filename="%s"
Content-Type: application/octet-stream

[file]
------WebKitFormBoundarytED18J4GyGmsQyPw--'''%filename.split('/')[-1]
    file=open(filename,'rb').read()
    data=bytes(data,'utf-8')
    data=data.replace(bytes('[file]','utf-8'),file)
    req=urllib.request.Request(url)
    req.add_header('Content-Type','multipart/form-data; boundary=----WebKitFormBoundarytED18J4GyGmsQyPw')
    html=urllib.request.urlopen(req,data=data).read().decode('utf-8')
    ent.delete(0,END)
    ent.insert(0,'http://127.0.0.1:5000/%s'%html)
    print(html)
root = Tk()
root.title('网盘')
ent=Entry(root,width=40)#输入框控件
pan_upload=Button(root,text=' 上 传 ',command=upload)
pan_download=Button(root,text=' 下 载 ',command=download)
ent.grid()#grid()方法是用来做页面布局的
pan_upload.grid()
pan_download.grid()
mainloop()
