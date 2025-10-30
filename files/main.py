from filehandling import list_dir, create_dir, delete_dir, rename_dir, search_dir
import sys

def main() :
    print("File and Directory Handler")
    print("-------Main Menu--------")
    print("""
    A.)List file/directory
    B.)Create file/directory
    C.)Delete file/directory
    D.)Rename file/directory
    E.)Search File Name/Extention
    F.)Exit
        """)
    user_input = input("Select A-D > ")
    user_input = user_input.upper()

    if user_input == 'A':
        list_dir()
        main()
    elif user_input == 'B':
        create_dir()
        main()
    elif user_input == 'C':
        delete_dir()
        main()
    elif user_input == 'D':
        rename_dir()
        main()
    elif user_input == 'E':
        search_dir()
    elif user_input == 'F':
        sys.exit()
    else :
        print("Invalid Input Try Again!")


if __name__ == "__main__":
    main()
