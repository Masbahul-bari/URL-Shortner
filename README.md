# URL-Shortner

## Overview

This URL Shortener is a simple and efficient tool that allows you to convert long URLs into shorter, more manageable links. Built using Python and Tkinter for the graphical interface, it leverages the TinyURL service to generate shortened links.

## Features

- **Easy-to-Use Interface**: Paste the long URL into the input field and click "Shorten URL."
- **Clipboard Copy**: Quickly copy the shortened URL to your clipboard for easy sharing.
- **Error Handling**: Provides alerts for invalid URLs or other issues.

## How It Works

1. The user enters a long URL into the input field.
2. The application uses the `pyshorteners` library to connect to the TinyURL API.
3. The TinyURL service returns a shortened version of the URL.
4. The shortened URL is displayed in the application, and the user can copy it to the clipboard with a single click.

## How to Use

1. **Install Dependencies**:

   - Install Python 3.x on your machine.
   - Install the required Python library using pip:
     ```bash
     pip install pyshorteners
     ```

2. **Run the Application**:

   - Save the Python script (`url_shortener_gui.py`) to your computer.
   - Execute the script:
     ```bash
     python url_shortener_gui.py
     ```

3. **Shorten URLs**:

   - Paste a long URL into the input field.
   - Click the "Shorten URL" button.
   - Copy the generated short URL by clicking "Copy to Clipboard."

## Dependencies

- Python 3.x
- `pyshorteners`
- `Tkinter` (comes pre-installed with Python)

## Example Usage

1. Enter: `https://exam.com`
2. Shortened Output: `https://tinyurl.com/exam`

## Troubleshooting

- If you see an error related to missing libraries, ensure you have installed `pyshorteners`.
- Make sure you have an active internet connection as the application relies on the TinyURL API.

## License

This project is open-source and available for personal or educational use.

