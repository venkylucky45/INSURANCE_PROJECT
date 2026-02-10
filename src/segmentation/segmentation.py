from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pickle

class SegmentationModel:
    def __init__(self, path):
        self.path = path

    def train(self, df):
        features = df[["travel_frequency", "loyalty_score", "past_claims"]]
        model = KMeans(n_clusters=4, random_state=42)
        df["segment"] = model.fit_predict(features)
        pickle.dump(model, open(self.path, "wb"))
        return df

    def predict(self, data):
        model = pickle.load(open(self.path, "rb"))
        sil_score = silhouette_score(data, model.labels_)
        print("Silhouette Score:", sil_score)
        return model.predict(data)

    