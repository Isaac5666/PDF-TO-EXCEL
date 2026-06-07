import fitz
import os


class PDFProcessor:

    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def pdf_to_images(self):

        pdf = fitz.open(self.pdf_path)

        image_paths = []

        os.makedirs("output/pages", exist_ok=True)

        for page_num in range(len(pdf)):

            page = pdf.load_page(page_num)

            zoom = 3

            matrix = fitz.Matrix(zoom, zoom)

            pix = page.get_pixmap(matrix=matrix)

            image_path = f"output/pages/page_{page_num + 1}.png"

            pix.save(image_path)

            image_paths.append(image_path)

        pdf.close()

        return image_paths