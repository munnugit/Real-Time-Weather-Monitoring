# Real-Time-Weather-Monitoring

 Overview

The Real-Time Weather Monitoring application is a Flask-based web application that provides users with up-to-date weather information for multiple cities. It displays current weather conditions, daily summaries, and allows users to set alerts based on temperature and weather conditions.

 Features

- Current weather conditions for selected cities
- Daily weather summary with average, maximum, and minimum temperatures
- Ability to set alert thresholds for temperature and weather conditions
- Real-time data updates every 5 minutes
- Responsive design using Bootstrap for mobile compatibility

Technologies Used

- Python: Backend logic with Flask framework
-Flask: Web framework for building the application
- Bootstrap: Frontend framework for responsive design
- JavaScript/jQuery: For real-time data fetching and dynamic updates
- OpenWeatherMap API: For fetching weather data (API key required)


# Real-Time Weather Monitoring

 Overview

The Real-Time Weather Monitoring application is a Flask-based web application that provides users with up-to-date weather information for multiple cities. It displays current weather conditions, daily summaries, and allows users to set alerts based on temperature and weather conditions.

 Features

- Current weather conditions for selected cities
- Daily weather summary with average, maximum, and minimum temperatures
- Ability to set alert thresholds for temperature and weather conditions
- Real-time data updates every 5 minutes
- Responsive design using Bootstrap for mobile compatibility

 Technologies Used

- Python: Backend logic with Flask framework
- Flask: Web framework for building the application
- Bootstrap: Frontend framework for responsive design
- JavaScript/jQuery: For real-time data fetching and dynamic updates
- OpenWeatherMap API: For fetching weather data (API key required)

File Structure

/your_project_folder
│
├── /app                  # Main application folder
│   ├── __init__.py      # Application factory
│   ├── routes.py        # Application routes
│   ├── models.py        # Database models (if using a database)
│   ├── forms.py         # Forms for user input (Flask-WTF)
│   ├── /static          # Static files (CSS, JavaScript, images)
│   │   ├── /css
│   │   │   └── styles.css
│   │   ├── /js
│   │   │   └── scripts.js
│   │   └── /images      # Images (if any)
│   └── /templates       # HTML templates
│       └── index.html   # Main template
│
├── /venv                # Virtual environment
│
├── requirements.txt     # List of dependencies
│
├── config.py            # Configuration settings (if needed)
│
└── run.py               # Entry point to run the application


## Installation

1. Clone this repository:
`bash
   git clone https://github.com/yourusername/real-time-weather-monitoring.git
   cd real-time-weather-monitoring
  

2. Set up a virtual environment:
  bash
   python -m venv venv
 

3. Activate the virtual environment:
   - On Windows:
   bash
     venv\Scripts\activate

   - On macOS/Linux:
  bash
     source venv/bin/activate
  

4. Install the required packages:
bash
   pip install -r requirements.txt


5. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api) and add it to your configuration.

6. Run the application:
 bash
   python run.py


7. Open your web browser and navigate to `http://127.0.0.1:5000`.

 Usage

- **Current Weather**: View the current weather conditions for the listed cities.
- **Daily Summary**: Check the daily weather summary for average, maximum, and minimum temperatures.
- **Set Alerts**: Enter temperature and weather condition thresholds to receive alerts.










