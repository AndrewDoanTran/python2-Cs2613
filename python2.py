
try:
    list = ["SUM", "AVG", "MAX", "MIN", "FXP", "FPO", "FSN", "FCS", "END"]
    
    def string_check (x):
        for element in list:
            if x == element:
                return True
             
        return False
    num = 0
    sum = 0.0
    avg = 0.0
    max = 0.0
    min = 100000000000.0
    count = 0.0
    fxp = []
    fpo = []
    fsn = []
    fcs = []
    
    file = open('/home1/ugrads/q6ptb/Desktop/cs2613-Q/DataInput.txt','r')
    file1 = open ('/home1/ugrads/q6ptb/Desktop/cs2613-Q/DataOutPut.txt', 'w')
    
    # while line != "END":
    #     line = file.readline().strip()
    #     element = line.split()
        
    #     if element[0] == "SUM":
    #         nextline = file.readline()
    #         next_element = nextline.split()
    #         if string_check(nextline[0]) != True:
    #             sum += float (next_element[0])
                
        
    #     elif element[0] == "AVG" :
    #         nextline = file.readline()
    #         next_element = nextline.split()
    #         if string_check(nextline[0]) != True:    
    #             count += 1
    #             avg += float (next_element[0])
    #             if line == True:
    #                 avg = avg/count  
        
    #     elif element[0] == "MAX":
    #         nextline = file.readline()
    #         next_element = nextline.split()
    #         if string_check(nextline) != True:    
    #             if max < float (next_element[0]):
    #                 max = float (next_element[0])
        
    #     elif element[0] == "MIN":
    #         nextline = file.readline()
    #         next_element = nextline.split()
    #         if string_check(nextline) != True:
    #             if min > float (next_element[0]):
    #                 min = float (next_element[0])
    # print("SUM: ", sum)
    # print("AVG: ", avg)976931348623157e+308
    # print("MAX: ", max)
    # print("MIN: ", min)
    line = ""
    while line != "END":
        line = file.readline().strip()
        word = line.split()
        
        if word[0] == "SUM":
            line = file.readline().strip()
            word = line.split()
            num = int (word[0])
            i = 0
            while i < num:
                word = line.split()
                sum += float(word[0])
                i += 1
                line = file.readline().strip()    
            file1.write("Sum: " + str(sum) + "\n")


        if word[0] == "AVG":
            line = file.readline().strip()
            word = line.split()
            num = float (word[0])
            i = 0
            while i < num:
                word = line.split()
                avg += float(word[0])
                i += 1
                line = file.readline().strip()   
            avg = avg/num
            file1.write("Average: " + str(avg) + "\n")
        
        if word[0] == "MAX":
            line = file.readline().strip()
            word = line.split()
            num = int (word[0])
            
            i = 0
            while i < num:
                word = line.split()
                if float(word[0]) > max:
                    max = float(word[0])
                i += 1
                line = file.readline().strip()
            file1.write("Maximum " + str(max) + "\n")
            
        
        
        if word[0] == "MIN":
            line = file.readline().strip()
            word = line.split()
            num = int (word[0])
            i = 0
            while i < num:
                word = line.split()
                if float(word[0]) < min:
                    min = float(word[0])
                i += 1
                line = file.readline().strip()
            file1.write("Minimum " + str(min) + "\n")
        
    file.close()
    file1.close()   
    print("SUM: ", sum)
    print("AVG: ", avg)
    print("MAX: ", max)
    print("MIN: ", min)          
        
        

            














except IOError:
        print("File not found")
        