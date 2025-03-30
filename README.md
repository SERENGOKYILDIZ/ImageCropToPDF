# Image Cropper & PDF Converter

## Overview
This is a simple yet effective GUI-based tool that allows users to crop images from a selected folder and convert them into a PDF. The application is built using Python and Tkinter and includes a progress bar for real-time feedback during processing.

## Features
- **Select Source Folder:** Choose the directory containing images to be cropped.
- **Set Crop Coordinates:** Specify cropping coordinates (x1, y1, x2, y2) for batch processing.
- **Crop Images:** Process all images in the source folder and save cropped versions to the target folder.
- **Convert to PDF:** Merge the cropped images into a single PDF file.
- **Progress Bar:** Visual feedback during cropping and PDF conversion.
- **User-Friendly GUI:** Aesthetic and easy-to-use interface.

## Installation
Ensure you have Python installed on your system. Install required dependencies using:
```sh
pip install pillow
```

## Usage
1. Run the script:
   ```sh
   python main.py
   ```
2. Select the source folder containing images.
3. Set the target folder for cropped images.
4. Define the cropping coordinates.
5. Click "Crop Images" to process the images.
6. Select a target folder for the PDF and click "Convert to PDF" to generate the file.

## Dependencies
- Python 3.x
- Tkinter (built-in with Python)
- PIL (Pillow library for image processing)

## Author
Created by **SERENGOKYILDIZ**.

## License
This project is open-source and free to use for any purpose.

