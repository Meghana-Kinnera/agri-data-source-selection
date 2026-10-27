def hesitant_fuzzy_score(value):
    """
    Generate hesitant fuzzy membership values
    and compute average score
    """
    hesitant_values = [
        value,
        max(0, value - 0.05),
        min(1, value + 0.05)
    ]
    return sum(hesitant_values) / len(hesitant_values)

def apply_hesitant_fuzzy(data):
    """
    Apply hesitant fuzzy logic to all criteria
    """
    hf_data = data.copy()
    numeric_columns = data.select_dtypes(include='number').columns

    for col in numeric_columns:
        hf_data[col] = data[col].apply(hesitant_fuzzy_score)

    return hf_data