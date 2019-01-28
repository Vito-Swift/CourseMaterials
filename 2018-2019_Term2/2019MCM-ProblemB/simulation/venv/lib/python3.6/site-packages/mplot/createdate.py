import datetime

'''
25-Nov-13 15:30:00
1/10/2012 0:24:23
'''


MONTH = {
'Jan':1,
'Feb':2,
'Mar':3,
'Apr':4,
'May':5,
'Jun':6,
'Jul':7,
'Aug':8,
'Sep':9,
'Oct':10,
'Nov':11,
'Dec':12
}





def convertdateslash(string):
	'''
	15/01/2008
	'''
	bits = string.split('/')
	year = int(bits[2])
	month = int(bits[1])
	day = int(bits[0])
	return year,month,day

def convertdatedash(string):
	'''
	25-Nov-13
	2012-01-01
	'''
	t1,month,t2 = string.split('-')
	if MONTH.has_key(month):
		return convertcrazydash(t2,month,t1)
	year = int(t1)
	day = int(t2)
	month = int(month)
	return year,month,day

def convertcrazydash(year,month,day):
	'''
	25-Nov-13
	'''
	day = int(day)
	month = MONTH[month]
	year = 2000+ int(year)
	return year,month,day
	
def convertdate(rawstring):
        string = rawstring.replace('"','')
        if '/' in string:
                return convertdateslash(string)
        if '-' in string:
                return convertdatedash(string)
        raise Exception()
	
	
def converttime(rawtime):
        time = rawtime.replace('"','')
        mytime = [0,0,0]
        bits = time.split(':')
        for i in range(0,len(bits)):
                mytime[i] = int(bits[i])
        return tuple(mytime)
	
	
def convertdatetime(string):
        #print(string)
        if ' ' in string:
                date,time = string.split(' ')
                hour,minute,second = converttime(time)
        else:
                hour = 0
                minute = 0
                second = 0
                date = string
        year,month,day = convertdate(date)
        return datetime.datetime(year,month,day,hour,minute,second)

def getdate(rawstring):
        string = rawstring.split(' ')[0]
        y,m,d = convertdate(string)
        return datetime.datetime(y,m,d)
