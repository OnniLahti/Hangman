
def is_date(date):
    year, month, day = date.split('-')
    error_count = 0

    if year.isdigit() == False or month.isdigit() == False or day.isdigit() == False:
        return False
        
    if int(year) < 0:
        error_count += 1
    if int(month) < 0 or int(month) > 12:
        error_count += 1
    if int(day) < 0 or int(day) > 31:
        error_count += 1

    return True if error_count == 0 else False