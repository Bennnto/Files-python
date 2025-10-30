import os

def list_dir (max_depth = 3) :
    current_dir = os.getcwd()
    print(f"Current Directory : {current_dir}")
    print('List your directory')
    path = input('input your file / directory path > ')
    exist = os.path.exists(path)
    if exist :
        for root, dirs, files in os.walk(path):
            level = root.replace(path, '').count(os.sep)
            #stop max depth
            if level >= max_depth :
                dirs[:] = [] #don't go deeper
                continue

            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['venv', '__pycache__', 'node_modules']]
            indent = ' ' * level

            #print directory
            if level > 0 :
                print(f"{indent}📁 {os.path.basename(root)}/")

            file_indent = ' ' * (level + 3)
            visible_files = [f for f in files if not f.startswith('.')][:5]

            for file in visible_files:
                print(f"{file_indent}|-{file}")

            if len(files) > 5 :
                print(f"{file_indent}|_({len(file)-5} more files)")


def create_dir() :
    current_dir = os.getcwd()
    print(f"Current Directory : {current_dir}")
    print('Create file')
    path = input('input your file / directory path > ')
    name = input('input your file name > ')
    touch_file = f"{path}/{name}"
    exist = os.path.exists(path)
    try:
        if exist :
            open(touch_file, 'a')
        else :
            os.mkdir(path)
            os.chdir(path)
            open(name, 'a')
    except ValueError:
        print("Couldn't find your path")
    print('file / directory created')

def delete_dir() :
    current_dir = os.getcwd()
    print(f"Current Directory : {current_dir}")
    print('Delete file / Directory')
    user = input('Delete File select F , Delete Directory select D > ')
    user = user.upper()
    while True :
        if user in ('F', 'D'):
            break
        else :
            print("Invalid Input Try Again")
            continue
    path = input('input your file / directory path > ')
    exist = os.path.exists(path)
    try :
        if exist :
            if user == 'F':
                os.remove(path)
                print(f'Removed File from {path}')
            elif user == 'D':
                os.rmdir(path)
                print(f'Removed Directory from {path}')
        else :
            print("Your input directory doesn't exist")
    except ValueError :
            print("Not found Directory")

def rename_dir() :
    current_dir = os.getcwd()
    print(f"Current Directory : {current_dir}")
    print('Rename File/Directory')
    path = input('input your file / directory path > ')
    change_path = input('input your path/[new filename/new directory name] > ')
    exist = os.path.exists(path)
    if exist :
        os.rename(path, change_path)
        print('Renamed file / Directory')
    else :
        print("Path doesn't exist")

def search_dir() :
    skip_dirs = {'venv', '__pycache__', 'node_modules'}
    current_dir = os.getcwd()
    print(f"Current Directory : {current_dir}")
    print('Search directory')
    print('A.) Search by Exec Name')
    print('B.) Search by file extention')
    user = input('Please Select A or B > ')
    user = user.upper()
    while True :
        if user in ('A', 'B'):
            break
        else :
            print('Invalid Input Try Again!')
            continue
    path = input('input your file / directory path > ')
    exist = os.path.exists(path)
    results = [ ]
    if exist :
        if user == 'A':
            filename = input('Filename to search > ')
            for root, dirs, files in os.walk(path):
                dirs[:] = [d for d in dirs if d not in skip_dirs and not d.startswith('.')]
                for file in files:

                    if file.startswith('.'):
                        continue
                    if file == filename :
                        full_path = os.path.join(root, file)
                        file_size = os.path.getsize(full_path)
                        results.append({
                            'name' : file,
                            'path' : full_path,
                            'size' : file_size,
                            'dir' : root
                        })
                    else :
                        print('File not found')
        elif user == 'B':
            extention = input('File extension to search > ')
            ext = '.' + extention
            for root, dirs, files in os.walk(path):
                dirs[:] = [d for d in dirs if d not in skip_dirs and not d.startswith('.')]
                for file in files:

                    if file.startswith('.'):
                        continue

                    if file.endswith(ext):
                        full_path = os.path.join(root, file)
                        file_size = os.path.getsize(full_path)
                        results.append({
                            'name' : file,
                            'path' : full_path,
                            'size' : file_size,
                            'dir' : root
                        })
    else :
        print("Invalid Path")
    if results:
        print(f"Found {len(results)} file(s)\n")
        for i, result in enumerate(results, 1):
            size_kb = result['size'] / 1024
            print(f"{i}. file: {result['name']}")
            print(f" path : {result['path']}")
            print(f" size : {size_kb:2f} KB")
            print(f" Directory : {result['dir']}")
    else :
        print("\n Not Matching Found")
if __name__ == "__main__":
   search_dir()
