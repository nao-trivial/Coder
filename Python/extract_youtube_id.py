import re

def extract_youtube_id(url):
    # Pattern for full YouTube URL
    full_url_pattern = r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]+)'
    # Pattern for shortened YouTube URL
    short_url_pattern = r'(?:https?://)?youtu\.be/([a-zA-Z0-9_-]+)'

    # Try to match the full URL pattern
    match = re.search(full_url_pattern, url)
    if match:
        return match.group(1)
    
    # Try to match the shortened URL pattern
    match = re.search(short_url_pattern, url)
    if match:
        return match.group(1)
    
    return None

# Sample input
url1 = input()

# Extract and print video IDs
print(extract_youtube_id(url1))  # Output: RRW2aUSw5vU
