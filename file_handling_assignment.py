# File Creation
try:
    # Open a file in write mode
    with open('my_file.txt', 'w') as file:
        # Write three lines of text
        file.write('Hello, World!\n')
        file.write('The answer is: {}\n'.format(42))
        file.write('Good day, World!\n')

    # File Reading and Display
    # Open the file in read mode
    with open('my_file.txt', 'r') as file:
        # Read and print the contents of the file
        print(file.read())

    # File Appending
    # Open the file in append mode
    with open('my_file.txt', 'a') as file:
        # Append three additional lines of text
        file.write('Appending first line.\n')
        file.write('Appending second line.\n')
        file.write('Appending third line.\n')

    # Re-read and display the updated content
    with open('my_file.txt', 'r') as file:
        print(file.read())

# Error Handling
except FileNotFoundError:
    print('The file was not found.')
except PermissionError:
    print('You do not have the permission to read/write to the file.')
finally:
    print('File operations are complete.')

