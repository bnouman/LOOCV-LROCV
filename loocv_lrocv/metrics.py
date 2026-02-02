from scipy.stats import somersd

def cindex(true, pred) -> float:
    s_d = somersd(true, y=pred, alternative="two-sided")
    return (s_d.statistic + 1.0) / 2.0
