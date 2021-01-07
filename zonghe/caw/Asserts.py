'''
断言
'''
import pytest_check as ck
# check(r.json(),ogin_data['expect'],'code,msg,status')
def check(r_json,expect,keys):
    '''
    校验r_json与expect中响应的key对应的value
    :param r_json: 实际响应的结果：r.json
    :param expect: 预期结果
    :param keys: 校验的key列表，用逗号分隔，code,msg,status
    :return:
    '''
    ks=keys.split(",")
    for k in ks:
        real=r_json[k]
        exp=expect[k]
        try:
            # assert str(real)==str(exp)
            ck.equal(str(real),str(exp))
        except Exception as e:
            print(f"响应的信息：{r_json},预期的结果：{expect},校验{k}失败")

