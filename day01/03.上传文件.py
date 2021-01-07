'''
上传文件，本地的文件上传到服务器，比如上传头像，上传附件
'''

import requests
# 上传文件的接口
url="http://www.httpbin.org/post"
# 要上传的文件（本地磁盘的文件）
'''Dictionary of ``'name': file-like-objects``
 {'name': file-tuple}
 ``file-tuple`` can be a 
 2-tuple ``('filename', fileobj)``, 
 3-tuple ``('filename', fileobj, 'content_type')``
 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, 
     where ``'content-type'`` is a string defining the content type of'''

filepath="d:/test.txt"
filepath2="d:/test.png"
with open(filepath,'rb') as f:
    with open(filepath2,"rb") as f2:
        file={
            "file1":(filepath,f), #文件路径，文件对象
            "file2":(filepath2,f2,"image/png")
        }
        r=requests.post(url,files=file)
        print(r.text)