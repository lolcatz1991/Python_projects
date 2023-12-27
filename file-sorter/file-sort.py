import os
import shutil


# Create folders based on filetypes
def folder_maker(directory):
    if os.path.exists(directory):
        print(f"The folder {directory} already exists")
        return
    else:
        os.makedirs(directory)


# images folder
directory_images = "G:\My Drive\Downloads\images"
folder_maker(directory_images)
# pdf folder
directory_pdf = "G:\My Drive\Downloads\pdf"
folder_maker(directory_pdf)
# misc folder
directory_misc = "G:\My Drive\Downloads\misc"
folder_maker(directory_misc)

# Get the list of files in the folder
file_list = os.listdir("G:\My Drive\Downloads")

# Arrange the list of files into the folders
for file_name in file_list:
    # print(file_name)
    match file_name[-4:]:
        case ".svg":
            shutil.move(f"G:\My Drive\Downloads\{file_name}", directory_images)

        case ".png":
            shutil.move(f"G:\My Drive\Downloads\{file_name}", directory_images)

        case ".jpg":
            shutil.move(f"G:\My Drive\Downloads\{file_name}", directory_images)

        case "jpeg":
            shutil.move(f"G:\My Drive\Downloads\{file_name}", directory_images)

        case ".pdf":
            shutil.move(f"G:\My Drive\Downloads\{file_name}", directory_pdf)

        case ".exe":
            shutil.move(f"G:\My Drive\Downloads\{file_name}", directory_misc)

        case _:
            print(f"{file_name} does not fit in a folder yet...")
