import os
import shutil


# Create folders based on filetypes
def folder_maker(directory):
    if os.path.exists(directory):
        print(f"The folder {directory} already exists")
        return
    else:
        os.makedirs(directory)


chosen_folder = input("Paste the folder you want to clean here ( full path ):")

# images folder
directory_images = f"{chosen_folder}\images"
folder_maker(directory_images)
# pdf folder
directory_pdf = f"{chosen_folder}\pdf"
folder_maker(directory_pdf)
# misc folder
directory_misc = f"{chosen_folder}\misc"
folder_maker(directory_misc)

# Get the list of files in the folder
file_list = os.listdir(f"{chosen_folder}")

# Arrange the list of files into the folders
for file_name in file_list:
    # print(file_name)
    match file_name[-4:]:
        case ".svg":
            shutil.move(f"{chosen_folder}\{file_name}", directory_images)

        case ".png":
            shutil.move(f"{chosen_folder}\{file_name}", directory_images)

        case ".jpg":
            shutil.move(f"{chosen_folder}\{file_name}", directory_images)

        case "jpeg":
            shutil.move(f"{chosen_folder}\{file_name}", directory_images)

        case ".pdf":
            shutil.move(f"{chosen_folder}\{file_name}", directory_pdf)

        case ".exe":
            shutil.move(f"{chosen_folder}\{file_name}", directory_misc)

        case _:
            print(f"{file_name} does not fit in a folder yet...")
