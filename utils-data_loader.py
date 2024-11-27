def load_text_data(file_path):
    """Loads text data from a file."""
    with open(file_path, "r") as file:
        return file.read().strip()

