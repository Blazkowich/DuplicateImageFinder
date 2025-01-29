import cv2
from PIL import Image
import Levenshtein
import pytesseract

class ImageComparator:
    def __init__(self, image_similarity_threshold=10, text_similarity_threshold=0.8):
        self.image_similarity_threshold = image_similarity_threshold
        self.text_similarity_threshold = text_similarity_threshold

    def load_image(self, image_path):
        """Load image for both visual and text comparison."""
        try:
            gray_img = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
            if gray_img is None:
                raise ValueError(f"Could not load image: {image_path}")
            
            color_img = cv2.imread(str(image_path))
            
            return gray_img, color_img
        except Exception as e:
            print(f"Error processing {image_path}: {str(e)}")
            return None, None

    def extract_text(self, image):
        """Extract text from image using OCR."""
        try:
            pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

            text = pytesseract.image_to_string(pil_image)
            return text.strip().lower()
        except Exception as e:
            print(f"OCR Error: {str(e)}")
            return ""

    def calculate_image_hash(self, image):
        """Calculate perceptual hash of the image."""
        img_resized = cv2.resize(image, (8, 8))
        mean = img_resized.mean()
        hash_str = ''.join(['1' if pixel > mean else '0' for pixel in img_resized.flatten()])
        return hash_str

    def compare_text(self, text1, text2):
        """Compare two text strings using Levenshtein distance."""
        if not text1 and not text2:
            return True
        if not text1 or not text2:
            return False
            
        similarity = Levenshtein.ratio(text1, text2)
        return similarity >= self.text_similarity_threshold

    def compare_images(self, img1_gray, img1_color, img2_gray, img2_color):
        """Compare two images using both visual features and text content."""
        if img1_gray is None or img2_gray is None:
            return False

        img1_gray = cv2.resize(img1_gray, (200, 200))
        img2_gray = cv2.resize(img2_gray, (200, 200))
        
        hash1 = self.calculate_image_hash(img1_gray)
        hash2 = self.calculate_image_hash(img2_gray)
        hamming_distance = sum(c1 != c2 for c1, c2 in zip(hash1, hash2))
        visual_match = hamming_distance <= self.image_similarity_threshold

        text1 = self.extract_text(img1_color)
        text2 = self.extract_text(img2_color)
        text_match = self.compare_text(text1, text2)

        return visual_match and text_match
