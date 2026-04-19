def compute_factors(data):

    momentum = 1 if data["dma50"] > data["dma200"] else 0

    quality = data.get("roe", 15)
    value = 1 / max(data.get("pe", 1), 1)
    growth = data.get("growth", 15)

    return {
        "momentum": momentum,
        "quality": quality,
        "value": value,
        "growth": growth
    }