#
# import urllib.request
#
# url = 'https://api.douban.com/v2/book/2129650'
#
# with urllib.request.urlopen(url) as f:
#     headers = f.getheaders()  # 报文头部
#     body = f.read()  # 报文内容
#
#     print(f.status, f.reason)  # 打印状态码、原因语句
#     for k, v in headers:
#         print(k + ': ' + v)
#
#     print(body.decode('utf-8'))


# # 导入urllib 库下request模块
# from urllib import request
#
# # 向指定的url发送请求，并返回服务器响应的类文件对象
# response = request.urlopen("http://www.baidu.com")
#
# # 类文件对象支持 文件对象的操作方法，如read()方法读取文件全部内容，返回字符串
# html = response.read()
#
# # 打印字符串
# print(html)

from urllib import request


def loadPage():
    # 包含一个请求报头的headers, 发送的请求会附带浏览器身份发送
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'}
    # 构造一个请求对象
    req = request.Request("http://www.baidu.com/", headers=headers)
    # 发送http请求，返回服务器的响应内容
    # response响应是一个类文件对象
    response = request.urlopen(req)
    # 类文件对象支持文件操作的相关方法，比如read()：读取文件所有内容，返回字符串
    return response.read()


if __name__ == "__main__":
    # print __name__
    html = loadPage()
    # 打印字符串，也就是整个网页的源码
    print(html)
