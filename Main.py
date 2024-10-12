import random

# Function to generate random recipe
def generate_random_recipe():
    # Randomly pick one ingredient
    ingredient = random.choice(['Chicken', 'egg', 'Tofu'])
    
    # Randomly pick one cooking method
    cooking_method = random.choice(['grilled', 'fried', 'boiled'])
    
    # Combine and return the recipe
    return f"Random Recipe: {cooking_method.capitalize()} {ingredient}."

# Main program
if __name__ == "__main__":
    print("Welcome to the easy peasy Random Recipe Generator!")
    print(generate_random_recipe())

