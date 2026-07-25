from PIL import Image, ImageDraw, ImageFont

# Load your generated background image
img = Image.open("sticker_studio.png")
draw = ImageDraw.Draw(img)

# Load a pixel font (or default to a standard font)
# Replace 'PressStart2P-Regular.ttf' with your preferred pixel font file path
font = ImageFont.truetype("PressStart2P-Regular.ttf", size=16)

# Colors (Hex or RGB)
text_color = (40, 30, 60)

# --- 1. Fill in Menu Items (Top-Right Container) ---
menu_items = [
    "1. Custom Stickers",
    "2. Vinyl Prints",
    "3. Holographic",
    "4. Drip Pins",
    "5. Exit Studio"
]

# Set starting X, Y coordinates for the menu box
menu_x = 760
menu_y = 120
line_height = 28

for i, item in enumerate(menu_items):
    draw.text((menu_x, menu_y + (i * line_height)), item, fill=text_color, font=font)

# --- 2. Fill in Dialogue Bubble (Bottom Container) ---
dialogue_text = "Hey there~♪"
dialogue_x = 50
dialogue_y = 920

draw.text((dialogue_x, dialogue_y), dialogue_text, fill=text_color, font=font)

# Save the final image
img.save("sticker_studio_with_text.png")
