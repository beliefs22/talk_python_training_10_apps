import requests
import os
import shutil


def get_cat(folder, name):
    """
    Saves a cat image to give file as .jpg
    :param folder: folder to save image to
    :param name: name to give image file
    :return: No return
    """
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    cat_data = get_data_from_url(url)
    save_image(folder, name, cat_data)


def get_data_from_url(url):
    """
    Return raw response data from a given url
    :param url: url to give response
    :return: raw data
    """
    response = requests.get(url, stream=True)
    if response.status_code == requests.codes.ok:
        return response.raw


def save_image(folder, name, image_data):
    """
    Saves an image to the given folder with the specified name as .jpg
    :param folder: folder to save image to
    :param name: name to give the image
    :param image_data: image data to save
    :return: No return
    """
    image_file_path = os.path.join(folder, '{}.jpg'.format(name))
    with open(image_file_path, 'wb') as image_file:
        print("Saving Image {} to  {}".format(name, image_file_path))
        shutil.copyfileobj(image_data, image_file)
