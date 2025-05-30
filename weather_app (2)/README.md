# 🌦️ Weather App

A simple Flask web application that allows users to search for a city and view its current weather and upcoming daily forecast using the Open-Meteo API.

## 🚀 Features

- Search for any city worldwide
- Get current weather conditions
- View 7-day forecast (temperature, precipitation probability, and weather codes)
- Keeps track of 5 most recent city searches

## 🧰 Technologies Used

- Python 3
- Flask
- HTML/CSS (with Bootstrap)
- JavaScript (with Fetch API)
- Open-Meteo API (Weather and Geocoding)

---

## 📥 Installation

1. **Download or Clone the Repository**

   _Or download the ZIP file and extract it to your local machine._

2. **Install Python Dependencies**

   Make sure you have Python 3 installed. Then install required packages:

   ```bash
   pip install flask requests
   ```

---

## 🏁 Running the App

1. Open your terminal or command prompt inside the project folder.
2. Run the Flask app:

   ```bash
   python app.py
   ```

3. Open your browser and visit:

   ```
   http://127.0.0.1:5000/
   ```

---

## 📂 Project Structure

```
weather_app/
├── app.py              # Main Flask application
├── templates/
│   └── index.html      # Main HTML UI
├── static/
│   └── (optional)      # Any static files (CSS/JS/images)
├── README.md           # Project instructions (this file)
```

---

## 🌐 API Source

- [Open-Meteo Weather API](https://open-meteo.com/en/docs)
- [Open-Meteo Geocoding API](https://open-meteo.com/en/docs/geocoding-api)

---

## 📎 Notes

- The app runs locally and does not require an API key.
- Make sure you're connected to the internet to access the weather API.
- Works best in modern browsers.

---

## 🛠️ License

This project is open source and free to use for educational purposes.