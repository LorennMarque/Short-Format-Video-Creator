from PIL import Image, ImageDraw, ImageFont

def generate_image_with_text(text, font_path, font_size, text_color, output_path):
    # Define image size with a vertical 16:9 aspect ratio
    width =  324 # Width is 16 * 36 (font size)
    height = 576  # Height is 9 * 36 (font size)
    
    # Create a blank image with transparent background
    image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    
    # Load font
    font = ImageFont.truetype(font_path, font_size)
    
    # Create a drawing context
    draw = ImageDraw.Draw(image)
    
    # Calculate text size and position
    bbox = draw.textbbox((x, y), text, font=font)
    x = bbox[2] - bbox[0]
    y = bbox[3] - bbox[1]

    
    # Draw text on image
    draw.text((x, y), text, fill=text_color, font=font)
    
    # Save the image
    image.save(output_path)

# Example usage
text = "Hello, world!"
font_path = "font.ttf"
font_size = 36
text_color = (255, 250, 0)  # Red color, adjust as needed
output_path = "output_image.png"

generate_image_with_text(text, font_path, font_size, text_color, output_path)
