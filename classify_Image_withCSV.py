#引入相关库
import os
import pandas as pd
import shutil #用于移动文件
# 输入图片路径
directory_name="C:\\Users\\fan\\Desktop\\archive\\Images\\"
# 输出图片路径
pathWrite = "C:\\Users\\fan\\Desktop\\archive\\train\\"

#输入表格所在路径+名称并读取，如D:/data/label.csv,文件后缀不要忘记
csv_path = "C:\\Users\\fan\\Desktop\\archive\\Train.csv"
list=pd.read_csv(csv_path)

# 创建文件夹
for i in range(1,8):  # "1,8"指的是1-7总共7个类别
    if not os.path.exists(pathWrite + str(i)):  # 最后一个 / 不要漏
        os.mkdir(pathWrite + str(i))

# 分类
for i in range(1,8):
    listnew = list[list["labels"] == i]
    l = listnew["images"].tolist()  # 对应csv文件图片那一栏的标题

    for each in l:
        shutil.move(directory_name + each +'.jpeg', pathWrite + str(i)+"\\")
