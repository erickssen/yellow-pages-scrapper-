#!/usr/bin/python
#coding: utf-8
import os, argparse, time
import urlparse, random
import sys
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




									


print	"""	      
XXXSSSXSXXSXXXXXXXSXXS2XS221>~::__:===:;::. . ~{vvnnoo22oonnnno2ooonnononooo2nno
XS22ooS2X2S2SSX2S2S22S12*!{==|=-:-.:::: .. .  . "{xvnnnooovvnnooonnnnnnnnonnnnnn
X2X2S2SSS2S2X2SS2S22o}|+:+==--...:;:::::==_. .    +lvvvnvnnnnvnnnnnvvvvvnnnoooon
XSSS2SS2SS22222o22n}=|:=;-:--. ....:;----. .   . . .:=+{vvvnvnvvvvnvnvnvnnnnnnnn
X2SSSS2XS222o2o2oe||~--.....  ..-. -.   ----- .     :<i|||lvvvvvvnvvvvvvvvv1nvvv
XS2SS222So22222!~:- . : . .......-.- ... --- ::.  ...:+*ia=+=iillvvvvvvIvIvnvvvv
X2X22oo2ooonn}-. ..- . . ....... ._:..  . . _.    :.:==|ii+>=><llIvvIvlvvvvIvvvv
XS2o222oooe}`    .         ._.-- .  ----  .. . ..-.:<xii||_-:=+iillvlilIvvvvvvv
S2222oonn|-   .                          .    .   ..:<uas==i;:.:=iilllllllllllII
2o2oooon%-   .                                 .::=|xdXZXo===. .-+|||ililiiiiilv
X2o22onv=                . . .  .            .:==|ioX####Xc; :.  -==iiiiiililill
XoSo2ovv`               ..:_==::;;;.... .. .:=iinnXXZ#Z##Xni: .   -=|iiiiIllllll
2ooooonv_.             ...<iiiiiiiisi=|====iixuoSoXZZZZXZZSs=.     :=iiilllii|il
2o2ooovvi;            .:=|Ivvvvvvvvvvnvvivvvoo2o2SXZXZS2XXo1>..    .=iiIllIIi||i
22ooonnnxi          ..:=|iIvvvvlvvnnnnnnnxnnoogodXZZUZXSnonl>:    ==|illIIIIlili
2o22oonnvI;        ..:;=|ilvvvIvvnnoono2SSXXXZZUUZ##ZZXoonli|;. .|il|iiiillllli|
oooo2ooonv(        ...:+||iilivvvII1I1nnX2XXZZXZXXXX1IIlsunvi+.. <ii|iiiiilili||
oooonnonnvI=         .:=|=||iliilIxnsxiII1111111I|++|iil>+=-=::..-<i|i|||iiiii||
nnnnnnnnvvvi.       .::=;==|+:------+"++::;===+=::  -       ...:  :iii|i|i|ii|||
nnnvnvnvvnI*i|   . .:::-:::-  .             ::::.  .          .:- =|||||||||||||
nnvnxvvvv>  . ..   .:::-. .                 .::.              .::::|+|+||+||||+|
vvvv1nnvn; ...   . :::::..                 .=|=;      ..    .....:=||=|++||+||||
vvvnvvvvx=-::. .   .::::..   . .-:. .      .|vni,.  .. . ..:::::.:i|||+||+||||||
vvvv1vvIvi::: .    ::.:.:;:::;;:..:. ....::=iXXn|;.:.....:.;:=::.=|||||||||+|+||
vvvvvvIvvv=::.    .=:..-:====:;::;:.:.::=;=|iXX1li|=;.... -::::::|||||||+|+||||+
vvvvvIvIIIi=:.. . ;;::..::====;:.:...:=;=|||xZXoni>==||=;;::..::>=+++++++||||+|+
vIvIIvIvIvli;:::_::|;::.:.:::;=:;:;;||+:-.:<xSXX1l|=..=<||=;...=>|+++|+||+||>+|+
vvlIllIlIllli;==>~:+==::.....:..:=|||=- .|=|%nS2ovlIi  :====;::=|+|+|+|+++||||+|
IllIlIlIlIllli||;:=||=::::-:::::;===:.. +i|+|!!!*++~~:...====::=|+|+||++|+|++|++
IIIllIlIlIlli|i+||:===;::::-.:::::::.  : . . ..      ;; -:====;+||+++++|++|+|=+|
lllllllllIlIliii=__+==;::::::::::::_. ==:.           .:<|=;:===i++|=+++++|+|++++
illllllllllIlIllIIv====:;::::::::-:=_===:.           ..:<i|<===l+|=|=|++|=++|+++
lilllllllillllliiii>;;=:=:::::-:.:=+|(|:.--.. .        .-=<ii|=|++|==+++++++|=+=
iillliIllilliliiiii|;;:::=:;;:;::==|+=: -.                -:=||+++++++|+++|++|=+
llllllllliiilli||i|x`::::;=:;:;;=+|=-:.                    .::<|+++|==+=+|=|++++
liliiilliiiii||||=~; -::.:-:::::==:-. .          .          ..:|=|=+=+++|=+|+++|
illiillliiiii|i|`  s ..-.-:::-::=::.                       ..  -==+++==+=+++++|=
lllllliiii||||=    ]b,:.:.::::=;:... .  .   . ..... . .. ..:=.. .:++|;=++|=|++++
llliiiiii||i>-..   ;4Whs..:=::..:.:::.:. .. ...:...=::==_====      -===+=+++++|=
vlliliii||>- .     q.!4hos,==:..-==|=|=;;=;=::::.=.::=+|====: .      --===++++=+
vllili||+`         3b, -Ymos>:.:-:=|iii:;;:...::.=i=;=::||===.          -:===+=+
liiii|+ .          )#Bma. -5vs,....=||===-..=+.;=i=ii+<=:=|==                --=
li>--               XZmBWWwc "Ic .. .+|==:;===<===I|i||x==<;:                .  
~               . . )##mBWWWQgaa|,....-:==;+=====:+||||ii|<;:                   
               .     "XWWWBBWm#Zmwc... :=>|=>:x|===|+|=i|xz`=;.                 
                   ..  )XBBmWBm#W#Zos,...-+{lsixx||i||iiwm'.jk.                 
             .  . .  .. "{dYV#mBWmm#Xoai_=:.::==|IIvixno#X.<Qm;                 
               .    . )s,s/4WXwwdW###XXvl|+===|=|iiivoSSXZ<QW#z.     .  .       
            .      .   <w,:.)#m#####ZXov>|==:-====||lxooXmQWmWo;   .            
        .  .     .     -WQmc ."9#m#ZXni+         :+ixvoXZWmWWW2>                
       .      .      .  ]WQWw,:."V#X1+`  .    .. ..-~^?XmWWWWBXc  .         .   
           .            .4WWWQgc -~-=:..-:......:= . _u#BWWWBB#n;   .  .  .     
         .               -#WWWWmw;.   :=;;:=:::-    sqmmWWWBWB#n;  .            
                          )#WWWWWWmc .     ..    _wX##WWWWWWWBmS(               
                           4WWWWWWBWmas,  . __saom###BWWWWWWBW#X(  . .  .       
                           -#WWWWBWBm#mmXw1.>#SX#U##mWWBWWQWWW#Z1 .          .  
                            ]mWWmWWWWBmm(-:...  SmmWWWWQQQQQWWm#z    .          
                             3WBWWWWmWmBa,.:--:)mBWWWWQQQQQQQWm#e . .    .      
                              4BWWWWWBWD!ii,%|=xa)WBWQQQQQQWWWW#e            .  
                              -WmWWBWQmmmZ1%32`J#mWWQWQQQQQWWQm#[ .             
                               ]QmWWW#Qmm#Xr^ -=?QT\3WQQQQQQQQB#[   .   .       
                                VWmWWBm(uZ9%=;=+:]YYLXWQQQQQQWm#[  .         .  
                                -WmWWWQb?Y%!uc_xc(=?1mQQQQQQQWB#[      .       .
                                 ]QQWmB#hCxs;<:w%wmmmWQQQQQQQWmBk  . .      . ..
                                  4WBWWWmuoXwam#moWmQWQQQQQQQQW#Z .      .    

"""			  
	
		    



links = [] 


def get_emails(page):
	print 'in get_emails def...'
	# links = []
	for link in page.find_all('a'):
		url = link.get('href')
		if url:
			if 'mailto:' in url:
				links.append(url) 

	if len(links) > 0:
		for link in links:
			print link
	else:
		print 'No emails in this page!'
	 



def write_to_file(email_list):

	f = open('business_emails.txt', 'w')

	for line in email_list:
		f.write(str(line).split(':')[1] + '\n')  
	f.close()	

					 


def goto_info_page(browser):
	try:
		browser.find_element_by_link_text('More Info').click()
		print 'in "More Info" page: ', browser.current_url 
	except:
		print 'cant find " More Info " links'
		 



def next_page(browser, url, count=10):
	
	current_page = get_page_num(url) + 1
	
	browser.get(url)
	
	for i in range(count):	
		try:
			x = current_page + i
			print x
			link = browser.find_element_by_link_text(str(x)).click()
			print 'link: ', link
			browser.switch_to_window() 
		except:
			pass



def get_page_num(url):
	try:
		print 'getting page No....'
		url_components = urlparse.urlparse(url)
		url_str_items = url_components[4].split('=')
		page_number = url_str_items[3]
		return int(page_number) 
	except:
		pass
	 



def scrap_current_page(browser):
	time.sleep(1)
	current_page_source = BeautifulSoup(browser.page_source, 'html.parser')
	current_url = browser.current_url
	links = current_page_source.find_all('a', {'class':'track-more-info'})

	for link in links:
		url = link.get('href')
		url = "https://www.yellowpages.com" + url
		browser.get(url)
		info_page_source = BeautifulSoup(browser.page_source, 'html.parser') 
		print browser.current_url
		get_emails(info_page_source)
		browser.execute_script("window.history.go(-1)") 
	print 'done with page ', get_page_num(browser.current_url)	 



def main():  
	if len(sys.argv) < 2:
		print 'usage:  ./scrapper.py --scrap bussiness_type'
		sys.exit(1)

	bussiness_input = sys.argv[2]
	browser = webdriver.Chrome()

	#initial url
	yp_url = 'https://www.yellowpages.com/search?search_terms='+bussiness_input+'&geo_location_terms=Miami%2C%20FL&page=1'


	command = sys.argv[1]
	if command == '--scrap':


		current_page_num = get_page_num(yp_url)

		if current_page_num is not None:
			current_page_num = get_page_num(yp_url) + 1
		else:
			current_page_num = 1

		browser.get(yp_url) 

		#scrap current page
		scrap_current_page(browser) 

		more_info_links = []
		for i in range(2):	
			try:
				x = current_page_num + i
				#click on next page# link
				browser.find_element_by_link_text(str(x)).click()	
				print 'in page: ', x
				page_source = BeautifulSoup(browser.page_source, 'html.parser')

				scrap_current_page(browser) 
			except:
				pass
		write_to_file(links) 

		




if __name__ == '__main__':
	main()




