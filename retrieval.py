import numpy as np
import config
import utils
from DenseNet import DenseNet


def get_similar_images_deep(curFeature, featurePath, limit):
    # 加载聚合特征文件
    sum_matrix = np.load(featurePath)
    # 计算欧式距离
    variance_distance = (((sum_matrix - curFeature) ** 2).sum(1)) ** 0.5
    # 排序
    distanceIdx = list(np.argsort(variance_distance))[:limit]
    # 将排序后的距离映射到类名+图片名上
    imgSetPaths = utils.get_imgSet_paths()
    resultData = []
    for i, distance_id in enumerate(distanceIdx):
        imgClass = utils.get_imgCls_from_imgPath(imgSetPaths[distance_id])
        resultData.append({
            "imgPath": imgSetPaths[distance_id],
            "imgClass": imgClass
        })
    return resultData


def image_retrieval(imgPath, limit=10):
    model = DenseNet()
    curFeature = model.cal_feature(imgPath)
    featurePath = config.featurePath
    resultData = get_similar_images_deep(curFeature, featurePath, limit)

    return resultData


if __name__ == '__main__':
    featMethod = ["SIFT"]
    print("hello")

