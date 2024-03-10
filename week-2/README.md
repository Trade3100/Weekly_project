# QR Code Utility

A simple Python script that provides utility functions for working with QR codes. The script allows users to read QR codes from an image file or a webcam, as well as generate QR codes for a given input.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [How to Use](#how-to-use)
- [Dependencies](#dependencies)
- [License](#license)

## Introduction

This Python script serves as a utility for interacting with QR codes. It offers three main functionalities:

1. **Read from file:** Decode QR codes from an image file.
2. **Read from Camera:** Use a webcam to scan and decode QR codes in real-time.
3. **Make a QR code:** Generate a QR code for a given input and display it.

## Features

- Read QR codes from image files.
- Scan and decode QR codes using a webcam.
- Generate and display QR codes for user-provided data.

## How to Use

1. Run the script and choose one of the following actions:
   - (1) Read from file: Enter the file name when prompted.
   - (2) Read from Camera: Use a webcam to scan QR codes in real-time.
   - (3) Make a QR code: Enter the output file name and data when prompted.

2. Follow on-screen instructions for each action.

## Dependencies

The script relies on the following external libraries:

- [OpenCV](https://pypi.org/project/opencv-python/): For image processing and webcam access.
- [qrcode](https://pypi.org/project/qrcode/): For generating QR codes.
- [pyzbar](https://pypi.org/project/pyzbar/): For decoding QR codes.
- [webbrowser](https://docs.python.org/3/library/webbrowser.html): For opening web links.

Install dependencies using:

```bash
pip install opencv-python qrcode[pil] pyzbar
