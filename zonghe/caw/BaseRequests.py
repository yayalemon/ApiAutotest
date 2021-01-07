'''
1.增加异常的处理
2.新建一个session，使用session发送请求，自动管理cookie
'''
import requests
class BaseRequests:
    def __init__(self):
        self.session=requests.session()

    def get(self,url,**kwargs):
        '''
        封装requests中get方法，增加打印，增加异常处理，使用session发送请求
        :param url:
        :param kwargs:关键字参数
        :return:
        '''
        try:
            r=self.session.get(url,**kwargs)
            print(f"发送get请求，URL：{url},请求参数：{kwargs}成功")
            return r
        except Exception as e:
            print(f"发送get请求，URL：{url},请求参数：{kwargs}异常，异常信息为：{e}")
    def post(self,url, data=None,json=None,**kwargs):
        '''

        :param url:
        :param data:
        :param json:
        :param kwargs:
        :return:
        '''

        try:
            r=self.session.post(url,data=data,json=json,**kwargs)
            print(f"发送post请求，URL：{url},请求参数data：{data},json：{json}，其他：{kwargs}成功")
            return r
        except Exception as e:
            print(f"发送post请求，URL：{url},请求参数data：{data},json：{json}，其他：{kwargs}异常，异常信息为：{e}")

if __name__ == '__main__':
    pass
    # data={"mobilephone":15006007018,"pwd":"1258868"}
    # r=BaseRequests().get(r"http://jy001:8081//futureloan/mvc/api/member/login")
    # print(r.text)
    # d=BaseRequests().post("http://www.httpbin.org/post",data=data)
    # print(d.text)