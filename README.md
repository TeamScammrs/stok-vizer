# Investment Chatbot README

## Introduction

This is a **Gemini-powered investment chatbot** designed to assist users with any queries related to investing. It provides real-time financial data, tracks chat history, and offers a **company analysis dashboard** for in-depth insights.

## Features

- **Multi-theme chatbot**: Choose from different themes for a personalized experience.
- **Real-time financial data**: Fetch the latest stock and investment information.
- **Chat history tracking**: Maintains consistency and remembers past interactions.
- **Company analysis dashboard**:
  - Enter a **ticker symbol** to fetch relevant data instantly.
  - View performance charts and key financial metrics.
  - Get the latest news about the company.
- **Investment advisory**: Explains financial jargon and provides insights based on user queries.
- **Persistent chatbot on the dashboard**: Allows users to continue conversations with previous data in context.

## Installation

1. Clone this repository:

   ```sh
   git clone https://github.com/TeamScammrs/stok-vizer
   ```

2. Navigate to the project directory:

   ```sh
   cd chat
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Set up API keys:

   - Example `.env` file:
     ```
     GEMINI_API_KEY=your_gemini_api_key
     ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
     ```

5. **Django Setup**:
   - This repository contains only the necessary files for a Django application.
   - You need to set up a Django project and create an app where these files will be placed.
   - Run the following command to start a new Django project:
     ```sh
     django-admin startproject myproject
     ```
   - Navigate into the project directory and create an app:
     ```sh
     cd myproject
     python manage.py startapp chat
     ```
   - Place the provided files (`chatbot.py`, `views.py`, `chat.html`, `stock.html`) inside the appropriate directories of your Django app.
   - Configure `settings.py` to include the new app.

6. Run the application:

   ```sh
   python manage.py runserver
   ```

## Usage

- Open the chatbot interface and enter investment-related queries.
- Use the company analysis dashboard by entering a **ticker symbol**.
- Explore financial insights, stock performance, and company news.

## Files Overview

- **chatbot.py**: Handles chatbot interactions, fetches financial data using Gemini 2.0 Flash and Alpha Vantage APIs.
- **views.py**: Manages frontend interactions and dashboard functionalities.
- **chat.html**: Frontend template for the chatbot interface.
- **stock.html**: Dashboard UI for company analysis.

## Future Enhancements

- **Enhanced AI responses** with deeper financial insights.
- **More data sources** for a wider range of investments.
- **Personalized recommendations** based on user preferences.
