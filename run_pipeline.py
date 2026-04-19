import os
import pandas as pd
from engine.scanner import run
from engine.portfolio import build_portfolio
from ai.report import generate_report

def main():
    # ✅ ensure folder exists
    os.makedirs("output", exist_ok=True)

    symbols = pd.read_csv("data/symbols.csv")["Symbol"].tolist()

    df = run(symbols)

    df.to_csv("output/stocks.csv", index=False)

    portfolio = build_portfolio(df)
    portfolio.to_csv("output/portfolio.csv", index=False)

    report = generate_report(df.iloc[0])

    with open("output/report.txt", "w") as f:
        f.write(report)

    print("Pipeline completed.")

if __name__ == "__main__":
    main()