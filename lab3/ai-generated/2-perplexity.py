# https://www.perplexity.ai

# CalcTree8

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value   # int: 0–9 для листа, -1..-6 для операций
        self.left = left     # Node | None
        self.right = right   # Node | None

    def __repr__(self):
        return f"Node({self.value})"


# соответствие символ операции -> код
OP_CODE = {
    '+': -1,
    '-': -2,
    '*': -3,
    '/': -4,
    '%': -5,
    '^': -6,
}

def parse_prefix(tokens, pos=0):
    """
    Строит дерево по префиксной записи.
    tokens: список строк (операторы и числа)
    pos: текущая позиция
    Возвращает (поддерево, новая_позиция).
    """
    t = tokens[pos]

    if t in OP_CODE:
        code = OP_CODE[t]
        left, pos1 = parse_prefix(tokens, pos + 1)
        right, pos2 = parse_prefix(tokens, pos1)
        return Node(code, left, right), pos2
    else:
        # операнд (0..9)
        return Node(int(t)), pos + 1


def eval_node(node):
    """
    Вычисляет значение поддерева node (int).
    Предполагается, что node описывает корректное выражение.
    """
    if node.left is None and node.right is None:
        return node.value

    a = eval_node(node.left)
    b = eval_node(node.right)

    if node.value == -1:   # +
        return a + b
    elif node.value == -2: # -
        return a - b
    elif node.value == -3: # *
        return a * b
    elif node.value == -4: # /
        # нацело, предположим, деления на 0 нет во входе
        return a // b
    elif node.value == -5: # %
        return a % b
    elif node.value == -6: # ^
        return a ** b
    else:
        raise ValueError("Unknown operator code")


def transform(node):
    """
    Преобразует дерево: для любого поддерева, у которого
    значение левого или правого поддерева равно 0, заменить
    это поддерево на лист (его числовое значение).
    Возвращает пару (новый_корень, значение_поддерева).
    """
    if node is None:
        return None, 0

    # лист
    if node.left is None and node.right is None:
        return node, node.value

    # рекурсивно работаем с детьми
    left_node, left_val = transform(node.left)
    right_node, right_val = transform(node.right)

    node.left = left_node
    node.right = right_node

    # если значение левого или правого поддерева равно 0 –
    # сворачиваем ТЕКУЩЕЕ поддерево в лист с его значением
    if left_val == 0 or right_val == 0:
        val = eval_node(node)
        return Node(val), val

    # иначе ничего не сворачиваем, просто возвращаем значение
    val = eval_node(node)
    return node, val


def main():
    # читаем одну строку с выражением в префиксной форме
    with open('filename', 'r', encoding='utf-8') as f:
        line = f.read().strip()

    # допустим, токены разделены пробелами;
    # если нет — можно просто пройти по символам
    tokens = line.split()
    if len(tokens) == 1:  # например "+2 3" отсутствует, а есть "+23"
        # тогда разбиваем по символам
        tokens = list(line.strip())

    root, _ = parse_prefix(tokens)

    # преобразуем дерево
    new_root, _ = transform(root)

    # "Выведите указатель на корень" — в Python это просто объект new_root.
    # Если нужно что-то вывести в файл, можно, например, вывести id(new_root)
    # или сериализованное дерево. Здесь выведем id().
    with open('out.txt', 'w', encoding='utf-8') as fout:
        fout.write(str(id(new_root)) + '\n')


if __name__ == '__main__':
    main()