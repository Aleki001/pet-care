# Pet Adoption Web App

Welcome to the Pet Adoption Web App! This web application allows users to browse available pets for adoption, read blogs related to pet care and adoption, and view a gallery of pets. This README provides detailed instructions for setting up and running the application.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- List available pets for adoption
- Detailed pet profiles
- Blog section with posts about pet care and adoption
- Gallery of pet images
- User authentication (sign up, log in, log out)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python (version 3.8 or higher)
- Django (version 3.2 or higher)
- pip (Python package installer)
- Git (optional, for version control)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Aleki001/pet-care.git
   cd pet-care
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Configure the database:**

   By default, the project uses SQLite. If you wish to use a different database (e.g., PostgreSQL), update the `DATABASES` setting in `pet_adoption/settings.py`.

## Database Setup

1. **Apply the database migrations:**

   ```bash
   python manage.py migrate
   ```

2. **Create a superuser to access the admin panel:**

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create your admin user.

## Running the Application

1. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

2. Open your web browser and visit `http://127.0.0.1:8000` to access the application.

## Usage

- **Admin Panel:** Visit `http://127.0.0.1:8000/admin` to log in with your superuser credentials and manage the content.
- **Pet Listings:** Browse available pets for adoption on the homepage.
- **Blog:** Read articles related to pet care and adoption in the blog section.
- **Gallery:** View images of pets in the gallery section.
- **Authentication:** Sign up, log in, and log out using the links provided in the navigation bar.

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Thank you for using the Pet Adoption Web App! If you have any questions or issues, please feel free to contact us or open an issue on GitHub.