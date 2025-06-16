import base64
import json
import sys

def save_base64_image(response_file, output_file):
    with open(response_file, 'r') as f:
        response = json.load(f)
    
    if 'output' in response and 'images' in response['output']:
        for idx, img_data in enumerate(response['output']['images']):
            if img_data['type'] == 'base64':
                image_base64 = img_data['data']
                # Remove data URL prefix if present
                if ',' in image_base64:
                    image_base64 = image_base64.split(',', 1)[1]
                
                # Decode and save
                image_data = base64.b64decode(image_base64)
                with open(output_file, 'wb') as f:
                    f.write(image_data)
                print(f"Image saved to {output_file}")
                return
    
    print("No base64 image found in response")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python save_image.py <response_file.json> <output_file.png>")
        sys.exit(1)
    
    save_base64_image(sys.argv[1], sys.argv[2]) 