f = open('data/data.csv', 'r')
    
def makeData():
    dataTable = ''
    line = f.readline()
    while line:
        dataTable += '<tr>'
        for i in line.split(',')[:-1]:
            dataTable += ('<td>' + str(i) + '</td>')
            dataTable += '</tr>'
            line = f.readline()
    return dataTable

def analyzeData():
    dataTable = ''
    k = open('data/data.csv', 'r')
    f = open('data/data.csv', 'w')
    L = []
    L2 = []
    L3 = []
    Lyear = []
    line = k.readline()
    line = k.readline()
    while line:
        L.append(line.split(',')[1])
        Lyear.append(line.split(',')[0])
        line = k.readline()
        k.close()

    f.write('Year Interval' + ',' + 'Amount of change between every two years' + '\n')
    for i in range(1,len(Lyear)):
        L2.append(int(L[i]) - int(L[i-1]))
        L3.append(str(Lyear[i-1]) + '-' + str(Lyear[i]))
        f.write(Lyear[i-1] + '-' + Lyear[i] + ',' + str(int(L[i]) - int(L[i-1])) + '\n')
        f.close()

    w = open('data/data.csv', 'r')
    line = w.readline()
    while line:
        dataTable += '<tr>'
        for i in line.split(','):
            dataTable += ('<td bgcolor = "#EBB6FA">' + str(i) + '</td>')
            dataTable += '</tr>'
            dataTable += w.readline()
            w.close()

    L2 = L2[1:]
    for i in range(0,len(L2)):
        if L2[i] >= 0:
            dataTable += '<p>' + L3[i] + ': ' + (L2[i] * '=') + '</p>'
        else:
            dataTable += '<p>' + L3[i] + ': negative' + '</p>'
    return dataTable
