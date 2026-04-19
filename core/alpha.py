def alpha_score(f):
    return (
        f["momentum"] * 2 +
        f["quality"] * 0.2 +
        f["growth"] * 0.3 +
        f["value"] * 1
    )