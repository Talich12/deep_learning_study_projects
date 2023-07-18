class Neuron:

    def __init__(self, w, f = lambda x: x):
        self._w = w
        self._f = f
        self._last_forward = None

    def forward(self, x):
        sum = x[0] * self._w[0]
        for i in range (1, len(x)):
            sum += x[i] * self._w[i]
        
        self._last_forward = x
        return self._f(sum)

    def backlog(self):
        if self._last_forward == None:
            return None

        return self._last_forward