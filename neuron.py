import numpy as np


class Neuron(object):
    def __init__(self, num_inputs, activation_fn):
        super().__init__()
        self.W = np.random.rand(num_inputs)
        self.b = np.random.rand(1)
        self.activation_fn = activation_fn

    def forward(self, x):
        z = np.dot(x, self.W) + self.b
        return self.activation_fn(z)


np.random.seed(42)

x = np.random.rand(3).reshape(1, 3)

print(x)

step_fn = lambda y: 0 if y < 0 else 1

print(x.size)

perceptron = Neuron(num_inputs=x.size, activation_fn=step_fn)

out = perceptron.forward(x)

print(out)
