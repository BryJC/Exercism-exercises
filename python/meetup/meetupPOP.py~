from calendar import Calendar, day_name
cal_inst = Calendar()
from datetime import date

def meetup_day(year, month, name_of_day):
    
    # take first day of month and add appropriate time according to arguments
    # adding arguments: name_of_day(M, Tu, W, Th, Fr, Sa, Su) & day_of_month(1st, 2nd, 3rd, 4th, teenth, last) 
    
    # convert the names of days into a cardinal list --> [0-6]
    name_of_day_num_list = list(enumerate(day_name))
    for k, v in name_of_day_num_list:
        while name_of_day == v:
            name_of_day_num = k
            break
        else:
            pass
            
    #returns calendar iterator(tuple) for specified year, month (date.day#, wkday#)
    cal = list(cal_inst.itermonthdays2(year, month))
    
    #append a new list with all of that weekdays values (i.e. all Mondays, Tuesdays, etc.)
    new_list = [k for k, v in cal if v == name_of_day_num and k != 0]

    #enumerate new_list
    new_list = list(enumerate(new_list))
    
    return new_list
