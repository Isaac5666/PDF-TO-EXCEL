class ConfidenceEngine:

    def calculate(self, data):

        total = len(data)

        found = 0

        for value in data.values():

            if value:
                found += 1

        if total == 0:
            return 0

        return round(
            (found / total) * 100,
            2
        )