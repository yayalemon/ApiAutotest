'''
用户模块的管理，按模块管理
'''
import requests
def register(url,baserequests,data):
    '''
    注册接口
    :param url:
    :param baserequests:
    :param data:
    :return:
    '''
    url=url+"futureloan/mvc/api/member/register"
    return baserequests.post(url,data=data)

def querylist(url,baserequests):
    '''

    :param url:
    :param baserequests:
    :return:
    '''
    url = url + "futureloan/mvc/api/member/list"
    return baserequests.get(url)

def login(url,baserequests,data):
    '''
    登录的接口
    :param url:
    :param baserequests:
    :param data:
    :return:
    '''
    url = url + "futureloan/mvc/api/member/login"
    return baserequests.post(url, data=data)