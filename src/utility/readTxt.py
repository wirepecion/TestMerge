def read_txt_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    file_path = 'path_to_your_file.txt'
    content = read_txt_file(file_path)
    print(content)