class DocumentParser:

    def __init__(self):
        self.documents = {
            "insurance": [],
            "claim_form": [],
            "death_certificate": [],
            "aadhaar": [],
            "medical": [],
            "hospital": [],
            "unknown": []
        }

    def add_document(
        self,
        doc_type,
        text
    ):

        self.documents[doc_type].append(text)

    def get_documents(self):

        return self.documents