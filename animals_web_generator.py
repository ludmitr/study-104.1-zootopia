import json


def main():
    animals_data = load_data('animals_data.json')
    print_animals_data(animals_data)


def print_animals_data(data):
    for animal in data:
        print("----------------")
        print(f"Name: {animal['name']}")
        print(f"Diet: {animal['characteristics']['diet']}")
        print(f"Location: {animal['locations'][0]}")
        if "type" in animal['characteristics']:
            print(f"Type: {animal['characteristics']['type']}")


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


if __name__ == '__main__':
    main()
