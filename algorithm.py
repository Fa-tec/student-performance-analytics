# Student Performance Analytics - Weak Area Identification (FR2)

def identify_weak_areas(marks, threshold=50):
    weak_count = 0
    status = []

    for i in range(len(marks)):
        if marks[i] < threshold:
            status.append("Weak")
            weak_count += 1
        else:
            status.append("Satisfactory")

    return status, weak_count
