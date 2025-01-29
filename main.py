import numpy as np
from pathlib import Path
import pytesseract
from image_comparator import ImageComparator



def find_duplicates(folder_path, tesseract_path):
    """Find duplicates in the specified folder."""
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
    comparator = ImageComparator()
    folder = Path(folder_path)
    image_files = list(folder.glob('*.jpg')) + list(folder.glob('*.png'))
    
    duplicates = []
    total_files = len(image_files)
    
    print(f"Processing {total_files} images...")
    
    for i, file1 in enumerate(image_files):
        print(f"\rAnalyzing image {i+1}/{total_files}...", end="", flush=True)
        img1_gray, img1_color = comparator.load_image(file1)
        if img1_gray is None:
            continue
            
        for file2 in image_files[i+1:]:
            img2_gray, img2_color = comparator.load_image(file2)
            if img2_gray is None:
                continue
                
            if comparator.compare_images(img1_gray, img1_color, img2_gray, img2_color):
                duplicates.append((str(file1.name), str(file2.name)))
    
    print("\nAnalysis complete!")
    return duplicates

def main():
    folder_path = r""
    tesseract_path = r""
    
    print("Starting duplicate image analysis...")
    duplicates = find_duplicates(folder_path, tesseract_path)
    
    if not duplicates:
        print("No identical images found.")
    else:
        print(f"\nFound {len(duplicates)} pairs of identical images (matching both visually and text):")
        for file1, file2 in duplicates:
            print(f"• {file1} ←→ {file2}")

if __name__ == "__main__":
    main()