#-*- coding:utf-8 -*-
#coding:gbk
from tkinter import *
import time
import sys
import re

LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("臭猪")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1068x681+10+10')
        self.init_window_name["bg"] = "Seashell"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.init_data_label = Label(self.init_window_name, text="每天的推送")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.init_window_name, text="结果")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)
        #文本框
        self.init_data_Text = Text(self.init_window_name, width=67, height=35)  #原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=70, height=49)  #处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        #按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="按我！", bg="lightblue", width=10,command=self.num_sta)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=1, column=11)


    #功能函数
    def num_sta(self):
        src = self.init_data_Text.get(1.0,END).strip().replace("\n","").replace(" ","")
        #print("src =",src)
        reg = re.compile('(20\d{2}([\.\-/|年月\s]{1,3}\d{1,2}){2}日?(\s?\d{2}:\d{2}(:\d{2})?)?)|(\d{1,2}\s?(分钟|小时|天)前)')

        M = reg.sub('',src)
        reg1 = re.compile('([0-9.]+)[ ]*时')
        MM = reg1.sub('', M)
        reg3 = re.compile('(20\d{2})[ ]*(年|开)')
        MMM = reg3.sub('', MM)
        reg4 = re.compile('([0-9]+)[ ]*月')
        MMMM = reg4.sub('', MMM)
        reg5 = re.compile('([0-9]+)[ ]*日')
        N = reg5.sub('', MMMM)
        #print("\n\n\n去除时间日期后文本\n\n\n", N)
        a = re.findall('([0-9.]+%)(~|\-|到|至)([0-9.]+%)', N)
        a = set(a)
        a = [x for x in a]
        #print("\n\n范围数据(如12%~15%)\n", a)
        #print("数量", len(a))
        reg2 = re.compile('([0-9.]+%)(~|\-|到|至)([0-9.]+%)')
        O = reg2.sub('', N)
        b = re.findall('([0-9.]+)(%|百|美|城|克|-|版|估|手|\|合|世|逾|英|来|票|港|关|房|笔|市|折|涨|平|套|板|毫|微|起|派|区|的|两|附|宗|一|千|[A-Za-z]|毛|动态|指数|台|条|辆|元|城市|高|转|（|袋|股|行|万|处|人|、|型|“|左右|等|分|件|字|是|米|号|位|届|名|后|次|欧|℃|斤|公里|点|场|英里|位|周|架|座|度|M|成|寸|秒|P|k|像素|分钟|K|G|省|小时|公斤|项|户|吨|大|百万|金|种|份|岁|年|款|只|千万|亿|倍|余|多|天|以上|左右元|块|支|美元|家|个|亩|平米|平方米|平方千米|基点|关口)', O)
        b = set(b)
        b = [x for x in b]
        #print("\n\n其他数据(根据数字后词语)\n", b)
        #print("数量", len(b))
        reg6=re.compile( '([0-9.]+)(%|手|套|票|-|百|强|来|世|笔|房|逾|两|英|派|市|合|区|涨|港|平|折|关|起|的|一|毫|估|微|宗|附|版|板|城|条|美|台|高|动态|指数|辆|克|千|转|（|袋|股|行|[A-Za-z]|毛|元|万|型|处|人|、|”|左右|是|等|分|件|字|米|号|位|届|名|后|次|欧|℃|斤|公里|点|场|英里|位|周|架|座|省|度|M|成|寸|秒|P|k|像素|分钟|K|G|小时|公斤|项|户|吨|大|百万|金|种|份|岁|年|款|只|千万|亿|倍|余|多|天|以上|左右元|块|支|美元|家|个|亩|平米|平方米|平方千米|基点|关口)')
        NN=reg6.sub('',O)
        c=re.findall('(超过|超|近|名|或|比|现|高|及|入|逾|值|强|数|到|的|看|涨|自|是|至|以||上|冲|从|探|点|报|达|大|在|约|共计|为|[A-Za-z]|于|总计|分|出|了|前|第|合计|达到|增加|增长|上升|下降|跌破|击穿|产值|持股)([0-9.]+)',NN)
        c = set(c)
        c = [x for x in c]
        #print("\n\n其他数据(根据数字前词语)\n",c)
        #print("数量", len(c))
        reg7=re.compile('(超过|超|近|值|及|数|报|到|的|高|逾|现|入|看|是|自|名|冲|涨|或|比|点|探|至|以|大|在|上|从|达|约|共计|为|[A-Za-z]|于|总计|分|出|了|前|第|合计|达到|增加|增长|上升|下降|跌破|击穿|产值|持股)([0-9.]+)')
        NNN=reg7.sub('',NN)
        ERROR=re.findall('(.{2}[0-9.]+.{2})',NNN)
        #print('\n\n遗漏\n',ERROR)
        self.result_data_Text.insert(1.0,ERROR)
        ind_num=len(a)+len(b)+len(c)
        #print(ind_num)
        self.result_data_Text.delete(1.0,END)
        self.result_data_Text.insert(1.0,ERROR)
        self.result_data_Text.insert(1.0,"lost:  \n")
        self.result_data_Text.insert(1.0,"\n")
        self.result_data_Text.insert(1.0,ind_num)
        self.result_data_Text.insert(1.0,'num:    \n')
        self.write_log_to_Text("INFO:count success")

    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)


def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()