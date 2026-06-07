import cv2
from pyzbar.pyzbar import decode


class QRScanner:

    def preprocess(self, image):

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        gray = cv2.equalizeHist(gray)

        gray = cv2.GaussianBlur(gray, (3, 3), 0)

        _, thresh = cv2.threshold(
            gray,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        return thresh

    def scan_qr(self, image_path):

        image = cv2.imread(image_path)

        processed = self.preprocess(image)

        decoded_objects = decode(processed)

        results = []

        for obj in decoded_objects:

            try:
                results.append(
                    obj.data.decode("utf-8")
                )

            except:
                pass

        return results