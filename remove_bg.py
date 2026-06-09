import numpy as np
from PIL import Image

def remove_background(image_path, output_path):
    img = Image.open(image_path).convert("RGBA")
    data = np.array(img)
    
    # Let's inspect unique colors and background characteristics
    # We will print some diagnostic info
    width, height = img.size
    print(f"Image dimensions: {width}x{height}")
    
    # Check the corners to find typical background color
    corners = [
        data[0, 0], data[0, -1], data[-1, 0], data[-1, -1],
        data[2, 2], data[2, -3], data[-3, 2], data[-3, -3]
    ]
    print("Corner pixel values (possible background):", [list(c) for c in corners])
    
    # Let's find dominant colors in the image (excluding transparent pixels)
    pixels = data.reshape(-1, 4)
    non_transparent = pixels[pixels[:, 3] > 0]
    if len(non_transparent) > 0:
        # Get unique colors and counts
        colors, counts = np.unique(non_transparent[:, :3], axis=0, return_counts=True)
        sort_idx = np.argsort(-counts)
        print("Top 5 colors by count (RGB):")
        for i in range(min(5, len(sort_idx))):
            idx = sort_idx[i]
            print(f"Color: {colors[idx]} - Count: {counts[idx]}")
            
    # Simple background removal:
    # If the background is near-white or a specific color, we can turn it transparent.
    # Let's assume background is white or light gray (since corner pixels are often background).
    # Let's compute a mask for pixels that are very close to white/light-gray, or transparent.
    # Let's also check if there is an existing alpha channel.
    
    # We will make pixels transparent if they are very close to white (e.g. RGB > 240)
    # or if they match the corner color within some tolerance.
    corner_color = corners[0][:3]
    
    # Define a tolerance
    tol = 15
    
    # Create mask of background pixels
    # Condition 1: close to corner color
    mask_corner = np.all(np.abs(data[:, :, :3] - corner_color) <= tol, axis=-1)
    
    # Condition 2: very close to white (RGB > 245)
    mask_white = np.all(data[:, :, :3] > 245, axis=-1)
    
    # Combine masks
    bg_mask = mask_corner | mask_white
    
    # Let's keep the main body.
    # If we make it transparent:
    new_data = data.copy()
    new_data[bg_mask, 3] = 0
    
    # Let's save the result
    result_img = Image.fromarray(new_data)
    result_img.save(output_path)
    print(f"Background removed image saved to {output_path}")

if __name__ == "__main__":
    remove_background('/Users/catherinetseng/Desktop/375x.png', '/Users/catherinetseng/.gemini/antigravity/scratch/jelly_person.png')
