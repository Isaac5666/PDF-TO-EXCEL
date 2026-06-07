import json

from modules.pdf_processor import PDFProcessor
from modules.ocr_engine import OCREngine
from modules.document_classifier import DocumentClassifier
from modules.document_parser import DocumentParser
from modules.document_exporter import DocumentExporter
from modules.smart_extractor import SmartExtractor
from modules.final_validator import FinalValidator
from modules.excel_writer import ExcelWriter


def main():

    pdf_path = "input/document.pdf"

    processor = PDFProcessor(pdf_path)

    pages = processor.pdf_to_images()

    ocr = OCREngine()

    classifier = DocumentClassifier()

    parser = DocumentParser()

    print("\nRunning OCR...\n")

    for page in pages:

        try:

            text = ocr.extract_text(page)

        except Exception as e:

            print(
                f"OCR Error on {page}"
            )

            continue

        doc_type = classifier.classify(
            text
        )

        parser.add_document(
            doc_type,
            text
        )

    documents = parser.get_documents()

    DocumentExporter().export(
        documents
    )

    with open(
        "output/extraction_dump.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            documents,
            file,
            indent=4,
            ensure_ascii=False
        )

    extractor = SmartExtractor(
        documents
    )

    data = extractor.extract()

    validator = FinalValidator()

    data = validator.validate(
        data
    )

    with open(
        "output/final_data.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )

    print("\nSMART EXTRACTION\n")

    for key, value in data.items():

        print(
            f"{key}: {value}"
        )

    writer = ExcelWriter(
        "templates/Format.xlsx"
    )

    row = writer.write_data(
        data
    )

    print(
        f"\nWritten To Row {row}"
    )

    print(
        "\nExcel Saved: output/extracted.xlsx"
    )

    print(
        "JSON Saved: output/final_data.json"
    )


if __name__ == "__main__":
    main()