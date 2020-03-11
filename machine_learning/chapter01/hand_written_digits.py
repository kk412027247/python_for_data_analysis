import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import mnist
import os



# raise EOFError("Compressed file ended before the "
# import tempfile
# print(tempfile.gettempdir())
# Then go to that directory and delete train-images-idx3-ubyte.gz.
#  rm /tmp/train-images-*

proxy = 'http://127.0.0.1:8123'
os.environ['http_proxy'] = proxy
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy

np.random.seed(42)

X_train, y_train = mnist.train_images(), mnist.train_labels()
X_test, y_test = mnist.test_images(), mnist.test_labels()
num_classes = 10  # classes are the digits from 0 to 9

#
# X_train, X_test = X_train.reshape(-1, 28 * 28), X_test.reshape(-1, 28 * 28)
#
# y_train = np.eye(num_classes)[y_train]

img_idx = np.random.randint(0, X_test.shape[0])
plt.imshow(X_test[img_idx], cmap=matplotlib.cm.binary)
plt.axis("off")
plt.show()

print(y_test[img_idx])

X_train, X_test = X_train.reshape(-1, 28 * 28), X_test.reshape(-1, 28 * 28)

print('Pixel value between {} and {}'.format(X_train.min(), X_train.max()))

X_train, X_test = X_train / 255., X_test / 255
print('Normalized pixel value between {} and {}'.format(X_train.min(), X_train.max()))

y_train = np.eye(num_classes)[y_train]
print(y_train)
