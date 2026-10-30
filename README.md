# Country Explorer

A command-line Python application that retrieves country information from the REST Countries API.

## Features

- **Country Information:** View a country's official name, capital, region, population, area, currencies, and languages.
- **Country Comparison:** Compare two countries by population and area.
- **African Countries:** List countries in Africa.
- **Regional Search:** List countries by region.
- **Interactive Menu:** Navigate the application through a simple CLI menu.

## Requirements

- Python 3.10+
- A REST Countries API key
- `requests`
- `python-dotenv` (for loading environment variables from `.env`)

## Setup

1. Clone the repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   cd YOUR_PROJECT_DIRECTORY
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   On Windows:

   ```bash
   .venv\Scripts\activate
   ```

   On Linux/macOS:

   ```bash
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   python -m pip install requests python-dotenv
   ```

4. Create a `.env` file and add your API key:

   ```text
   REST_COUNTRIES_API_KEY=your_api_key
   ```

5. Run the application:

   ```bash
   python country_explorer.py
   ```

   Replace `country_explorer.py` with your actual Python filename if different.

## Technologies

- Python
- Requests
- REST Countries API
- JSON

## Future Improvements

- Add automated tests.
- Improve API error handling and input validation.
- Support pagination and more country statistics.
- Build a web version using Flask or Django.

## Security

Never commit API keys or other secrets to version control. Keep your `.env` file private.
