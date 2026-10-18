import json, numpy as np
FS=48000.0
def peak(f0,g,q,w):
    A=10**(g/40.0); w0=2*np.pi*f0/FS; al=np.sin(w0)/(2*q)
    b=[1+al*A,-2*np.cos(w0),1-al*A]; a=[1+al/A,-2*np.cos(w0),1-al/A]
    z=np.exp(-1j*2*np.pi*w/FS)
    return (b[0]+b[1]*z+b[2]*z**2)/(a[0]+a[1]*z+a[2]*z**2)
def shelf(f0,g,q,w,hi):
    A=10**(g/40.0); w0=2*np.pi*f0/FS; al=np.sin(w0)/2*np.sqrt((A+1/A)*(1/q-1)+2)
    c=np.cos(w0); s=2*np.sqrt(A)*al
    if hi:
        b=[A*((A+1)+(A-1)*c+s),-2*A*((A-1)+(A+1)*c),A*((A+1)+(A-1)*c-s)]
        a=[(A+1)-(A-1)*c+s,2*((A-1)-(A+1)*c),(A+1)-(A-1)*c-s]
    else:
        b=[A*((A+1)-(A-1)*c+s),2*A*((A-1)-(A+1)*c),A*((A+1)-(A-1)*c-s)]
        a=[(A+1)+(A-1)*c+s,-2*((A-1)+(A+1)*c),(A+1)+(A-1)*c-s]
    z=np.exp(-1j*2*np.pi*w/FS)
    return (b[0]+b[1]*z+b[2]*z**2)/(a[0]+a[1]*z+a[2]*z**2)
def curve(eq,w):
    H=np.ones_like(w,dtype=complex)
    for n in '1234': H*=peak(eq[n+'f'],eq[n+'g'],eq[n+'q'],w)
    H*=shelf(eq['lf'],eq['lg'],eq['lq'],w,False)
    H*=shelf(eq['hf'],eq['hg'],eq['hq'],w,True)
    return 20*np.log10(np.abs(H))
w=np.logspace(np.log10(100),np.log10(12000),400)
v9=json.load(open('/home/user/GHC-AUDIO-MIX/console/GHC BROADCAST V9.snap'))['ae_data']
v11=json.load(open('/home/user/GHC-AUDIO-MIX/console/GHC BROADCAST V11.snap'))['ae_data']
for c,who in (('14','Dehil'),('16','Peggy'),('24','Elsie')):
    a=curve(v9['ch'][c]['eq'],w); b=curve(v11['ch'][c]['eq'],w)
    print('\n=== ch%s %s ==='%(c,who))
    print('%-7s %8s %8s %8s'%('Hz','V9','V11','change'))
    for f in (160,250,400,500,630,800,1000,1250,1600,2000,2500,3150,4000,5000,6300,8000):
        i=np.argmin(abs(w-f)); print('%-7d %+8.1f %+8.1f %+8.1f'%(f,a[i],b[i],b[i]-a[i]))
    m=(w>=700)&(w<=4000)
    print('700-4k spread (peak-to-trough): V9 %.1f dB   V11 %.1f dB'%(np.ptp(a[m]),np.ptp(b[m])))
    print('700-4k average:                 V9 %+.1f dB  V11 %+.1f dB'%(a[m].mean(),b[m].mean()))
