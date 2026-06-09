import base64

def convert_to_base64(image_path, output_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        data_url = f"data:image/png;base64,{encoded_string}"
        
        with open(output_path, "w") as out_file:
            out_file.write(data_url)
        print(f"Base64 length: {len(data_url)}")
        print(f"Saved to {output_path}")

if __name__ == "__main__":
    convert_to_base64('/Users/catherinetseng/.gemini/antigravity/scratch/jelly_person.png', '/Users/catherinetseng/.gemini/antigravity/scratch/jelly_base64.txt')
