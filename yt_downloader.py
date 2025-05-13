import sys
from yt_dlp import YoutubeDL

def download_video(url, format_code):
    ydl_opts = {
        'format': format_code,
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'noplaylist': True
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            print(f"❌ Download failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python yt_downloader.py <url> [format_code]")
        sys.exit(1)

    url = sys.argv[1]
    format_code = sys.argv[2] if len(sys.argv) > 2 else "bestvideo+bestaudio"
    download_video(url, format_code)
