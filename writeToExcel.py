import xlwt

def writeToExcel(id_list, fileName, sheetName="UsersID"):
	#Init workbook 
	wb = xlwt.Workbook()

	#Add sheet
	ws = wb.add_sheet(sheetName)

	#Write to sheet
	for i in range(len(id_list)):
		ws.write(i, 0, id_list[i])

	#Saving in file
	wb.save(fileName)