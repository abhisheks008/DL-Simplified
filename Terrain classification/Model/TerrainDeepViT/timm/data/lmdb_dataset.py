"""Modified from https://github.com/Lyken17/Efficient-PyTorch/blob/master/tools/folder2lmdb.py

Usage:
    To generate lmdb dataset from raw dataset, run
    `python utils/lmdb_dataset.py --src_dir ${src_dir} --dst_dir ${dst_dir}`
"""

import os
import six
from PIL import Image

import lmdb
from tqdm import tqdm

import torch
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder

# Must import after torch, may due to C++ ABI issue
import pyarrow as pa


class ImageFolderLMDB(Dataset):
    """Lmdb dataset."""

    def __init__(self, db_path, transform=None, target_transform=None):
        self.db_path = db_path
        self.env = lmdb.open(db_path,
                             subdir=os.path.isdir(db_path),
                             readonly=True,
                             lock=False,
                             readahead=False,
                             meminit=False)
        with self.env.begin(write=False) as txn:
            self.length = pa.deserialize(txn.get(b'__len__'))
            self.keys = pa.deserialize(txn.get(b'__keys__'))
        # align with run manager syntax
        self.samples = zip(([0]*self.length,self.keys))
        self.transform = transform
        self.target_transform = target_transform

    def __getitem__(self, index):
        img, target = None, None
        env = self.env
        with env.begin(write=False) as txn:
            # print('current val is ==================:',self.db_path)
            byteflow = txn.get(self.keys[index])
        unpacked = pa.deserialize(byteflow)
        # load image
        imgbuf = unpacked[0]
        buf = six.BytesIO()
        buf.write(imgbuf)
        buf.seek(0)
        img = Image.open(buf).convert('RGB')

        # load label
        target = unpacked[1]

        if self.transform is not None:
            img = self.transform(img)

        if self.target_transform is not None:
            target = self.target_transform(target)

        return img, target

    def __len__(self):
        return self.length

    def __repr__(self):
        return self.__class__.__name__ + ' (' + self.db_path + ')'


def raw_reader(path):
    """Read in binary format."""
    with open(path, 'rb') as f:
        bin_data = f.read()
    return bin_data


def dumps_pyarrow(obj):
    """Serialize an object.

    Returns:
        Implementation-dependent bytes-like object
    """
    return pa.serialize(obj).to_buffer()


def folder2lmdb(src_dir, dst_dir, name="train", write_frequency=5000):
    """Convert torchvision's `ImageFolder` to lmdb dataset."""
    directory = os.path.expanduser(os.path.join(src_dir, name))
    print("Loading dataset from %s" % directory)
    dataset = ImageFolder(directory, loader=raw_reader)
    data_loader = DataLoader(dataset, num_workers=16, collate_fn=lambda x: x)

    lmdb_path = os.path.join(dst_dir, name)
    os.makedirs(lmdb_path)
    isdir = os.path.isdir(lmdb_path)

    print("Generate LMDB to %s" % lmdb_path)
    db = lmdb.open(lmdb_path,
                   subdir=isdir,
                   map_size=1099511627776 * 2,
                   readonly=False,
                   meminit=False,
                   map_async=True)

    txn = db.begin(write=True)
    for idx, data in enumerate(tqdm(data_loader)):
        image, label = data[0]
        txn.put(u'{}'.format(idx).encode('ascii'), dumps_pyarrow(
            (image, label)))
        if idx % write_frequency == 0:
            txn.commit()
            txn = db.begin(write=True)

    # finish iterating through dataset
    txn.commit()
    keys = [u'{}'.format(k).encode('ascii') for k in range(idx + 1)]
    with db.begin(write=True) as txn:
        txn.put(b'__keys__', dumps_pyarrow(keys))
        txn.put(b'__len__', dumps_pyarrow(len(keys)))

    print("Flushing database ...")
    db.sync()
    db.close()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--src_dir', help='ILSVRC dataset dir')
    parser.add_argument('--dst_dir', help='dst dir')
    args = parser.parse_args()

    for name in ['val', 'train']:
        folder2lmdb(args.src_dir, args.dst_dir, name=name)

        dataset = ImageFolderLMDB(os.path.join(args.dst_dir, name))
        img, label = dataset[len(dataset) - 1]
        print('Test {} with len {}'.format(name, len(dataset)))
        print(img.size, label)
