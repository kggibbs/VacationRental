import collections
import csv

dataVRPs = {}
dataPrcls = {}
dataMgrd = {}

fnmVRPS = '/home/gibbs/SJIs/VacationRentals/Data/VRPs.csv'
fnmPrcls = '/home/gibbs/SJIs/VacationRentals/Data/Prcls.csv'
fnmMgrd = '/home/gibbs/SJIs/VacationRentals/Data/Mgrd.csv'

def init_Record(field_names):
    Record = collections.namedtuple('Record',field_names)
    return Record

def read_CSVs():
    rows = 0
    with open(fnmVRPS) as fin:
        csv_reader = csv.reader(fin)
        field_names = next(csv_reader)
        rec = init_Record(field_names)
        dataVRPs.clear()
        for row in csv_reader:
            rows += 1
            if rows > 6:
                break
            r = rec(*row)
            dataVRPs[r.Parcel] = r
    rows = 0
    with open(fnmPrcls) as fin:
        csv_reader = csv.reader(fin)
        field_names = next(csv_reader)
        rec = init_Record(field_names)
        dataPrcls.clear()
        for row in csv_reader:
            rows += 1
            if rows > 6:
                break
            r = rec(*row)
            dataPrcls[r.PIN] = r

#def merge_recds():
    # if dict.has_key(key):
    #     print
    #     "Present, value =", dict[key]
    # else:
    #     print
    #     "Not present"
    #     a.update(b)
#        basket = dict(basket_one, **basket_two)

        # with open(csv_file, 'w') as csvfile:
        #     writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        #     writer.writeheader()
        #     for data in dict_data:
        #         writer.writerow(data)

def main():
    read_CSVs()
    # print(dataVRPs['140752003000 '])
    # print(dataPrcls['140752003000 '])

    with open('test.csv', 'w') as csvfile:
        newdict = dict(dataPrcls,**dataVRPs)
        print(newdict)
        print(type(newdict))
        csv_columns = newdict.keys()
        print(csv_columns)
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in newdict:
            writer.writerow(data)

if __name__ == '__main__':
    main()

