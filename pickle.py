# --- Introduction to the Pickle Module ---
# The `pickle` module in Python is used for serializing and deserializing Python objects.
# Serialization (pickling) converts Python objects (e.g., lists, dictionaries, custom classes) into a byte stream,
# which can be saved to a file or transmitted over a network.
# Deserialization (unpickling) converts the byte stream back into Python objects.
# Key features:
# - Supports a wide range of Python objects (lists, dictionaries, sets, classes, etc.).
# - Allows saving objects to files (`dump`/`load`) or in-memory (`dumps`/`loads`).
# - Provides protocol versions for compatibility and efficiency.
# - Caution: Unpickling untrusted data can pose security risks (arbitrary code execution).
# - Part of Python's standard library, no installation required.


import pickle
from datetime import datetime

# --- 1. Basic Pickling and Unpickling ---
print("--- Basic Pickling and Unpickling ---")
# Sample data: various Python objects
data = {
    "name": "Alice",
    "age": 30,
    "scores": [95, 88, 92],
    "date": datetime.now(),
    "tuple": (1, 2, 3),
    "set": {1, 2, 3}
}

# Serialize (pickle) to a file
with open('data.pkl', 'wb') as file:  # 'wb' for binary write mode
    pickle.dump(data, file)
print("Data pickled to 'data.pkl'")

# Deserialize (unpickle) from a file
with open('data.pkl', 'rb') as file:  # 'rb' for binary read mode
    loaded_data = pickle.load(file)
print("Unpickled data:", loaded_data)
print("Type of loaded data:", type(loaded_data))  # Output: Type of loaded data: <class 'dict'>

# --- 2. Pickling to Bytes (In-Memory Serialization) ---
print("\n--- Pickling to Bytes ---")
# Serialize to bytes
serialized_bytes = pickle.dumps(data)
print("Serialized bytes:", serialized_bytes[:50], "...")  # Show first 50 bytes

# Deserialize from bytes
loaded_from_bytes = pickle.loads(serialized_bytes)
print("Unpickled from bytes:", loaded_from_bytes)

# --- 3. Pickling Multiple Objects to a Single File ---
print("\n--- Pickling Multiple Objects ---")
data1 = ["list", "of", "items"]
data2 = {"key": "value"}
data3 = 42

# Pickle multiple objects
with open('multiple.pkl', 'wb') as file:
    pickle.dump(data1, file)
    pickle.dump(data2, file)
    pickle.dump(data3, file)
print("Multiple objects pickled")

# Unpickle multiple objects
with open('multiple.pkl', 'rb') as file:
    loaded1 = pickle.load(file)
    loaded2 = pickle.load(file)
    loaded3 = pickle.load(file)
print("Unpickled objects:", loaded1, loaded2, loaded3)

# --- 4. Handling Complex Objects (Classes) ---
print("\n--- Pickling Custom Classes ---")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

# Create an instance
person = Person("Bob", 25)

# Pickle the object
with open('person.pkl', 'wb') as file:
    pickle.dump(person, file)

# Unpickle the object
with open('person.pkl', 'rb') as file:
    loaded_person = pickle.load(file)
print("Unpickled person:", str(loaded_person))  # Output: Unpickled person: Person(name=Bob, age=25)

# --- 5. Customizing Pickling Behavior ---
print("\n--- Customizing Pickling Behavior ---")
class CustomPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __getstate__(self):
        # Customize what gets pickled
        state = self.__dict__.copy()
        state['age'] = self.age + 10  # Modify age during pickling
        return state
    
    def __setstate__(self, state):
        # Customize how state is restored
        self.__dict__.update(state)
        self.name = state['name'].upper()  # Convert name to uppercase during unpickling

custom_person = CustomPerson("Charlie", 30)
with open('custom_person.pkl', 'wb') as file:
    pickle.dump(custom_person, file)

with open('custom_person.pkl', 'rb') as file:
    loaded_custom_person = pickle.load(file)
print("Custom unpickled person:", loaded_custom_person.name, loaded_custom_person.age)  # Output: CHARLIE, 40

# --- 6. Handling Non-Picklable Objects ---
print("\n--- Handling Non-Picklable Objects ---")
# Example: File objects cannot be pickled directly
try:
    with open('test.txt', 'w') as file:
        pickle.dumps(file)  # This will raise an error
except pickle.PicklingError as e:
    print("Error: Cannot pickle file object:", e)

# Workaround: Pickle serializable data instead
file_content = "Some text"
with open('content.pkl', 'wb') as file:
    pickle.dump(file_content, file)
print("Pickled file content instead")

# --- 7. Protocol Versions ---
print("\n--- Using Different Protocol Versions ---")
# Pickle with a specific protocol (higher protocols are more efficient)
with open('protocol.pkl', 'wb') as file:
    pickle.dump(data, file, protocol=pickle.HIGHEST_PROTOCOL)
print("Pickled with highest protocol")

# --- 8. Error Handling ---
print("\n--- Error Handling ---")
# Handle corrupted or invalid pickle file
try:
    with open('corrupted.pkl', 'wb') as file:
        file.write(b"invalid pickle data")  # Write invalid data
    with open('corrupted.pkl', 'rb') as file:
        pickle.load(file)
except pickle.UnpicklingError as e:
    print("Unpickling error:", e)

# Handle missing file
try:
    with open('nonexistent.pkl', 'rb') as file:
        pickle.load(file)
except FileNotFoundError as e:
    print("File not found:", e)

# --- 9. Security Considerations ---
print("\n--- Security Note ---")
# Warning: Unpickling untrusted data can execute arbitrary code
print("Warning: Only unpickle data from trusted sources to avoid security risks.")

# --- 10. Checking Picklable Objects ---
print("\n--- Checking Picklable Objects ---")
def is_picklable(obj):
    try:
        pickle.dumps(obj)
        return True
    except (pickle.PicklingError, AttributeError, TypeError):
        return False

print("Is dict picklable?", is_picklable(data))  # Output: True
print("Is lambda picklable?", is_picklable(lambda x: x))  # Output: False

# --- 11. Pickling Large Data (Memory Considerations) ---
print("\n--- Pickling Large Data ---")
large_data = [i for i in range(1000000)]  # Large list
with open('large_data.pkl', 'wb') as file:
    pickle.dump(large_data, file)
print("Large data pickled successfully")
