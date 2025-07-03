import matplotlib.pyplot as plt
import numpy as np 

char_dict = {
    # Uppercase A-Z
    "A": [1,1,1,0,0,1,0,0,1],
    "B": [1,1,1,1,0,0,1,0,1],
    "C": [1,1,1,1,0,0,1,1,1],
    "D": [1,1,1,0,0,1,1,1,1],
    "E": [1,1,1,1,0,0,1,0,0],
    "F": [1,1,1,1,0,0,1,0,1],
    "G": [1,1,1,1,0,1,1,1,0],
    "H": [1,0,1,1,1,1,1,0,1],
    "I": [1,1,1,0,1,0,1,1,1],
    "J": [0,0,1,0,0,1,1,1,1],
    "K": [1,1,1,1,0,1,1,0,0],
    "L": [1,0,0,1,0,0,1,1,1],
    "M": [1,0,1,1,0,0,1,1,1],
    "N": [1,1,1,1,0,1,1,0,1],
    "O": [1,1,1,1,0,1,1,1,1],
    "P": [1,1,1,1,0,1,1,0,0],
    "Q": [1,0,0,1,1,1,1,0,1],
    "R": [1,1,1,1,0,0,1,1,0],
    "S": [0,1,1,0,1,0,1,1,1],
    "T": [1,1,1,0,1,0,0,1,0],
    "U": [1,0,1,1,0,1,1,1,1],
    "V": [1,0,1,1,0,1,1,1,0],
    "W": [1,0,1,1,0,1,0,1,1],
    "X": [1,1,1,1,0,1,0,1,1],
    "Y": [1,1,1,0,0,1,0,1,1],
    "Z": [1,1,1,1,0,1,1,1,0],

    # Digits 0–9
    "0": [1,1,1,1,1,1,1,1,1],
    "1": [0,0,1,0,0,0,1,1,1],
    "2": [1,0,1,0,0,0,1,1,1],
    "3": [1,1,0,0,0,0,1,1,1],
    "4": [0,1,1,0,0,0,1,1,1],
    "5": [1,0,1,1,0,1,1,0,1],
    "6": [1,1,1,0,0,0,0,0,1],
    "7": [1,1,1,0,0,0,1,0,1],
    "8": [1,1,1,0,0,0,1,1,0],
    "9": [1,1,1,0,0,0,0,1,1],

    # ASCII punctuation (printable symbols)
    "!": [1,1,1,0,0,0,0,1,0],
    "\"": [1,0,1,0,0,0,0,0,0],
    "#": [1,0,1,0,1,0,1,0,1],
    "$": [1,1,0,1,0,1,1,1,1],
    "%": [1,1,0,0,1,1,0,0,1],
    "&": [1,1,0,0,1,1,1,0,1],
    "'": [1,0,0,0,0,0,0,0,0],
    "(": [0,0,1,0,1,0,0,1,1],
    ")": [1,0,0,0,1,0,1,1,0],
    "*": [1,1,1,0,1,0,0,0,0],
    "+": [0,1,0,1,1,1,0,1,0],
    ",": [0,0,0,1,1,0,0,1,0],
    "-": [0,0,0,1,1,1,0,0,0],
    ".": [0,0,0,0,0,0,1,0,0],
    "/": [1,0,0,1,0,0,1,1,0],
    ":": [1,0,0,0,0,0,1,0,0],
    ";": [1,0,0,0,0,0,1,1,0],
    "<": [0,0,1,0,1,0,0,0,1],
    "=": [1,1,1,0,0,0,1,1,1],
    ">": [1,0,0,0,1,0,1,0,0],
    "?": [1,1,1,0,0,1,0,1,0],
    "@": [0,1,1,1,0,1,1,1,0],
    "[": [0,1,1,0,1,0,0,1,1],
    "\\": [1,1,0,0,1,0,0,1,0],
    "]": [1,1,0,0,1,0,1,1,0],
    "^": [0,1,0,1,0,1,0,0,0],
    "_": [0,0,0,0,0,0,1,1,1],
    "`": [1,1,0,0,0,0,0,0,0],
    "{": [1,1,0,1,0,1,1,1,0],
    "|": [0,1,0,0,1,0,0,1,0],
    "}": [0,1,1,1,0,1,0,1,1],
    "\t": [0,0,0,0,0,0,0,0,0],
    "~": [0,1,0,1,1,1,0,0,0],
    " ": [0,0,0,0,0,0,0,0,0],  # space

    # Unknown
    "unknown": [1,0,1,0,1,0,1,0,1]
}

text = "Hello world! \nWe gather here today to witness the new world of living, with my muse, Navi, I shall conquer the new world! Would my love prevail, perhaps?\nThat I have no idea, but I have leared to automate my fuckass language from when I was dumb and 16, which is worth it, I suppose. I am net worth 500 Pesos, so no one really cares.\nThey say it is the duty of the conquered to wallow upon their master's whims, which is saddening, definitely, but something people really find no problem addressing. What with life being fucked and all that shit. All I pray now is that I am united with my dear Navi, who I have not seen for 3 moons now. What a shame.\n Is it possible to automate text this way? Is it even fair, and I suppose not. We fit all that we can in such a small space that it is hardly wondrous to observe.\n\n What is 1+1? That is the question, is it not, to find symbold such that 1+1=2, or such and so other combinations of the 10 other or 125 other fucking combinations. What is it, then; We know not how we serve, but how to serve."

text = "The lion does not concern himself with the opinion of the small dog that barks\n And it is in fact more economical to do so, I suppose.\n 10+1 = 11\n I have 1,000,000 gold in rise of kingdoms\n The lion rapes the small dog when it barks. 69, nice.\n [How small is this, then?]\t there is no try"

with open(r"vercil_hub\js\text.txt", "r", encoding="utf-8") as file:
    text = file.read()
print(text)
def encoder(text, imsave=False, text_width=35, hyphenate = False, indent = 0):
    if "-" not in char_dict:
        raise ValueError("char_dict must contain '-' for overflow indicator.")

    glyph_height, glyph_width = 3, 3
    hspace, vspace = 1, 1  # 1px spacing between glyphs and lines

    # Step 1: Parse text and handle wrapping + newlines
    logical_lines = []
    for paragraph in text.split('\n'):
        paragraph = paragraph.strip()
        if paragraph.startswith("\t"):
            paragraph = "  " + paragraph
        paragraph = " "*indent + paragraph
        while len(paragraph) > text_width:
            if hyphenate:
                logical_lines.append(paragraph[:text_width - 1] + "-") #// Hyphen padding
                paragraph = paragraph[text_width - 1:]
            else:
                logical_lines.append(paragraph[:text_width])
                paragraph = paragraph[text_width:]
        logical_lines.append(paragraph)
        logical_lines.append(None)  # Treat \n as a full blank row

    if logical_lines and logical_lines[-1] is None:
        logical_lines.pop()  # remove trailing None

    # Step 2: Render each line
    rendered_lines = []
    for line in logical_lines:
        if line is None:
            # Full blank line (3px height), to be padded later
            rendered_lines.append(np.zeros((glyph_height, 1), dtype=int))
            continue

        row_glyphs = []
        for idx, char in enumerate(line):
            upper_char = char.upper()
            glyph = np.array(char_dict.get(upper_char, char_dict["unknown"])).reshape(glyph_height, glyph_width)
            row_glyphs.append(glyph)
            if idx != len(line) - 1:
                row_glyphs.append(np.zeros((glyph_height, hspace), dtype=int))  # horizontal gap

        if row_glyphs:
            full_row = np.hstack(row_glyphs)
            rendered_lines.append(full_row)
            rendered_lines.append(np.zeros((vspace, full_row.shape[1]), dtype=int))  # normal 1px vertical gap

    if rendered_lines and rendered_lines[-1].shape[0] != glyph_height:
        rendered_lines.pop()  # remove final vspace if present

    # Step 3: Pad all lines to same width
    max_width = max(row.shape[1] for row in rendered_lines)
    for i, row in enumerate(rendered_lines):
        if row.shape[1] < max_width:
            pad = np.zeros((row.shape[0], max_width - row.shape[1]), dtype=int)
            rendered_lines[i] = np.hstack([row, pad])

    # Step 4: Stack and display
    final_img = np.vstack(rendered_lines)
    plt.imshow(1 - final_img, cmap='gray', vmin=0, vmax=1)
    plt.axis('off')
    plt.show()

    # Save if requested
    if imsave:
        from PIL import Image
        Image.fromarray((1 - final_img) * 255).convert("L").save("encoded_text.png")

    return final_img

encoder(text)
def decoder():
    pass