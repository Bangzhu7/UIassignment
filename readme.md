# Beauty Salon Web Application

## Overview

This project is a multi-page web application for a beauty salon, built using Flet. The app provides an intuitive and user-friendly interface for visitors to explore services, contact information, booking options, and client details.

## Features

- Responsive, single-page application navigation
- Multiple pages:
  - Home Page
  - About Page
  - Services Page
  - Contact Page
  - Booking Calendar
  - Client Details

## Prerequisites

- Python 3.8+
- Flet library

## Installation

### 1. Clone the Repository

```bash
git clone https://your-repository-url.git
cd beauty-salon-app
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install flet
```

### 4. Run the Application

```bash
python main.py
```

## Project Structure

```
beauty-salon-app/
│
├── main.py           # Main application entry point
├── home.py           # Home page component
├── about.py          # About page component
├── service.py        # Services page component
├── contact.py        # Contact page component
├── Booking_calendar.py # Booking calendar page
├── clientdetails.py  # Client details page
└── README.md         # Project documentation
```

## Navigation

The application uses Flet's routing system with a consistent navigation bar across pages:

- Home
- About
- Service
- Contact
- Book Calendar
- Client Details

## Customization

- Modify page content in respective page files
- Adjust styling in the main application file
- Customize navigation bar in `make_nav_bar()` function

## Technologies Used

- Python
- Flet Framework
