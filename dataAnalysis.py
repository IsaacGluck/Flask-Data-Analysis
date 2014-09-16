f = open('data/data.csv', 'r')
    
def makeData():
    dataTable = ""
    line = f.readline()
    while line:
        dataTable += '<tr>'
        for i in line.split(',')[:-1]:
            dataTable += ('<td>' + str(i) + '</td>')
            dataTable += '</tr>'
            line = f.readline()
    return dataTable
