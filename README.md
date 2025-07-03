# Badger Cropping Pipeline

A pipeline for automatically detecting and cropping badger images from video footage using SpeciesNet.

## Overview

This pipeline extracts frames from videos and uses SpeciesNet to detect badgers, automatically cropping them for further analysis or re-identification tasks.

## Features

- **Video Frame Extraction**: Extract frames at specified intervals
- **Badger Detection**: Use SpeciesNet v4.0.1a for robust badger detection
- **Automatic Cropping**: Crop detected badgers from frames
- **Batch Processing**: Process multiple videos efficiently

## Files

- `video_to_badger_crops.py`: Main script for cropping badgers from video frames
- `Badger_detection.py`: Complete video processing pipeline with SpeciesNet
- `requirements.txt`: Required dependencies

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Download SpeciesNet model (will be auto-downloaded on first use)

## Usage

### Basic Usage
```python
# Modify parameters in video_to_badger_crops.py
INPUT_DIR = "path/to/your/video/frames"
OUTPUT_DIR = "path/to/save/crops"
CONFIDENCE_THRESHOLD = 0.6

# Run the script
python video_to_badger_crops.py
```

### Complete Pipeline
```python
# Use Badger_detection.py for full video processing
python Badger_detection.py
```

## Configuration

Key parameters:
- `CONFIDENCE_THRESHOLD`: Detection confidence (default: 0.6)
- `FRAME_INTERVAL_SECONDS`: Frame extraction interval
- `COUNTRY_CODE`: Geographic filtering (optional)

## Dependencies

- PyTorch
- OpenCV
- SpeciesNet (CameraTrapAI)
- NumPy
- PIL
- tqdm

## Output

Cropped badger images saved to specified output directory with naming convention:
`cropped_{video_name}_frame{frame_number}_det{detection_number}.jpg` 