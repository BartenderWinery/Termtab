from googlesearch import *
from termcolor import *
from colorama import *
from bs4 import BeautifulSoup
import requests, threading, colorama, webbrowser, argparse

colorama.init()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A quick term indexing tool to quickly find websites related to your keywords.")
    parser.add_argument('DNS', metavar='DNS', action='store', help='Domain term search')
    parser.add_argument('--MSR', metavar='MSR', type=int, help='Maximum search range', default=10)
    parser.add_argument("--Threads", metavar='Threads', type=int, help='Threads to use', default=1)
    parser.add_argument("--PDR", metavar="PDR", action='store', help='Prefered domain for searches')
    args = parser.parse_args()

list = []
#Add threading; thread control semi-complete: no dividing done

def ccprint(respo,printpack,color): #mass print
    for pack in range(len(printpack)):
        cprint(respo[pack]+printpack[pack],color)
class terminal(): #terminal super bundle
    def SLR(package): #Search lookup return
        cprint("Searching for: "+package[0], "blue")
        for index in search(package[0], tld="co.in", num=package[1], stop=package[1], pause=2): #Googlesearch
            try:
                list.append(str(index))
                link = requests.get(index); cprint(str(len(list))+"; "+index+"; "+str(link.elapsed.total_seconds()*100),"magenta"); soup = BeautifulSoup(link.text, features="lxml"); metas = soup.find_all('meta')
                cprint([meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description'], "red")
            except:
                cprint("###: "+index+" :###", "magenta")
    def thread(RTP): #Requested Threading profiling; simple control to start defs
        for thread in range(len(RTP)):
            cprint("Threading: "+RTP[thread], "blue")
            RTP[thread].start()

ccprint(["DNS lookup: ", "Range set: "],[args.DNS, str(args.MSR)],"green") #return list
terminal.SLR([args.DNS,args.MSR])

web = input(Fore.BLUE+"Open: ")
try:
    cprint("Opening: "+str(list[int(web)-1]), "green")
    webbrowser.open_new(str(list[int(web)-1]))
except:
    cprint("Requested link out of range or not valid; please check spelling")
cprint("Script finshed", "red")