import os
import imageio

mp4_path = r"d:\PORTFOLIO\assets\videos\pyvideo.mp4"
webm_path = r"d:\PORTFOLIO\assets\videos\pyvideo.webm"

if os.path.exists(mp4_path):
    print("Converting pyvideo.mp4 to pyvideo.webm...")
    reader = imageio.get_reader(mp4_path)
    fps = reader.get_meta_data().get('fps', 24)
    writer = imageio.get_writer(webm_path, fps=fps, codec='libvpx-vp9')
    for frame in reader:
        writer.append_data(frame)
    writer.close()
    reader.close()
    print("Successfully generated pyvideo.webm!")
