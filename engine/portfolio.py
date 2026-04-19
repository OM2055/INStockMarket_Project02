def build_portfolio(df):

    df = df.head(10)

    total = df["alpha"].sum()

    df["weight"] = df["alpha"] / total

    return df