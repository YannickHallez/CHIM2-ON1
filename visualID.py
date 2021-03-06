import os,sys,platform
from datetime import datetime
import datetime, time
from IPython.core.display import display,Image,Markdown,HTML
_start_time   = None
_end_time     = None
_chrono_start = None
_chrono_stop  = None

def css_styling():
    styles = open("./css/visualID.css", "r").read()
    display(HTML(styles))

def display_md(text):
    display(Markdown(text))
    
def hdelay(sec):
    return str(datetime.timedelta(seconds=int(sec)))    
    
# Return human delay like 01:14:28 543ms
# delay can be timedelta or seconds
def hdelay_ms(delay):
    if type(delay) is not datetime.timedelta:
        delay=datetime.timedelta(seconds=delay)
    sec = delay.total_seconds()
    hh = sec // 3600
    mm = (sec // 60) - (hh * 60)
    ss = sec - hh*3600 - mm*60
    ms = (sec - int(sec))*1000
    return f'{hh:02.0f}:{mm:02.0f}:{ss:02.0f} {ms:03.0f}ms'

def chrono_start():
    global _chrono_start, _chrono_stop
    _chrono_start=time.time()

# return delay in seconds or in humain format
def chrono_stop(hdelay=False):
    global _chrono_start, _chrono_stop
    _chrono_stop = time.time()
    sec = _chrono_stop - _chrono_start
    if hdelay : return hdelay_ms(sec)
    return sec

def chrono_show():
    print('\nDuration : ', hdelay_ms(time.time() - _chrono_start))

def init():
    global _start_time
    # Styling notebook
    #
    css_styling()
    # Today, now and hostname
    #
    _start_time = datetime.datetime.now()
    start_time = _start_time.strftime("%A %d %B %Y, %H:%M:%S")
    _h = platform.uname()
    h = _h[1]+" ("+_h[0]+")"
    md = f'**Début à:** {start_time}  \n'
    md+= f'**Hostname:** {h}'
    display_md(md)
    #print('Run time             :', _start_time.strftime("%A %d %B %Y, %H:%M:%S"))
    #print('Hostname             :', f'{h[1]} ({h[0]})')
    md = '<p style="text-align: center"><img width="800px" src="./svg/logoBegin.svg" style="margin-left:auto; margin-right:auto"></img></p>'
    display_md(md)
    
def end():
    global _end_time
    _end_time = datetime.datetime.now()
    end_time = time.strftime("%A %d %B %Y, %H:%M:%S")
    duration = hdelay_ms(_end_time - _start_time)
    md = f'**Fin à:** {end_time}  \n'
    md+= f'**Durée:** {duration}'
    display_md(md)
    md = '<p style="text-align: center"><img width="800px" src="./svg/logoEnd.svg" style="margin-left:auto; margin-right:auto"></img></p>'
    display_md(md)
