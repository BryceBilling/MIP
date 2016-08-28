

def main():
    uniquenessCount = open("C:/Users/Bryce Billing/Desktop/MIP/uniqueness.txt", 'wb')

    with open("C:/Users/Bryce Billing/Desktop/MIP/USsuccess.txt", 'rb') as successUS:
        output = set()
        count =0
        for line in successUS:
            x = getIP(line.replace('\n',''))
            if (str(x) != ''):
                output.add(str(x))
                count +=1
        uniquenessCount.write("America "+str(len(output)))
        print ("done US ",count)

    with open("C:/Users/Bryce Billing/Desktop/MIP/Chsuccess.txt", 'rb') as successCh:
        output = set()
        count = 0
        for line in successCh:
            x = getIP(line.replace('\n',''))
            if(str(x)!=''):
                output.add(str(x))
                count +=1
        uniquenessCount.write("\nChina "+str(len(output)))
        print("Done China ",count)

    with open("C:/Users/Bryce Billing/Desktop/MIP/IRasuccess.txt", 'rb') as successIr:
        output = set()
        count = 0
        for line in successIr:
            x = getIP(line.replace('\n',''))
            if (str(x) != ''):
                output.add(str(x))
                count+=1
        uniquenessCount.write("\nIran "+str(len(output)))
        print("Done Iran ", count)

    with open("C:/Users/Bryce Billing/Desktop/MIP/SAsuccess.txt", 'rb') as successSA:
        output = set()
        count = 0
        for line in successSA:
            x = getIP(line.replace('\n',''))
            if (str(x) != ''):
                output.add(str(x))
                count+=1
        uniquenessCount.write("\nSA "+str(len(output)))
        print("Done SA ", count)

def getIP(x):
    if(x!=''):
        y = x.replace(': ', ':')
        z = y.split(" ")
        a = z[1].split(':')
        return a
    else:
        return ''

main()