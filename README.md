File Sorter
Overview
File Sorter is a Python-based utility designed to organize files in a directory by moving them into categorized folders based on their file extensions. The tool is highly configurable, allowing users to define custom folder names and associated file extensions. It also supports advanced sorting options using user-defined prefixes and suffixes.

Features
Default Categorization: Predefined folders for common file types:

Images: .jpg, .png, .jpeg, .gif, .bmp, .tiff

Applications: .exe, .msi, .dmg, .deb, .pkg, .apk, .apks

Videos: .mp4, .mkv, .avi, .mov, .wmv

Documents: .pdf, .doc, .docx, .txt, .xlsx, .ppt, .pptx

Compressed Files: .zip

Custom Configuration:

Add or remove folders.

Assign or unassign file extensions to specific folders.

Sorting Options:

Normal Sort: Organizes all files in the current working directory (CWD) based on their extensions.

Custom Sort: Allows sorting based on user-defined prefixes and/or suffixes.

Interactive CLI:

Menu-driven interface for configuration and sorting tasks.

Displays current folder-to-filetype mappings in a tabular format.

Persistence:

Saves configurations in settings.json for folder and filetype mappings.

Stores custom prefix and suffix settings in custom_query.json.

How It Works
Initialization:

If settings.json or custom_query.json does not exist, default configurations are created.

The program displays a banner using the pyfiglet library.

Main Menu:

Options to configure folders, sort files, or perform custom sorting.

File Sorting Logic:

Files are matched against the configured extensions.

Matched files are moved to their respective folders, which are created if they do not already exist.

Custom Sorting:

Users can define a prefix and/or suffix for targeted sorting.

Files matching the prefix/suffix criteria are organized accordingly.

Usage
Run the script in the directory where you want to organize files.

Follow the interactive prompts to configure folders or sort files:

Restore default configurations or customize your own.

Choose between normal sorting or custom sorting based on prefixes/suffixes.

Dependencies
The script requires the following Python libraries:

json: For reading and writing configuration files.

os: For interacting with the filesystem.

shutil: For moving files between directories.

sys: For handling system-level operations like exiting the program.

tabulate: For displaying folder-to-filetype mappings in a table format.

pyfiglet: For rendering ASCII art banners.

Install dependencies using:

bash
pip install tabulate pyfiglet
Example
Default Sorting:

text
> python File_Sorter.py
RESTORED DEFAULT FOLDERS + FILE EXTENSIONS
Files sorted into respective folders based on extensions!
Custom Sorting:

text
> python File_Sorter.py
Current prefix: "~null~"; Current suffix: "~null~"
Enter new prefix: "project_"
Enter new suffix: "_final"
Files starting with "project_" and ending with "_final" sorted!
Contribution
Feel free to fork this repository, make improvements, and submit pull requests!

