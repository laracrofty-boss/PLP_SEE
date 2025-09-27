# File_read_write_error handling.py
try:
    # Step 1 open the file that the user wants to read
    filename = input("enter the file name you want to open: ").strip()
    infile = open("sample.txt", "r")
    content = infile.read()
    infile.close()

    # Step 2 modify the text (make everything uppercase)
    modified_content = content.upper()

    # Step 3 open a new file to write the modified text
    outfile = open("sample_modified.txt", "w")
    outfile.write(modified_content)
    outfile.close()

    # Step 4 tell the user it worked
    print("file has been modified and saved as modified as sample_modified.txt")

# if the file to be read doesn't exist
except FileNotFoundError:
    print("file not found")

# if somthing else goes wrong
except Exception as e:
    print("An unexpected error occured", e)


# Error_handling_lab_py
try:

    # Step 1 ask the user to type the file name
    filename = input("enter the file name you want to open")

    # Step 2 try to open and read the file
    infile = open(filename, "r")
    content = infile.read()
    infile.close()

    # Step 3 show the file contents to the user
    print(content)

# If the file is not found
except FileNotFoundError:
    print("The file was not found")

# If anything goes wrong
except Exception as e:
    print("unexpected error occured", e)
