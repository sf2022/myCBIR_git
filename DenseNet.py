import cv2
import numpy as np
from keras.applications.densenet import DenseNet121, preprocess_input
from numpy import linalg as la
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
import config
import utils


class DenseNet:
    def __init__(self):
        self.input_shape = (224, 224, 3)
        self.pooling = 'avg'  # 池化
        num_classes = len(utils.get_imgSet_imgCls())

        base_model = DenseNet121(weights=None,
                                 input_shape=(self.input_shape[0], self.input_shape[1], self.input_shape[2]),
                                 include_top=False)
        x = base_model.output
        x = GlobalAveragePooling2D()(x)
        x = Dense(512, activation='relu')(x)
        predictions = Dense(num_classes, activation='softmax')(x)
        self.model = Model(inputs=base_model.input, outputs=predictions)
        self.model.load_weights(config.DenseNet_fine_tuned_weight_path)

    def cal_feature(self, img_path):
        # img_path可能是路经，可也能是cv2读入的ndarray
        if isinstance(img_path, np.ndarray):
            img = img_path.copy()
        else:
            img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (self.input_shape[0], self.input_shape[1]))

        img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)
        feat = self.model.predict(img)
        norm_feat = feat[0] / la.norm(feat[0])
        return norm_feat.reshape(1, -1)


if __name__ == '__main__':
    # DenseNet_fine_tuned()
    model = DenseNet()
    imgPath = r"K:\myCBIR_v2\dataset_test_v2\train\barrel\barrel_image_0004.jpg"
    image = cv2.imread(imgPath)
    feature = model.cal_feature(image)
    print(feature)
    # feature = model.cal_feature(imgPath)
    # print(feature)
    # print(len(feature))
    # print("hello")
