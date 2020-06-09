# outputs the total minutes, given days and hours
# outputs days, hours and minutes, given total minutes
def minutes(days, hours, minutes):
	return 1440*days + 60*hours + minutes       #returns total number of minutes given number of days, hours and minutes

def daysHoursMinutes(minutes):
    return minutes//1440, minutes//60, minutes%60   #converts minutes to days, hours and minutes

'''
Test Case:
>>> minutes(2, 50, 12)
5892
>>> daysHoursMinutes(241)
(0, 4, 1)
'''
