# Code By Mr.D`HACK
# Code Date: 2/1/2020
# coding=utf-8
#######import modules########
import os,requests,sys,urllib
#############################
#########color###############
pu = '\033[37m'
ijo = '\033[32m'
me = '\033[31m'
ku = '\033[33m'
bi = '\033[34m'
cy = '\033[36m'
#########api_url#############
api_url = "http://tinyurl.com/api-create.php"
#############################

class short:
         def main(self,url):
                 try:
                         get = api_url+ "?" \
                               +urllib.parse.urlencode({"url": url})
                         req = requests.get(get)

                         if "Error" in req.text:
                                 os.system('clear')
                                 print ('\033[36m╔═════════════════════════════════════════╗')
                                 print ("\033[37m║\033[37m [\033[31m!\033[37m] URL SALAH!: "+url)
                                 print ('\033[36m╚═════════════════════════════════════════╝')
                                 sys.exit()
                         else:
                                 os.system('clear')
                                 os.system('sh b.sh')
                                 print ('\033[36m╔═════════════════════════════════════════╗')
                                 print ('\033[37m║\033[37m [\033[32m+\033[37m] Url: '+url)
                                 print ('\033[37m║\033[37m [\033[32m+\033[37m] Url Berhasil di pendekan')
                                 print ("\033[37m║\033[37m [\033[32m√\033[37m] Hasil: " +pu +req.text)
                                 print ('\033[36m╚═════════════════════════════════════════╝')
                                 sys.exit()
                 except Exception as e:
                         print ("+[!] Error"+e)
                         sys.exit()
if __name__ == '__main__':
        os.system('clear')
        os.system('sh b.sh')
        print ('\033[36m╔═════════════════════════════════════════╗')
        url = input('\033[37m║\033[37m [\033[32m*\033[37m] Url\033[31m: \033[37m')
        print ('\033[36m╚═════════════════════════════════════════╝')
        short().main(url)

