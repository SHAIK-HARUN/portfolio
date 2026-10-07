import os
import math
import numpy as np
import cv2
import imageio
from PIL import Image

base_img_path = r"C:\Users\User\.gemini\antigravity\brain\baf0e5a0-9ec9-4d43-9cba-099167254d6f\anime_video_base_1791391775754.png"
output_dir = r"d:\PORTFOLIO\assets\videos"
os.makedirs(output_dir, exist_ok=True)
output_mp4 = os.path.join(output_dir, "shaik-harun-anime-video.mp4")

# Load base image
pil_base = Image.open(base_img_path).convert("RGB")

# Target dimensions
WIDTH = 720
HEIGHT = 960
FPS = 30
DURATION_SEC = 10
TOTAL_FRAMES = FPS * DURATION_SEC # 300 frames

# Random particle seeds
np.random.seed(42)
num_particles = 45
particles = []
for _ in range(num_particles):
    particles.append({
        'x': np.random.randint(0, WIDTH),
        'y': np.random.randint(0, HEIGHT),
        'speed': np.random.uniform(1.2, 3.5),
        'size': np.random.randint(2, 5),
        'color': (220, 120, 255) if np.random.rand() > 0.4 else (255, 220, 120) # RGB format
    })

print(f"Generating 10-second web-compatible H.264 MP4 video ({TOTAL_FRAMES} frames)...")

# Initialize ImageIO H.264 Video Writer with yuv420p pixel format for browser compatibility
writer = imageio.get_writer(
    output_mp4,
    fps=FPS,
    codec='libx264',
    pixelformat='yuv420p',
    macro_block_size=1
)

for frame_idx in range(TOTAL_FRAMES):
    t = frame_idx / TOTAL_FRAMES # 0.0 to 1.0
    angle = t * 2 * math.pi
    
    # 1. Subtle camera zoom oscillation (1.0 to 1.04)
    zoom = 1.0 + 0.03 * (0.5 + 0.5 * math.sin(angle))
    crop_w = int(pil_base.width / zoom)
    crop_h = int(pil_base.height / zoom)
    crop_x = int((pil_base.width - crop_w) / 2 + 10 * math.cos(angle))
    crop_y = int((pil_base.height - crop_h) / 2 + 8 * math.sin(angle))
    
    cropped = pil_base.crop((crop_x, crop_y, crop_x + crop_w, crop_y + crop_h))
    resized = cropped.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    
    # Convert PIL to numpy array (RGB)
    img = np.array(resized)
    
    # 2. Pulsating Neon Overlay
    pulse_intensity = 0.15 * (0.5 + 0.5 * math.sin(angle * 2))
    purple_overlay = np.zeros_like(img, dtype=np.uint8)
    purple_overlay[:, :, 0] = 150 # Red
    purple_overlay[:, :, 2] = 200 # Blue
    img = cv2.addWeighted(img, 1.0, purple_overlay, pulse_intensity, 0)
    
    # 3. Holographic Scanline Sweep (3 sweeps over 10 seconds)
    scan_y = int((t * 3) % 1.0 * HEIGHT)
    cv2.line(img, (0, scan_y), (WIDTH, scan_y), (100, 200, 255), 3) # RGB
    cv2.line(img, (0, scan_y - 2), (WIDTH, scan_y - 2), (200, 100, 255), 1)
    
    # 4. Animated Floating Particles
    for p in particles:
        p['y'] = (p['y'] - p['speed']) % HEIGHT
        px = int(p['x'] + 5 * math.sin(angle * 3 + p['y'] * 0.02)) % WIDTH
        py = int(p['y'])
        cv2.circle(img, (px, py), p['size'], p['color'], -1)
    
    writer.append_data(img)

writer.close()
print(f"Successfully rendered web-compatible video: {output_mp4}")
