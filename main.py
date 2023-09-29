import os
import time
import random
from generate_vector import Generate_vector_10000
from busca_binaria import Binary_search, bubble_sort, quicksort

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right

    def search(self, value):
        current = self.root
        while current:
            if value == current.value:

                print(f'The value {value} is present in the tree')
                return 1
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        print(f'The value {value} isnt present in the tree')
        return 0

    def list(self):
        result = []
        stack = []
        current = self.root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.value)
            current = current.right
        return result

    def find_leaf (self):

        result = []
        stack = []
        count = ''
        delivery = int(0)
        current = self.root
        while current or stack:
            while current:
                stack.append(current)
                #print(stack , '<<<')
                current = current.left
            current = stack.pop()

            if current.right == None and current.left == None and current.value != None:

                delivery += 1
                count = count + f'{current.value} '


            result.append(current.value)
            current = current.right

        return f'there is {delivery} leaf nodes, these nodes have the values {count}'

    def find_highest_and_lowest (self):

        def find_highest (self):

            result = []
            stack = []
            current = self.root

            highest = 0

            while current or stack:
                while current:
                    stack.append(current)
                    current = current.left
                current = stack.pop()
                result.append(current.value)

                if current.value > highest:

                    highest = current.value

                current = current.right

            return highest

        def find_lowest (self):

            result = []
            stack = []
            current = self.root

            lowest = int(34324)

            while current or stack:
                while current:
                    stack.append(current)
                    current = current.left
                current = stack.pop()
                result.append(current.value)

                if current.value < lowest:

                    lowest = current.value

                current = current.right

            return lowest

        highest = find_highest(self)
        lowest =  find_lowest(self)

        return f'the highest number is {highest}\nthe lowest number is {lowest}'

if __name__ == "__main__":

    values =  Generate_vector_10000()
    all = values
    binary_tree = BinaryTree(values[0])
    values.remove(values[0])

    while len(values) != 0:

        if len(values) > 0:

            for value in values:
                binary_tree.insert(value)

            values = []
            
    result = 0
    while result != 1:
        print('tentando')

        SEARCH_VALUE = random.randint(1, 100000)

        start_time = time.perf_counter()
        tree_search = binary_tree.search(SEARCH_VALUE)
        tree_time = time.perf_counter() - start_time
        
        #print(start_time, tree_time, start_time - tree_time)

        if tree_search == 0:
            print('tree_time >>>>>', tree_time)
            continue

        else:
            os.system('cls')
            print('calculando tempo...')
            start_time = time.perf_counter()
            aranged_vector = bubble_sort(all)
            bubble_fix = time.perf_counter() - start_time
            os.system('cls')
            print('calculando tempo.')
            #print('bubble_fix', bubble_fix)
            
            start_time = time.perf_counter()
            quick_aranged_vector = quicksort(all)
            quick_fix = time.perf_counter() - start_time
            
            os.system('cls')
            print('calculando tempo..')
            #print('quick_fix', quick_fix)
            
            start_time = time.perf_counter()
            binary_tree = Binary_search(aranged_vector, SEARCH_VALUE)
            binary_look_time = time.perf_counter() - start_time

            os.system('cls')
            print('calculando tempo...')
            #print('binary search: ', binary_look_time)

            
            start_time = time.perf_counter()

            result = 0
            count = 0

            for number in all:

               #print(number, type(number), type(SEARCH_VALUE), SEARCH_VALUE)

                if number == SEARCH_VALUE:

                    linear_time = time.perf_counter() - start_time
                    #print('acho :3')
                    break

                count += 1
                
            
        break
    os.system('cls')
    print(f'''
        <<<<<    Valor --- {SEARCH_VALUE} --- Valor     >>>>> 
        
{quick_fix} QuickSort sort para organizar o vetor
{bubble_fix} Bubble sort para organizar de o vetor    

{tree_time} Arvore
{binary_look_time} Busca Binaria
{linear_time} Busca Linear

Vetor e numero de busca gerado aleatoriamente.''')
