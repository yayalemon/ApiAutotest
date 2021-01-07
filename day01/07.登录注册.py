import requests

'''
1.
"mobilephone='15006007018'
pwd='123456'
regname=''"
'''
# cs={"mobilephone":15006007017,"pwd":123456,"regname":""}
# r=requests.post(url,data=cs)
# print(r.text)
# assert r.json()["code"]=="10001"
'''"
2.
mobilephone='15006008107'
pwd='123456789112345678'
regname='haha'"
'''
# cs={"mobilephone":15006007015,"pwd":123456789112345678,"regname":"haha"}
# r=requests.post(url,data=cs)
# print(r.text)
# assert r.json()["code"]=="10001"

'''
3.
"mobilephone='15006008111'
pwd=''
regname=''"	
{"status":"0","code":"20103","data": "msg": "参数错误：参数不能为空"}
'''
# cs={"mobilephone":15006008111,"pwd":"","regname":""}
# r=requests.post(url,data=cs)
# print(r.text)
# assert r.json()["code"]=="20103"

'''
4.
"mobilephone=''
pwd='85846215'
regname=''"
{"status":"0","code":"20103","data": "msg": "参数错误：参数不能为空"}
'''
def test(mobilephone,pwd,code,regname="",register_url="http://jy001:8081//futureloan/mvc/api/member/register"):
    url=register_url
    cs={"mobilephone":mobilephone,"pwd":pwd,"regname":regname}
    r=requests.post(url,data=cs)
    print(r.text)
    assert r.json()["code"]=="%s"%code
test('','85846215',20103)
'''
5.
"mobilephone=''
pwd=''
regname=''"	{"status":"0","code":"20103","data": "msg": "参数错误：参数不能为空"}
'''
test('','',20103)
'''
6.
"mobilephone='18006007167'
pwd=''
regname='丫丫'"	{"status":"0","code":"20103","data": "msg": "密码不能为空"}

'''
test('18006007167','',20103,regname="丫丫")
'''
7.
"mobilephone=''
pwd='aaa58585'
regname='wawa'"	{"status":"0","code":"20103","data": "msg": "参数错误：参数不能为空"}
'''
test('','aaa58585',20103,regname="wajjjjjjjjjj")
'''
8.
"mobilephone='15060715011'
pwd='aaa55'"	{"status":"0","code":"20108","data": "msg": "密码长度必须为6~18"}

'''
test('15060715011','aaa55',20108)
'''
9.
"mobilephone='15060715012'
pwd='abc'"	{"status":"0","code":"20108","data": "msg": "密码长度必须为6~18"}
'''
test('15060715012','abc',20108)
'''
10.
"mobilephone='15060715012'
pwd='aaaaaa1952154126415'"	{"status":"0","code":"20108","data": "msg": "密码长度必须为6~18"}
'''
test('15060715012','aaaaaa1952154126415',20108)
'''
11.
"mobilephone='1'
pwd='abc1234'"	{"status":"0","code":"20109","data": "msg": "手机号码格式不正确"}
'''
test('1','abc1234',20109)
'''
12.
"mobilephone='136485'
pwd='abc1234'"	{"status":"0","code":"20109","data": "msg": "手机号码格式不正确"}
'''
test('136485','abc1234',20109)
'''
13.
"mobilephone='1234567890'
pwd='abc1234'"	{"status":"0","code":"20109","data": "msg": "手机号码格式不正确"}
'''
test('1234567890','abc1234',20109)
'''
14.
"mobilephone='12345678941012'
pwd='abc1234'"	{"status":"0","code":"20109","data": "msg": "手机号码格式不正确"}

'''
test('12345678941012','abc1234',20109)
'''
15.
"mobilephone='11111111111'
pwd='abc1234'"	{"status":"0","code":"20109","data": "msg": "手机号码格式不正确"}
'''
test('11111111111','abc1234',20109)
'''
16.
"mobilephone='15006007018'
pwd='abc1234'"	{"status":"0","code":"20110","data": "msg": "手机号码已被注册"}
'''
test('15006007018','abc1234',20110)
def test1(mobilephone,pwd,code,register_url="http://jy001:8081//futureloan/mvc/api/member/login"):
    url=register_url
    cs={"mobilephone":mobilephone,"pwd":pwd}
    r=requests.post(url,data=cs)
    print(r.text)
    assert r.json()["code"]=="%s"%code
'''
1.
"mobilephone='15006007018'
pwd='abc1234'"	{"status":"1","code":"10001","data": "msg": "成功"}
2.
"mobilephone='15006007018'
pwd='abc1234'"	{"status":"0","code":"20102","data": "msg": "服务器异常"}
3.
"mobilephone='15006007018'
pwd=''"	{"status":"0","code":"20103","data": "msg": "参数错误：参数不能为空"}
4.
"mobilephone=''
pwd='abc1234'"	{"status":"0","code":"20103","data": "msg": "参数错误：参数不能为空"}
5.
"mobilephone=''
pwd=''"	{"status":"0","code":"20103","data": "msg": "参数错误：参数不能为空"}
6.
"mobilephone='15871034161'
pwd='123456'"	{"status":"0","code":"20111","data": "msg": "用户名或者密码错误"}
'''
test1('15006007017','123456',10001)
test1('15006007018','',20103)
test1('','123456',20103)
test1('','',20103)
test1('15871034161','123456',20111)

'''
7.
"mobilephone='123'
pwd='123456'"	{"status":"0","code":"20111","data": "msg": "用户名或者密码错误"}
8.
"mobilephone='15006007018'
pwd='12568'"	{"status":"0","code":"20111","data": "msg": "用户名或者密码错误"}
9.
"mobilephone='15006007018'
pwd='1258868'"	{"status":"0","code":"20111","data": "msg": "用户名或者密码错误"}

'''
test1('123','123456',20111)
test1('15006007018','12568',20111)
test1('15006007018','1258868',20111)