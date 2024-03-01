import os
import random
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip


font_path = "old/font.ttf"
font_size = 150
text_color = (255, 250, 0)
text_offset = 60  # Adjust this value to control the separation from the edge

def generate_text(text_top="", text_mid="", text_top_size=font_size, text_mid_size=font_size):
    # Define image size with a vertical 16:9 aspect ratio
    width = 1080
    height = 1920
    
    # Create a blank image with transparent background
    image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    
    # Load font
    font = ImageFont.truetype(font_path, font_size)
    
    # Create a drawing context
    draw = ImageDraw.Draw(image)
    
    # Calculate text size and position for top text
    if text_top:
        font_top = ImageFont.truetype(font_path, text_top_size)
        text_width, text_height = draw.textsize(text_top, font=font_top)
        x = (width - text_width) / 2
        y = text_offset
        draw.text((x, y), text_top, fill=text_color, font=font_top)
    
    # Calculate text size and position for middle text
    if text_mid:
        font_mid = ImageFont.truetype(font_path, text_mid_size)
        text_width, text_height = draw.textsize(text_mid, font=font_mid)
        x = (width - text_width) / 2
        y = (height - text_height) / 2
        draw.text((x, y), text_mid, fill=text_color, font=font_mid)
    
    # Generate a random output path
    output_dir = "output_images"
    os.makedirs(output_dir, exist_ok=True)
    random_filename = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=10))
    output_path = os.path.join(output_dir, random_filename + ".png")
    
    # Save the image
    image.save(output_path)
    
    # Return the generated output path
    return output_path

    # Example usage
    # generated_output_path = generate_text(text_top = "Top Text", text_mid = "Middle Text")

def add_image(video_clip, img_path):
    # Load the image
    img_clip = ImageClip(img_path)
    
    # Make the image clip the same size as the video clip
    img_clip = img_clip.resize(width=video_clip.size[0], height=video_clip.size[1])
    
    # Set the duration of the image clip to match the duration of the video clip
    img_clip = img_clip.set_duration(video_clip.duration)
    
    # Composite the image clip on top of the video clip
    final_clip = CompositeVideoClip([video_clip, img_clip.set_position(('center', 'center'))])
    
    # Close the image clip
    img_clip.close()
    
    return final_clip

final = add_image(VideoFileClip("video.mp4"), generate_text(text_mid="Hola mundito!\nEspero estes contento :)", text_mid_size=100))
final.write_videofile("output_video.mp4")