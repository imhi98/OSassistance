import math
import os
import sys
import time
import datetime
from Exceptionhandler import ExceptionHandler

class assistance():
    def __init__(self) -> None:
        self._username = "khoda mibinad"
        self._password = "123456789"
        self._example = "{index} {name} {family} {job} {telephone} {comment} {last modified date} "
        self._logger = []
    
    def save(self,filename="main.txt"):
        self._logger.append(f"save function called")
        self._direname = self.where_am_i()
        self._direfile = os.path.join(self._direname, filename)
        with open(self._direfile,"r") as f :
            self._last_index = len(f.readlines())
            self._logger.append(f"{filename} opened for reading at {self._last_modified}")
        print("data will stored as shown respectivly","\n",self._example)
        self._sample = f"\n{self._last_index+1} {self._name} {self._family} {self._job} {self._phone} {self._comments} {self._last_modified}"
        with open(self._direfile,"a") as f :
            f.write(self._sample)
            self._logger.append(f"{filename} opened for appending {self._sample} at {self._last_modified}")
        return self._sample

    def beautifier(self,start=True,end=False):
        if start and (not end):
            print()
            print("_____________________/\/\/\/\/\/\/\/\/\/\_____________________")
            print()
        elif end and (not start):
            print()
            print("_____________________\/\/\/\/\/\/\/\/\/\/_____________________")
            print()
        elif (not start) and (not end):
            print()
        else:
            pass
    
    def load(self,filename = "main.txt",khat = 0 , soton = 0):
        self._logger.append(f"load function called")
        self._direname = self.where_am_i()
        self._direfile = os.path.join(self._direname, filename) 
        if khat==0 and soton==0:
            khat-=1
            soton-=1
            with open(self._direfile , "r") as f:
                self._loaded_data = f.readlines()
                self._logger.append(f"{filename} opened for reading in load Function")
            return self._loaded_data
        elif khat!=0 and soton!=0:
            khat-=1
            soton-=1
            with open(self._direfile , "r") as f:
                self._loaded_data = f.readlines()
                self._logger.append(f"{filename} opened for reading in load function")
                for i in range(len(self._loaded_data)):
                    if khat==self._loaded_data[i]:
                        self._splited = self._loaded_data[i].split()
                        for j in range(len(self._splited)):
                            if self._splited[j]==soton:
                                return self._splited[j]
    
    def select_command(self,comand:str):
        self.mode=""
        if comand == "1":
            self.mode = "Read"
        elif comand == "2":
            self.mode = "Write"
        elif comand == "3":
            self.mode = "Reset"
        elif comand == "4":
            self.mode = "Exit"
        return self.mode
        
    def get_input(self,msg):
        self._last_input = input(msg)
        self._logger.append(f"get_input function called {self._last_input}")
        return self._last_input

    def show_file(self,filename="main.txt"):
        self._logger.append(f"show_file function called")
        self._direname = self.where_am_i()
        self._direfile = os.path.join(self._direname, filename)
        with open(self._direfile ,"r") as f:
            self._data = f.readlines()
            self._logger.append(f"{filename} opened for reading in show_file")
            self.beautifier(True,False)
            for line in self._data:
                self.beautifier(False,False)
                print(line)
        self.beautifier(False,True)
        input("\nPress Enter To Continiue")
        return self._data
    
    def reset_the_file(self,filename="main.txt"):
        self._direname = self.where_am_i()
        self._direfile = os.path.join(self._direname, filename)
        self._logger.append(f"reset_the_file function is called")
        with open(self._direfile ,"w") as f:
            f.write("")
        print("\nFile Reset is Done!!\n")
    
    def info(self,**kwargs):
        self._name = kwargs["name"].replace(" ", "")
        self._family = kwargs["family"].replace(" ", "")
        self._job = kwargs["job"].replace(" ", "")
        self._phone = kwargs["phone"].replace(" ", "")
        self._comments = kwargs["comment"].replace(" ", "")
        self._last_modified = kwargs["last_modified"].replace(" ", "")
        self._logger.append(f"info function called with kwargs {self._name} {self._family} {self._job} {self._phone} {self._comments} {self._last_modified}")

    def where_am_i(self):
        self._direname = os.path.dirname(__file__)
        self._logger.append(f"where_am_i function is called with {self._direname}")
        return self._direname
    
    def what_time_isit(self):
        self._d = datetime.date.today()
        now = datetime.datetime.now()
        self._t = now.strftime("%H:%M:%S")
        print(self._d)
        self._logger.append(f"what_time_isit function is called with {self._d} {self._t}")
        return self._d,self._t
    
    def logger(self):
        self._direname = self.where_am_i()
        self._direfile = os.path.join(self._direname, "log.txt")
        with open(self._direfile,"a") as f:
            for logs in self._logger:
                f.write("\n")
                f.write(logs)
    
    def __call__(self):
        pass

    def __str__(self):
        pass
