'''def centuryFromYear(year):
	years=year%100
	century=year-years
	count =0
	if year%100==0:
		count=century//100
		print(count)
	elif year>century:
		count=user//100
		count+=1
		print(count)

user=int(input("Enter the year: "))
centuryFromYear(user)



function centuryFromYear(year) {
    if (year%100===0){
        return parseInt(year/100);
    }
    else{
        return parseInt(year/100+1);
    }

}
'''

def centuryFromYear(year):
	if year%100==0:
		return year//100
	else:
		return year//100+1

user=int(input("Enter the year: "))
print(centuryFromYear(user))