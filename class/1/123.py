def determine_grade(scores):
    if scores >= 90:
        return 'A'
    elif scores >= 80:
        return 'B'
    elif scores >= 70:
        return 'C'
    elif scores >= 60:
        return 'D'
    elif scores >= 50:
        return 'E'
    else:
        return 'F'