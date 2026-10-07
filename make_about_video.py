import os
import math
import numpy as np
import cv2
import imageio
from PIL import Image

def clamp(val, min_val, max_val):
    return max(min_val, min(max_val, val))

base_img_path = r"C:\Users\User\.gemini\antigravity\brain\baf0e5a0-9ec9-4d43-9cba-099167254d6f\shaik_harun_typing_about_1791393444165.png"
output_dir = r"d:\PORTFOLIO\assets\videos"
os.makedirs(output_dir, exist_ok=True)

mp4_out = os.path.join(output_dir, "shaik-harun-about-video.mp4")
webm_out = os.path.join(output_dir, "shaik-harun-about-video.webm")

# Load base image
pil_base = Image.open(base_img_path).convert("RGB")

WIDTH = 768
HEIGHT = 1024
FPS = 30
DURATION_SEC = 10
TOTAL_FRAMES = FPS * DURATION_SEC # 300 frames

pil_base = pil_base.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)

np.random.seed(99)
num_particles = 40
particles = []
for _ in range(num_particles):
    particles.append({
        'x': np.random.randint(WIDTH // 4, 3 * WIDTH // 4),
        'y': np.random.randint(HEIGHT // 2, HEIGHT),
        'speed': np.random.uniform(1.5, 4.0),
        'size': np.random.randint(2, 5),
        'color': (56, 189, 248) if np.random.rand() > 0.4 else (192, 132, 252)
    })

print(f"Generating 10-second About typing video ({TOTAL_FRAMES} frames)...")

# Write MP4
writer_mp4 = imageio.get_writer(
    mp4_out,
    fps=FPS,
    codec='libx264',
    pixelformat='yuv420p',
    macro_block_size=1
)

frames_buffer = []

for frame_idx in range(TOTAL_FRAMES):
    t = frame_idx / TOTAL_FRAMES # 0.0 to 1.0
    angle = t * 2 * math.pi
    
    # 1. Micro-typing rhythm motion (subtle keystroke sway)
    typing_sway_y = 4 * math.sin(t * 12 * math.pi)
    typing_sway_x = 3 * math.cos(angle * 2)
    zoom = 1.0 + 0.02 * (0.5 + 0.5 * math.sin(angle))
    
    crop_w = int(pil_base.width / zoom)
    crop_h = int(pil_base.height / zoom)
    crop_x = int(clamp((pil_base.width - crop_w) / 2 + typing_sway_x, 0, pil_base.width - crop_w))
    crop_y = int(clamp((pil_base.height - crop_h) / 2 + typing_sway_y, 0, pil_base.height - crop_h))
    
    cropped = pil_base.crop((crop_x, crop_y, crop_x + crop_w, crop_y + crop_h))
    resized = cropped.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    
    img = np.array(resized)
    
    # 2. Typing Keyboard & Screen Glow Pulse
    glow_intensity = 0.14 * (0.5 + 0.5 * math.sin(t * 16 * math.pi))
    glow_overlay = np.zeros_like(img, dtype=np.uint8)
    glow_overlay[HEIGHT//2:, :, 0] = 50  # Red
    glow_overlay[HEIGHT//2:, :, 1] = 180 # Green/Cyan
    glow_overlay[HEIGHT//2:, :, 2] = 240 # Blue
    img = cv2.addWeighted(img, 1.0, glow_overlay, glow_intensity, 0)
    
    # 3. Floating Code Particles rising from Laptop Screen
    for p in particles:
        p['y'] = (p['y'] - p['speed']) % (HEIGHT - HEIGHT//3) + HEIGHT//3
        px = int(p['x'] + 4 * math.sin(angle * 3 + p['y'] * 0.03)) % WIDTH
        py = int(p['y'])
        cv2.circle(img, (px, py), p['size'], p['color'], -1)
        
    writer_mp4.append_data(img)
    frames_buffer.append(img)

writer_mp4.close()
print(f"Generated MP4: {mp4_out}")

# Write WebM
writer_webm = imageio.get_writer(
    webm_out,
    fps=FPS,
    codec='libvpx-vp9'
)
for frame_img in frames_buffer:
    writer_webm.append_data(frame_img)
writer_webm.close()
print(f"Generated WebM: {webm_out}")

print("About section typing video successfully generated!")
