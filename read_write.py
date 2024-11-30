# Function to modify file content (e.g., make all text uppercase)
def modify_file_content(content):
    return content.upper()  # Converts all text to uppercase

# Function to read from a file, modify the content, and write to a new file
def read_and_write_files():
    try:
        # Ask the user for the input file name
        input_file = input("Enter the name of the file to read (e.g., story.txt): ").strip()

        # Ask the user for the output file name
        output_file = input("Enter the name of the file to save the modified content (e.g., new_story.txt): ").strip()

        # Open the input file and read its content
        with open(input_file, 'r') as file:
            content = file.read()

        # Modify the content (e.g., make it uppercase)
        modified_content = modify_file_content(content)

        # Write the modified content to the output file
        with open(output_file, 'w') as file:
            file.write(modified_content)

        print(f"Success! The modified content has been saved to '{output_file}'.")

    # Handle case where the input file doesn't exist
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist. Please check the file name and try again.")

    # Handle permission errors or unexpected issues
    except PermissionError:
        print(f"Error: You don't have permission to access the file '{input_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Function to add content to the file (for testing purposes)
def add_content_to_file(filename):
    with open(filename, 'a') as file:  # 'a' means append mode
        file.write("\nHello, world!\n")  # Adds a new line with text
        file.write("This is a test file.\n")
        file.write("Python is fun.\n")
        file.write("Let's modify it with Python!\n")
    print(f"Content has been added to '{filename}'.")

# Call the function to add content to 'story.txt'
add_content_to_file("story.txt")

# Start the program
if __name__ == "__main__":
    read_and_write_files()
