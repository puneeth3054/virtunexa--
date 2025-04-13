from PIL import Image, ImageDraw, ImageFont
import os
import logging

# === Logging Setup ===
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/watermark_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# === Add Watermark to Single Image ===
def add_watermark(image_path, text, output_path, opacity=128):
    try:
        base = Image.open(image_path).convert("RGBA")
        width, height = base.size

        # Create watermark image
        watermark = Image.new("RGBA", base.size)
        draw = ImageDraw.Draw(watermark)

        # Use a built-in font
        font_size = int(height / 20)
        font = ImageFont.load_default()

        text_width, text_height = draw.textsize(text, font)
        position = (width - text_width - 10, height - text_height - 10)

        draw.text(position, text, fill=(255, 255, 255, opacity), font=font)

        # Combine images
        combined = Image.alpha_composite(base, watermark)
        combined = combined.convert("RGB")  # remove alpha for saving in JPG

        combined.save(output_path)
        print(f"✅ Watermark added: {output_path}")
        logging.info(f"Watermarked image saved: {output_path}")
    except Exception as e:
        print(f"❌ Error: {e}")
        logging.error(f"Failed to watermark {image_path}: {e}")

# === Batch Process Multiple Images ===
def batch_watermark(input_folder, watermark_text, output_folder, opacity=128):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"watermarked_{filename}")
            add_watermark(input_path, watermark_text, output_path, opacity)

# === Main Console UI ===
def main():
    print("=== 🖼️ Image Watermarking Tool ===")
    print("1. Watermark single image")
    print("2. Watermark batch images")
    choice = input("Choose an option: ")

    if choice == "1":
        img = input("Enter path to image: ")
        text = input("Enter watermark text: ")
        out = input("Enter output path: ")
        opac = int(input("Enter transparency (0-255): "))
        add_watermark(img, text, out, opac)

    elif choice == "2":
        folder = input("Enter input folder path: ")
        text = input("Enter watermark text: ")
        out_folder = input("Enter output folder path: ")
        opac = int(input("Enter transparency (0-255): "))
        batch_watermark(folder, text, out_folder, opac)

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
