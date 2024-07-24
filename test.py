import torch
from torch.functional import F

x = torch.randn([1, 3, 28, 28])
w = torch.randn([16, 3, 5, 5])
b = torch.randn([16])

tensor = F.conv2d(x, w, b, stride=1, padding=1)
print(tensor.shape)

tensor = F.conv2d(x, w, b, stride=2, padding=1)
print(tensor.shape)

tensor = F.conv2d(x, w, b, stride=3, padding=1)
print(tensor.shape)

tensor = F.conv2d(x, w, b, stride=4, padding=1)
print(tensor.shape)

tensor = F.conv2d(x, w, b, stride=5, padding=1)
print(tensor.shape)

tensor = F.conv2d(x, w, b, stride=3, padding=2)
print(tensor.shape)

tensor = F.conv2d(x, w, b, stride=3, padding=3)
print(tensor.shape)




