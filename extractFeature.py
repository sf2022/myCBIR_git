import numpy as np
import config
import utils
from DenseNet import DenseNet


def extract_deep_feat(trainData, method):
    featFilePath = config.featurePath
    print("准备提取{}特征......".format(method))

    model = DenseNet()

    all_features = []
    i = 0
    for data in trainData.itertuples():
        imgPath = getattr(data, "imgPath")
        feature = model.cal_feature(imgPath)  # [512]
        if len(all_features) == 0:
            all_features = feature
        else:
            all_features = np.vstack((all_features, feature))
        i += 1
        print(i)
    np.save(featFilePath, all_features)
    print("{}特征提取完毕".format(method))


if __name__ == '__main__':
    # extract_feature(["SIFT"])
    img_data = utils.get_imgSet_data()
    extract_deep_feat(img_data, "DenseNet")
    # extract_sift_feat_v2(img_data)
    print("hello")
