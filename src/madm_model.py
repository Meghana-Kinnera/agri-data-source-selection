import numpy as np

def madm_ranking(data, weights=None):
    """
    Multi-Attribute Decision-Making (MADM) ranking
    """
    criteria = data.columns[1:]

    if weights is None:
        # Equal weights for all criteria
        weights = np.ones(len(criteria)) / len(criteria)

    scores = data[criteria].values @ weights

    data = data.copy()
    data["Final_Score"] = scores

    ranked_data = data.sort_values(by="Final_Score",ascending=False)
    ranked_data.insert(0, "Rank", range(1, len(ranked_data) + 1))

    return ranked_data