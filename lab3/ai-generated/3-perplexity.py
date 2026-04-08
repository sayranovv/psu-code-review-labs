# https://www.perplexity.ai

def count_numbers(N, K):
    # dp[j] = dp[i][j] для текущей длины i, j = 0,1,2
    dp = [0, 0, 0]

    # длина 1
    dp[0] = K - 1  # заканчиваются ненулём
    dp[1] = 1      # заканчиваются одним нулём
    dp[2] = 0

    for _ in range(2, N + 1):
        prev0, prev1, prev2 = dp

        # добавляем ненулевой символ
        new0 = (K - 1) * (prev0 + prev1 + prev2)

        # добавляем ноль
        new1 = prev0      # ...0
        new2 = prev1      # ...00

        dp = [new0, new1, new2]

    return sum(dp)


if __name__ == "__main__":
    N = int(input("N = "))
    K = int(input("K = "))
    print(count_numbers(N, K))
