def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")
    
greet()


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
        
greet_with_name("Bob")
greet_with_name("Alice")
greet_with_name("Mark Smith")  
 

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
    
greet_with("Bob", "London")
greet_with(location="Nowhere", name="Jack")
    