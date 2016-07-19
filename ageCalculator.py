def howOld():
    print("Let's see how long you have lived in days, minutes and seconds!")
    name = raw_input("name: ")
    print("Great," +name+ ". Now go ahead and enter your age.")
    age = int(raw_input("age: "))
    days = age * 365
    minutes = age * 852948
    seconds = age * 31556926
    print (name+ " has been alive for a shocking "+ str(days)+ " days " +str(minutes)+ " minutes and "+ str(seconds)+ " seconds! Holy Toledo!")
howOld()
