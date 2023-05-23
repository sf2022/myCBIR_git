import os
curDir = os.path.dirname(os.path.abspath(__file__))
featurePath = os.path.join(curDir, 'DenseNet_fine_tuned.npy')

# 图像库的路径
dst_imgSetPath = os.path.join(curDir, 'dataset_test')

# 图像库所有图像的路径和类
DB_csv = os.path.join(curDir, 'imgLibInfo/data.csv')

# 图像库的类和类下图片的个数
clsCnt_csv = os.path.join(curDir, 'imgLibInfo/cls_count.csv')

imgLibInfoFiles = [DB_csv, clsCnt_csv]

imgLibFiles_usage = {DB_csv: "保存所有图像的路径和类",
                     clsCnt_csv: "保存图像库的类和类下图像的个数"
                     }

DenseNet_fine_tuned_weight_path = os.path.join(curDir, 'dense121_fine_tuned.h5')

if __name__ == "__main__":
    print(os.getcwd())
    print('hello')
