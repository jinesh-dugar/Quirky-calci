import random

def generate_zero_expression():
    expressions = [
        "2 + 2 - 4",
        "3 * 3 - 9",
        "10 % 5",
        "8 - (2 * 4)",
        "1 - 1",
        "5 - 5",
        "6 // 3 - 2",
        "2 ** 3 - 8",
        "9 - 3 * 3",
        "(4 - 2) * (1 + 1) - 4"
    ]
    return random.choice(expressions)

def quirky_calculator(expression):
    try:
        result = int(eval(expression))
    except:
        return "Oops! That's not a valid expression. Try again!"

    emojis = ["🍎", "🍌", "🍕", "🚀", "🎈", "🐶", "🐱", "🦄", "🌟", "🎭"]
    
    result_str = str(abs(result))
    emoji_result = []
    
    for i, digit in enumerate(result_str):
        count = int(digit)
        if count == 0:
            emoji_result.append(generate_zero_expression())
        else:
            emoji = emojis[i % len(emojis)]
            emoji_result.append(emoji * count)
    
    return "\n".join(emoji_result)

print("Welcome to the Enhanced Emoji Calculator!")
print("Enter a mathematical expression, and I'll give you a fun emoji answer.")
print("If you see a mathematical expression in the answer, solve it to find out which digit is zero!")
print("Type 'quit' to exit.")

while True:
    user_input = input("\nEnter your calculation: ")
    
    if user_input.lower() == 'quit':
        print("Thanks for using the Enhanced Emoji Calculator!")
        break
    
    result = quirky_calculator(user_input)
    print(result)