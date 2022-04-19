from ast import ExceptHandler
from assistance import assistance

bixby = assistance()
username = bixby.get_input("Please insert valid username!\n")
pasword = bixby.get_input("Please insert valid password!\n")

if (bixby._username==username) and (bixby._password==pasword):
    while True:
        comand = bixby.get_input("what is your command to be Done?\n1 : Read File\n2 : Write File\n3 : Reset File\n4 : Exit\n")
        mode = bixby.select_command(comand)
        if mode=="Read":
            filename = bixby.get_input("which file do you want to Read?\nmain.txt\nlog.txt\n")
            if filename=="main.txt" or filename=="log.txt":
                data = bixby.show_file(filename)
            else:
                raise Exception("invalid filename Inserted!!")
            bixby.logger()
        elif mode=="Write":
            bixby.info(name=bixby.get_input("Insert Name:\n"), family=bixby.get_input("Insert Family:\n"), job=bixby.get_input("Insert Job:\n") , phone=bixby.get_input("Insert Phone:\n"), comment=bixby.get_input("Insert Comment:\n"),last_modified=bixby.what_time_isit()[1])
            bixby.save("main.txt")
            print("\ndata set in file!\n")
            bixby.show_file("main.txt")
            bixby.logger()
            bixby._logger=[]
        elif mode=="Reset":
            bixby.reset_the_file(filename=bixby.get_input("main.txt or log.txt?\n"))
            bixby._logger=[]
        elif mode=="Exit":
            bixby.logger()
            bixby._logger=[]
            break

elif (bixby._username!=username) and (bixby._password==pasword):
    print("Invalid Username!!!!!!")
elif (bixby._username==username) and (bixby._password!=pasword):
    print("Invalid Password!!!!!!")
else:
    print("Invalid Username & password!!!")

print("We Hope The best For You!")