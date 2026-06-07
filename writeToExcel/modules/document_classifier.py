class DocumentClassifier:

    def classify(self, text):

        text = text.upper()

        if "DEATH CERTIFICATE" in text:
            return "death_certificate"

        elif "AADHAAR" in text:
            return "aadhaar"

        elif "CLAIM FORM" in text:
            return "claim_form"

        elif "CERTIFICATE OF INSURANCE" in text:
            return "insurance"

        elif "MEDICAL ATTENDANT" in text:
            return "medical"

        elif "DISCHARGE SUMMARY" in text:
            return "hospital"

        return "unknown"