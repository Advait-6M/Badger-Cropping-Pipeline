# --- HARDCODED PARAMETERS ---
INPUT_DIR = r"E:\Badger Detection\Badger dataset\Manual_Masking_Test"  # Directory of input images
OUTPUT_DIR = r"E:\Badger Detection\Badger dataset\Cropped Images"  # Directory to save cropped images
CONFIDENCE_THRESHOLD = 0.6  # Detection confidence threshold (lowered from 0.7)

import os
import glob
from PIL import Image
from cameratrapai.speciesnet.detector import SpeciesNetDetector
from cameratrapai.speciesnet.utils import PreprocessedImage
from tqdm import tqdm

def main():
    input_dir = INPUT_DIR
    output_dir = OUTPUT_DIR
    confidence_threshold = CONFIDENCE_THRESHOLD

    input_dir_name = os.path.basename(os.path.normpath(input_dir))
    os.makedirs(output_dir, exist_ok=True)

    # Get all image files
    image_files = sorted(glob.glob(os.path.join(input_dir, '*.jpg')) +
                        glob.glob(os.path.join(input_dir, '*.jpeg')) +
                        glob.glob(os.path.join(input_dir, '*.png')))
    print(f"Found {len(image_files)} images in {input_dir}")

    # Initialize SpeciesNetDetector
    print("Loading SpeciesNet Detector...")
    detector = SpeciesNetDetector("kaggle:google/speciesnet/pyTorch/v4.0.1a")
    print("✓ SpeciesNet Detector loaded.")

    crop_count = 0
    for idx, img_path in enumerate(tqdm(image_files, desc="Processing images")):
        image = Image.open(img_path).convert('RGB')
        preprocessed = detector.preprocess(image)
        result = detector.predict(img_path, preprocessed)
        detections = result.get('detections', [])
        for det_idx, det in enumerate(detections):
            label = det.get('label', '')
            conf = det.get('conf', 0)
            bbox = det.get('bbox', None)
            label_lower = label.lower()
            if (("meles" in label_lower) or ("badger" in label_lower) or ("animal" in label_lower)) and conf >= confidence_threshold and bbox is not None:
                # bbox is [x_min, y_min, width, height] in normalized coordinates
                x_min, y_min, width, height = bbox
                x0 = int(x_min * image.width)
                y0 = int(y_min * image.height)
                x1 = int((x_min + width) * image.width)
                y1 = int((y_min + height) * image.height)
                crop = image.crop((x0, y0, x1, y1))
                crop_filename = f"cropped_{input_dir_name}_frame{idx:06d}_det{det_idx}.jpg"
                crop_path = os.path.join(output_dir, crop_filename)
                crop.save(crop_path)
                crop_count += 1
    print(f"Done! Saved {crop_count} cropped badger images to {output_dir}")

if __name__ == "__main__":
    main() 