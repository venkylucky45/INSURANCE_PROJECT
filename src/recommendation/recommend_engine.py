class RecommendEngine:
    def recommend(self, segment):
        mapping = {
            0: "Premium Frequent Traveler Plan",
            1: "Seasonal Coverage Plan",
            2: "Business Flyer Plan",
            3: "Basic Travel Protection"
        }
        return mapping.get(segment, "General Travel Plan")
