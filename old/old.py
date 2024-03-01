from moviepy.editor import *
# from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip,ImageClip

def generate_intro(input_video, audio_file):
    try:
        # Preload the video clip
        clip = VideoFileClip(input_video)
        
        # Preload the audio clip
        audio_clip = AudioFileClip(audio_file)
        
        # Determine the duration for cropping
        buffer_duration = 1  # seconds
        start_time = max(0, audio_clip.start - buffer_duration)
        end_time = min(clip.duration, audio_clip.end + buffer_duration)
        
        # Crop the video to match the duration of the audio with buffer
        clip = clip.subclip(start_time, end_time)
        
        # Calculate cropping parameters for phone view (1080 x 1920)
        target_width = 1080
        target_height = 1920
        
        # Calculate the aspect ratio of the target dimensions
        target_aspect_ratio = target_width / target_height
        
        # Calculate the aspect ratio of the original video
        original_aspect_ratio = clip.size[0] / clip.size[1]
        
        if original_aspect_ratio > target_aspect_ratio:
            # Video is wider than the target, crop the sides
            new_width = int(target_height * original_aspect_ratio)
            left_padding = (new_width - target_width) // 2
            crop_area = (left_padding, 0, new_width - left_padding, target_height)
        else:
            # Video is taller than the target, crop the top and bottom
            new_height = int(target_width / original_aspect_ratio)
            top_padding = (new_height - target_height) // 2
            crop_area = (0, top_padding, target_width, new_height - top_padding)
        
        # Crop the video
        clip_cropped = clip.crop(*crop_area)
        
        # Resize the cropped video to match the target dimensions
        clip_resized = clip_cropped.resize((target_width, target_height))
        
        # Add audio to the resized video
        video_with_audio = clip_resized.set_audio(audio_clip)
        
        return video_with_audio
    except Exception as e:
        print("Error in generate_intro:", e)
        return None


# Example usage:
input_video = "video2.mp4"
audio_file = "audio.mp3"
output_video = "intro.mp4"

cropped_clip_with_audio = generate_intro(input_video, audio_file)
# cropped_clip_with_audio.write_videofile(output_video, codec="libx264", fps=24)  # Adjust codec and fps as needed

def generate_portrait(part):
    # Load the image
    image_path = f"portadas/{part}.jpg"  # Assuming the image format is JPEG
    image_clip = ImageClip(image_path, duration=1)  # Duration is set to 1 second
    
    # Load the audio
    audio_file = f"numeros/{part}.mp3"
    audio_clip = AudioFileClip(audio_file)
    
    # Extend the duration of the audio if less than 1 second
    if audio_clip.duration < 1:
        audio_clip = audio_clip.set_duration(1)
    
    # Resize the image to occupy 1080x1920 without stretching
    image_clip = image_clip.resize(height=1920)
    
    # Calculate horizontal padding needed to center the image
    padding = (image_clip.w - 1080) // 2
    
    # Crop the image to the desired resolution
    image_clip = image_clip.crop(x1=padding, x2=image_clip.w - padding)
    
    # Combine image and audio
    video_with_audio = image_clip.set_audio(audio_clip)
    
    return video_with_audio

# Example usage:
part = "1"
output_video = f"{part}_video.mp4"

video_with_audio = generate_portrait(part)
section = generate_intro("video.mp4", "audio2.mp3")

final_clip = concatenate_videoclips([cropped_clip_with_audio, video_with_audio,section])
final_clip.write_videofile("CODIF.mp4", codec="libx264", fps=24,  preset="medium", bitrate="5000k")
