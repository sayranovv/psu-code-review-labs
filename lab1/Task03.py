#Recur15. Вывести значение целочисленного выражения, заданного в виде строкиS. Выражение определяется следующим образом:
#<выражение> ::= <терм> | <выражение> + <терм> |
#<выражение> − <терм>
#<терм> ::= <цифра> | <терм> * <цифра>

def evaluate_exp_rec(expstr):   #Вычисляет значение целочисленного выражения, используя рекурсию
    def parse_term_rec(s, index):
        #Рекурсивно разбирает терм, начиная с заданного индекса
        if index >= len(s) or not s[index].isdigit():
            return 0, index
        value = int(s[index])
        index += 1
        if index < len(s) and s[index] == '*':
            index += 1
            if index >= len(s) or not s[index].isdigit():
                raise ValueError("Ожидалась цифра после '*'")
            digit = int(s[index])
            term_value, next_index = parse_term_rec(s, index + 1)  #Рекурсивный вызов
            return value * digit , next_index
        else:
            return value, index

    def parse_exp_rec(s, index):
        #Рекурсивно разбирает выражение, начиная с заданного индекса
        term_value, index = parse_term_rec(s, index)
        expression_value = term_value

        if index < len(s) and (s[index] == '+' or s[index] == '-'):
            operator = s[index]
            index += 1
            term_value, index = parse_exp_rec(s, index) # Рекурсивный вызов
            if operator == '+':
                expression_value += term_value
            elif operator == '-':
                expression_value -= term_value
        return expression_value, index
    result, index = parse_exp_rec(expstr, 0)
    if index != len(expstr):
        raise ValueError("Некорректный синтаксис")

    return result

s = input('Введите строку с выражением: ')
try:
    print(evaluate_exp_rec(s))
except ValueError as e:
    print(e)