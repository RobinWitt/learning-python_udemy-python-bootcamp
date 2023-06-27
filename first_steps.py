first_name = "JANE" # string / Zeichenkette
last_name = "Roe" # string
upper_name = "max"
lower_name = "MORITZ"
x = 13 # int / integer / ganze Zahl
y = 2.3 # float / floating point / Kommazahl
a, b, c = 3, 4.5, 10 # use multiple variables in one line

overwritten_var = "Currywurst"
overwritten_var = "Brokkoli" # overwrites the initial value


print(f"Hello, {first_name.title()} {last_name}")
print(f"{upper_name.upper()}, {lower_name.lower()}")
print(x + y, a, b, c)
print(overwritten_var)