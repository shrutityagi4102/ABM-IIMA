import Individual
import World
import xlsxwriter

whole = Individual.sim() #GETTING THE INDIVIDUAL FROM INDIVIDUAL FILE
workbook = xlsxwriter.Workbook('ans.xlsx') #MAKING THE EXCEL FILE
worksheet = workbook.add_worksheet('Individual') #MAKING THE INDIVIDUAL SHEET
#ASSIGNING COLUMNS
worksheet.write('A1', 'SimTime')
worksheet.write('B1', 'IndiId')
worksheet.write('C1', 'Assigned Location')
colu = 3
for i in range(len(Individual.ng)):
    worksheet.write(0,colu,Individual.ng[i][0])
    colu+=1
for i in range(len(Individual.errng)):
    worksheet.write(0,colu,Individual.errng[i][0])
    colu+=1
for i in range(len(Individual.loc)):
    worksheet.write(0,colu,Individual.loc[i][0])
    colu+=1
for i in range(len(Individual.cst)):
    worksheet.write(0,colu,Individual.cst[i][0])
    colu+=1
for i in range(len(Individual.errcst)):
    worksheet.write(0,colu,Individual.errcst[i][0])
    colu+=1
for i in range(len(Individual.inst)):
    worksheet.write(0,colu,Individual.inst[i][0])
    colu+=1
for i in range(len(Individual.errinst)):
    worksheet.write(0,colu,Individual.errinst[i][0])
    colu+=1
for i in range(len(Individual.endw)):
    worksheet.write(0,colu,Individual.endw[i][0])
    colu+=1
for i in range(len(Individual.errendw)):
    worksheet.write(0,colu,Individual.errendw[i][0])
    colu+=1
for i in range(len(Individual.avail)):
    worksheet.write(0,colu,Individual.avail[i][0])
    colu+=1
for i in range(len(Individual.erravail)):
    worksheet.write(0,colu,Individual.erravail[i][0])
    colu+=1
#FILLING THE COLUMNS AS PER THE VALUE OF INDIVIDUAL
row ,column, c = 1, 0, 1
content = list(whole.keys())
for item in content :
    worksheet.write(row, column, item)
    q = whole[item]
    for k in Individual.indids:
        worksheet.write(row, c, k)
        worksheet.write(row, c+1, q[k][0])
        col = c+1
        for i in range(len(Individual.ng)):
            col += 1
            worksheet.write(row, col, q[k][1][0][i][-1])
        for i in range(len(Individual.errng)):
            col += 1
            worksheet.write(row, col, q[k][1][1][i][-1])
        for i in range(len(Individual.loc)):
            col += 1
            worksheet.write(row, col, q[k][1][2][i][-1])
        for i in range(len(Individual.cst)):
            col += 1
            worksheet.write(row, col, q[k][1][3][i][-1])
        for i in range(len(Individual.errcst)):
            col += 1
            worksheet.write(row, col, q[k][1][4][i][-1])
        for i in range(len(Individual.inst)):
            col += 1
            worksheet.write(row, col, q[k][1][5][i][-1])
        for i in range(len(Individual.errinst)):
            col += 1
            worksheet.write(row, col, q[k][1][6][i][-1])
        for i in range(len(Individual.endwcst)):
            col += 1
            worksheet.write(row, col, q[k][1][7][i][-1])
        for i in range(len(Individual.errendwcst)):
            col += 1
            worksheet.write(row, col, q[k][1][8][i][-1])
        for i in range(len(Individual.endwavail)):
            col += 1
            worksheet.write(row, col, q[k][1][9][i][-1])
        for i in range(len(Individual.errendwavail)):
            col += 1
            worksheet.write(row, col, q[k][1][10][i][-1])
        row += 1
        
#MAKING THE WORLD SHEET
works = workbook.add_worksheet('World')
wholeworld = World.population #GETTING THE WORLD INFORMATION FROM THE WORLD FILE
#ASSIGNING COLUMNS
works.write('A1', 'WorldID')
worrow,worcolumn = 1,0
allwids = list(wholeworld.keys())
worcolumn += 1
for i in range(len(World.endwtoidlist)):
    works.write(0,worcolumn,World.endwtoidlist[i])
    worcolumn+=1
for i in range(len(World.errendwtoidlist)):
    works.write(0,worcolumn,World.errendwtoidlist[i])
    worcolumn+=1
for i in range(len(World.prdtotnslist)):
    works.write(0,worcolumn,World.prdtotnslist[i])
    worcolumn+=1
for i in range(len(World.endwvalidlist)):
    works.write(0,worcolumn,World.endwvalidlist[i])
    worcolumn+=1
for i in range(len(World.errendwvalidlist)):
    works.write(0,worcolumn,World.errendwvalidlist[i])
    worcolumn+=1
#FILLING THE COLUMNS AS PER THE VALUE OF WORLD
wrow ,wcolumn = 1,0
for item in allwids :
    works.write(wrow, wcolumn, item)
    q = wholeworld[item]
    wc = 0
    for i in range(len(World.endwtoidlist)):
        wc += 1
        works.write(wrow, wc, q[0][i][-1])
    for i in range(len(World.errendwtoidlist)):
        wc += 1
        works.write(wrow, wc, q[1][i][-1])
    for i in range(len(World.prdtotnslist)):
        wc += 1
        works.write(wrow, wc, q[2][i][-1])
    for i in range(len(World.endwvalidlist)):
        wc += 1
        works.write(wrow, wc, q[3][i][-1])
    for i in range(len(World.errendwvalidlist)):
        wc += 1
        works.write(wrow, wc, q[4][i][-1])
    wrow+=1
workbook.close()