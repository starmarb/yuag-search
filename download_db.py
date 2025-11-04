import requests
import sys

def download_file_from_google_drive(file_id, destination):
    URL = "https://docs.google.com/uc?export=download"
    
    session = requests.Session()
    response = session.get(URL, params={'id': file_id}, stream=True)
    
    # Handle large file confirmation
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            params = {'id': file_id, 'confirm': value}
            response = session.get(URL, params=params, stream=True)
    
    with open(destination, "wb") as f:
        for chunk in response.iter_content(chunk_size=32768):
            if chunk:
                f.write(chunk)
    
    print(f"Downloaded {destination}")

if __name__ == "__main__":
    file_id = "1Xbo9Rbyi3YU0UGk9AVk1hUYTX7nTyZzo"  # Replace with your Google Drive file ID
    download_file_from_google_drive(file_id, "lux.sqlite")
