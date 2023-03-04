from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up the YouTube API client
api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "secret.json"

# Get the authenticated service object
service = build(api_service_name, api_version, credentials=creds)

# Set up the video metadata
video_title = "My Video"
video_description = "This is a description of my video."
video_tags = ["tag1", "tag2"]
video_category = "22"  # See https://developers.google.com/youtube/v3/docs/videoCategories/list

# Set up the file to be uploaded
video_file = "output.mp4"

# Create the request to upload the video
request = service.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": video_title,
            "description": video_description,
            "tags": video_tags,
            "categoryId": video_category
        },
        "status": {
            "privacyStatus": "private"
        }
    },
    media_body=video_file
)

# Execute the request and print the response
response = request.execute()
print(response)
