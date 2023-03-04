from moviepy.editor import VideoFileClip, ImageClip, AudioFileClip, CompositeVideoClip
import random
import os


# Function to add the overlay and music to the video
def add_overlay_and_music(image_path, sound_dir, video_dir, output_dir):
  # Get a list of all the videos in the video directory
  videos = os.listdir(video_dir)
  
  # Choose a random video from the list
  video_path = os.path.join(video_dir, random.choice(videos))
  
  # Load the video
  video = VideoFileClip(video_path)
  
  # Load the image
  image = ImageClip(image_path)

  video_h = video.size
  
  # Resize the image to fit the video
  image = image.resize(video_h)
  
  # Get a list of all the sounds in the sound directory
  sounds = os.listdir(sound_dir)
  
  # Choose a random sound from the list
  sound_path = os.path.join(sound_dir, random.choice(sounds))
  
  # Load the sound
  sound = AudioFileClip(sound_path)
  
  # Trim the sound to 4 seconds
  sound = sound.subclip(0, 4)
  
  # Add the image overlay to the video for duration 5 sec
  video = video.set_pos((0,0)).set_duration(4).set_audio(sound)
  video = video.add_mask()
  
  # Set the position of the image to the center of the video
  image = image.set_pos((video.w/2 - image.w/2, video.h/2 - image.h/2))
  
  # Create the composite video with the video behind the image
  final_clip = CompositeVideoClip([video, image])
  
  # Trim the video to 5 seconds
  final_clip = final_clip.subclip(0, 4)
  
  # Create the output directory if it does not exist
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)
  
  # Save the video to the output directory with a modified name
  final_clip.write_videofile(os.path.join(output_dir, f"{os.path.basename(image_path).split('.')[0]}_output.mp4"), threads = 4, fps=24)

# Test the function with a sample image, sound directory,


# Set the directory containing the images
directory = "Fun"

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


# Get a list of all files in the directory
files = os.listdir(directory)

# Iterate through the list of files
for u, file in enumerate(files):
  # Get the file extension
  extension = os.path.splitext(file)[1]
  # Only rename image files (e.g. jpeg, png, gif)
  if extension in [".jpg", ".jpeg", ".png", ".gif"]:
    # Build the new filename
    new_filename = "image" + str(u+1) + extension
    



for i in range (441,n+1,1):
    image_path = f'{directory}/image ({i}).png'
    add_overlay_and_music(image_path, "sounds", "input","output")


