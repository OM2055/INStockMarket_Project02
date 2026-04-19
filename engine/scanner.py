from concurrent.futures import ThreadPoolExecutor
import pandas as pd

from core.scraper import get_nse_data
from core.indicators import get_technical
from core.factors import compute_factors
from core.alpha import alpha_score

def process(symbol):

    base = get_nse_data(symbol)
    tech = get_technical(symbol)

    if not base or not tech:
        return None

    data = {**base, **tech}

    # dummy fundamentals (replace later)
    data["roe"] = 18
    data["growth"] = 15

    factors = compute_factors(data)
    data["alpha"] = alpha_score(factors)

    return data


def run(symbols):
    results = []

    with ThreadPoolExecutor(max_workers=15) as ex:
        futures = [ex.submit(process, s) for s in symbols]

        for f in futures:
            r = f.result()
            if r:
                results.append(r)

    df = pd.DataFrame(results)
    return df.sort_values("alpha", ascending=False)