from typing import Any


class Node:

    def __init__(self, char: Any, frequency: int, esq=None, dir=None):
        self.char = char
        self.frequency = frequency
        self.esq = esq
        self.dir = dir

    def get_frequency(self):
        return self.frequency

    def nodes(self) -> tuple:
        return self.esq, self.dir

    def __repr__(self):
        return f"Node({self.char}, {self.frequency})"


class Huffman:

    def __init__(self, text):
        self.text = text

    def get_code_tree(self) -> dict:
        char_frequency = self.__get_char_frequency()
        root_node = self.__generate_tree(char_frequency=char_frequency)

        return self.__get_dict_of_huffman_codes(root_node)

    def __generate_tree(self, char_frequency: dict) -> Node:
        # ORDENAR LISTA EM NODES - EX: [Node('a', 54), Node('c', 50), Node('b', 5)]
        nodes = []
        for char, frequency in char_frequency.items():
            nodes.append(Node(char=char, frequency=frequency))

        nodes = sorted(nodes, key=Node.get_frequency)

        # Gera arvore
        while len(nodes) > 1:
            # Captura os dois ultimos
            node1 = nodes[0]
            node2 = nodes[1]

            nodes = nodes[2:]

            # Adicina o No, com a soma das frequencias
            node = Node(char=None,
                        frequency=(node1.frequency + node2.frequency),
                        esq=node1,
                        dir=node2)

            nodes.append(node)

            # Ordena a lista
            nodes = sorted(nodes, key=Node.get_frequency)

        return nodes[0]

    def __get_dict_of_huffman_codes(self, node: Node, binString='') -> dict:
        # Gera os codigos de huffmann - EX: {'a': '001', 'b': '100'}
        if node.char is not None:
            return {node.char: binString if len(binString) > 0 else '0'}

        node_esq, node_dir = node.nodes()

        codes = {}
        codes.update(self.__get_dict_of_huffman_codes(node_esq, binString + '0'))
        codes.update(self.__get_dict_of_huffman_codes(node_dir, binString + '1'))
        return codes

    def __get_char_frequency(self) -> dict:
        # CONTAGEM DE FREQUENCIA DE CADA CARACTER - return: {'a': 54, 'b': 5, 'c': 30}
        char_frequency = {}
        for char in self.text:
            if char_frequency.get(char):
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1

        return char_frequency


# Carregar arquivo
file = open('./files_tests/49999.in')
# text = file.readline()
file.close()
text = "aaaaaaaa"

huffman = Huffman(text)
huffman_code_tree = huffman.get_code_tree()


print(' Caracter | Código Huffman ')
print('---------------------------')
for char, huffman_code in huffman_code_tree.items():
    print(' %-6r |%15s' % (char, huffman_code))

#FORMAR BINARIO
binary = ''
for char in text:
    binary += huffman_code_tree[char]

print('==== Relátorio ====')
print('Tamanho original', len(text), "bytes")
print("Tamanho comprimido", len(binary)/8, "bytes")
