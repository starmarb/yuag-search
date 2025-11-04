# Yale University Art Gallery Search Engine

**Teammates:** Sammi Kwon, Thomas Walter

## Overview
This project was completed for CPSC 419: Full Stack Web Programming in Fall 2023. 
It's a web application that allows users to search and explore the Yale University Art Gallery's collection database.

**[Try out the live app here!](https://yuag-search.onrender.com)** *(Hosted on free tier - initial load may take 30-60 seconds)*

## Features
- **Advanced Search**: Filter artworks by Label, Classifier, Agent, and Date
- **Table View**: Browse search results in an organized, sortable table
- **Detailed Object Pages**: View comprehensive information about each artwork including:
  - Accession number, date, place, and department
  - Production details and artist information
  - Classifications and references
  - High-resolution images (when available)
- **Direct Links**: Share specific artworks via URL

## Tech Stack
- **Backend**: Python, Flask
- **Frontend**: HTML, Jinja2 templates, JavaScript
- **Database**: SQLite (184 MB Yale University Art Gallery collection data)
- **Deployment**: Render (free tier)
- **Image CDN**: Yale University Art Gallery media server

## Project Structure
```
├── luxapp.py           # Main Flask application
├── luxinfo.py          # Database queries for search functionality
├── luxdetails.py       # Database queries for object details
├── templates/          # HTML templates
│   ├── index.html
│   ├── object_details.html
│   ├── searchresults.html
│   └── error.html
├── static/             # Static assets
│   └── main.js
└── requirements.txt    # Python dependencies
```

## Local Setup
1. **Clone the repository**
```bash
   git clone https://github.com/starmarb/yuag-search.git
   cd yuag-search
```

2. **Install dependencies**
```bash
   pip install -r requirements.txt
```

3. **Add the database**
   - Download `lux.sqlite` (Please reach out to Sammi Kwon for access to file, as it has limitations on access).
   - Place it in the root directory

4. **Run the application**
```bash
   python luxapp.py
```
   Visit `http://localhost:5000` in your browser

## Database
The application uses a SQLite database (`lux.sqlite`, 184.4 MB) containing data about objects in the Yale University Art Gallery collection. The database includes:
- Object metadata (labels, dates, departments, places)
- Artist/agent information (names, nationalities, timespans)
- Classifications and references
- Production details

*Note: The database file is not tracked in git due to its size.*

## Deployment Notes
- Database is downloaded from Dropbox during the build process on Render
- Free tier hosting may result in cold starts (30-60 second initial load)
- Images are served directly from Yale's media CDN

## Contributors
**Sammi Kwon**: Base website setup, endpoint requirements, error handling, POST to GET method conversion, URL query handling, pylint compliance, object detail page formatting, SQL query optimization

**Thomas Walter**: Frontend-backend integration, HTML templates, basic luxapp.py functionality, image URL fetching with timeout handling

## Acknowledgments
- Yale University Art Gallery for providing the collection database
- CPSC 419 course staff for assignment guidance and specifications


*This project was created as an educational assignment and is not affiliated with Yale University Art Gallery.*
