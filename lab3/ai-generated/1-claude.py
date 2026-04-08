# https://claude.ai

"""
Graf10 — Юный путешественник
Поиск всех маршрутов из города K1 в город K2 по матрице смежности.
"""

import sys
from itertools import groupby


def read_input(filename: str) -> tuple[int, list[list[int]]]:
    """Читает матрицу смежности из файла."""
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    n = int(lines[0])
    matrix = []
    for i in range(1, n + 1):
        row = list(map(int, lines[i].split()))
        matrix.append(row)

    return n, matrix


def find_all_paths(
    matrix: list[list[int]],
    n: int,
    start: int,
    end: int,
) -> list[list[int]]:
    """
    DFS-обход для поиска всех простых маршрутов из start в end.
    Города нумеруются с 0 внутри алгоритма, с 1 — в выводе.
    """
    all_paths: list[list[int]] = []
    visited = [False] * n

    def dfs(current: int, path: list[int]) -> None:
        if current == end:
            all_paths.append(path[:])
            return

        visited[current] = True
        for neighbor in range(n):
            if matrix[current][neighbor] == 1 and not visited[neighbor]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()
        visited[current] = False

    visited[start] = True
    dfs(start, [start])

    return all_paths


def sort_paths(paths: list[list[int]]) -> list[list[int]]:
    """
    Сортирует маршруты: сначала по длине (кол-во городов),
    затем лексикографически внутри одной длины.
    """
    return sorted(paths, key=lambda p: (len(p), p))


def write_output(filename: str, paths: list[list[int]]) -> None:
    """Записывает результат в файл."""
    with open(filename, "w") as f:
        if not paths:
            f.write("-1\n")
            return

        f.write(f"{len(paths)}\n")
        for path in paths:
            # Номера городов с 1
            f.write(" ".join(str(city + 1) for city in path) + "\n")


def main() -> None:
    # --- Настройки ---
    filename_in  = "input.txt"   # FileName1
    filename_out = "output.txt"  # FileName2

    # K1 и K2 можно передать аргументами командной строки:
    #   python graf10.py input.txt output.txt 1 5
    # или задать прямо здесь:
    k1_default, k2_default = 1, 4   # города с 1

    if len(sys.argv) >= 5:
        filename_in  = sys.argv[1]
        filename_out = sys.argv[2]
        k1 = int(sys.argv[3])
        k2 = int(sys.argv[4])
    elif len(sys.argv) >= 3:
        filename_in  = sys.argv[1]
        filename_out = sys.argv[2]
        k1, k2 = k1_default, k2_default
    else:
        k1, k2 = k1_default, k2_default

    n, matrix = read_input(filename_in)

    # Перевод в 0-based индексы
    start = k1 - 1
    end   = k2 - 1

    if start < 0 or start >= n or end < 0 or end >= n:
        print(f"Ошибка: города должны быть в диапазоне 1..{n}")
        sys.exit(1)

    paths = find_all_paths(matrix, n, start, end)
    paths = sort_paths(paths)

    write_output(filename_out, paths)

    # Дублируем результат в консоль для удобства проверки
    if not paths:
        print("Маршрутов нет → -1")
    else:
        print(f"Найдено маршрутов: {len(paths)}")
        for path in paths:
            print(" → ".join(str(c + 1) for c in path))


if __name__ == "__main__":
    main()