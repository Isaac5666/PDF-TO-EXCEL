import os


class DocumentExporter:

    def export(self, documents):

        os.makedirs(
            "output/documents",
            exist_ok=True
        )

        for doc_type, pages in documents.items():

            path = (
                f"output/documents/"
                f"{doc_type}.txt"
            )

            with open(
                path,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(
                    "\n\n".join(pages)
                )