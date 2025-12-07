1.MTF Analysis of an N-BK7 Biconvex Lens
This project analyzes the Modulation Transfer Function (MTF) of a standard N-BK7 biconvex singlet lens.
The goal is to detect where the lens loses image quality due to spherical aberration.
The script reads MTF data exported from Zemax, cleans it, and automatically finds where the contrast drops below 10%, which is considered the “failure region” for the lens.

2. What the Project Does
* Reads FFT MTF data from a Zemax text file
* Extracts Frequency, Sagittal, and Tangential MTF
* Converts the raw text into usable numeric data
* Finds where the MTF is below 0.1 (10% contrast)
* Plots the MTF curves
* Highlights the failing region
This helps show how spherical aberration reduces image quality at higher spatial frequencies.

3.Folder Structure
/Zemax_MTF_Analyser
     /---Src
         /---abberation_analyser.py
         /---MTF-Biconvex_data.txt
     /---Images
??? README.md

4.How to Run
1. Place your Zemax MTF text file inside the data/ folder
2. Install the dependencies:
pip install -r requirements.txt
3. Run the main script:
python src/main.py


5. Output
The program prints:
Sagittal failure: start ? end (cycles/mm)
Tangential failure: start ? end (cycles/mm)
And shows a plot of:
* Sagittal MTF
* Tangential MTF
* 10% threshold line
* Marked failure region

6.Required Files from Zemax
Please export:
* FFT MTF text file (saved as MTF_Biconvex_data.txt)
* (Optional) Ray trace image
* (Optional) Lens prescription screenshot

7.Why This Project Is Useful
This project shows:
* basic Zemax data extraction
* optical performance evaluation
* Python data processing
* plotting and visualization
It’s simple but demonstrates real optical engineering analysis.

