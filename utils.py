import csv
import os
import pandas as pd
import config


def get_imgSet_paths():
    """
    所有图像的路径
    :return:  list
    """
    data = pd.read_csv(config.DB_csv)
    return list(data["imgPath"])


def get_imgSet_data():
    """
    图像库的数据
    :return: 所有图像的路径和类，daraFrame
    """
    try:
        if os.path.exists(config.DB_csv):
            data = pd.read_csv(config.DB_csv)
            return data
    except OSError as e:
        pass


def get_imgSet_imgCls():
    """
    图像库的类
    :return:  set
    """
    data = pd.read_csv(config.DB_csv)
    return set(data["imgClass"])


def get_imgSet_clsCnt(imgClass):
    """
    查询图像库中属于imgClass的图片数
    :param imgClass:
    :return: int
    """
    clsCnt_csv = config.clsCnt_csv
    clsCnt = 0
    with open(clsCnt_csv) as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == imgClass:
                clsCnt = int(row[1])
                break
    file.close()
    return clsCnt


def get_imgCls_from_imgPath(imgPath):
    """
    从图片名中可以得知图片所属的类
    :param imgPath:
    :return: str
    """
    #  K:/myCBIR/dataset_test/101_ObjectCategories/accordion/accordion_image_0001.jpg
    imgName = imgPath.split('/')[-1]
    imgClass = imgName[:-15]
    return imgClass









