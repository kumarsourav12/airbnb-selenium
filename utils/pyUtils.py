from datetime import date

def getCurrentDateOnly():
    today = date.today()
    return today.day

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month