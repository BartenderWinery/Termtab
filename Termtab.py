import googlesearch as see, requests, bs4, termcolor as c, argparse, colorama as cc
parser = argparse.ArgumentParser(description="A quick term indexing tool to quickly find websites related to your keywords.")
parser.add_argument('dns', metavar='dns', action='store', help='Term to search')
parser.add_argument('-msr', metavar='msr', type=int, help='Maximum search range', default=10)
parser.add_argument("-threads", metavar='threads', type=int, help='Threads to use', default=1)
parser.add_argument("-pdr", metavar="pdr", action='store', help='Prefered domain for searches')
if __name__=="__main__":
    args = parser.parse_args(); cc.init()
    web=see.search(args.dns, num_results=args.msr)
    for index in web: #Add threading supporting for faster searching
        c.cprint(">>: "+index,"magenta")
        try:
            c.cprint("      "+bs4.BeautifulSoup(requests.get(index).text,features="lxml").title.text,"blue") #Add code snippet support
        except:
            print()
        #Add description/perfered domains/and threading