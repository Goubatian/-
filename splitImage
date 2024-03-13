import os
from PIL import Image
# 输入读取文件的地址：
pathRead="D:\\AADeveloper\\PCworkspace\\ultralytics-main\\ultralytics-main\\datasets\\wheatperiod\\train\\yuedong"
# 保存图片的地址
pathWrite="D:\\AADeveloper\\PCworkspace\\ultralytics-main\\ultralytics-main\\datasets\\wheatperiod\\train\\yuedong\\"
# 请问要分割为多少列多少行？比如三列三行为九宫格
x = 3 # 列
y = 3 # 行
# 读取函数，用来读取文件夹中的所有函数，输入参数是文件名
def read_directory(directory_name):
    for filename in os.listdir(directory_name):
        print("正在处理" + filename)
        image = Image.open(directory_name + "/" + filename)
        # (640,640)是要输出的图片格式
        image.resize((640,640)).save(pathWrite+filename)
        # pieces = split_image(image)
        #
        # for i, piece in enumerate(pieces):
        #      piece.resize((640, 640)).save(pathWrite + filename+str(i) + ".jpg")
            # piece.save("C:\\Users\\fan\\Desktop\\wheatperiod\\train\\bajie")
            # piece.show(title=f"Piece {i + 1}")


def split_image(image):
    width, height = image.size
    piece_width = width // x
    piece_height = height // y
    pieces = []

    for i in range(x):
        for j in range(y):
            left = j * piece_width
            top = i * piece_height
            right = left + piece_width
            bottom = top + piece_height

            piece = image.crop((left, top, right, bottom))
            pieces.append(piece)

    return pieces

def main():
    read_directory(pathRead)

if __name__ == "__main__":
    main()
