class FeatureBuilder:
    def transform(self, df):
        df["frequency_score"] = df["travel_frequency"] / df["travel_frequency"].max()
        df["value_score"] = df["loyalty_score"] / 100
        df["customer_score"] = (
            0.5 * df["frequency_score"] +
            0.3 * df["value_score"] +
            0.2 * (1 - df["past_claims"])
        )
        df.to_csv("data/features/feature_builder.csv", index=False)

        return df
