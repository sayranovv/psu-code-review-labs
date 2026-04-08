# https://claude.ai

"""
CalcTree8 — Дерево арифметического выражения в префиксной форме.

Задача:
  1. Прочитать префиксное выражение из файла.
  2. Построить дерево; операторы кодируются отрицательными числами:
       + → -1,  - → -2,  * → -3,  / → -4,  % → -5,  ^ → -6
  3. Оптимизировать дерево: если левое ИЛИ правое поддерево вычисляется
     в 0 — заменить всё поддерево листом со значением результата.
  4. Вывести дерево (корень и всё дерево).
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
import sys


# ──────────────────────────────────────────────
# Кодировка операторов
# ──────────────────────────────────────────────
OP_CODE = {'+': -1, '-': -2, '*': -3, '/': -4, '%': -5, '^': -6}
CODE_OP = {v: k for k, v in OP_CODE.items()}


# ──────────────────────────────────────────────
# Узел дерева
# ──────────────────────────────────────────────
@dataclass
class Node:
    value: int                      # >=0 — операнд; <0 — оператор
    left:  Optional['Node'] = field(default=None, repr=False)
    right: Optional['Node'] = field(default=None, repr=False)

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None

    def label(self) -> str:
        if self.value >= 0:
            return str(self.value)
        return CODE_OP[self.value]


# ──────────────────────────────────────────────
# Парсинг префиксного выражения
# ──────────────────────────────────────────────
def tokenize(expr: str) -> list[str]:
    """Разбивает строку на токены (поддерживает числа >9 и пробелы)."""
    return expr.split()


def parse(tokens: list[str], pos: list[int]) -> Node:
    """Рекурсивно строит дерево из списка токенов."""
    if pos[0] >= len(tokens):
        raise ValueError("Неожиданный конец выражения")

    tok = tokens[pos[0]]
    pos[0] += 1

    if tok in OP_CODE:
        node = Node(value=OP_CODE[tok])
        node.left  = parse(tokens, pos)
        node.right = parse(tokens, pos)
        return node
    else:
        return Node(value=int(tok))


def build_tree(filename: str) -> Node:
    with open(filename, 'r') as f:
        expr = f.read().strip()
    tokens = tokenize(expr)
    pos = [0]
    root = parse(tokens, pos)
    return root


# ──────────────────────────────────────────────
# Вычисление значения узла/поддерева
# ──────────────────────────────────────────────
def evaluate(node: Node) -> int:
    if node.is_leaf():
        return node.value

    l = evaluate(node.left)
    r = evaluate(node.right)
    op = node.value

    if op == -1: return l + r
    if op == -2: return l - r
    if op == -3: return l * r
    if op == -4:
        if r == 0:
            raise ZeroDivisionError(f"Деление на ноль в узле")
        return l // r
    if op == -5:
        if r == 0:
            raise ZeroDivisionError(f"Остаток от деления на ноль")
        return l % r
    if op == -6: return l ** r
    raise ValueError(f"Неизвестный оператор: {op}")


# ──────────────────────────────────────────────
# Оптимизация дерева
# ──────────────────────────────────────────────
def optimize(node: Node) -> Node:
    """
    Постординый обход.
    Если левое ИЛИ правое поддерево == 0, вычисляем всё поддерево
    и заменяем его листом.
    """
    if node.is_leaf():
        return node

    node.left  = optimize(node.left)
    node.right = optimize(node.right)

    l_val = evaluate(node.left)
    r_val = evaluate(node.right)

    if l_val == 0 or r_val == 0:
        try:
            total = evaluate(node)
            return Node(value=total)
        except ZeroDivisionError:
            pass  # оставляем узел как есть

    return node


# ──────────────────────────────────────────────
# Вывод дерева
# ──────────────────────────────────────────────
def print_tree(node: Optional[Node], prefix: str = "", is_left: bool = True) -> None:
    if node is None:
        return
    connector = "├── " if is_left else "└── "
    print(prefix + connector + node.label())
    ext = "│   " if is_left else "    "
    if not node.is_leaf():
        print_tree(node.left,  prefix + ext, is_left=True)
        print_tree(node.right, prefix + ext, is_left=False)


def tree_to_prefix(node: Optional[Node]) -> str:
    """Восстанавливает префиксное выражение из дерева."""
    if node is None:
        return ""
    if node.is_leaf():
        return str(node.value)
    return f"{node.label()} {tree_to_prefix(node.left)} {tree_to_prefix(node.right)}"


def write_output(filename: str, root: Node) -> None:
    """
    Выводит в файл кодированное дерево в виде префиксного обхода
    (значение узла: число >=0 для листа, <0 для оператора).
    """
    def encode_prefix(node: Optional[Node]) -> list[int]:
        if node is None:
            return []
        result = [node.value]
        result += encode_prefix(node.left)
        result += encode_prefix(node.right)
        return result

    codes = encode_prefix(root)
    with open(filename, 'w') as f:
        f.write(' '.join(map(str, codes)) + '\n')


# ──────────────────────────────────────────────
# Главная функция
# ──────────────────────────────────────────────
def main() -> None:
    filename_in  = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    filename_out = sys.argv[2] if len(sys.argv) > 2 else "output.txt"

    print(f"Читаем выражение из: {filename_in}")
    root = build_tree(filename_in)

    print("\n── Исходное дерево ──")
    print("  " + root.label())
    print_tree(root.left,  prefix="  ", is_left=True)
    print_tree(root.right, prefix="  ", is_left=False)
    print(f"\nПрефиксная запись : {tree_to_prefix(root)}")
    try:
        print(f"Значение          : {evaluate(root)}")
    except ZeroDivisionError as e:
        print(f"Ошибка вычисления : {e}")

    print("\n── Оптимизация (замена поддеревьев с нулевым результатом) ──")
    root = optimize(root)

    print("\n── Оптимизированное дерево ──")
    print("  " + root.label())
    print_tree(root.left,  prefix="  ", is_left=True)
    print_tree(root.right, prefix="  ", is_left=False)
    print(f"\nПрефиксная запись : {tree_to_prefix(root)}")
    try:
        print(f"Значение          : {evaluate(root)}")
    except ZeroDivisionError as e:
        print(f"Ошибка вычисления : {e}")

    print(f"\nУказатель на корень: <Node value={root.value} label='{root.label()}'>")

    write_output(filename_out, root)
    print(f"\nКодированное дерево записано в: {filename_out}")


if __name__ == "__main__":
    main()