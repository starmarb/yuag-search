# Yale University Art Gallery Search Engine
Try out the live demo **[here](https://starmarb.github.io/yuag-search-demo/)

**Teammates:** Sammi Kwon, Thomas Walter

## Overview
This project was completed for CPSC 419: Full Stack Web Programming in Fall 2023. 
It's a web application that allows users to search and explore the Yale University Art Gallery's collection database.

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

## Database
The application uses a SQLite database (`lux.sqlite`, 184.4 MB) containing data about objects in the Yale University Art Gallery collection. The database includes:
- Object metadata (labels, dates, departments, places)
- Artist/agent information (names, nationalities, timespans)
- Classifications and references
- Production details

*Note: The database file is not tracked in git due to its size.*

## Contributors
**Sammi Kwon**: Base website setup, endpoint requirements, error handling, POST to GET method conversion, URL query handling, pylint compliance, object detail page formatting, SQL query optimization

**Thomas Walter**: Frontend-backend integration, HTML templates, basic luxapp.py functionality, image URL fetching with timeout handling

## Acknowledgments
- Yale University Art Gallery for providing the collection database
- CPSC 419 course staff for assignment guidance and specifications


*This project was created as an educational assignment and is not affiliated with Yale University Art Gallery.*
