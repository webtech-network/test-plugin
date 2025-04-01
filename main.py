# main.py

def read_and_print_file():
    try:
        with open('utils/data.txt', 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("The file 'data.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    read_and_print_file()