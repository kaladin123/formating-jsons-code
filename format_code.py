def format_data(data_list):
    for i, entry in enumerate(data_list, 1):
        print(f"{i}.")
        for key, value in entry.items():
            formatted_key = ' '.join([word.capitalize() for word in key.split()])
            if isinstance(value, list) and not value:
                print(f"- {formatted_key}: (Empty)")
            else:
                print(f"- {formatted_key}: {value}")
        print("---\n") # Separator



def format_with_bullets(data_list):
    for i, entry in enumerate(data_list, 1):
        print(f"• Data {i}:")
        for key, value in entry.items():
            print(f"    - {key.capitalize()}: {value}")


def human_readable_format(data_list):
    separator = '-' * 40  # Separator for clarity between dictionaries

    for i, entry in enumerate(data_list, 1):
        print(f"Data {i}:")
        for key, value in entry.items():
            # If value is an empty list, display '(Empty)'
            value = '(Empty)' if isinstance(value, list) and not value else value
            print(f"  {key.capitalize()}: {value}")
        print(separator)  # Print separator after each dictionary


def boxed_format(data_list):
    box_top = '+' + '-' * 38 + '+'
    box_bottom = '+' + '-' * 38 + '+'

    for i, entry in enumerate(data_list, 1):
        print(box_top)
        print(f"| Dictionary {i}".ljust(38) + " |")
        for key, value in entry.items():
            value = '(Empty)' if isinstance(value, list) and not value else value
            print(f"|  {key.capitalize()}: {value}".ljust(38) + " |")
        print(box_bottom)
        print()  # Space between dictionaries


def arrow_pointers_format(data_list):
    for i, entry in enumerate(data_list, 1):
        print(f"Data {i} =>")
        for key, value in entry.items():
            value = '(Empty)' if isinstance(value, list) and not value else value
            print(f"    --> {key.capitalize()}: {value}")
        print('-' * 40)  # Separator


def bullet_points_format(data_list):
    for i, entry in enumerate(data_list, 1):
        print(f"• Data {i}:")
        for key, value in entry.items():
            value = '(Empty)' if isinstance(value, list) and not value else value
            print(f"  - {key.capitalize()}: {value}")
        print()


def double_indent_format(data_list):
    for i, entry in enumerate(data_list, 1):
        print(f"• Data {i}:")
        for key, value in entry.items():
            value = '(Empty)' if isinstance(value, list) and not value else value
            print(f"    • {key.capitalize()}: {value}")
        print()

def numbered_with_bullets_format(data_list):
    for i, entry in enumerate(data_list, 1):
        print(f"{i}. Data:")
        for key, value in entry.items():
            value = '(Empty)' if isinstance(value, list) and not value else value
            print(f"  • {key.capitalize()}: {value}")
        print()

def emoji_bullet_format(data_list):
    for i, entry in enumerate(data_list, 1):
        print(f"📔 Data {i}:")
        for key, value in entry.items():
            value = '(Empty)' if isinstance(value, list) and not value else value
            print(f"  📌 {key.capitalize()}: {value}")
        print()
