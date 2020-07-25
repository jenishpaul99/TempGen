from tkinter import *
from tkinter import filedialog
import pickle
import os
root = Tk()
root['bg']='#b9fabe'
root.title('TempGen')

directoryFile = open('directoryPickle', 'rb')      
direct = pickle.load(directoryFile) 
directoryFile.close()

def directorySettings():
    def folderSelector():
        folderDirectory=filedialog.askdirectory(initialdir='/',title='Choose Folder')
        extension=extensionsEntry.get()
        if extension!='' and folderDirectory!='':
            direct[extension]=folderDirectory+'/'
            directoryFile = open('directoryPickle', 'wb')
            pickle.dump(direct, directoryFile)
            directoryFile.close()

    def directoryDetails():
        directoryWindow=Toplevel(window)
        directoryWindow['bg']='#b9fabe'
        r=0
        for i in direct:
            temp=Label(directoryWindow,text=i+' : '+direct[i],bg='#b9fabe',font='Calibri 12 bold')
            temp.grid(row=r,sticky=W)
            r+=1

    window=Toplevel(root)
    window['bg']='#b9fabe'
    extensionsLabel=Label(window,text='Enter extension:\n(For Nodejs and Front End \nuse node and fe as extension)',bg='#b9fabe',font='Calibri 16')
    extensionsEntry=Entry(window,bd=0,bg='#6983ff',font='Calibri 16 bold')
    directorySelectBtn=Button(window,bd=1,text='Choose Directory',command=folderSelector,bg='#fff',font='Calibri 16')
    directoryDetailsBtn=Button(window,bd=1,text='Directory Details',command=directoryDetails,bg='#fff',font='Calibri 14')
    extensionsLabel.grid(row=0,padx=30,pady=10)
    extensionsEntry.grid(row=1,padx=30,pady=10)
    directorySelectBtn.grid(row=2,padx=30,pady=10)
    directoryDetailsBtn.grid(row=3,padx=30,pady=10)
    window.mainloop()

def test():
    filename=name.get().split('.')
    headerTemp=['<!DOCTYPE html>\n', '<html>\n', '    <head>\n', '        <title>\n', '            Document\n', '        </title>\n', 
'''
       <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">\n''', '    </head>\n', '''
<body>\n''', '    <nav class="navbar navbar-default">\n', '        <div class="container-fluid">\n', '            <div class="navbar-header">\n', '                <a href="/" class="navbar-brand">Document</a>\n', '            </div>\n', '''
      <div class="collapse-navbar-collapse">\n''', '                <ul class="nav navbar-nav navbar-right">\n', '''
           <li><a href="/">Login</a></li>\n''', '                    <li><a href="/">Sign Up</a></li>\n', '''
    <li><a href="/">LogOut</a></li>\n''', '                </ul>\n', '            </div>\n', '        </div>\n', '    </nav>\n', '   ']
    footerTemp=['</body>\n', '<footer>\n', '    TradeMark 2019\n', '</footer>\n', '</html>']
    if varNode.get():
        os.mkdir(direct['node']+filename[0])
        os.mkdir(direct['node']+filename[0]+'/views/')
        os.mkdir(direct['node']+filename[0]+'/models/')
        os.mkdir(direct['node']+filename[0]+'/public/')
        os.mkdir(direct['node']+filename[0]+'/middleware/')
        os.mkdir(direct['node']+filename[0]+'/routes/')
        os.mkdir(direct['node']+filename[0]+'/views/partials')
        header=open(direct['node']+filename[0]+'/views/partials/header.ejs','w')
        footer=open(direct['node']+filename[0]+'/views/partials/footer.ejs','w')
        header.write(''.join(headerTemp))
        footer.write(''.join(footerTemp))
        header.close()
        footer.close()
        os.system('cmd /c code '+'"'+direct['node']+filename[0]+'/app.js'+'"')

    elif varFE.get():
        os.mkdir(direct['fe']+filename[0])
        os.system('cmd /c code ' + '"'+direct['fe']+filename[0]+'/'+filename[0]+'.html'+'"')
        os.system('cmd /c code ' + '"'+direct['fe']+filename[0]+'/'+filename[0]+'.css'+'"')
        os.system('cmd /c code ' + '"'+direct['fe']+filename[0]+'/'+filename[0]+'.js'+'"')
        
    else:
        os.system('cmd /c code '+'"'+direct[filename[1]]+'.'.join(filename)+'"')

label=Label(root,text= 'Enter file name',bg='#b9fabe',font='Calibri 16')
name=Entry(root,bd=0,bg='#6983ff',font='Calibri 16 bold')
btn=Button(root,text='Create',command=test,bd=1,bg='#fff',font='Calibri 16')
addbtn=Button(root,text='Settings',bd=1,bg='#fff',font='Calibri 16',command=directorySettings)
varNode=IntVar()
node=Checkbutton(root,text='Node',variable=varNode,bg='#b9fabe',font='Calibri 16')
varFE=IntVar()
fe=Checkbutton(root,text='FE',variable=varFE,bg='#b9fabe',font='Calibri 16')
root.bind('<Return>', lambda event=None: btn.invoke())
label.grid(row=0,padx=30,pady=10)
name.grid(row=1,padx=30,pady=10)
name.focus()
btn.grid(row=3,padx=30,pady=10)
node.grid(row=2,sticky=W,padx=30,pady=10)
addbtn.grid(row=4,padx=30,pady=10)
fe.grid(row=2,sticky=E,padx=30,pady=10)
root.mainloop()