def function_with_uncommon_error(a, b):
    try:
        if a == 0:
            return 0
        return b / a
    except ZeroDivisionError:
        return float('inf')

result = function_with_uncommon_error(0, 10)
print(result)
result = function_with_uncommon_error(1, 10)
print(result)
result = function_with_uncommon_error(0, 0)
print(result)