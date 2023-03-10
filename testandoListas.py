from Lista_dupla import DoubledList

# Criando uma lista com de 5 elementos
my_list = DoubledList(max_length=5)

# Adicionando elementos na lista
my_list.append(1)
my_list.append(2)
my_list.append(3)

# Imprimindo a lista
print(my_list)

# Adicionando um elemento em uma posição específica
my_list.insert(1, 4)

# Imprimindo a lista novamente
print(my_list)

# Atualizando o valor de um elemento
my_list.update_value(2, 5)

# Imprimindo a lista novamente
print(my_list)

# Encontrando o índice de um valor
print(my_list.get_index(4))

# Removendo um elemento
my_list.remove(1)

# Imprimindo a lista novamente
print(my_list)

# Imprimindo a lista de trás para frente
print(my_list.print_reverse())

# Adicionando uma lista a outra
other_list = DoubledList()
other_list.append(6)
other_list.append(7)
my_list.extend(other_list)

# Imprimindo a lista novamente
print(my_list)

# Acessando um elemento da lista pelo índice
print(my_list[2])

# Atribuindo um valor a um elemento da lista pelo índice
my_list[3] = 8

# Imprimindo a lista novamente
print(my_list)

# pegando o comprimento da lista
print(len(my_list))