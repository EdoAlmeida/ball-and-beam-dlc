# Ball and Beam Video Analysis using DeepLabCut

This repository contains the Jupyter notebooks and Python source code used for extracting the angular position and angular velocity of a Ball and Beam system from video recordings using DeepLabCut and Python-based data processing tools.

The workflow combines markerless pose estimation with geometric reconstruction to estimate the beam angle from tracked keypoints.

To keep the repository lightweight, only the notebooks and source scripts are included. Raw videos and large intermediate files generated during processing are intentionally excluded.

## Project Structure

The repository is organized as follows:

repository/
│
├── notebooks/  
├── src/
└── README.md

- `notebooks` – Jupyter notebooks used for video preprocessing, DeepLabCut analysis, and signal processing.
- `src` – Python scripts containing helper functions for data processing and analysis.

The repository intentionally contains only notebooks and source scripts. Raw videos and large intermediate files are not included due to GitHub size limitations.  

## Expected Directory Structure

Before running the notebooks, the project directory should follow the structure below:
DLC_projects4/
│
├── notebooks/
│   Jupyter notebooks used for preprocessing, DeepLabCut analysis,
│   and signal processing.
│
├── src/
│   Python helper scripts used by the notebooks.
│
├── videos/
│   Raw experimental videos used as input for the analysis.
│   These files are not included in the repository.
│
├── results/
│   Generated outputs such as processed data and figures.
│
└── README.md

The notebooks assume this directory structure when loading input videos and saving results.

Users should place the experimental videos inside the `videos` directory before running the analysis notebooks. Processed data and figures generated during execution will be stored in the `results` directory.

## Method Overview

The general processing pipeline used in this project is:

Video recording → Video format conversion (.mov → .mp4) → DeepLabCut pose estimation → Extraction of keypoint coordinates (x, y) → Geometric reconstruction of beam angle (θ) → Signal filtering (Savitzky–Golay filter) → Angular velocity estimation (ω)

This approach allows the estimation of the beam motion directly from video recordings without attaching physical sensors to the system.

## Video Conversion

Some experimental videos were originally recorded in `.mov` format. Since some tools and libraries work more reliably with `.mp4`, a dedicated notebook is included in the `notebooks` directory to convert `.mov` files into `.mp4`.

The typical conversion workflow is:

`.mov` video → Python conversion notebook → `.mp4` video → DeepLabCut processing

This conversion step helps avoid codec compatibility issues during video processing.

## Requirements

The project was developed using Python 3.10. The main dependencies used in the notebooks include:

- DeepLabCut  
- NumPy  
- Pandas  
- Matplotlib  
- SciPy  
- Jupyter Notebook  

DeepLabCut is the main library used for markerless pose estimation.

The official DeepLabCut website is available at:

https://www.deeplabcut.org

The official documentation can be found at:

https://deeplabcut.github.io/DeepLabCut/docs/installation.html

A simple installation using pip can be done with:

`pip install deeplabcut`

Alternatively, the recommended installation using Conda is:

`conda create -n dlc python=3.10`  
`conda activate dlc`  
`pip install deeplabcut`

Additional Python libraries required by the notebooks can be installed using:

`pip install numpy pandas matplotlib scipy jupyter`

## Ball and Beam Dataset Utilities

This project also uses utilities from the `bab_datasets` repository developed by Prof. Helon Ayala. This package provides helper functions to load synchronized Ball and Beam experimental data and videos.

The repository is available at:

https://github.com/helonayala/bab_datasets

The package can be installed directly from GitHub using:

`pip install "bab_datasets[video,notebook] @ git+https://github.com/helonayala/bab_datasets.git"`

These utilities facilitate loading and handling experimental datasets used in Ball and Beam experiments.

## Video Data

Due to GitHub file size limitations, the raw experimental videos used in this project are not included in the repository.

The videos used in the experiments can be accessed through external storage such as Google Drive, OneDrive, or other dataset repositories.

Example placeholder:

`[INSERT VIDEO STORAGE LINK HERE]`

## Running the Notebooks

To run the notebooks locally, first clone the repository:

`git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git`

Then navigate to the project directory:

`cd YOUR_REPOSITORY`

Start Jupyter Notebook with:

`jupyter notebook`

Open the notebooks located in the `notebooks` folder and run the cells sequentially.

## Notes

The notebooks provided in this repository contain the processed results and figures generated during the experiments. Large intermediate files generated by DeepLabCut, such as training datasets, pose estimation outputs, and raw videos, are intentionally excluded to keep the repository size manageable.

## Author

Edo Almeida  
MSc Student in Control and Automation Engineering  
Pontifical Catholic University of Paraná (PUCPR)

## License

This repository is intended for academic and research purposes.
