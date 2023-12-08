#!/usr/bin/env
import sys , requests , re
from multiprocessing.dummy import Pool
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init

init(autoreset=True)

fr  = Fore.CYAN																					
fg  = Fore.GREEN
rd  = Fore.RED
wh  = Fore.WHITE
bl  = Fore.BLUE
kn  = Fore.YELLOW


print """  
                             .8888b                   dP       
                             88   "                   88       
.d8888b. .d8888b. 88d8b.d8b. 88aaa  dP    dP .d8888b. 88  .dP  
Y8ooooo. 88ooood8 88'`88'`88 88     88    88 88'  `"" 88888"   
      88 88.  ... 88  88  88 88     88.  .88 88.  ... 88  `8b. 
`88888P' `88888P' dP  dP  dP dP     `88888P' `88888P' dP   `YP 13 
================================================================
Thanks To : - Semfuck Team | Cirebon Xploit
            - Cirebon Blackhat | Ganest Seven
"""

try:
    target =[i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
	path =  str(sys.argv[0]).split('\\')
	exit('\n Tulis Tools['+path[len(path)-1] + '] list.txt')
	

def URL(url):
	if url[-1] == "/":
		pattern = re.compile('(.*)/')
		site = re.findall(pattern,url)
		url = site[0]
	if url[:7] != "http://" and url[:8] != "https://":
		url = "http://" + url
	return url	
	
	
def filter(site):
	pet = re.compile('<meta name="generator" content="(.*)" />')
	try:
		site = URL(site)
		src = requests.get(site,timeout=15).content
		if re.findall(pet,src):
			generator = re.findall(pet,src)[0]
			if 'WordPress' in generator :
				print '=>[TERDETEKSI INI WEB] | '+site +' --> {}[WordPress]'.format(fg)
				with open('wordpress.txt', mode='a') as d:
					d.write(site+'/\n')
			elif 'Joomla' in generator :
				print '=>[TERDETEKSI INI WEB] | '+site +' --> {}[Joomla]'.format(fg)
				with open('joomla.txt', mode='a') as d:
					d.write(site+'/\n')
			elif 'Drupal' in generator :
				print '=>[TERDETEKSI INI WEB] | '+site +' --> {}[Drupal]'.format(fg)
				with open('drupal.txt', mode='a') as d:
					d.write(site+'/\n')
			elif 'PrestaShop' in generator :
				print '=>[TERDETEKSI INI WEB] | '+site +' --> {}[PrestaShop]'.format(fg)
				with open('prestashop.txt', mode='a') as d:
					d.write(site+'/\n')
			else :
				if 'wp-content/themes' in src :
					print '=>[TERDETEKSI INI WEB] | '+site +' --> {}[WordPress]'.format(fg)
					with open('wordpress.txt', mode='a') as d:
						d.write(site+'/\n')
				elif 'catalog/view/theme'	in src :
					print '=>[TERDETEKSI INI WEB] | '+site +' --> {}[OpenCart]'.format(fg)
					with open('opencart.txt', mode='a') as d:
						d.write(site+'/\n')
				elif 'sites/all/themes' in src :
					print '=>[TERDETEKSI INI WEB] | '+site +' --> {}[Drupal]'.format(fg)
					with open('drupal.txt', mode='a') as d:
						d.write(site+'/\n')
				elif 'vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php' in src :
					print '=>[TERDETEKSI INI WEB] | '+site +' --> {}[laravell stadin]'.format(fg)
					with open('laravell stadin', mode='a') as d:
						d.write(site+'/\n')
				elif '<script type="text/javascript" src="/media/system/js/mootools.js"></script>' in src or '/media/system/js/' in src or 'com_content' in src :
					print '=>[TERDETEKSI INI WEB] | '+site +' --> {}[Joomla]'.format(fg)
					with open('joomla.txt', mode='a') as d:
						d.write(site+'/\n')
				elif '<script type="text/javascript" src="/vendor/phpunit/phpunit/composer.json"></script>' in src or '/vendor/phpunit/phpunit/' in src or 'com_content' in src :
					print '=>[TERDETEKSI INI WEB] | '+site +' --> {}[laravell]'.format(fg)
					with open('laravell.txt', mode='a') as d:
						d.write(site+'/\n')
				elif 'js/jquery/plugins/' in src :
					print '=>[TERDETEKSI INI WEB] | '+site +' --> {}[PrestaShop]'.format(fg)
					with open('prestashop.txt', mode='a') as d:
						d.write(site+'/\n')
				else :
					print '=>[TERDETEKSI INI WEB] | '+site +' --> {}[GAK DIKETAHUI CMS NYA]'.format(fr)
					with open('GAK DIKETAHUI CMS NYA.txt', mode='a') as d:
						d.write(site+'/\n')
		else :
			if 'wp-content/themes' in src :
				print '=>[TERDETEKSI INI WEB] | '+site +' --> {}[WordPress]'.format(fg)
				with open('wordpress.txt', mode='a') as d:
					d.write(site+'/\n')
			elif 'catalog/view/theme'	in src :
				print '=>[TERDETEKSI INI WEB] | '+site +' --> {}[OpenCart]'.format(fg)
				with open('opencart.txt', mode='a') as d:
					d.write(site+'/\n')
			elif 'sites/all/themes' in src :
				print '=>[TERDETEKSI INI WEB] | '+site +' --> {}[Drupal]'.format(fg)
				with open('drupal.txt', mode='a') as d:
					d.write(site+'/\n')
			elif 'vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php' in src :
				print '=>[TERDETEKSI INI WEB] | '+site +' --> {}[laravell stadin]'.format(fg)
				with open('laravell stadin', mode='a') as d:
					d.write(site+'/\n')		
			elif '<script type="text/javascript" src="/vendor/phpunit/phpunit/composer.json"></script>' in src or '/vendor/phpunit/phpunit/' in src or 'com_content' in src :
				print '=>[TERDETEKSI INI WEB] | '+site +' --> {}[laravell]'.format(fg)
				with open('laravell.txt', mode='a') as d:
					d.write(site+'/\n')
			elif '<script type="text/javascript" src="/media/system/js/mootools.js"></script>' in src or '/media/system/js/' in src or 'com_content' in src :
				print '=>[TERDETEKSI INI WEB] | '+site +' --> {}[Joomla]'.format(fg)
				with open('joomla.txt', mode='a') as d:
					d.write(site+'/\n')
			elif 'js/jquery/plugins/' in src :
				print '=>[TERDETEKSI INI WEB] | '+site +' --> {}[PrestaShop]'.format(fg)
				with open('prestashop.txt', mode='a') as d:
					d.write(site+'/\n')
			elif 'osCommerce' in src :
				print '=>[TERDETEKSI INI WEB] | '+site +' --> {}[osCommerce]'.format(fg)
				with open('osCommerce.txt', mode='a') as d:
					d.write(site+'/\n')
			elif 'index.php?osCsid=' in src :
				print '=>[TERDETEKSI INI WEB] | '+site +' --> {}[osCommerce]'.format(fg)
				with open('osCommerce.txt', mode='a') as d:
					d.write(site+'/\n')
			elif 'index.php/cPath' in src :
				print '=>[TERDETEKSI INI WEB] | '+site +' --> {}[osCommerce]'.format(fg)
				with open('osCommerce.txt', mode='a') as d:
					d.write(site+'/\n')					
			else :
				print '=>[TERDETEKSI INI WEB] | '+site +' --> {}[GAK DIKETAHUI CMS NYA]'.format(fr)
				with open('GAK DIKETAHUI CMS NYA.txt', mode='a') as d:
					d.write(site+'/\n')			
	except :
		print '=> [INI WEB UDAH MATI] | '+site +' --> {}=> [Time Out Web nya]'.format(fr)
		
mp = Pool(150)
mp.map(filter, target)
mp.close()
mp.join()		
