def function_with_uncommon_error(a, b):
    if a != 0:
        return a + b
    else:
        return float('inf') # Or handle it appropriately, e.g., return a large number, raise an exception, etc. 

result = function_with_uncommon_error(0,5) 