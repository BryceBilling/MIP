import pygeoip
import csv


def main():
    results = open("C:/Users/Bryce Billing/Desktop/MIP/results.txt", 'wb')
    successUS = open("C:/Users/Bryce Billing/Desktop/MIP/USsuccess.txt", 'wb')
    successCh = open("C:/Users/Bryce Billing/Desktop/MIP/Chsuccess.txt", 'wb')
    successIra = open("C:/Users/Bryce Billing/Desktop/MIP/IRasuccess.txt", 'wb')
    successSA = open("C:/Users/Bryce Billing/Desktop/MIP/SAsuccess.txt", 'wb')

    with open("C:/Users/Bryce Billing/Desktop/MIP/america.txt", 'rb') as americafile:
        count = 0
        totalcount = 0
        for line in americafile:
            totalcount+=1
            if(getSuccess(line.replace('\n',''))):
                successUS.write(line)
                successUS.write('\n')
                count+=1
        results.write("America: "+ str(count)+ " / "+ str(totalcount)+'\n')
        print("Done america")

    with open("C:/Users/Bryce Billing/Desktop/MIP/china.txt", 'rb') as chinafile:
        count = 0
        totalcount = 0
        for line in chinafile:
            totalcount += 1
            if (getSuccess(line.replace('\n', ''))):
                successCh.write(line)
                successCh.write('\n')
                count += 1
        results.write("China: " + str(count) + " / " + str(totalcount) + '\n')
        print("Done china")

    with open("C:/Users/Bryce Billing/Desktop/MIP/iran.txt", 'rb') as iranfile:
        count = 0
        totalcount = 0
        for line in iranfile:
            totalcount += 1
            if (getSuccess(line.replace('\n', ''))):
                successIra.write(line)
                successIra.write('\n')
                count += 1
        results.write("Iran: " + str(count) + " / " + str(totalcount) + '\n')
        print("Done iran")

    with open("C:/Users/Bryce Billing/Desktop/MIP/southafrica.txt", 'rb') as southfile:
        count = 0
        totalcount = 0
        for line in southfile:
            totalcount += 1
            if (getSuccess(line.replace('\n', ''))):
                successSA.write(line)
                successSA.write('\n')
                count += 1
        results.write("South Africa: " + str(count) + " / " + str(totalcount) + '\n')
        print("Done south africa")

    print("Done")


def getSuccess(x):
    y = x.replace(': ',':')
    z= y.split(" ")
    a = z[8].split(':')
    if(int(a[1]) == 1):
        return True
    else:
        return False

if __name__ == '__main__':
    main()