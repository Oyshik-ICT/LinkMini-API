# URL Shortener API

A Django REST Framework based URL shortening service that allows you to create shortened URLs, manage them, and redirect to original URLs.

## Features

- Create shortened URLs from long URLs
- Retrieve, update, and delete shortened URLs
- Redirect from short URLs to original URLs
- Rate limiting for both authenticated and anonymous users
- API documentation using Swagger/ReDoc
- URL validation
- Database indexing for better performance

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Oyshik-ICT/LinkMini-API.git
cd LinkMini-API
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- On Windows:
```bash
venv\Scripts\activate
```
- On macOS/Linux:
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run database migrations:
```bash
python manage.py migrate
```

6. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

7. Start the development server:
```bash
python manage.py runserver
```

The server will start at `http://localhost:8000`

## API Endpoints

### 1. Create Short URL
- **URL:** `/create-url/`
- **Method:** POST
- **Request Body:**
```json
{
    "long_url": "https://example.com/very/long/url"
}
```
- **Response:**
```json
{
    "id": 1,
    "short_url": "myurl/abc12345",
    "long_url": "https://example.com/very/long/url",
    "created_at": "2024-02-14T12:00:00Z",
    "updated_at": "2024-02-14"
}
```

### 2. Manage Short URL
- **URL:** `/shorten/<short_url>`
- **Methods:** GET, PUT, DELETE
- **Description:** Retrieve, update, or delete a shortened URL

### 3. Redirect to Original URL
- **URL:** `/original/<short_url>`
- **Method:** GET
- **Description:** Redirects to the original long URL

## API Documentation with Swagger

The API documentation is available through Swagger UI and ReDoc. To access it:

1. Start the development server
2. Visit one of these URLs:
   - Swagger UI: `http://localhost:8000/api/schema/swagger-ui/`
   - ReDoc: `http://localhost:8000/api/schema/redoc/`

Through Swagger UI, you can:
- View all available endpoints
- Test the API directly from the browser
- See request/response schemas
- Download the OpenAPI specification

## Rate Limiting

The API implements rate limiting for both authenticated and anonymous users. Configure the rates in your Django settings:

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '100/day',    # Modify as needed
        'anon': '100/day',     # Modify as needed
    }
}
```


