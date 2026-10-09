colors = ["red", "green", "blue"]

print(len(colors))        # Output: 3
colors.append("yellow")   # Adds "yellow" to the end
print(colors)             # Output: ['red', 'green', 'blue', 'yellow']

colors.remove("red")      # Removes "red"
print(colors)             # Output: ['green', 'blue', 'yellow']

colors[0] = "purple"      # Replaces "green" with "purple"
print(colors)             # Output: ['purple', 'blue', 'yellow']

scores = [95, 82, 76, 91]

for score in scores:
    print(score)