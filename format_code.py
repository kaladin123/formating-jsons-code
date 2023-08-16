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
