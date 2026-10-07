import asyncio
import edge_tts
import os

TEXT = "Hey there. Welcome to my world, A mind full of ideas, a screen full of possibilities, and a passion for making them real."
VOICE = "en-US-ChristopherNeural" # Ultra-crisp natural male neural AI voice
OUTPUT_FILE = r"d:\PORTFOLIO\assets\audio\welcome.mp3"

async def main():
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    communicate = edge_tts.Communicate(TEXT, VOICE, rate="+0%", volume="+30%")
    await communicate.save(OUTPUT_FILE)
    print(f"Successfully generated Neural AI voice welcome.mp3 (voice: {VOICE})")

if __name__ == "__main__":
    asyncio.run(main())
