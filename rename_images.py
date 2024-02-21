import os
import shutil
import random
import string
from extract_filenames import read_file_names, extract_image_filenames


def copy_random_files(directory, target_number):
    try:
        # Get the list of files in the directory
        files_in_directory = os.listdir(directory)
        current_number = len(files_in_directory)

        # If the current number is already greater or equal to the target, return
        if current_number >= target_number:
            print(f"The directory already has {current_number} files.")
            return

        # Copy random files until the target number is reached
        while current_number < target_number:
            # Choose a random file
            random_file = random.choice(files_in_directory)

            # Generate a unique name for the copy
            random_string = ''.join(random.choices(string.ascii_letters, k=8))
            new_filename = f"{random_string}_{random_file}"

            # Copy the file to the same directory with the new name
            shutil.copy(os.path.join(directory, random_file), os.path.join(directory, new_filename))

            current_number += 1

        print(f"{current_number} files in the directory after copying.")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Example usage
    # directory_name = "your_directory_path"
    # target_number = 10  # Replace with the desired number
    # copy_random_files(directory_name, target_number)


def rename_images(directory, filenames):
    try:
        # Get the list of files in the directory
        files_in_directory = os.listdir(directory)
        current_number = len(files_in_directory)

        # If there are fewer images than the number of filenames, copy random files
        if current_number < len(filenames):
            copy_random_files(directory, len(filenames))

        # Get the list of files in the directory again
        files_in_directory = os.listdir(directory)

        # If there are more images than the number of filenames, keep the extra images unchanged
        if current_number > len(filenames):
            files_in_directory = files_in_directory[:len(filenames)]

        # Rename the images in the directory to match the list of filenames
        for old_filename, new_filename in zip(files_in_directory, filenames):
            old_path = os.path.join(directory, old_filename)
            new_path = os.path.join(directory, new_filename)

            # Rename the file
            os.rename(old_path, new_path)

        print("Image renaming completed.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Example usage
    directory_name = "w3images"
    new_filenames = read_file_names("index.html")
    rename_images(directory_name, new_filenames)
