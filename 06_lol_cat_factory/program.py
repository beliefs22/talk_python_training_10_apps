import os
import platform
import subprocess
import cat_service


def main():
    # print header
    # get or create cat folder
    # download cats
    # display cats

    print_header()
    folder = get_or_create_folder()
    download_cats(folder)
    display_cats(folder)


def print_header():
    """
    Print header for application
    :return: No return
    """
    print("-----------------------------------")
    print("               LOL Cat Factory APP")
    print("-----------------------------------")


def get_or_create_folder():
    """
    Create folder to store cat pictures in if needed
    :return: pathway to folder
    """
    folder_name = 'cat_pictures'
    base_folder = os.path.dirname(__file__)
    directory_pathway = os.path.join(base_folder, folder_name)

    if not os.path.exists(directory_pathway) or not os.path.isdir(directory_pathway):
        print("Creating your cat folder.")
        os.mkdir(directory_pathway)

    return directory_pathway


def download_cats(folder):
    """
    Save downloaded cats to the given folder
    :param folder: folder to save images to
    :return: No Return
    """
    number_of_cats = 8
    for i in range(1, number_of_cats + 1):
        cat_image_name = "lol_cat{}.jpg".format(i)
        cat_service.get_cat(folder, cat_image_name)


def display_cats(folder):
    """
    Display cat images in platform independently
    :param folder: folder that contains images
    :return: No return
    """

    current_platform = platform.platform()

    if current_platform.find('Darwin') != -1:
        subprocess.call(['open', folder])
    elif current_platform.find('Windows') != -1:
        subprocess.call(['explorer', folder])
    elif current_platform.find('Linux') != -1:
        subprocess.call(['xdg-open', folder])
    else:
        print("Sorry we don't support your weird OS")


if __name__ == '__main__':
    main()
