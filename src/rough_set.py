def rough_set_approximation(data):
    """
    Compute lower and upper approximations
    using rough set theory
    """
    numeric_data = data.select_dtypes(include="number")

    lower_approximation = numeric_data.min()
    upper_approximation = numeric_data.max()

    return lower_approximation, upper_approximation