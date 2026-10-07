import os
import imageio

videos = [
    ("aboutvideo.mp4", "aboutvideo.webm"),
    ("animevideo.mp4", "animevideo.webm"),
    ("carevideo.mp4", "carevideo.webm")
]

base_dir = r"d:\PORTFOLIO\assets\videos"

for mp4_file, webm_file in videos:
    mp4_path = os.path.join(base_dir, mp4_file)
    webm_path = os.path.join(base_dir, webm_file)
    
    if os.path.exists(mp4_path):
        print(f"Converting {mp4_file} -> {webm_file}...")
        try:
            reader = imageio.get_reader(mp4_path)
            fps = reader.get_meta_data().get('fps', 24)
            writer = imageio.get_writer(webm_path, fps=fps, codec='libvpx-vp9')
            for frame in reader:
                writer.append_data(frame)
            writer.close()
            reader.close()
            print(f"Successfully generated {webm_file}")
        except Exception as e:
            print(f"Error converting {mp4_file}: {e}")

print("All custom video conversions complete!")
