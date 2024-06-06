class Queue:
    def _init_(self):
        self.queue = []
        self.tipo_data = None

    def enqueue(self, valor):
        if self.tipo_data is None:
            self.tipo_data = type(valor)
        elif not isinstance(valor, self.tipo_data):
            raise TypeError(f"Todos os elementos tem de ser do tipo: {self.tipo_data._name_}")
        self.queue.append(valor)

    def dequeue(self):
        if not self.queue:
            raise IndexError("dequeue de um queue vazio")
        return self.queue.pop(0)

class Stack:
    def _init_(self):
        self.stack = []
        self.tipo_data = None

    def push(self, valor):
        if self.tipo_data is None:
            self.tipo_data = type(valor)
        elif not isinstance(valor, self.tipo_data):
            raise TypeError(f"Todos os elementos tem de ser do tipo: {self.tipo_data._name_}")
        self.stack.append(valor)

    def pop(self):
        if not self.stack:
            raise IndexError("pop from empty stack")
        return self.stack.pop()
