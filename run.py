# @time：2021/4/21 23:17
# @Aut：秋雨
# @File: .py
# @QQ：1957800403

from python_0414.lesson07 import read_data,api_fun,wirte_result

# 接口测试实战,封装成函数
def execute_fun(filename,sheetname):    #文件名，表单名
    cases = read_data(filename,sheetname)
    # print(cases)
    for case in cases:         #依次访问cases中的数据 ，保存到定义的case变量中  #for循环
        # print(case)           #打印结果  一整个字典数据
        case_id = case['case_id']
        url = case['url']         #做接口测试只需要获取它的url data就可以了，不需要整个字典数据
        data = eval(case['data'])
        # print(case_id,url,data)        #打印拿的url，data数据
        # print(type(data))            #data数据串的类型

        #获取期望结果，code msg信息
        expect =eval(case['expect'])
        expect_code = expect['code']
        expect_msg = expect['msg']
        print('预期结果code为：{}，msg为：{}'.format(expect_code,expect_msg))

        #执行接口测试
        # 获取case_id,url,data信息后，为了执行接口测试，获取执行接口测试   定义变量接收响应结果
        real_result = api_fun(url=url,data=data)
        # print(real_result)
        #获取实际结果code、msg
        real_code = real_result['code']
        real_msg = real_result['msg']
        print('实际结果code为：{}，msg为: {}'.format(real_code,real_msg))

        # 断言：预期VS实际结果
        if real_code == expect_code and real_msg == expect_msg:
            print('这{}条测试用例执行通过！'.format(case_id))
            final_re = 'passed'
        else:
            print('这{}条测试用例执行不通过！'.format(case_id))
            final_re = 'Failed'
        print('*'*50)

        #写入最终的测试结果到excel测试中，文件名，表单名,用例id,结果列8,参数值
        wirte_result(filename,sheetname,case_id+1,8,final_re)

#调用函数
# execute_fun('D:\\SCB20\\test_data\\test_case_api.xlsx','register')
execute_fun('D:\\SCB20\\test_data\\test_case_api.xlsx','login')