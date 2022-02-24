import argparse
import numpy as np
import torch
from dataset import myDataset
import torch.utils.data as data
import matplotlib.pyplot as plt
from torchvision import transforms


# device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

# # argument parser

# parser = argparse.ArgumentParser()
# #parser.add_argument("--n_samples", help="amount of samples to train with", type=int, default=1000)
# args = parser.parse_args()


# load datasets

# Constants
IMAGES_PAHT_LOW = 'data/bothDatasets/Low'
IMAGES_PAHT_HIGH = 'data/bothDatasets/High'
BATCH_SIZE = 64
TEST_SET_SIZE = 0.9
VAL_SET_SIZE = 0.05

transform = transforms.Compose([
    transforms.ToTensor()
])

my_dataset = myDataset(IMAGES_PAHT_LOW, IMAGES_PAHT_HIGH, transform)
print(my_dataset.len())

# Getting size of sets 
dataset_len = len(my_dataset)
num_train = int(np.floor(dataset_len * TEST_SET_SIZE))
num_val = int(np.floor(dataset_len * VAL_SET_SIZE))
num_test = dataset_len - num_train - num_val
print(f'Num of train images: {num_train}, num of val images: {num_val}, num of test images: {num_test}')

# Getting sets
train_set, val_set, test_set = data.random_split(my_dataset, [num_train, num_val, num_test])

# Getting DataLoaders
train_dataloader = data.DataLoader(train_set, batch_size = BATCH_SIZE, shuffle=True)
val_dataloader = data.DataLoader(val_set, batch_size = BATCH_SIZE, shuffle=True)
test_dataloader = data.DataLoader(test_set, batch_size = BATCH_SIZE, shuffle=True)


# # Display image and label.
train_LOW, train_HIGH = next(iter(train_dataloader))
print(f"train_LOW shape: {train_LOW.size()}")
print(f"train_HIGH shape: {train_HIGH.size()}")
imgHIGH = train_HIGH[0].squeeze()
imgLOW = train_LOW[0].squeeze()

imgLOW = transforms.ToPILImage(mode='RGB')(imgLOW)
imgHIGH = transforms.ToPILImage(mode='RGB')(imgHIGH)

imgLOW.show()
imgHIGH.show()


# train

