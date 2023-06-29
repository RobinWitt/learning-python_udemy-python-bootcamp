ingredients = []
print(f"Empty list: {ingredients}")

ingredients.append("Rice")
ingredients.append("Broccoli")
ingredients.append("Smoked Tofu")
print(f"List with entries: {ingredients}")

ingredients.pop()
print(f"Remove last element: {ingredients}")

ingredients.insert(1, "Red Onions")
print(f"Insert new element: {ingredients}")

print(f"Last element: {ingredients[-1]}")
