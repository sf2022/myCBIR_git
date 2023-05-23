import random
import cv2
import pandas as pd
import os
import config
import shutil
import utils

DB_csv = config.DB_csv
clsCnt_csv = config.clsCnt_csv

class Database:
    def __init__(self, imgSetPath):
        self.imgSetPath = imgSetPath

    def img_lib_init(self):
        # 图像库的初始化
        # 将图片重命名同时生成data.csv文件
        self.create_imgSet()
        # 将图片统一大小为(256, 256)
        # self.img_resize()
        # 计算每个类下图片的数目
        self.cls_count()

    def create_imgSet(self):
        # 本循环有两个操作，一个是将图片的路径和类写入csv，一个是将文件名称改为:“类_原名称”的形式
        # 设置随机数种子
        random.seed(123)

        # 数据集根目录
        dataset_root = self.imgSetPath
        # dst_root = r"K:\myCBIR_v2\dataset_v2"
        dst_root = config.dst_imgSetPath

        # 遍历每个类别
        with open(DB_csv, 'w', encoding='UTF-8') as f:
            f.write("imgPath,imgClass")
            for cls_name in os.listdir(dataset_root):
                if not os.path.isdir(os.path.join(dataset_root, cls_name)):
                    continue
                # 创建类别的训练集、验证集和测试集目录
                dst_cls_dir = os.path.join(dst_root, cls_name)
                if not os.path.exists(dst_cls_dir):
                    os.makedirs(dst_cls_dir)

                # 获取类别下的所有图像文件名
                img_files = os.listdir(os.path.join(dataset_root, cls_name))
                # 拷贝图像文件到新目录
                for i, img_file in enumerate(img_files):
                    src_path = os.path.join(dataset_root, cls_name, img_file)
                    # if img_file[:-15] == cls_name:
                    #     new_name = img_file
                    # else:
                    #     new_name = cls_name + '_' + img_file
                    if i < 10:
                        str_i = "0" + i.__str__()
                    else:
                        str_i = i.__str__()
                    new_name = cls_name + '_image_00' + str_i + ".jpg"
                    dst_path = os.path.join(dst_cls_dir, new_name)
                    shutil.copy(src_path, dst_path)
                    dst_path = '/'.join(dst_path.split('\\'))
                    f.write("\n{},{}".format(dst_path, cls_name))
        f.close()

    def img_resize(self):
        for _, imgPath in enumerate(utils.get_imgSet_paths()):
            image = cv2.imread(imgPath)
            # 高斯模糊 添加后准确率降低！？？
            # image = cv2.GaussianBlur(image, (3, 3), 0.8)
            # 改变图像大小为
            resized_image = cv2.resize(image, (256, 256))
            # 替换原图像
            cv2.imwrite(imgPath, resized_image)

    def cls_count(self):
        """
        计算图像库每个类下对应的图片数，写入cls_count.csv文件
        :return:
        """
        cls_list = self.get_data()['imgClass'].tolist()
        with open(clsCnt_csv, 'w', encoding='UTF-8') as file:
            for cls in self.get_class():
                cnt = cls_list.count(cls)
                file.write("{},{}\n".format(cls, cnt))
        file.close()

    def get_class(self):
        """
        获得图像库的类
        :return: 类 set
        """
        classes = set(self.get_data()["imgClass"])
        return classes

    def get_data(self):
        """
        图像库的数据
        :return: 所有图像的路径和类，daraFrame
        """
        data = pd.read_csv(DB_csv)
        return data


if __name__ == "__main__":
    # datasetPath = r'K:\myCBIR_v2\dataset_test'
    # data_augmented(datasetPath)
    datasetPath = r'K:\myCBIR_git\dataset_57'
    db = Database(datasetPath)
    db.img_lib_init()
    # imgPath = r"K:/myCBIR_v2/dataset_test/val/archive/archive_image_0036.jpg"
    # image = cv2.imread(imgPath)
    # resized_image = cv2.resize(image, (256, 256))
    print('hhh')
    # db.gen_testInfo_file()
