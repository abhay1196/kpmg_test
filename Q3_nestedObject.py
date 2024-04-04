def print_value(obj, key):
    keys = key.split('/')
    current = obj
    for k in keys:
        if isinstance(current, dict) and k in current:
            current = current[k]
        else:
            print("Key not found")
            return
    print("Value:", current)

# Given object
obj_str = input('Input nested object like {"a": {"b": "c"}}: ')
try:
    obj = eval(obj_str)
except Exception as e:
    print("Invalid input:", e)
    exit()

# Given key
key = input("Input key like a/b: ")
print_value(obj, key)
