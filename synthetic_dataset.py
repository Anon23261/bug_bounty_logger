# Synthetic dataset for bug detection

data = [
    "def buggy_function():\n    x = 1\n    y = 0\n    return x / y",  # Division by zero
    "def clean_function():\n    x = 1\n    y = 2\n    return x / y",  # No bug
    "def another_buggy_function():\n    for i in range(5):\n        print(i)\n    print(j)",  # Undefined variable 'j'
    "def yet_another_clean_function():\n    return sum([1, 2, 3, 4])",  # No bug
]

labels = [1, 0, 1, 0]  # 1 indicates buggy, 0 indicates clean

# The dataset is simple and synthetic, meant for demonstration purposes
