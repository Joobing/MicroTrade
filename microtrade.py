import re
import random
from pynput.mouse import Button, Controller
mouse= Controller()

from pynput.keyboard import Key, Controller
keyboard= Controller()

from bs4 import  BeautifulSoup
import requests
from re import sub
from decimal import Decimal
import numpy as np

from time import time
from time import sleep
from datetime import datetime, timezone, timedelta

#from IPython.display import Audio, display
import winsound
import pyperclip

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

timezone_offset = +2.0  # Pacific Standard Time (UTC−08:00)
tzinfo = timezone(timedelta(hours=timezone_offset))


def CMC(c):
    u_r_l= 'https://coinmarketcap.com/currencies/'+ str(c)
    page = requests.get(u_r_l, headers=headers, timeout=20)
    soup = BeautifulSoup(page.text, 'lxml')
    price = soup.find('div', class_='priceValue').text
    price = Decimal(sub(r'[^\d.]', '', price))
    return price


def zzz(t):
    s=np.random.randint(t[0],t[1])
    sleep(s)
    #print('.................last update ' + str(s) + ' seconds ago')


def left(a,b):
    # Press and release
    sleep(random.uniform(0.15, 0.3))
    mouse.position=(a, b)
    mouse.press(Button.left)
    mouse.release(Button.left)
    sleep(random.uniform(0.15, 0.3))

def right(a,b):
    # Press and release
    mouse.position=(a, b)
    mouse.press(Button.right)
    mouse.release(Button.right)
    sleep(random.uniform(0.15, 0.3))
    

def drag(a,b,c,d):
    # Press and release
    mouse.position=(a, b)
    mouse.press(Button.left)
    sleep(random.uniform(0.1, 0.2))   
    mouse.move(c, d)
    sleep(random.uniform(0.1, 0.2))   
    mouse.release(Button.left)
    sleep(random.uniform(0.1, 0.2)) 
    
def prss(k):
    keyboard=Controller()
    keyboard.press(k)
    sleep(random.uniform(0.1, 0.15)) 
    keyboard.release(k)
    sleep(random.uniform(0.1, 0.15)) 

def clcl(a,b):
    mouse.position=(a,b)
    mouse.click(Button.left, 2)
    mouse.click(Button.left)
    sleep(random.uniform(0.15, 0.3))

def ctrv():    
    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release('a')
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl)

def ctrc():
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl)
    sleep(random.uniform(0.15, 0.3))
    return pyperclip.paste()
    
def prc(tag):
    pricetag= float(re.findall("\d+\.\d+", tag)[0])
    return pricetag

def cancel(i):
    c=1
    while c < 3:#cancel pending order
        left(2135,830+20*(i-1))
        sleep(random.uniform(0.15,0.2))
        prss(Key.enter)
        prss(Key.enter)
        c=c+1
    sleep(random.uniform(0.1,0.15))

def sell(wait):
    cancel(1)
    left(2440,280)#manual
    left(2220,320)#buy
    left(2250,320)#sell
    left(2250,355)#Limit
    clcl(2250,450)#reset balance
    left(2000,490)#allin 99%
    drag(2400, 490, 105, 0)#allin 100%
    left(1325, 460-20*(wait))#update price      
    
    left(2365,580)#BOOM!!!
    left(2220,320)#buy
    left(2250,320)#sell
    clcl(2250,450)#reset balance
    prss(Key.backspace)

'''clcl(1600,225)#update price
prc(ctrc())
clcl(2220,405)#current price
ctrv()'''

    
    
def buy(wait):
    cancel(1) #cancel existing orders
    sleep(10)
    left(2440,280)#manual
    left(2250,320)#sell
    left(2220,320)#buy
    left(2250,355)#Limit
    clcl(2250,450)#reset balance
    left(2400,490)#allin 99%
    drag(2400, 490, 105, 0)#allin 100%
    left(1325, 520+20*(wait))#update price      
    
    left(2365,580)#BOOM!!!
    left(2250,320)#sell
    left(2220,320)#buy
    clcl(2250,450)#reset balance
    prss(Key.backspace)
    
    #left(2365,580)#BOOM!!!
    #drag(2400,490, 2510,490)

###############################################################################

'''Parameters'''
n=350   #number of iterations
mi=0
 #minimum much price increase that is considered significant
md=0 #minimum much price decrease that is considered significant
u=1    #how many times price should go up before buying
d=1     #how many times price should down up before selling
f=5       #number of  bearish times until reassuring sell 
l=7       #number of  pumps until reassuring buy               


#Price refresh rates
slow=[50,70]
good=[25,35]
fast=[5,15]

'''Preset'''

#Starting values
i=1
j=1
hold= False
profit=[]
fear=0
luck=0
up=0
down=0

#Trading currency
clcl(1580,200)
coin= ctrc()[0:-2]

#Balance
left(2440,280)#manual
left(2250,355)#Limit
left(2220,320)#buy
clcl(2479,520)
Balance0=prc(ctrc())

#Starting Price
clcl(1600,225)
price1 = prc(ctrc())

#Strating time
now = datetime.now(tzinfo)
current_time = now.strftime("%H:%M:%S")
starttime=time()
print('START:', current_time, 'coin:', coin, 'investing:', Balance0)


'''Trading Loop'''

while j < n+1 and sum(profit) > -1:
   
    if j < n:
        
        if hold is True:
            pace=fast
        elif up>0:
            pace=fast
        else:#out    
            pace=fast
            
        zzz(pace)
        clcl(1600,225)
        price2 =  prc(ctrc())


        
        if price2 > price1*(1+0.01*mi):
            if hold is False:

                if up<u:
                    up=up+1
                    print('knock knock', up)
                    price1=price2
                    j=j+1
                    
                else:
                    winsound.Beep(1500,200)
                    #display(Audio('C:/Users/u811717/Music/bell-ring-01.wav', autoplay=True))
                    print('____________________________')
                    print('buy'+str(i)+': ', price2, '$')
                    #cancel()

                    buy(0)
                    buy(0)
                    cancel(2)
                    bought=price2


                    hold= True
                    up=0

                    j=j+1
                    price1=price2 

            else:

                j=j+1
                p= (price2-bought)/bought
                price1=price2
                print( '......................', p, "% profit @ ", price2, "total:", sum(profit) )
                luck=luck+1
                if luck> l: 
                    buy(0)
                    buy(0)
                    luck=0                
                #buy(0)                    
                #print('order updated at price:', price2,' and pace:', pace)

        elif price2 < price1*(1-0.01*md):
            up=0
            
            if hold is True:
                
                if down<d:
                    down=down+1
                    print('oops!')

                    price1=price2
                    
                else:
                    print('sell'+str(i)+': ', price2, '$')
                    winsound.Beep(2000,200)
                    sell(0)
                    sell(0)
                    #display(Audio('C:/Users/u811717/Music/MONEYWIN.WAV', autoplay=True))
                    hold= False
                    #pace= slow
                    sold= price2
                    p= (sold-bought)*100/bought
                    profit.append(p)
                    print('profit: ', p, '%')
                    print('____________________________')

                    down=0
                    i=i+1
                    j=j+1
                    price1=price2   

            else:
                j=j+1
                price1=price2        
                up=0
                fear=fear+1
                print('......................bears.. bears..', up, fear)
                if fear> f: 
                    cancel(1)
                    sell(0)
                    fear=0


        else:
            if hold is True:
                print('......................price unchanged')
                j=j+1
                price1=price2 

            else:
                price1=price2
                print('......................Let\'s see what happens..', up)


                    



    else:
        if hold is True:
            winsound.Beep(2000,200)
            print('sell'+str(i)+': ', price2, '$')
            sell(1)
            #display(Audio('C:/Users/u811717/Music/MONEYWIN.WAV', autoplay=True))
            hold= False
            #pace=slow
            sold=price2
            p= (sold-bought)/bought
            profit.append(p)
            tp= sum(profit)
            print('CONGRATULATIONS! total profit: ', tp, '%.. second only to Zlatan..')
            j=j+1
        
        else:
            winsound.Beep(2000,200)
            print('sell'+str(i)+': ', price2, '$')
            sell(1)
            #display(Audio('C:/Users/u811717/Music/MONEYWIN.WAV', autoplay=True))
            tp= sum(profit)
            print('CONGRATULATIONS! total profit: ', tp, '%... second only to Zlatan..')
            j=j+1    
else:
    print('Last Call') 
    sell(3)
    sleep(60)
    sell(2)
    sleep(120)
    sell(0)
    sleep(120)
    
    left(2440,280)#manual
    left(2250,355)#Limit
    left(2220,320)#buy
    clcl(2479,520)
    Balance1=prc(ctrc())

    print('from:', Balance0, ' to:', Balance1)
    
runtime=time()-starttime
print(now.strftime("%H:%M:%S"), 'runtime:', runtime/1600)