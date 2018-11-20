import csv
with open('abc.txt') as t:
    k=['cname','complaint']
    writer=csv.DictWriter(t,k)
    writer.writeheader()
    writer.writerow({'cname':'customer1','complaint':'98'})
    writer.writerow({'cname':'customer2','complaint':'54'})
    writer.writerow({'cname':'customer3','complaint':'45'})
    writer.writerow({'cname':'customer4','complaint':'54'}) 
with open('abc.txt') as t:
    reader=csv.DictReader(t)
    for i in reader:
        print(i)