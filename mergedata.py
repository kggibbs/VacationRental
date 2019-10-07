import csv

dataVRPs = {}
dataPrcls = {}
dataMgrd = []
parpers = []

fnmVRPS = '/home/gibbs/SJIs/VacationRentals/Data/VRs.csv'
fnmPrcls = '/home/gibbs/SJIs/VacationRentals/Data/Prcls.csv'
fnmMgrd = '/home/gibbs/SJIs/VacationRentals/Data/Mgrd.csv'

#def init_Record(field_names):
#    Record = collections.namedtuple('Record',field_names)
#    return Record

colnmsVRPS = ''
colnmsPrcls = ''

def parPper(par,per):
    parper = par+' '+per
    if parper in parpers:
        print(parper, 'is already in the list')
    parpers.append(parper)
    return parper

def parMper(parper):
    return str.split(parper,' ')[0]

def read_CSVs():
    global colnmsVRPS, colnmsPrcls
    with open(fnmVRPS) as fin:
        csv_reader = csv.reader(fin)
        colnmsVRPS = next(csv_reader)
        for row in csv_reader:
            parper = parPper(row[4],row[3])
            dataVRPs[parper] = row
    with open(fnmPrcls) as fin:
        csv_reader = csv.reader(fin)
        colnmsPrcls = next(csv_reader)
        for row in csv_reader:
            dataPrcls[row[3]] = row

def merge_recds():
    global dataMgrd
    for parper in dataVRPs.keys():
        par = parMper(parper)
        if par in dataPrcls:
            rec = dataPrcls[par]+dataVRPs[parper]
            dataMgrd.append(rec)
        else:
            print('missing key in dataPrcls',par)

def main():
    read_CSVs()
    merge_recds()
    colnmsMrgd = colnmsPrcls+colnmsVRPS
    with open('MrgdRecs.csv', 'w') as writeFile:
        writeFile.write(','.join(colnmsMrgd))
        writeFile.write('\n')
        writer = csv.writer(writeFile)
        writer.writerows(dataMgrd)

if __name__ == '__main__':
    main()

