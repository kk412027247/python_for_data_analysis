import numpy as np


class FullyConnectLayer(object):
    def __init__(self, num_inputs, layer_size, activation_function, derivated_activation_function=None):
        super().__init__()
        self.W = np.random.standard_normal((num_inputs, layer_size))
        self.b = np.random.standard_normal(layer_size)
        self.size = layer_size

        self.activation_function = activation_function
        self.derivated_activation_function = derivated_activation_function
        self.x, self.y = None, None

    def forward(self, x):
        z = np.dot(x, self.W) + self.b
        self.y = self.activation_function(z)
        self.x = x
        return self.y

    def backward(self, dL_dy):
        dy_dz = self.derivated_activation_function(self.y)
        dL_dz = (dL_dy * dy_dz)
        dz_dw = self.x.T
        dz_dx = self.W.T
        dz_db = np.ones(dL_dy.shape[0])
        self.dL_dW = np.dot(dz_dw, dL_dz)
        self.dL_db = np.dot(dz_db, dL_dz)

        dL_dx = np.dot(dL_dz, dz_dx)
        return dL_dx

    def optimize(self, epsilon):
        self.W -= epsilon * self.dL_dW
        self.b -= epsilon * self.dL_db


np.random.seed(42)

x1 = np.random.uniform(-1, 1, 2).reshape(1, 2)
x2 = np.random.uniform(-1, 1, 2).reshape(1, 2)

relu_function = lambda y: np.maximum(y, 0)

layer = FullyConnectLayer(num_inputs=2, layer_size=3,
                          activation_function=relu_function, derivated_activation_function=None)

out1 = layer.forward(x1)
out2 = layer.forward(x2)

x12 = np.concatenate((x1, x2))
out12 = layer.forward(x12)

print(out12)
