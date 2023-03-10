class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class DoubledList:
    def __init__(self, max_length=None, force_type=None):
        self.head = None
        self.tail = None
        self.length = 0
        self.max_length = max_length
        self.force_type = force_type

    def append(self, value):
        #Adicionar um elemento no final da lista
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        if self.max_length is not None and self.length > self.max_length:
            self.remove(0)

    def insert(self, index, value):
        # Adicionar um elemento em uma index na lista
        # Se for no final, usar o append
        if index >= self.length:
            self.append(value)
        else:
            new_node = Node(value)
            current_node = self.head
            for i in range(index):
                current_node = current_node.next

            if current_node.prev is not None:
                current_node.prev.next = new_node
                new_node.prev = current_node.prev
            else:
                self.head = new_node

            new_node.next = current_node
            current_node.prev = new_node

            self.length += 1
            if self.max_length is not None and self.length > self.max_length:
                self.remove(0)

    def update_value(self, index, value):
        # Adicionar um elemento em uma posição na lista
        current_node = self.head
        for i in range(index):
            current_node = current_node.next

        # Atualiza o valor do nó
        current_node.value = value

    def get_index(self, value):
        # retornar o index (posição) do primeiro elemento
        # que encontrar na lista
        # caso não encontre, retornar um raise ValueError()
        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.value == value:
                return index
            current_node = current_node.next
            index += 1

        # Se não encontrou o valor, lança um ValueError
        raise ValueError("Valor não encontrado na lista")

    def clear(self):
        # Remove todas as referências aos nós da lista
        self.head = None
        self.tail = None
        self.length = 0

    def remove(self, index):

        if index >= self.length:
            raise IndexError("Índice fora do intervalo")
        if index == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
        elif index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current_node = self.head
            for i in range(index):
                current_node = current_node.next
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
        self.length -= 1

    def extend(self, other_list):
        if not isinstance(other_list, DoubledList):
            raise TypeError("Outra lista deve ser uma instância DoubledList")
        for value in other_list:
            self.append(value)

    def get_item(self, index):
        if index >= self.length:
            raise IndexError("Índice fora do intervalo")
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node

    def get_length(self) -> int:
        return self.length

    def __str__(self):
        #retornar uma string com todos os elementos da lista
        values = []
        current_node = self.head
        while current_node is not None:
            values.append(str(current_node.value))
            current_node = current_node.next
        return '[' + ', '.join(values) + ']'

    def print_reverse(self):
        values = []
        current_node = self.tail
        while current_node is not None:
            values.append(str(current_node.value))
            current_node = current_node.prev
        return '[' + ', '.join(values) + ']'


    def __len__(self):
        return self.get_length()


    def __getitem__(self, index):
        return self.get_item(index).value


    def __setitem__(self, index, value):
        self.update_value(index, value)



