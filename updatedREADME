alterEXIFpy3
Modernized EXIF GPS Metadata Modification Tool (Python 3)

Overview
alterEXIFpy3 is a fully modernized, Python 3 compatible tool for modifying or spoofing GPS EXIF metadata in JPEG images.
It is designed for:

Privacy protection

OSINT training

Photo anonymization

Testing applications that rely on GPS metadata

Batch processing of large image sets

General EXIF manipulation workflows

This version is a complete upgrade of the original alterEXIF script, featuring improved structure, safety, performance, and usability.

Key Features

Python 3 modernized codebase

Single pass EXIF processing (fewer operations)

GPS spoofing options:

Explicit latitude and longitude

City based spoofing

Randomized radius offsets

Random or user defined altitude

Batch mode for processing entire folders

EXIF backup to JSON for safe restoration

Overwrite protection to prevent accidental data loss

Robust error handling

Logging system with verbose mode

Clean, modular architecture

AI assisted modernization (fully disclosed)

Installation
Install required dependencies:

pip install piexif pillow

Clone or download this repository, then run the script directly:

python3 alterEXIFpy3.py

Usage

Single File Mode
Modify a single image:

python3 alterEXIFpy3.py single --src input.jpg --dst output.jpg

Spoof to a specific city
python3 alterEXIFpy3.py single --src input.jpg --city Chicago

Spoof within a radius (km)
python3 alterEXIFpy3.py single --src input.jpg --city Chicago --radius 2

Explicit coordinates
python3 alterEXIFpy3.py single --src input.jpg --lat 41.88 --lon -87.62

Batch Mode
Process all JPEGs in a folder:

python3 alterEXIFpy3.py folder --folder ./images --out ./modified

EXIF Backup
Before modifying any image, the script automatically saves a JSON backup of the original EXIF metadata:

image.jpg.exif.json

This allows full restoration if needed.

AI Assistance Disclosure
This project includes code sections that were modernized, optimized, or refactored with the assistance of Microsoft Copilot.
AI assistance was used to:

Improve structure and readability

Add error handling and validation

Enhance performance and memory efficiency

Add CLI and batch processing

Add realistic GPS spoofing features

Add EXIF backup functionality

All AI generated code was manually reviewed and validated.

Project Structure
alterEXIFpy3.py     - Main script
README.md           - Documentation
LICENSE             - Open Use License

Open Use License (OUL) v1.0

Copyright (c) 2026 Rick

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to use, copy, modify, merge, publish, distribute, sublicense, and or sell copies of the Software, and to permit others to do the same, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

The Software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the Software or the use or other dealings in the Software.

Users of this Software are not required to disclose modifications, derivative works, or private use. Attribution beyond the copyright notice is appreciated but not required.

This license places no restrictions on commercial use, private use, redistribution, or modification.

This license is intended to maximize freedom for developers, researchers, and end users while providing basic legal protection for the author.but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the Software or the use or other dealings in the Software.

Users of this Software are not required to disclose modifications, derivative works, or private use. Attribution beyond the copyright notice is appreciated but not required.

This license places no restrictions on commercial use, private use, redistribution, or modification.

This license is intended to maximize freedom for developers, researchers, and end users while providing basic legal protection for the author.
