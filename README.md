# Image Generation API

## Overview

This Django application provides an API for generating images based on textual prompts using the Stability AI service. It includes endpoints for creating new images and listing all generated images.

## Requirements

- Python 3.6+
- Django 3.0+
- Django REST framework
- Stability AI service integration (custom service)

## Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/CodeWithNeha/ImageGeneration.git

   ```

2. **Create Virtual Env:**

   ```sh
   python3 -m venv venv
   source venv/bin/activate

   ```

3. **Install dependencies:**

   ```sh
   pip install -r requirements.txt

   ```

4. **Set up the database:**

   ```sh
   python manage.py migrate

   ```

5. **Run the server:**
   ```sh
   python manage.py runserver
   celery -A ImageGeneration worker -l INFO -P gevent
   ```

## API Endpoints

1. **Generate Image**

- URL: /generate_images/
- Method: POST
- Description: Generates an image based on the provided prompt.
- Request Body:

{
"prompt": "A beautiful sunset over the mountains."
}

- Response:
  {
  "message": "Image generated successfully."
  }

2. **List All Generated Images**

- URL: /generate_images/
- Method: GET
- Description: Retrieves a list of all generated images.

## File Descriptions

- views.py: Contains the ImageGeneration viewset for handling image generation and listing.
- models.py: Defines the GeneratedImage model.
- serializers.py: Contains the GeneratedImageSerializer for serializing the GeneratedImage model.
- urls.py: Configures the URL routing for the API endpoints.
- utils/constants.py: Contains application-wide constants.
- stability/services.py: Contains the StabilityAiService class for interacting with the Stability AI service.
- stability/generators/image_generator.py: Contains the ImageGenerator class for image generation.
