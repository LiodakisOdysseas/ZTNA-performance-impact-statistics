import random
import json
import sys

# Function to generate a random JSON object with specified number of attributes
def generate_large_json(num_attributes):
    def random_value():
        value_type = random.choice(["Number", "String", "Boolean"])
        if value_type == "Number":
            return random.randint(1, 1000)
        elif value_type == "String":
            return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ', k=random.randint(5, 15)))
        elif value_type == "Boolean":
            return random.choice([True, False])
    
    json_obj = {
        "id": f"Room{num_attributes}",
        "type": "Room"
    }
    
    for i in range(num_attributes):
        attribute_name = f"attribute_{i + 1}"
        json_obj[attribute_name] = {
            "value": random_value(),
            "type": random.choice(["Number", "String", "Boolean"])
        }
    
    return json_obj

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_json.py <num_attributes> <output_file>")
        sys.exit(1)

    try:
        num_attributes = int(sys.argv[1])
    except ValueError:
        print("The number of attributes must be an integer.")
        sys.exit(1)

    output_file = sys.argv[2]

    # Generate the JSON object
    large_json = generate_large_json(num_attributes)

    # Convert to JSON string and pretty print
    large_json_str = json.dumps(large_json, indent=2)

    # Output JSON to a file
    with open(output_file, 'w') as f:
        f.write(large_json_str)

    print(f"Generated large JSON with {num_attributes} attributes saved to '{output_file}'")

