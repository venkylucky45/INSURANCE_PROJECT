class DataPreprocessing:
    def clean(self, df):
        df = df.drop_duplicates()
        df["loyalty_score"] = df["loyalty_score"].fillna(df["loyalty_score"].median())
        df["past_claims"] = df["past_claims"].fillna(0)
        df.to_csv("data/processed/clean_df.csv", index=False)
        return df
