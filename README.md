# Flask-Notes-App

Flask-Notes-App is a simple web application built with Flask, MySQL, and Flask-Login for user authentication. It allows users to sign up, log in, create notes, and log out.



https://github.com/googly1030/User-Authentication-in-a-Flask-App/assets/95157270/326b20f2-7028-4e13-a876-c97b86c08426



## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication (sign up, log in, log out) using Flask-Login
- MySQL database for storing user information
- Creation and display of notes for authenticated users
- Password matching and email uniqueness checks during signup
- Flash messages for user feedback

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python (3.6 or higher)
- Flask
- Flask-MySQLdb
- Flask-Login
- MySQL server

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/flask-notes-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd flask-notes-app
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure MySQL:

    - Create a MySQL database and update the `config['MYSQL_DB']` in `app.py` with your database name.

5. Run the application:

    ```bash
    python app.py
    ```

The application should be running on [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Usage

1. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
2. Sign up for a new account or log in with existing credentials.
3. Once logged in, you can create and view your notes on the '/notes' page.
4. Log out when you're done.


---

