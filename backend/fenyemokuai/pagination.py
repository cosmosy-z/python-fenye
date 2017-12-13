# Author Z
import math

class Pagination(object):
    def __init__(self,page,xiaoxigeshu,href,listinfo):
        self.page = int(page)
        self.xiaoxigeshu = xiaoxigeshu #每页多少个消息
        self.href = href
        self.listinfo= listinfo #把全局变量的那个LISTINFO弄过来，搞成一个字段，就是把列表里的东西全部导过来

    def pagemessage(self,):
        if not self.page: #如果没有传入值
            self.page = 1#则值为1
        try:
            self.page = int(self.page)#如果page传进来了，就把它转换为数字
        except:
            self.page = 1 #如果数字都不是，则值为1

        if self.page < 1:# 如果page小于1
            self.page = 1 # page就＝1

        start = (self.page - 1) * self.xiaoxigeshu  # start
        end = self.page *self.xiaoxigeshu  # end

        return start,end

    def fenyeyema(self):#得出下方的页码号
        str_page = """"""
        all_pager = math.ceil(len(self.listinfo) / self.xiaoxigeshu)

        if all_pager <= 10:
            c = 0
            t = all_pager
        elif all_pager > 10:

            if self.page <= 6:
                c = 0
                t = 10
            elif self.page > 6:
                if self.page + 5 > all_pager:
                    c = all_pager - 11
                    t = all_pager
                else:
                    c = self.page - 5
                    t = self.page + 5

        # 跳转导首页

        first_page = "<a href='/%s/1'>首页</a>" % (self.href)
        str_page = str_page + first_page

        # 上一页
        if self.page - 1 <= 0:
            previous_page = "<a href='/%s/1'>上一页</a>" % (self.href)
        else:
            previous_page="<a href='/%s/%s'>上一页</a>"%(self.href,self.page-1)
        str_page = str_page + previous_page

        for p in range(c, t):
            if p + 1 == self.page:
                temp = "<a class = 'active' href='/" + self.href + "/" + str(p + 1) + "'>" + str(p + 1) + "</a>"
            else:
                temp = "<a href='/" + self.href + "/" + str(p + 1) + "'>" + str(p + 1) + "</a>"
            str_page = str_page + temp

        # 下一页
        if self.page + 1 > all_pager:
            next_page = "<a href='/%s/%s'>下一页</a>" % (self.href,all_pager)
        else:
            next_page="<a href='/%s/%s'>下一页</a>"%(self.href,self.page + 1)
        str_page = str_page + next_page


        # 跳转到尾页

        last_page = "<a href='/%s/%s'>尾页</a>" % (self.href,all_pager)
        str_page = str_page + last_page

        #页面跳转
        jump = """<input type='text'/><a onclick="Jump('%s',this);">GO</a>""" % (self.href,)
        script = """<script>
                   function Jump(baseUrl,ths){
                       var val = ths.previousElementSibling.value;
                       if(val.trim().length>0){
                           location.href = val;
                       }
                   }            
                   </script>"""
        str_page = str_page + jump + script


        return str_page

    def pagenow(self):#得出现在的页面
        # 传给前端的页数，保证是当前页数，这一句话相当于有多少信息 ／ 每页5条 ＝ 当前是第多少页,
        #  比如当前已经有5条信息，这个时候pagenow就要等于2了，因为这时候如果＝1，那么发过去到前端，
        # 前端这时的current——page还是1，前端点提交psot往后端发的时候，发过来的就是1，而不是2，
        # 所以第5条的时候，pagenow要等于2
        page_now = math.ceil((len(self.listinfo) + 1) / self.xiaoxigeshu)
        return page_now

    def currentlist(self):#得出每页展示的内容
        start,end = self.pagemessage()
        current_list = self.listinfo[start:end]#得出每页的消息切片值
        return current_list