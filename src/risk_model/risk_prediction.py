# from xgboost import XGBClassifier
# import pickle

# class RiskModel:
#     def __init__(self, path):
#         self.path = path

#     def train(self, df):
#         X = df[["age", "travel_frequency", "loyalty_score", "segment"]]
#         y = df["risk_score"]
#         model = XGBClassifier()
#         model.fit(X, y)
#         pickle.dump(model, open(self.path, "wb"))
#         return model

#     def predict(self, X):
#         model = pickle.load(open(self.path, "rb"))
#         return model.predict(X)

from xgboost import XGBRegressor
import pickle

class RiskModel:
    def __init__(self, path):
        self.path = path

    def train(self, df):
        X = df[["age", "travel_frequency", "loyalty_score", "segment"]]
        y = df["risk_score"]                   # continuous value
        model = XGBRegressor()
        model.fit(X, y)

        pickle.dump(model, open(self.path, "wb"))
        return model

    def predict(self, X):
        model = pickle.load(open(self.path, "rb"))
        return model.predict(X)
