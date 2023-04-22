import json


def main():
    # getting data
    animals_data = load_data('animals_data.json')

    animals_data_string_for_html = serialization_of_data_for_html(animals_data)

    # creating animal1.html with serialized data
    html_page_data = read_file("animals_template.html")
    html_page_data_reworked = html_page_data.replace(
        "__REPLACE_ANIMALS_INFO__", animals_data_string_for_html
    )
    write_file("animal1.html", html_page_data_reworked)


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
    output += f"<strong>Diet</strong>: {animal['characteristics']['diet']}</br>\n"
    output += f"<strong>Location</strong>: {animal['locations'][0]} </br>\n"
    if "type" in animal['characteristics']:
        output += f"<strong>Type</strong>: {animal['characteristics']['type']}</br>\n"
    output += "</p>\n"
    output += "</li>\n"

    return output

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


if __name__ == '__main__':
    main()
