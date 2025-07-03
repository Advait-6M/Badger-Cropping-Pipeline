#!/usr/bin/env python3
"""
Example usage of the Badger Cropping Pipeline

This script demonstrates how to use the pipeline to extract badger crops from videos.
"""

import os
from video_to_badger_crops import main as crop_badgers
from Badger_detection import extract_frames, run_speciesnet_on_frames, process_speciesnet_results

def example_basic_cropping():
    """
    Example 1: Basic badger cropping from video frames
    """
    print("=== Example 1: Basic Badger Cropping ===")
    
    # Configuration
    input_video = "your_video.mp4"  # Replace with your video path
    frames_dir = "extracted_frames"
    crops_dir = "badger_crops"
    
    # Step 1: Extract frames from video
    print("Step 1: Extracting frames...")
    extracted_frames, fps = extract_frames(input_video, frames_dir, interval_seconds=1)
    
    if not extracted_frames:
        print("No frames extracted. Check video path.")
        return
    
    # Step 2: Run SpeciesNet detection
    print("Step 2: Running SpeciesNet detection...")
    predictions_file = "speciesnet_predictions.json"
    run_speciesnet_on_frames(frames_dir, predictions_file)
    
    # Step 3: Process results and crop badgers
    print("Step 3: Processing results and cropping badgers...")
    process_speciesnet_results(predictions_file, target_species_keywords=["meles", "badger", "animal"])
    
    print(f"Badger crops saved to: {crops_dir}")

def example_direct_cropping():
    """
    Example 2: Direct cropping using the main cropping script
    """
    print("\n=== Example 2: Direct Cropping ===")
    
    # This uses the video_to_badger_crops.py script directly
    # You need to modify the parameters in that file first:
    # INPUT_DIR = "path/to/your/frames"
    # OUTPUT_DIR = "path/to/save/crops"
    # CONFIDENCE_THRESHOLD = 0.6
    
    print("To use direct cropping:")
    print("1. Modify parameters in video_to_badger_crops.py")
    print("2. Run: python video_to_badger_crops.py")

def example_complete_pipeline():
    """
    Example 3: Complete pipeline using Badger_detection.py
    """
    print("\n=== Example 3: Complete Pipeline ===")
    
    # This uses the complete Badger_detection.py pipeline
    # Modify the configuration at the top of Badger_detection.py:
    # DEFAULT_VIDEO_PATH = "your_video.mp4"
    # FRAME_INTERVAL_SECONDS = 1
    # COUNTRY_CODE = "GBR"  # Optional
    
    print("To use complete pipeline:")
    print("1. Modify configuration in Badger_detection.py")
    print("2. Run: python Badger_detection.py")

if __name__ == "__main__":
    print("Badger Cropping Pipeline - Example Usage")
    print("=" * 50)
    
    # Show examples
    example_basic_cropping()
    example_direct_cropping()
    example_complete_pipeline()
    
    print("\n" + "=" * 50)
    print("Choose the method that best fits your needs:")
    print("- Example 1: Step-by-step control")
    print("- Example 2: Simple cropping from existing frames")
    print("- Example 3: Complete automated pipeline") 