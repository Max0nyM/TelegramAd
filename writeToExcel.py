import xlwt

def writeToExcel(id_list, fileName):
	#Init 
	wb = xlwt.Workbook()
	ws = wb.add_sheet("UsersID")

	#Write to sheet
	for i in range(len(id_list)):
		ws.write(i, 0, id_list[i])

	wb.save(fileName)


