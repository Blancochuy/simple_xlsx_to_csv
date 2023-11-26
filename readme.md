# XLSX to Text Converter

## Introduction
XLSX to Text Converter is a user-friendly desktop application that allows you to convert Excel (.xlsx) files to plain text (.txt or .csv) format. It features a simple and intuitive GUI, which includes a progress bar, customizable delimiter selection, and multithreading support for faster processing.

## Features
- **Batch Conversion**: Convert multiple XLSX files at once.
- **Custom Delimiters**: Choose the delimiter for the output text files.
- **Multithreading**: Speed up conversions by leveraging multiple CPU cores.
- **Progress Tracking**: Visually track the progress of the conversion process.
- **User Preferences**: Save and remember your settings for future sessions. (WIP)

## Getting Started
To use the XLSX to Text Converter, follow these simple steps:
1. Download the executable from the `dist` folder.
2. Run the application on your Windows machine (no installation required).
3. Click the 'Browse' button to select the XLSX files you wish to convert.
4. Choose your output directory where the converted files will be saved.
5. Select your preferred delimiter and number of threads.
6. Click 'Start Conversion' and watch the progress bar fill up as files are converted.

## Requirements
- Windows 7 or later.
- No additional software installation is required.

## Building from Source
If you prefer to run the application from the source code or contribute to its development, you will need Python 3.6 or later and the following packages:
- `tkinter`
- `openpyxl`
- Install these packages using `pip install -r requirements.txt`.

To build your own executable:
```sh
pyinstaller --onefile --windowed conversion_gui.py
