def classify_season(month: int) -> str:
    if month in [3, 4, 5]:
        return "spring"
    elif month in [9, 10, 11]:
        return "fall"
    else:
        return "other"