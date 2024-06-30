# This is a basic Python script that demonstrates variables, functions, loops, and conditionals.

# Variables
name = "John"
age = 30

# Function to print a greeting
def greet(person_name):
        print(f"Hello, {person_name}!")

        # Call the greet function
        greet(name)

        # Conditional statement
        if age < 18:
                print("You are a minor.")
            elif age < 65:
                    print("You are an adult.")
                else:
                        print("You are a senior.")

                        # Loop through a list
                        numbers = [1, 2, 3, 4, 5]
                        for number in numbers:
                                print(f"Number: {number}")

                                # While loop example
                                count = 0
                                while count < 5:
                                        print(f"Count is {count}")
                                            count += 1

                                            # Function to calculate the sum of two numbers
                                            def add(a, b):
                                                    return a + b

                                                # Call the add function
                                                result = add(5, 3)
                                                print(f"The sum of 5 and 3 is {result}")

                                                # Using a dictionary
                                                person = {
                                                            "name": "Alice",
                                                                "age": 28,
                                                                    "city": "New York"
                                                                    }

                                                # Access dictionary values
                                                print(f"{person['name']} is {person['age']} years old and lives in {person['city']}.")

