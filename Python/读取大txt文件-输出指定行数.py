# 程序用于读取大txt文件, 读取指定行数,
# 程序会跳过空行
# Python2.7下运行正常, 3.x版本的没有测试.





# 这2个是设置项, 请根据自己的需要修改

filename = "large-file.txt"
# 要读取的txt文件名

num = 3
# 要读取的行数



















# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 
# 下面的是代码, 无需修改.


import sys



# ==== 获得文件一共有多少航 ==== 

how_many_line = 0
# 待会用来存放这个文件一共有多少行(空行也算数)

with open(filename) as lines:
    for l in lines:
        how_many_line = how_many_line + 1

# ==============================





# ==== 判断用户想要的行数 是否超出 文件的实际行数 ==== 

if num > how_many_line:
    output_string = '文件一共 {0} 行, 你想输出 {1} 行, 臣妾做不到啊'.format(str(how_many_line), str(num))
    print (output_string)
    sys.exit()

# ==============================








print ('文件一共有 ' + str(how_many_line) + ' 行')
print ('你想输出的是 ' + str(num) + ' 行')
print ('---- 后面的是文件内容 ----')








f = open(filename, "r")
# 打开文件



try:
    while True:
        if num == 0: 
            break   # 如果读取了指定的行数就退出
        line = f.readline() # 否则的话就读取一行
        sys.stdout.write(line)
        num = num - 1
except e:
    print('读取出错' + str(e))



f.close()
# 关闭文件











