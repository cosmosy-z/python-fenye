# Author Z
import tornado.web
import math

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

        if not page: #如果没有传入值
            page = 1#则值为1
        try:
            page = int(page)#如果page传进来了，就把它转换为数字
        except:
            page = 1 #如果数字都不是，则值为1

        if page < 1:# 如果page小于1
            page = 1 # page就＝1
        start = (page - 1) * 5 # start
        end = page * 5 #end
        current_list = LIST_INFO[start:end] #分片取出



        page_now = math.ceil((len(LIST_INFO)+1)/5) #传给前端的页数，保证是当前页数，这一句话相当于有多少信息 ／ 每页5条 ＝ 当前是第多少页, 比如当前已经有5条信息，这个时候pagenow就要等于2了，因为这时候如果＝1，那么发过去到前端，前端这时的current——page还是1，前端点提交psot往后端发的时候，发过来的就是1，而不是2，所以第5条的时候，pagenow要等于2

        #接下来要尝试把这个做成一个模块
        str_page = """"""
        all_pager = math.ceil(len(LIST_INFO)/5)

        if all_pager <=10:
            c = 0
            t = 10
        elif all_pager > 10:
            if page <= 6:
                c=0
                t=10
            elif page > 6:
                if page + 5 > all_pager:
                    c = all_pager -11
                    t = all_pager
                    print("page+5>all_pager")
                else:
                    c = page - 5
                    t = page + 5
        print(all_pager,c,t)
        for p in range(c , t):
            if p+1 == page :
                temp = "<a class = 'active' href='/index/" + str(p + 1) + "'>" + str(p + 1) + "</a>"
            else:
                temp = "<a href='/index/"+str(p+1) + "'>"+str(p+1)+"</a>"
            str_page=str_page+temp



        self.render('home/index.html',list_info = current_list,current_page=page_now,str_page=str_page) #显示分片取出的信息


    def post(self,page):
        user = self.get_argument('username')
        email = self.get_argument('email')
        temp = {"username":user,"email":email}
        LIST_INFO.append(temp) #将新添加的东西加入LIST，当然没有数据库之前一重启服务器这些数据肯定都没了，因为这写数据现在存在内存里
        self.redirect("/index/"+page)#重定向