import pygeoip
import csv
import reader2
file1 = open("C:/Users/Bryce Billing/Downloads/1t45u19qoikklizr-53-dns-lookup-full_ipv4-20160731T023001-zmap-results.csv", 'rb')
# file2 = open("C:/Users/Bryce Billing/Downloads/america.txt", 'wb')
# file3 = open("C:/Users/Bryce Billing/Downloads/southafrica.txt", 'wb')
# file4 = open("C:/Users/Bryce Billing/Downloads/china.txt", 'wb')
file5 = open("C:/Users/Bryce Billing/Downloads/iran.txt", 'wb')
reader = csv.reader(file1)
count = 0
country = ''
for row in reader:
    #count += 0
    ip1 = row[0].split(':')
    ip2 = ip1[1]
    gi = pygeoip.GeoIP('GeoIP.dat',1)
    ip2 = ip2.replace('"','')

    ip2 = ip2.replace(' ','')
    country = gi.country_name_by_addr(ip2)
    if(country is not None):
        # if(country == 'United States'):
        #     print('US')
        #     for item in row:
        #         file2.write("%s" % item)
        #     file2.write('\n')
        # elif(country == 'South Africa'):
        #     print(country)
        #     for item in row:
        #         file3.write("%s" % item)
        #     file3.write('\n')
        # elif(country == 'China'):
        #     print(country)
        #     for item in row:
        #         file4.write("%s" % item)
        #     file4.write('\n')
        if (country == 'Iran, Islamic Republic of'):
            print(country)
            for item in row:
                file5.write("%s" % item)
            file5.write('\n')
    else:
        print ('none')
        
    #if(count == 1):
        #break
file1.close()
# file2.close()
# file3.close()
# file4.close()
file5.close()
print ("Done")
