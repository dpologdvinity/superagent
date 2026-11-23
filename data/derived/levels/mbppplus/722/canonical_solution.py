def filter_data(students,h,w):
    return {k: s for k, s in students.items() if s[0] >= h and s[1] >= w}
