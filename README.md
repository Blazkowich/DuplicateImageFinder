# Duplicate Image Finder

## Overview

This project is a Python-based tool that detects duplicate images in a given folder using both visual similarity and text extraction. It utilizes OpenCV for image processing and Tesseract OCR for text recognition.

## Features

- Compares images based on perceptual hash similarity.
- Extracts and compares text content from images using Tesseract OCR.
- Detects duplicate images efficiently.

## Requirements

- Python 3.7 or higher, in current project used Python 3.13
- Tesseract OCR (must be installed separately)
- Required Python packages (listed in `requirements.txt`)

## Installation

1. Clone this repository:

   ```sh
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Install Tesseract OCR:
   - **Windows:** Download and install from [Tesseract's official site](https://github.com/UB-Mannheim/tesseract/wiki).
   - **Linux/macOS:** Install via package manager:

     ```sh
     sudo apt install tesseract-ocr  # Debian/Ubuntu
     brew install tesseract          # macOS
     ```

## Usage

1. Update `main()` in `find_duplicates.py` with:

   ```python
   folder_path = "path/to/your/images"
   tesseract_path = "path/to/tesseract"
   ```

2. Run the script:

   ```sh
   python find_duplicates.py
   ```

3. The script will analyze images and print detected duplicates.

## Dependencies

See `requirements.txt` for required packages.

## Author

Otar Iluridze
