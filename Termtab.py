from googlesearch import *
from termcolor import *
from colorama import *
from bs4 import BeautifulSoup
import requests, threading, colorama, webbrowser

colorama.init()

DNS = input(Fore.BLUE+"DNS: ")
MSR = int(input(Fore.BLUE+"Max range: "))

list = []
#Add threading; thread control semi-complete: no dividing done

def ccprint(respo,printpack,color): #mass print
    for pack in range(len(printpack)):
        cprint(respo[pack]+printpack[pack],color)
def thread(RTP): #Requested Threading profiling; simple control to start defs
    for thread in range(len(RTP)):
        cprint("Threading: "+RTP[thread], "blue")
        RTP[thread].start()
class terminal(): #terminal super bundle
    def SLR(package): #Search lookup return
        cprint("Searching for: "+package[0], "blue")
        for index in search(package[0], tld="co.in", num=package[1], stop=package[1], pause=2): #Googlesearch
            try:
                list.append(str(index))
                link = requests.get(index); cprint(str(len(list))+"; "+index+"; "+str(link.elapsed.total_seconds()*100),"magenta"); soup = BeautifulSoup(link.text); metas = soup.find_all('meta')
                cprint([meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description'], "red")
            except:
                cprint("###: "+index+" :###", "magenta")

ccprint(["DNS lookup: ", "Range set: "],[DNS, str(MSR)],"green") #return list
terminal.SLR([DNS,MSR])

web = int(input(Fore.BLUE+"Open: "))

try:
    cprint("Opening: "+str(list[web]), "green")
    webbrowser.open_new(str(list[web]))
except:
    cprint("...")
cprint("Script finshed", "red")