import os
import math
import numpy as np
import cv2
import imageio
from PIL import Image

output_dir = r"d:\PORTFOLIO\assets\videos"
os.makedirs(output_dir, exist_ok=True)

projects = [
    {
        "name": "careconnect",
        "input_img": r"d:\PORTFOLIO\assets\images\project-careconnect.png",
        "mp4_out": os.path.join(output_dir, "project-careconnect-video.mp4"),
        "webm_out": os.path.join(output_dir, "project-careconnect-video.webm"),
        "particle_colors": [(56, 189, 248), (124, 92, 255), (255, 255, 255)], # Cyan / Violet / White (RGB)
        "overlay_color": (30, 20, 60), # Dark violet tone
        "scan_color": (56, 189, 248) # Cyan laser sweep
    },
    {
        "name": "pypractice",
        "input_img": r"d:\PORTFOLIO\assets\images\project-pypractice.png",
        "mp4_out": os.path.join(output_dir, "project-pypractice-video.mp4"),
        "webm_out": os.path.join(output_dir, "project-pypractice-video.webm"),
        "particle_colors": [(192, 132, 252), (244, 63, 94), (250, 204, 21)], # Purple / Rose / Yellow (RGB)
        "overlay_color": (40, 15, 65), # Deep purple
        "scan_color": (192, 132, 252) # Purple laser sweep
    }
]

FPS = 30
DURATION_SEC = 10
TOTAL_FRAMES = FPS * DURATION_SEC # 300 frames

for proj in projects:
    print(f"Processing project video: {proj['name']}...")
    pil_base = Image.open(proj['input_img']).convert("RGB")
    
    # Dimensions derived from base image aspect ratio (capped at max 1280x720)
    WIDTH, HEIGHT = 1280, 720
    pil_base = pil_base.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    
    np.random.seed(101)
    num_particles = 50
    particles = []
    for _ in range(num_particles):
        color_idx = np.random.randint(0, len(proj['particle_colors']))
        particles.append({
            'x': np.random.randint(0, WIDTH),
            'y': np.random.randint(0, HEIGHT),
            'speed': np.random.uniform(1.0, 3.2),
            'size': np.random.randint(2, 6),
            'color': proj['particle_colors'][color_idx]
        })
    
    # 1. Write MP4 (libx264, yuv420p)
    writer_mp4 = imageio.get_writer(
        proj['mp4_out'],
        fps=FPS,
        codec='libx264',
        pixelformat='yuv420p',
        macro_block_size=1
    )
    
    frames_buffer = []
    
    for frame_idx in range(TOTAL_FRAMES):
        t = frame_idx / TOTAL_FRAMES # 0.0 to 1.0
        angle = t * 2 * math.pi
        
        # Subtle slow pan and zoom
        zoom = 1.0 + 0.035 * (0.5 + 0.5 * math.sin(angle))
        crop_w = int(pil_base.width / zoom)
        crop_h = int(pil_base.height / zoom)
        crop_x = int((pil_base.width - crop_w) / 2 + 12 * math.sin(angle))
        crop_y = int((pil_base.height - crop_h) / 2 + 10 * math.cos(angle))
        
        cropped = pil_base.crop((crop_x, crop_y, crop_x + crop_w, crop_y + crop_h))
        resized = cropped.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
        
        img = np.array(resized)
        
        # Ambient Color Pulse
        pulse = 0.12 * (0.5 + 0.5 * math.sin(angle * 2))
        overlay = np.zeros_like(img, dtype=np.uint8)
        overlay[:, :, 0] = proj['overlay_color'][0]
        overlay[:, :, 1] = proj['overlay_color'][1]
        overlay[:, :, 2] = proj['overlay_color'][2]
        img = cv2.addWeighted(img, 1.0, overlay, pulse, 0)
        
        # Holographic Sci-Fi Laser Sweep
        scan_y = int((t * 2) % 1.0 * HEIGHT)
        cv2.line(img, (0, scan_y), (WIDTH, scan_y), proj['scan_color'], 3)
        cv2.line(img, (0, scan_y - 2), (WIDTH, scan_y - 2), (255, 255, 255), 1)
        
        # Floating Glow Particles
        for p in particles:
            p['y'] = (p['y'] - p['speed']) % HEIGHT
            px = int(p['x'] + 6 * math.sin(angle * 2.5 + p['y'] * 0.02)) % WIDTH
            py = int(p['y'])
            cv2.circle(img, (px, py), p['size'], p['color'], -1)
            
        writer_mp4.append_data(img)
        frames_buffer.append(img)
        
    writer_mp4.close()
    print(f"Generated MP4: {proj['mp4_out']}")
    
    # 2. Write WebM (libvpx-vp9)
    writer_webm = imageio.get_writer(
        proj['webm_out'],
        fps=FPS,
        codec='libvpx-vp9'
    )
    for frame_img in frames_buffer:
        writer_webm.append_data(frame_img)
    writer_webm.close()
    print(f"Generated WebM: {proj['webm_out']}")

print("All project videos generated successfully!")
