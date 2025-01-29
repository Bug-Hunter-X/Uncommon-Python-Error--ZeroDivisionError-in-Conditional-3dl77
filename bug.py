def function_with_uncommon_error(a, b):
    if a == 0:
        return 1 / a  # ZeroDivisionError
    return a + b

result = function_with_uncommon_error(0, 5)