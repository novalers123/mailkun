# Python bytecode 2.7 (62211)
# Embedded file name: main.py
# Compiled at: 2019-01-19 21:39:24
# Decompiled by https://python-decompiler.com
from lib import *
import os, time
BOLD = '\x1b[1m'
CEND = '\x1b[0m'
CSELECTED = '\x1b[7m'
WARNING = '\x1b[93m'
CWHITE2 = '\x1b[97m'
CRED2 = '\x1b[91m'
CGREEN2 = '\x1b[92m'
CYELLOW2 = '\x1b[93m'
CBLUE2 = '\x1b[94m'
CVIOLET2 = '\x1b[95m'
CGREEN = '\x1b[32m'
CBEIGEBG = '\x1b[46m'

def timex():
    t = time.localtime()
    hr = t.tm_hour
    mn = t.tm_min
    sc = t.tm_sec
    return ('[{}:{}:{}] ').format(hr, mn, sc)


def logo():
    print CRED2 + '\n     _ _  _        _               ___   ___'
    time.sleep(0)
    print CGREEN2 + '  __| | || |  _ __| | ___ __ ___  / _ \\ / _ \\ _ __  ___'
    time.sleep(0)
    print CYELLOW2 + " / _` | || |_| '__| |/ / '_ ` _ \\| | | | | | | '_ \\/ __|"
    time.sleep(0)
    print CBLUE2 + '| (_| |__   _| |  |   <| | | | | | |_| | |_| | | | \\__ \\ '
    time.sleep(0)
    print CVIOLET2 + ' \\__,_|  |_| |_|  |_|\\_\\_| |_| |_|\\___/ \\___/|_| |_|___/\n' + CEND
    time.sleep(0)
    print '|create by     : ' + BOLD + CWHITE2 + 'd4rkm00ns' + CEND
    print '|contact person: ' + BOLD + CWHITE2 + 'd4rkm00ns@protonmail.com' + CEND
    print '|date created  : 31 desember 2018'
    print '|date update   : 20 Januari 2019'
    print '|tools version : ' + CBEIGEBG + '1.1 [ LUXURY Version ]' + CEND
    print "|what's new..? : Fix several problem"
    print '|tools for     : ' + CSELECTED + 'Email Valid Checker + Email Filter' + CEND
    print '|RECODE BY     : ' + CBEIGEBG + 'INDODARK' + CEND

logo()
time.sleep(0.5)
try:
    if not os.path.exists('Result'):
        os.makedirs('./Result')
    else:
        print ''
except OSError:
    print 'Error: Creating directory'
    print 'Buatlah folder Result'
finally:
    print '\t\t[^.^]-+ [d4rkm00ns] +-[^.^]'

print WARNING + "Note: Read 'PetunjukPenggunaan.txt' before using this Tools" + CEND
time.sleep(0.5)
print 'List Tools ./d4rkm00ns'
print '##[^.^][^.^][^.^][^.^][^.^][^.^][^.^]##\n'
print CBLUE2 + '[1]' + CEND + 'Main Checker Valid Email'
print CBLUE2 + '[2]' + CEND + 'Custom Valid Email Server'
print CBLUE2 + '[3]' + CEND + 'Custom Filter Email'
print CRED2 + '[0]' + CEND + 'EXIT\n'
print '##[^.^][^.^][^.^][^.^][^.^][^.^][^.^]##'
print WARNING + "Copyright by d4rkm00ns. Please don't remove copyright" + CEND
try:
    if not os.path.exists('ResFiltered'):
        os.makedirs('./ResFiltered')
    else:
        print ''
except OSError:
    print 'Error: Creating directory'
    print 'Buatlah folder ResFiltered'
finally:
    print '\t\t[^.^]-+ [Welcome to Undergrounds] +-[^.^]'

swit = input(timex() + BOLD + CWHITE2 + '[+]Your Choose root@d4rkm00ns: ' + CEND)
if swit == 1:
    print timex() + '[+]Set to Mail Checker'
    luxury(timex())
else:
    if swit == 2:
        print timex() + '[+]Set to Custom Mail Checker'
        customserver(timex())
    else:
        if swit == 3:
            print timex() + '[+]Set to Custom Filter Email'
            customfilter(timex())
        else:
            if swit == 0:
                print timex() + '[!]Exit..!!'
                print timex() + '[+]See You Again..!!'
                print timex() + '[+]./d4rkm00ns'
                print CGREEN + '[^.^]-+ [Thanks Was using Tools ./d4rkm00ns] +-[^.^]' + CEND
                exit()
            else:
                print timex() + WARNING + 'Invalid Choosing' + CEND
print '\n\t\t' + CGREEN + '==--+ [Finished..!!] +--=='
print '[^.^] [Thanks Was using Tools ./d4rkm00ns] [^.^]' + CEND