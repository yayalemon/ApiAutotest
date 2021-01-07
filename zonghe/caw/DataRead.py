'''
读文件的方法
'''
import configparser
import os

import yaml


def get_project_path():
    '''
    获取当前工程的路径
    :return:
    '''
    cp=os.path.realpath(__file__)
    # print(cp)  D:\ApiAutoTest\zonghe\caw\DataRead.py
    cd=os.path.dirname(cp)
    # print(cd)  #D:\ApiAutoTest\zonghe\caw
    return os.path.dirname(cd)+"\\"  #D:\ApiAutoTest\zonghe\
def read_ini(file_path,key):
    '''
    读取文件的配置
    :param file_path: 配置文件的路径
    :param key: key值
    :return: key对应的value
    '''
    file_path=get_project_path()+file_path
    config=configparser.ConfigParser()
    config.read(file_path)
    return config.get("env",key) #env对应的ini文件的[env]

def read_yaml(file_path):
    '''
    读取yaml文件
    :param file_path: 文件路径
    :return: 文件内容
    '''
    file_path=get_project_path()+file_path
    with open(file_path,"r",encoding="utf-8") as f:
        content=f.read()
        #content读取到的是文件的字符串格式，将其解析为yaml格式的文本
        return yaml.load(content,Loader=yaml.FullLoader)

if __name__ == '__main__':
    pass
    # url=read_ini(r"data_env\env.ini","url")pass
    # print(url)  #http://jy001:8081/
    # db=read_ini(r"data_env\env.ini","db")
    # print(db)
    # print(type(db))#<class 'str'> {"ip":"jy001","port":"4406","user":"root","pwd":"123456","dbname":"future"}
    # db=eval(db) #字符串转成字典
    # print(db)
    # print(type(db))#<class 'dict'> {'ip': 'jy001', 'port': '4406', 'user': 'root', 'pwd': '123456', 'dbname': 'future'}

    # c=read_yaml(r"data_case/register_fail.yaml")
#     # print(c)