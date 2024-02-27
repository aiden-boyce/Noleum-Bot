import os
from dotenv import load_dotenv
from imgurpython import ImgurClient
from shutil import copy


def get_imgur_details():
    """Get the Imgur Client ID and Imgur Client Secret"""
    dot_env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
    load_dotenv(dot_env_path)
    client_id = os.getenv("IMGUR_CLIENT_ID")
    client_secret = os.getenv("IMGUR_CLIENT_SECRET")
    return client_id, client_secret


def upload_image_to_imgur(file_path: str):
    """Upload a given image to Imgur"""
    client_id, client_secret = get_imgur_details()
    client = ImgurClient(client_id, client_secret)

    upload_response = client.upload_from_path(file_path, anon=True)

    uploaded_link = upload_response["link"]

    return uploaded_link


def move_file(source_file: str, destination_dir: str, destination_subdir: str):
    """Move a file to another folder"""
    # Create destination folder if it doesn't exist
    if destination_dir == destination_subdir:
        destination_path = os.path.join(
            os.path.dirname(__file__), "photocards", destination_dir
        )
    else:
        destination_path = os.path.join(
            os.path.dirname(__file__), "photocards", destination_dir, destination_subdir
        )

    os.makedirs(destination_path, exist_ok=True)

    copy(source_file, destination_path)


def rename_files(folder_path: str, id_number: int, category: str):
    """
    Rename files in a given folder path
    Start at a given ID number
    New File Name = 'ID_Category_OriginalName'
    """
    # Get list of files in the folder
    files = os.listdir(folder_path)

    # Open the photocards list
    photocards_list_file = os.path.join(
        os.path.dirname(__file__), "photocards_list.txt"
    )
    with open(photocards_list_file, "a") as f:
        # Iterate through files
        for file_name in files:
            # Generate new file name
            cut_off_index = file_name.index("_")
            name = file_name[:cut_off_index]
            new_file_name = f"{id_number:06d}_{category}_{name}"

            # Get file extension
            file_ext = os.path.splitext(file_name)[1]

            # Construct new file path
            new_file_path = os.path.join(folder_path, new_file_name + file_ext)

            # Rename the file
            os.rename(os.path.join(folder_path, file_name), new_file_path)

            # Upload to imgur and grab the link
            link = upload_image_to_imgur(new_file_path)

            # Save photocard to a text file
            photocard = f"{id_number:06d}, {category}, {name}, {link}.jpg"
            f.write(photocard + "\n")

            # Move the photocard to the everything directory
            destination_dir = "everything"
            destination_subdir = "everything"
            move_file(new_file_path, destination_dir, destination_subdir)

            # Move the photocard to the category/name directory
            destination_dir = f"{category}"
            destination_subdir = f"{name}"
            move_file(new_file_path, destination_dir, destination_subdir)

            # Remove the photocard from the current directory
            os.remove(new_file_path)

            id_number += 1


def main():
    id_num = int(input("What ID number would you like to start with? "))
    category = input("What category do these cards belong to? ")
    from_folder_path = input("What is the folder you are grabbing from? ")
    from_folder_path = os.path.join(os.path.dirname(__file__), from_folder_path)
    rename_files(from_folder_path, id_num, category)


if __name__ == "__main__":
    main()
