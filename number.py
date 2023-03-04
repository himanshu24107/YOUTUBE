import os
directory = "NEW"

#loop through the image directory
files = os.listdir(directory)

# Initialize a counter to store the number of images
n = 0

# Iterate over the list of files and directories
for item in files:
    # Get the file extension
    _, file_extension = os.path.splitext(item)

    # Check if the file is an image file (based on its extension)
    if file_extension in ['.jpg', '.png', '.gif']:
        # Increment the image counter
        n += 1

# Print the number of images
print(f'Number of images: {n}')