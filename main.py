import yt_dlp

def download_video(url, download_type="video"):
    # Options for downloading
    if download_type == "video":
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  # Select the best MP4 video and audio
            'merge_output_format': 'mp4',  # Merge video and audio into an MP4 container
            'outtmpl': '%(title)s.%(ext)s',  # Save with video title as the filename
        }
    elif download_type == "audio":
        ydl_opts = {
            'format': 'bestaudio/best',  # Downloads best audio format
            'outtmpl': '%(title)s.%(ext)s',  # Saves with title as filename
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',  # Converts to mp3
                'preferredquality': '192',
            }],
        }
    else:
        raise ValueError("Invalid download type. Use 'video' or 'audio'.")

    # Download using yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage
video_url = input("Enter Link: ")
download_type = input("(video / audio): ").lower()  # Change to "video" for video download
download_video(video_url, download_type)
print("Download completed!")