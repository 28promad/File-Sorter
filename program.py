import os
# shutil stands for shell utilities
import shutil

from guizero import App, Box, Text, TextBox, PushButton
# me being dumb for no reason
# background color of app
hexa = "#"
hexa += "b44422"
# application name, and dimensions
main = App("File sorter", height=125, width=360, bg=hexa)


# functions
# update path everytime you type a character
def update_path():
    temp = textbox.value
    if temp[-1] != "/":
        temp += "/"
    textbox.value = temp
    path_text.value = "Path:"
    path_text.value += "\""
    path_text.value += textbox.value
    path_text.value += "\""
    global path
    path = textbox.value
    print(path)


def confirm():
    # I'm going to add a pop-up for confirmation
    temp_str = "Are you sure you want to sort the following path:\n\""
    temp_str += path
    temp_str += "\""
    if main.yesno("Confirmation", temp_str):
        sort()

# the actual sorting thingy
def sort():
    file_name = os.listdir(path)
    for loop in range(len(folder_names)):  # range(0, 4):
        if not os.path.exists(path + folder_names[loop]):
            print(path + folder_names[loop])
            os.makedirs(path + folder_names[loop])
    for file in file_name:
        print(file)
        if ((".jpg" in file) or (".JPG" in file) or (".jpeg" in file) or (".webp" in file) or (".gif" in file) or (".png" in file)) and not os.path.exists(path + "image files/" + file):
            # this if statement checks for the presence of the '.jpg' extension on the name
            # of a file as well as if the jpg file is not in its correct folder
            # then below I'll just move the actual file, im working on it
            shutil.move(src=path + file, dst=path + "image files/" + file)
        elif (".mp3" in file or ".wav" in file) and not os.path.exists(path + "audio files/" + file):
            shutil.move(src=path + file, dst=path + "audio files/" + file)
            # print(".audio")
        elif ".txt" in file and not os.path.exists(path + "text files/" + file):
            shutil.move(src=path + file, dst=path + "text files/" + file)
            # print(".txt")
        elif ".xlsx" in file and not os.path.exists(path + "spreadsheets/" + file):
            # print(".xlsx")
            shutil.move(src=path + file, dst=path + "spreadsheets/" + file)
        elif (".zip" in file) or (".rar" in file) and not os.path.exists(path + "compressed files/" + file):
            shutil.move(src=path + file, dst=path + "compressed files/" + file)
        elif (".mp4" in file) and not os.path.exists(path + "videos/" + file):
            shutil.move(src=path + file, dst=path + "videos/" + file)
        elif (".exe" in file) or (".msi" in file) or (".appinstaller" in file) and not os.path.exists(path + "setup files/" + file):
            shutil.move(src=path + file, dst=path + "setup files/" + file)
    main.info("File sorter", "Your folder has successfully been sorted")
    # main.warn("Error", "You're gay")


def current_directory():
    global path
    path = os.getcwd()
    path += "/"
    while "\\" in path:
        path = path.replace("\\", "/")
    textbox.value = path
    update_path()


# containers
box1 = Box(main, layout="grid", align="top", border=1)
box2 = Box(main, layout="grid", align="top")

# extras
# variables
path = r"C:/Users/Phil/Desktop/Experiments/Unfiltered/"
folder_names = ["image files", "setup files", "audio files", "text files", "spreadsheets", "compressed files", "videos"]

"""
hello = os.getcwd()
print(hello)
"""
help_text = Text(main, color="#111111",
                 font="times new roman",
                 size=12,
                 align="bottom",
                 text="File Sorter v1.3\nEnter a path and press enter to sort")
square = 25
path_text = Text(box1,
                 grid=(0, 0),
                 text="Phil was here")
textbox = TextBox(box1, grid=(0, 1),
                  text="Enter or paste path here",
                  command=update_path, width=45)
accept = PushButton(box1,
                    grid=(1, 1),
                    height=square, width=square,
                    command=confirm,
                    image=r"C:/Users/Phil/Desktop/Experiments/Unfiltered/jpg files/accept.gif")

current = PushButton(box1,
                     grid=(2, 1),
                     height=square, width=square,
                     command=current_directory,
                     image=r"C:/Users/Phil/Desktop/Experiments/Unfiltered/jpg files/current.gif")

main.display()

