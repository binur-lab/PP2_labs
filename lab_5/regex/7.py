import re

with open(r"C:\Users\binur\OneDrive\Рабочий стол\PP2_labs\lab_5\row\row.txt", encoding="utf-8") as f:
    data = f.read()

modified_data = re.sub(r'_([a-z])', lambda m: m.group(1).upper(), data)
print("7:", modified_data)