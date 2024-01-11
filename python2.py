try:
    list = ["SUM", "AVG", "MAX", "MIN", "FXP", "FPO", "FSN", "FCS", "END"]
    
    def string_check (x):
        for element in list:
            if x == element:
                return True
             
        return False
    
    sum = 0.0
    avg = 0.0
    max = 0.0
    min = 0.0
    count = 0.0
    fxp = []
    fpo = []
    fsn = []
    fcs = []
    
    file = open('DataInput.txt')
    
    
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
    # print("AVG: ", avg)
    # print("MAX: ", max)
    # print("MIN: ", min)
    line = ""
    while line != "AVG":
        line = file.readline().strip()
        nextline = file.readline().strip()
        print(nextline)













except IOError:
        print("File not found")
        