# https://gemini.google.com

import sys

# Словарь для кодирования операций
OPERATIONS = {
    '+': -1, '-': -2, '*': -3, '/': -4, '%': -5, '^': -6
}

class Node:
    def __init__(self, value):
        self.value = value  # Число (0-9) или код операции (-1..-6)
        self.left = None
        self.right = None

def build_tree(tokens):
    """Строит дерево из списка токенов префиксного выражения."""
    if not tokens:
        return None
    
    token = tokens.pop(0)
    
    if token in OPERATIONS:
        node = Node(OPERATIONS[token])
        node.left = build_tree(tokens)
        node.right = build_tree(tokens)
        return node
    else:
        # Это число (операнд)
        return Node(int(token))

def evaluate(node):
    """Вычисляет значение поддерева."""
    if node.left is None and node.right is None:
        return node.value
    
    left_val = evaluate(node.left)
    right_val = evaluate(node.right)
    
    op = node.value
    if op == -1: return left_val + right_val
    if op == -2: return left_val - right_val
    if op == -3: return left_val * right_val
    if op == -4: return left_val // right_val if right_val != 0 else 0
    if op == -5: return left_val % right_val if right_val != 0 else 0
    if op == -6: return left_val ** right_val
    return 0

def simplify_tree(node):
    """
    Преобразует дерево: если результат вычислений левого или правого
    поддерева равен 0, заменяет поддерево его вычисленным значением.
    """
    if node is None or (node.left is None and node.right is None):
        return node

    # Рекурсивно обрабатываем детей
    node.left = simplify_tree(node.left)
    node.right = simplify_tree(node.right)

    # Проверяем левое поддерево
    if node.left and (node.left.left or node.left.right): # Если это не лист
        if evaluate(node.left) == 0:
            node.left = Node(0)

    # Проверяем правое поддерево
    if node.right and (node.right.left or node.right.right): # Если это не лист
        if evaluate(node.right) == 0:
            node.right = Node(0)

    return node

def print_tree(node, level=0):
    """Вспомогательная функция для визуализации дерева."""
    if node:
        print_tree(node.right, level + 1)
        print('    ' * level + str(node.value))
        print_tree(node.left, level + 1)

def main():
    filename = "input.txt" # Укажите имя вашего файла
    try:
        with open(filename, 'r') as f:
            expression = f.read().split()
    except FileNotFoundError:
        print("Файл не найден")
        return

    # 1. Построение дерева
    root = build_tree(expression)
    
    # 2. Преобразование дерева согласно условию
    root = simplify_tree(root)

    # 3. Вывод указателя (в Python это ссылка на объект)
    print(f"Указатель на корень: {id(root)}")
    print("Структура дерева (повернута на 90 градусов):")
    print_tree(root)

if __name__ == "__main__":
    main()