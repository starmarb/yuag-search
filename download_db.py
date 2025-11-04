import requests

def download_from_gdrive(file_id, destination):
    print(f"Downloading file ID: {file_id}")
    
    # First request to get confirmation token
    URL = "https://drive.google.com/uc?export=download"
    session = requests.Session()
    
    response = session.get(URL, params={'id': file_id}, stream=True)
    token = None
    
    # Look for confirmation token in response
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            token = value
            break
    
    # If we got a token, make second request with it
    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)
    
    # Check if we got HTML error page
    content_type = response.headers.get('content-type', '')
    if 'text/html' in content_type:
        print("ERROR: Got HTML instead of file. Trying alternative method...")
        # Try alternative download URL
        URL2 = f"https://drive.google.com/uc?id={file_id}&export=download&confirm=t"
        response = session.get(URL2, stream=True)
    
    # Save the file
    print("Saving file...")
    with open(destination, "wb") as f:
        for chunk in response.iter_content(chunk_size=32768):
            if chunk:
                f.write(chunk)
    
    print(f"Downloaded {destination} - Success!")

if __name__ == "__main__":
    file_id = "1Xbo9Rbyi3YU0UGk9AVk1hUYTX7nTyZzo"
    download_from_gdrive(file_id, "lux.sqlite")