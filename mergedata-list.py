import collections
import csv

dataVRPs = list()
dataPrcls = list()
dataMgrd = list()

fnmVRPS = '/home/gibbs/SJIs/VacationRentals/Data/VRPs.csv'
fnmPrcls = '/home/gibbs/SJIs/VacationRentals/Data/Prcls.csv'
fnmMgrd = '/home/gibbs/SJIs/VacationRentals/Data/Mgrd.csv'

def init_Record(field_names):
    Record = collections.namedtuple('Record',field_names)
    return Record

def read_CSVs():
#    row = 0
    with open(fnmVRPS) as fin:
        csv_reader = csv.reader(fin)
        field_names = next(csv_reader)
#        print(field_names)
        rec = init_Record(field_names)
#        rows=0
        dataVRPs.clear()
        for row in csv_reader:
#            rows+=1
#            if rows>5:
#                break
            r = rec(*row)
            dataVRPs.append(r)
#   row = 0
    with open(fnmPrcls) as fin:
        csv_reader = csv.reader(fin)
        field_names = next(csv_reader)
#        print(field_names)
        rec = init_Record(field_names)
#        rows=0
        dataPrcls.clear()
        for row in csv_reader:
#            rows+=1
#            if rows>5:
#                break
            r = rec(*row)
            dataPrcls.append(r)

def main():
    read_CSVs()
    print(type(dataVRPs))
#    print('140422002000 ' in dataVRPs[].Parcel)
    test = []
    temp = []
    temp.extend(list(dataPrcls[0]))
    temp.extend(list(dataVRPs[0]))
    test.append(temp)
    print(test)
    res = any('140752003000 ' in sublist for sublist in dataVRPs)
    print(res)

if __name__ == '__main__':
    main()

