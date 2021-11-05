import urllib
import urllib.request
import tarfile
import os

url = 'https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz'
filename = 'cifar-10-python.tar.gz'
data_root = 'data'
filepath = os.path.join(data_root, filename)

if not os.path.isdir(data_root):
    os.makedirs(data_root, exist_ok=True)
    urllib.request.urlretrieve(url, filepath)
    with tarfile.open(filepath, "r:gz") as tar:
        tar.extractall(path=data_root)
    os.remove(filepath)  # delete tar.gz file after extraction