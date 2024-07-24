import torch
import csv
from torch.utils.data import Dataset
from utils import ypath

DATA_FOLDER = r'D:\Repo_svn\90_Work\01_CCSPHM\06_Dataset.csv'


class CSVDataSet(Dataset):
    def __init__(self, folder_path):
        self.folder = folder_path
        self.files = ypath.files(self.folder, ".*\.csv", rescursion=True)

    def __len__(self):
        return len(self.files)

    def __getitem__(self, idx):
        with open(self.files[idx], 'r') as file:
            reader = csv.reader(file)
            next(reader)
            x = [float(i[0]) for i in reader]
            y = [1 if self.files[idx].__contains__('Fault') else 0]
            return torch.tensor(x), torch.tensor(y)


# print(ypath.files(DATA_FOLDER, ".*\.csv", rescursion=True))

# dataset = CSVDataSet(DATA_FOLDER)
#
# print(dataset.__len__())
#
# x, y = dataset.__getitem__(0)
#
# print(x)
# print(y)
