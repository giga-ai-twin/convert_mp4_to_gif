import sys
import os
from moviepy import VideoFileClip
import moviepy.video.fx as vfx
from moviepy.video.fx import MultiplySpeed

# === Configuration Section ===
CLIP_DURATION = 20.0  # Fixed capture duration of X seconds
# =============================

def convert_to_gif(input_file, start_time=0.0):
    # Automatically generate output filename (replace extension with .gif)
    base_name, _ = os.path.splitext(input_file)
    output_file = f"{base_name}.gif"

    print(f"🔄 Processing: {input_file}")

    try:
        # Load the video file
        clip = VideoFileClip(input_file)

        # Get total video duration
        total_duration = clip.duration

        # --- 🛡️ Safeguard Logic: Validate Time ---
        if start_time < 0:
            print("⚠️ Start time cannot be negative. Resetting to 0.")
            start_time = 0.0

        # If start time is too late and remaining duration is less than X seconds
        if start_time + CLIP_DURATION > total_duration:
            print(f"⚠️ Warning: Start time {start_time}s is too close to the end.")
            # Automatically adjust backward to capture the last X seconds (or the whole clip if too short)
            start_time = max(0, total_duration - CLIP_DURATION)
            print(f"   -> Auto-adjusted start time to: {start_time:.1f}s")

        end_time = min(total_duration, start_time + CLIP_DURATION)

        print(f"✂️ Cutting from {start_time:.1f}s to {end_time:.1f}s (Total: {end_time-start_time:.1f}s)")

        # --- ⚡ Execute Editing Chain ---
        new_clip = (clip
            .subclipped(start_time, end_time)
            .resized(0.5)                  # Resize the clip
            .with_effects([MultiplySpeed(3)])  # Speed up the video
        )

        # Export as GIF
        print(f"💾 Saving to {output_file}... (This might take a minute)")
        new_clip.write_gif(output_file, fps=10) # 10fps is usually the sweet spot
        print(f"✅ Success! GIF saved at: {output_file}")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if 'clip' in locals(): clip.close()
        if 'new_clip' in locals(): new_clip.close()

if __name__ == "__main__":
    # Check if filename is provided as an argument
    if len(sys.argv) < 2:
        print("⚠️ Usage: python convert_gif.py <video_filename> [start_seconds]")
        print("Example 1 (Default from 0s): python convert_gif.py demo.mp4")
        print("Example 2 (From 10s):        python convert_gif.py demo.mp4 10")
    else:
        filename = sys.argv[1]

        # Attempt to read the second argument (start time in seconds)
        start_seconds = 0.0
        if len(sys.argv) >= 3:
            try:
                start_seconds = float(sys.argv[2])
            except ValueError:
                print("⚠️ Invalid start time format. Using default 0s.")

        if os.path.exists(filename):
            convert_to_gif(filename, start_seconds)
        else:
            print(f"❌ File not found: {filename}")