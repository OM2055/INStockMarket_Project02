def generate_report(stock):

    score = stock["alpha"]

    if score > 8:
        verdict = "High probability multi-bagger (5-10x potential)"
    elif score > 5:
        verdict = "Moderate growth (2-5x)"
    else:
        verdict = "Low growth potential"

    report = f"""
Stock: {stock['symbol']}

Price: {stock['price']}

Analysis:
- Momentum: {'Bullish' if stock['dma50'] > stock['dma200'] else 'Bearish'}
- PE Ratio: {stock['pe']}
- PB Ratio: {stock['pb']}
- Alpha Score: {score}

Conclusion:
{verdict}
"""

    return report