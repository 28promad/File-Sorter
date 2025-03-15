import json
import os
import shutil
import sys
from tabulate import tabulate
from pyfiglet import Figlet
from random import choice


# main menu
def main():
    global filetypes
    if len(filetypes) == 0:
        prompt = input('There aren\'t any folders to assign file extensions to.\n'
                       '1. Restore default folders + assigned file extensions; OR\n'
                       '2. Assign your own folders + file extensions')

        if prompt == '2':
            change_menu()
        else:
            print('RESTORED DEFAULT FOLDERS + FILE EXTENSIONS')
            filetypes = {
                'Images': ['jpg', 'png', 'jpeg', 'gif', 'bmp', 'tiff'],
                'Applications': ['exe', 'msi', 'dmg', 'deb', 'pkg', 'apk', 'apks'],
                'Videos': ['mp4', 'mkv', 'avi', 'mov', 'wmv'],
                'Documents': ['pdf', 'doc', 'docx', 'txt', 'xlsx', 'ppt', 'pptx'],
                'Compressed Files': ['zip']
            }
            with open('settings.json', 'w') as file:
                json.dump(filetypes, file, indent=4)

    with open('settings.json', 'r') as temp_file:
        filetypes = json.load(temp_file)
    prompt = input('\n1. Configure folders & filetypes\n'
                   '2. Sort files in cwd\n'
                   '3. Custom sort\n'
                   'ENTER. Exit()\n'
                   '>>>')
    print(' '*15,':)')
    if prompt == '1':
        change_menu()
    elif prompt == '2':
        sort('null', 'null')
    elif prompt == '3':
        custom_sort()
    else:
        sys.exit()


def change_menu():
    configure()
    sample = tabulate(filetypes, headers=[k for k in filetypes.keys()], tablefmt='fancy_outline')
    print(sample)
    if len(filetypes) != 0:
        prompt = input('\n1. Add Folder\n'
                       '2. Add File type\n'
                       '3. Remove File type\n'
                       '4. Remove Folder\n'
                       'ENTER. Exit()\n'
                       '>>>')
        if prompt == '1':
            new_folder = input('Enter name of new folder: ')
            for c in new_folder:
                if c in r'\/:?*<>|':
                    sys.exit('Invalid character in folder name')
            file_name = input('Enter file type to assign to folder: ')
            for c in file_name:
                if c in r'\/:?*<>|':
                    sys.exit('Invalid character in file name')
            filetypes[new_folder] = [file_name]

        elif prompt == '2':
            for i in enumerate(filetypes.keys()):
                print(str(i).replace('(', '').replace(')', ''))
            prompt2 = input('Enter folder number from the list\n>>>').strip()
            try:
                selected_folder = list(filetypes.keys())[int(prompt2)]
                print(selected_folder)
            except ValueError:
                sys.exit('Invalid list number provided')
            except IndexError:
                sys.exit('Invalid list number provided')
            else:
                filetypes[selected_folder].append(input('Enter file extension '
                                                        'to assign to "{}"\n'
                                                        '>>>'.format(selected_folder)))

        elif prompt == '4':
            for i in enumerate(filetypes.keys()):
                print(str(i).replace('(', '').replace(')', ''))
            prompt2 = input('Enter folder number from the list\n>>>')
            try:
                del filetypes[list(filetypes.keys())[int(prompt2)]]
            except IndexError:
                sys.exit('The folder selected does not exist :(')
        elif prompt == '3':
            prompt2 = input('Enter file extension to remove\n>>>').strip()
            for key in filetypes:
                values = filetypes[key]
                temp_values = []
                for i in values:
                    if prompt2 != i:
                        temp_values.append(i)
                filetypes[key] = temp_values               
            print('(If {} exists, it\'s assignment will be removed)'.format(prompt2))
        with open('settings.json', 'w') as new_folder_file:
            json.dump(filetypes, new_folder_file, indent=4)
        configure()
    else:
        print('ADDING A NEW FOLDER...\n')
        new_folder = input('Enter name of new folder: ')
        for c in new_folder:
            if c in r'\/:?*<>|':
                sys.exit('Invalid character in folder name')
        file_name = input('Enter file type to assign to folder: ')
        for c in file_name:
            if c in r'\/:?*<>|':
                sys.exit('Invalid character in file name')
        filetypes[new_folder] = [file_name]
        


# logic for moving the file
def move_file(filename, folder):
    new_file_path = os.path.join(os.path.join(os.getcwd(), folder, filename))
    if not os.path.exists(os.path.join(os.getcwd(), folder)):
        os.makedirs(os.path.join(os.getcwd(), folder))
    old_file_path = os.path.join(os.getcwd(), filename)
    print(filename, 'moved to ', new_file_path)
    shutil.move(old_file_path, new_file_path)


def sort(pre, end):
    if pre == 'null' and end == 'null':
        #normal sort
        files = [i for i in os.listdir('.')]
        for f in files:
            # now at a specific file
            for key in filetypes.keys():
                for extension in filetypes[key]:
                    # print(extension, end='-')
                    if f.endswith(extension):
                        # print(f, 'goes into ', key)
                        # <-- Here you would have to move the file
                        move_file(f, key)
    # prefix provided
    elif pre != '~null~' and end == '~null~':
        # re implement normal sort but only for files starting with the prefix
        files = [i for i in os.listdir('.')]
        for f in files:
            # now at specific file
            # only selecting files with the prefix
            if f.startswith(pre):
                for key in filetypes.keys():
                    for extension in filetypes[key]:
                        if f.endswith(extension):
                            move_file(f, os.path.join(pre, key))
    # suffix provided
    elif pre == '~null~' and end != '~null~':
        # re implement normal sort but only for files ending with the prefix
        files = [i for i in os.listdir('.')]
        for f in files:
            # now as a specific file
            # only selecting those with the suffix
            filename = f.rsplit('.')
            if filename[0].endswith(end):
                for key in filetypes.keys():
                    for extension in filetypes[key]:
                        if f.endswith(extension):
                            move_file(f, os.path.join(end, key))
                            
    # both are provided
    else:
        # re implement the normal sort but only for files starting with both the prefix & suffix
        files = [i for i in os.listdir('.')]
        for f in files:
            # now at specific file
            # only selecting those with both the prefix & suffix
            filename = f.rsplit('.')
            if filename[0].endswith(end) and f.startswith(pre):
                for key in filetypes.keys():
                    for extension in filetypes[key]:
                        if f.endswith(extension):
                            move_file(f, os.path.join('{}-{}'.format(pre, end), key))

# custom sort in which the prefix & or suffix is customised, (set by the user)

def custom_sort():
    try:
        with open('custom_query.json', 'r') as file:
            data = json.load(file)
        print('Current prefix: "{}"; Current suffix: "{}"'.format(data['prefix'], data['suffix']))
        custom_prompt = int(input('1. Set your own custom prefix & or suffix\n'
                                  '2. Run custom_sort\n>>>'))
    except ValueError:
        print('Invalid selection')
    else:
        if custom_prompt == 1:
            configure_custom_query()
        elif custom_prompt == 2:
            print('SORTING USING LAST USED CUSTOM PROMPT')
            sort(data['prefix'], data['suffix'])
            
        

# configure file types and corresponding folders
def configure():
    global filetypes
    with open('settings.json', 'r') as temp_file:
        filetypes = json.load(temp_file)

# configuration of a custom query, reading from custom_query.json, & appending to that
def configure_custom_query():
     
    with open('custom_query.json', 'r') as file:
        data = json.load(file)
    print(data)
    temp_prefix = input('Leave blank for _null_\nSet prefix\n>>>')
    temp_suffix = input('Set suffix\n>>>')

    if temp_prefix == '' and temp_suffix == '':
        data['prefix'], data['suffix'] = '~null~', '~null~'
    if temp_prefix != '' and temp_suffix == '':
        data['prefix'], data['suffix'] = temp_prefix, '~null~'
    if temp_prefix == '' and temp_suffix != '':
        data['prefix'], data['suffix'] = '~null~', temp_suffix
    else:
        data['prefix'], data['suffix'] = temp_prefix, temp_suffix

    # saving current configuration to custom_query.json
    with open('custom_query.json', 'w') as file:
        json.dump(data, file, indent=4)

    # sorting with the new configuration
    print('Sorting using the new configuration')
    sort(data['prefix'],data['suffix'])

# setting default values of configuration file if it doesn't exist
if os.path.exists('settings.json'):
    configure()
if not os.path.exists('settings.json'):
    settings = {
        'Images': ['jpg', 'png', 'jpeg', 'gif', 'bmp', 'tiff'],
        'Applications': ['exe', 'msi', 'dmg', 'deb', 'pkg', 'apk', 'apks'],
        'Videos': ['mp4', 'mkv', 'avi', 'mov', 'wmv'],
        'Documents': ['pdf', 'doc', 'docx', 'txt', 'xlsx', 'ppt', 'pptx'],
        'Compressed Files': ['zip']
    }
    with open('settings.json', 'w') as temp:
        json.dump(settings, temp, indent=4)
    filetypes = settings

if not os.path.exists('custom_query.json'):
    custom_query = {
        'prefix': '~null~',
        'suffix': '~null~'
    }
    with open('custom_query.json', 'w') as temp:
        json.dump(custom_query, temp, indent=4)

# printing a description of the application
text = 'FILE SORTER v1.4'
figlet = Figlet()
figlet.setFont(font='big_money-se')
print(figlet.renderText(text))

while True:
    main()
