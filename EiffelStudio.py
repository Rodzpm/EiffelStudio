from gensound import Sine, Triangle, Square, Pan
from colorama import *
from sys import argv

class Config:
        def __init__(self, file_path):
                synth_list = {"Sine":Sine, "Triangle":Triangle, "Square":Square}
                with open(file_path, "r") as file:
                        res = file.read().split("----")
                        self.desc = res[0].split("\n")[:-1]                
                        self.title = self.desc[0]
                        self.author = self.desc[1]
                        self.BPM = 60e3/int(self.desc[2])
                        self.synth = self.desc[3].split()
                        for i in range(len(self.synth)):
                                self.synth[i] = synth_list[self.synth[i]]
                        res = res[1:]
                        for i in range(len(res)):
                                res[i] = res[i].split()
                                res[i] = " ".join(res[i])
                        self.song = res
                file.close()
        def print_config(self):
                init()
                print("Lecture de ", end="")
                print(Fore.RED + self.title, end="")
                print(Style.RESET_ALL, end=" ")
                print("par ", end="")
                print(Fore.GREEN + self.author, end="")
                print(Style.RESET_ALL, end=" ")
                print("à ", end="")
                print(Fore.BLUE + self.desc[2], end="")
                print(Style.RESET_ALL, end=" BPM\n")

def export_part():
        file_path = argv[1]
        config = Config(file_path)
        config.print_config()
        chorale = 0
        
        for i in range(len(config.song)):
                chorale += config.synth[i](config.song[i], duration=config.BPM)
        chorale.export(file_path[:-4]+".wav") # can you spot the parallel octaves?

if "__main__" == __name__:
        export_part()


