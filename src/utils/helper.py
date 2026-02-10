def normalize_column(df, col):
    return (df[col] - df[col].min()) / (df[col].max() - df[col].min())
