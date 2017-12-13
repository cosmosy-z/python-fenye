# Author Z
import tornado.web
import math
from backend.fenyemokuai.pagination import Pagination

LIST_INFO = [
    {"username":"alex","email":"alex@163.com"},
]


class IndexHandler(tornado.web.RequestHandler):
    def get(self, page):
    # 每页显示5条数据
    # page是当前页
    # 第一页：0:5
    # LIST_INFO[0:5]
    # 第二页：5:10
    # LIST_INFO[5:10]
    # start ＝ （page － 1） ＊5
    # end ＝ page＊5

        # if not page: #如果没有传入值
        #     page = 1#则值为1
        # try:
        #     page = int(page)#如果page传进来了，就把它转换为数字
        # except:
        #     page = 1 #如果数字都不是，则值为1
        #
        # if page < 1:# 如果page小于1
        #     page = 1 # page就＝1
        # start = (page - 1) * 5 # start
        # end = page * 5 #end

        page_obj = Pagination(page,10,"index",LIST_INFO)#创建分页模块对象
        str_page = page_obj.fenyeyema()#得出下方的页码号
        page_now = page_obj.pagenow()#得出现在的页面
        current_list = page_obj.currentlist()#得出每页展示的内容

        self.render('home/index.html',list_info = current_list,current_page=page_now,str_page=str_page) #显示分片取出的信息


    def post(self,page):
        user = self.get_argument('username')
        email = self.get_argument('email')
        temp = {"username":user,"email":email}
        LIST_INFO.append(temp) #将新添加的东西加入LIST，当然没有数据库之前一重启服务器这些数据肯定都没了，因为这写数据现在存在内存里
        self.redirect("/index/"+page)#重定向




