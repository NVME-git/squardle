import os
from PIL import Image, ImageDraw, ImageFont
from config import OUTPUT_DIR, CELL_SIZE, PADDING, FONT_SIZE


# =========================
# Image Generation
# =========================
def generate_image(
    grid: list[list[str]], rows: int, cols: int, word: str, path: list[tuple[int, int]]
) -> None:
    img_width = cols * CELL_SIZE + 2 * PADDING
    img_height = rows * CELL_SIZE + 2 * PADDING
    extra_height = 80
    img = Image.new("RGBA", (img_width, img_height + extra_height), "white")
    draw = ImageDraw.Draw(img)

    font = ImageFont.load_default(size=FONT_SIZE)

    # Draw grid
    for r in range(rows):
        for c in range(cols):
            x1 = PADDING + c * CELL_SIZE
            y1 = PADDING + r * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            fill_color = "white"
            if grid[r][c] == "#":
                fill_color = "lightgray"

            draw.rectangle([x1, y1, x2, y2], outline="black", fill=fill_color)

            if grid[r][c] != "#":
                letter = grid[r][c].upper()
                bbox = draw.textbbox((0, 0), letter, font=font)
                w = bbox[2] - bbox[0]
                h = bbox[3] - bbox[1]

                draw.text(
                    (x1 + (CELL_SIZE - w) / 2, y1 + (CELL_SIZE - h) / 2),
                    letter,
                    fill="black",
                    font=font,
                )

    # Draw path lines
    if path:
        points = []
        for r, c in path:
            x = PADDING + c * CELL_SIZE + CELL_SIZE // 2
            y = PADDING + r * CELL_SIZE + CELL_SIZE // 2
            points.append((x, y))

        draw.line(points, fill=(0, 0, 255, 128), width=5)

        # Highlight first and last
        for idx in [0, -1]:
            r, c = path[idx]
            x1 = PADDING + c * CELL_SIZE
            y1 = PADDING + r * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            draw.rectangle(
                [x1, y1, x2, y2], outline="red" if idx == -1 else "green", width=5
            )

    # Draw word below grid
    text = word.upper()
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]

    draw.text(
        ((img_width - w) / 2, img_height + 20),
        text,
        fill="black",
        font=font,
    )

    # Create subfolder based on word length
    word_len = len(word)
    letter_word = "letter" if word_len == 1 else "letters"
    subfolder = f"{word_len:02d}_{letter_word}"
    images_path = os.path.join(OUTPUT_DIR, "images", subfolder)

    if not os.path.exists(images_path):
        os.makedirs(images_path)

    # Convert RGBA to RGB before saving as PNG
    rgb_img = Image.new("RGB", img.size, "white")
    rgb_img.paste(img, mask=img.split()[3] if img.mode == "RGBA" else None)
    rgb_img.save(os.path.join(images_path, f"{word}.png"))
