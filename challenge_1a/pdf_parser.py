from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBoxHorizontal, LTTextLineHorizontal, LTChar
from collections import defaultdict, Counter
import re

def extract_structure(pdf_path):
    headings = []
    font_sizes = []
    fonts = defaultdict(list)
    first_page_title = ""
    first_page_fonts = []

    for page_num, page_layout in enumerate(extract_pages(pdf_path)):
        for element in page_layout:
            if isinstance(element, LTTextBoxHorizontal):
                for line in element:
                    if isinstance(line, LTTextLineHorizontal):
                        line_text = line.get_text().strip()
                        if not line_text:
                            continue

                        sizes = []
                        fontnames = []

                        for char in line:
                            if isinstance(char, LTChar):
                                sizes.append(round(char.size, 1))
                                fontnames.append(char.fontname)

                        if not sizes:
                            continue

                        avg_size = round(sum(sizes)/len(sizes), 1)
                        font_key = f"{avg_size}-{fontnames[0]}"

                        # Store text and page for each font cluster
                        font_sizes.append(avg_size)
                        fonts[font_key].append((line_text, page_num))

                        if page_num == 0:
                            first_page_fonts.append((avg_size, line_text))

    # Identify font size hierarchy
    size_counter = Counter(font_sizes)
    size_levels = sorted([size for size, _ in size_counter.most_common()], reverse=True)

    def get_heading_level(size):
        if not size_levels:
            return None
        if size >= size_levels[0]:
            return "H1"
        elif len(size_levels) > 1 and size >= size_levels[1]:
            return "H2"
        elif len(size_levels) > 2 and size >= size_levels[2]:
            return "H3"
        return None

    # Title: First page largest text
    if first_page_fonts:
        first_page_fonts.sort(reverse=True)
        first_page_title = first_page_fonts[0][1]

    for font_key, entries in fonts.items():
        size = float(font_key.split("-")[0])
        level = get_heading_level(size)
        if level:
            for text, page in entries:
                clean_text = re.sub(r"\s+", " ", text).strip()
                if len(clean_text.split()) < 2 or len(clean_text) > 300:
                    continue
                headings.append({
                    "level": level,
                    "text": clean_text,
                    "page": page
                })

    return {
        "title": first_page_title.strip(),
        "outline": headings
    }
