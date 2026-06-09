from PIL import Image
import numpy as np

def autocrop(image_path, output_path):
    img = Image.open(image_path).convert("RGBA")
    data = np.array(img)
    
    # Find bounding box of non-transparent pixels (alpha > 0)
    alpha = data[:, :, 3]
    non_empty_coords = np.argwhere(alpha > 0)
    
    if len(non_empty_coords) == 0:
        print("Image is fully transparent, cannot crop.")
        return
        
    # Get bounding box coordinates
    y0, x0 = non_empty_coords.min(axis=0)
    y1, x1 = non_empty_coords.max(axis=0) + 1  # max is inclusive, slice is exclusive
    
    # Crop and save
    cropped_img = img.crop((x0, y0, x1, y1))
    cropped_img.save(output_path)
    print(f"Autocropped from {img.size} to {cropped_img.size} and saved to {output_path}")

if __name__ == "__main__":
    autocrop('/Users/catherinetseng/.gemini/antigravity/scratch/jelly_person.png', '/Users/catherinetseng/.gemini/antigravity/scratch/jelly_person.png')
