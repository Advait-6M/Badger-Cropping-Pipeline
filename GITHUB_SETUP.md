# GitHub Setup Guide

## How to Share Your Badger Cropping Pipeline on GitHub

### Step 1: Create a New Repository on GitHub
1. Go to [GitHub.com](https://github.com)
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Name it: `badger-cropping-pipeline`
5. Make it public or private (your choice)
6. **Don't** initialize with README (we already have one)
7. Click "Create repository"

### Step 2: Initialize Local Git Repository
```bash
# Navigate to the badger-cropping-pipeline folder
cd badger-cropping-pipeline

# Initialize git repository
git init

# Add all files
git add .

# Make initial commit
git commit -m "Initial commit: Badger cropping pipeline"

# Add remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/badger-cropping-pipeline.git

# Push to GitHub
git push -u origin main
```

### Step 3: Verify Your Repository
Your GitHub repository should now contain:
- `README.md` - Documentation
- `requirements.txt` - Dependencies
- `video_to_badger_crops.py` - Main cropping script
- `Badger_detection.py` - Complete pipeline
- `example_usage.py` - Usage examples
- `.gitignore` - Git ignore rules

### Step 4: Share with Your Supervisor
Send your supervisor the GitHub repository URL:
```
https://github.com/YOUR_USERNAME/badger-cropping-pipeline
```

## What's Included

### Core Files:
1. **`video_to_badger_crops.py`** - Main script for cropping badgers from video frames
2. **`Badger_detection.py`** - Complete video processing pipeline with SpeciesNet
3. **`example_usage.py`** - Examples of how to use the pipeline

### Documentation:
- **`README.md`** - Overview, installation, and usage instructions
- **`requirements.txt`** - Required Python packages
- **`.gitignore`** - Excludes large files and temporary outputs

## What's NOT Included (Excluded by .gitignore):
- Large model files (*.pth, *.pt)
- Video files (*.mp4, *.avi)
- Image files (*.jpg, *.png)
- Output directories
- Training logs
- Cache files

## For Your Supervisor

Your supervisor can now:
1. Clone the repository: `git clone https://github.com/YOUR_USERNAME/badger-cropping-pipeline.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the pipeline by modifying parameters in the scripts
4. Follow the examples in `example_usage.py`

The pipeline focuses specifically on:
- Extracting frames from videos
- Detecting badgers using SpeciesNet
- Cropping detected badgers from frames
- Saving cropped images for further analysis 