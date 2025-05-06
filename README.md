# Flask Active Windows Logger

This project is a Flask web application that periodically logs the active windows on the desktop. It is designed for monitoring application usage for cybersecurity and productivity purposes.

## Project Structure

```
flask-active-windows-logger
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── logger.py
│   ├── templates
│   │   └── index.html
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   └── js
│   │       └── scripts.js
├── logs
│   └── active_windows.log
├── requirements.txt
├── run.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-active-windows-logger
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python run.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000` to access the application.

3. The application will display the logged active windows and provide options to start and stop the logging process.

## Logging

The active window information is logged in the `logs/active_windows.log` file. Each entry includes a timestamp and the name of the active window.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.