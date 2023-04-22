import json


def main():
    """Generate html page by skin type that gets from user"""
    # getting data
    animals_data = load_data('animals_data.json')

    # get skin type from user
    skin_types = get_skin_type_list(animals_data)
    skin_type = get_user_input(skin_types)

    animals_data_string_for_html = serialization_of_data_by_skin_type(animals_data, skin_type)

    # creating animal1.html with serialized data
    html_page_data = read_file("animals_template.html")
    html_page_data_reworked = html_page_data.replace(
        "__REPLACE_ANIMALS_INFO__", animals_data_string_for_html
    )
    write_file("animal1.html", html_page_data_reworked)


def serialization_of_data_by_skin_type(data, skin_type):
    """Serialization of data by skin type for html page.
    Returns string"""
    animals_data_as_string = ""

    for animal in data:
        if "skin_type" in animal["characteristics"] \
                and animal["characteristics"]["skin_type"].lower() == skin_type:
            animals_data_as_string += serialize_animal(animal)

    return animals_data_as_string


def get_user_input(skin_types):
    """Get user input. return string"""
    skin_types_lower = [skin_type.lower() for skin_type in skin_types]

    while True:

        print(skin_types)
        user_input = input("Choose skin type: ")

        if user_input.lower() in skin_types_lower:
            return user_input
        print("try again")



def get_skin_type_list(data):
    """Return list of animal skin types"""
    skin_types = set()
    for animal in data:
        skin_types.add(animal["characteristics"]["skin_type"])

    return list(skin_types)


def write_file(file_path, data):
    """Creates file_path with data"""
    with open(file_path, "w") as file:
        file.write(data)


def read_file(file_path):
    """Returns string data of file_path"""
    with open(file_path, "r") as file:
        return file.read()


def serialization_of_data_for_html(data):
    """Serialization of data for html page. Returns string"""
    animals_data_as_string = ""

    for animal in data:
        animals_data_as_string += serialize_animal(animal)

    return animals_data_as_string


def serialize_animal(animal):
    """Creates single animal serialization and returns it"""
    output = ""
    output += '<li class="cards__item">'
    output += f"<div class='card__title'>{animal['name']}</div>\n"
    output += "<p class='card__text'>\n"
    output += "<ul class='animal__card__list'>\n"
    output += f"<li><strong>Diet</strong>: {animal['characteristics']['diet']}</li>\n"
    output += f"<li><strong>Location</strong>: {animal['locations'][0]}</li>\n"
    if "type" in animal['characteristics']:
        output += f"<li><strong>Type</strong>: {animal['characteristics']['type']}</li>\n"
    output += "</ul>"
    output += "</p>\n"
    output += "</li>\n"

    return output

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


if __name__ == '__main__':
    main()
