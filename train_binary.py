from torch.utils.data import DataLoader
from torchvision.transforms import transforms
from datatest import CSVDataSet

# 数据预处理
data_transforms = transforms.Compose([
    transforms.ToTensor(),
    # 添加其他的变换操作
])

DATA_FOLDER = r'D:\Repo_svn\90_Work\01_CCSPHM\06_Dataset.csv'

# 加载数据集
dataset = CSVDataSet(DATA_FOLDER)

# 创建数据加载器
batch_size = 32
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# 遍历每一批数据
for inputs, labels in dataloader:
    # 在这里进行训练或推断操作
    # inputs和labels是分批加载的特征和标签
    print(inputs)
    print(labels)