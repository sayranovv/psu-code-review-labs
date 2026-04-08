# https://gemini.google.com

def find_all_paths(matrix, start, end, visited, path, all_paths):
    visited[start] = True
    path.append(start + 1)  # +1 для перевода в нумерацию с единицы

    if start == end:
        all_paths.append(list(path))
    else:
        for i in range(len(matrix)):
            if matrix[start][i] == 1 and not visited[i]:
                find_all_paths(matrix, i, end, visited, path, all_paths)

    # Шаг назад (backtracking)
    path.pop()
    visited[start] = False

def solve():
    file_name1 = "input.txt"  # Имя входного файла
    file_name2 = "output.txt" # Имя выходного файла
    
    # Номера городов для поиска (можно изменить или вводить с клавиатуры)
    k1 = int(input("Введите номер начального города (K1): "))
    k2 = int(input("Введите номер конечного города (K2): "))

    try:
        with open(file_name1, 'r') as f:
            n = int(f.readline().strip())
            matrix = []
            for _ in range(n):
                matrix.append(list(map(int, f.readline().split())))
    except FileNotFoundError:
        print(f"Файл {file_name1} не найден.")
        return

    all_paths = []
    visited = [False] * n
    
    # Запускаем поиск (индексы в матрице на 1 меньше номеров городов)
    find_all_paths(matrix, k1 - 1, k2 - 1, visited, [], all_paths)

    with open(file_name2, 'w') as f:
        if not all_paths:
            f.write("-1")
        else:
            # Сортировка: сначала по длине (len), затем лексикографически
            all_paths.sort(key=lambda x: (len(x), x))
            
            f.write(f"{len(all_paths)}\n")
            for path in all_paths:
                f.write(" ".join(map(str, path)) + "\n")

if __name__ == "__main__":
    solve()