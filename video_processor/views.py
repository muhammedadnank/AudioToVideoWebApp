import os
from django.shortcuts import render
from django.conf import settings
from .forms import VideoUploadForm
from .models import VideoFile
from moviepy import VideoFileClip, AudioFileClip, ColorClip

def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            input_path = instance.original_video.path
            file_ext = os.path.splitext(input_path)[1].lower()
            
            try:
                # Determine if input is audio or video
                is_audio = file_ext in ['.mp3', '.wav', '.aac', '.m4a', '.flac']
                
                if is_audio:
                    audio_clip = AudioFileClip(input_path)
                    duration = audio_clip.duration
                    size = (1280, 720) # Default HD size for audio-to-video
                else:
                    video_clip = VideoFileClip(input_path)
                    audio_clip = video_clip.audio
                    duration = video_clip.duration
                    size = video_clip.size
                
                # Create black background
                black_background = ColorClip(size=size, color=(0, 0, 0), duration=duration)
                
                # Combine
                final_video = black_background.with_audio(audio_clip)
                
                # Output setup
                output_filename = f"processed_{os.path.basename(input_path)}.mp4"
                output_dir = os.path.join(settings.MEDIA_ROOT, 'videos', 'processed')
                os.makedirs(output_dir, exist_ok=True)
                output_path = os.path.join(output_dir, output_filename)
                
                # Export
                final_video.write_videofile(output_path, codec="libx264", audio_codec="aac", fps=24)
                
                # Update model
                instance.processed_video = os.path.join('videos', 'processed', output_filename)
                instance.save()
                
                # Cleanup
                audio_clip.close()
                if not is_audio:
                    video_clip.close()
                final_video.close()
                
                return render(request, 'video_processor/upload.html', {
                    'form': VideoUploadForm(),
                    'processed_video_url': instance.processed_video.url
                })
                
            except Exception as e:
                return render(request, 'video_processor/upload.html', {
                    'form': form,
                    'error': f"Error processing file: {str(e)}"
                })
                
    else:
        form = VideoUploadForm()
    
    return render(request, 'video_processor/upload.html', {'form': form})
