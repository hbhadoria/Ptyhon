

#This is an application for the valuation of Fixed-for-Floating Interest Rate Swaps
#The Model assumes IRS as a series of FRAs thereby providing the flexibility to the user to use
#discounting factors not dependent on Libor rates ie OIS rates can be used for calcualting the discounting factors
#The model assumes a notional of USD 100Mn
#Created by: Hemant Bhadoria
#In case of any queries, please feel free to reach out
#@Email: hemant.bhadoria09@gmail.com
#@Cell : +91-869-295-8545


import math    # Importing the math module

print('Please choose one of the options below:\n')

print('1: If you want the Libor zero rates to be used for discounting\n')

print('2: If you want to specify interest rates for discounting\n')

choice = int(input('Option='))



#Defining the variables

t=[]           #t=reset time

fv=[]          #fv=future value

pv=[]          #pv=present value

z=[]           #z=libor zero rate

fcc=[]         #fcc=forward rate with continuous compounding

fsa=[]         #fsa=forward rate with semi annual compounding

df=[]          #df=discount factor


if choice==1:

    #fc= coupon rate for the fixed leg
    fc=float(input('\nPlease Enter the interest rate for the fixed leg in %: \n'))
    
    #ds=duration of swap
    ds=int(input('\nPlease Enter the duration of the swap in months:\n '))
    
    #lib0= Libor zero rate at the time of valuation
    lib0=float(input('\nPlease Enter the libor rate for the current period in %: \n'))
    
    #since lib0 is the semi-annual compounding rate for the current period
    fsa.append(lib0)
    
    #time left in the current period
    t0=(ds%6)/12
    
    #number of six month periods till maturity + 1
    tn=ds//6+1
    
    #calcuating the reset times
    for i in range(tn):
        ti=t0 + i*0.5
        t.append(ti)
    print('\nThe reset times vis-a-vis valuation time in yrs:\n', t)
    
    
    #taking in the libor zero rate from the user and calucating the discount factors
    for j in range(tn):
        print('\nPlease Enter the libor rate for the period ',j+1,'below\n')
        lib=float(input('libor rate='))
        z.append(lib)
        dfj=math.exp(-lib*t[j]/100)
        df.append(dfj)
    print('\n Libor zero rates starting next reset date in %:\n', z)
    print('\n The discounting factors :\n', df)
    
    #appending the libor zero at the first upcoming reset date to fcc
    fcc.append(z[0])
    
    
    #Calculating the forward rates with continuous compounding
    for k in range(1,tn):
        fcck=((z[k]*t[k]-z[k-1]*t[k-1])/(t[k]-t[k-1]))
        fcc.append(fcck)
    print('\n The forward rates with continuous compounding in %:\n',fcc)
    
    
    #Calcuating the forward rates with semi-annual compounding
    for l in range(1,tn):
        fsal=2*(math.exp(fcc[l]/200)-1)*100
        fsa.append(fsal)
    print('\n The forward rates with semi-annual compounding in %:\n',fsa)
    
    
    #Calculating the future values & present values of net payments
    for m in range(tn):
        fvm=(fsa[m]-fc)/2
        pvm=fvm*df[m]
        pv.append(pvm)
    
    print('\n The present values of net payments in USD Mn:\n',pv)
    PV=sum(pv)
    print("\n The value of the swap from fixed-rate payer's perspective in USD Mn:\n", PV)

elif choice==2:
    
    #fc= coupon rate for the fixed leg
    fc=float(input('\nPlease Enter the interest rate for the fixed leg in %: \n'))
    
    #ds=duration of swap
    ds=int(input('\nPlease Enter the duration of the swap in months: \n'))
    
    #since lib0 is the semi-annual compounding rate for the current period
    fsa.append(lib0)
    
    #time left in the current period
    t0=(ds%6)/12
    
    #number of six month periods till maturity + 1
    tn=ds//6+1
    
    #calcuating the reset times
    for i in range(tn):
        ti=t0 + i*0.5
        t.append(ti)
    print('\nThe reset times vis-a-vis valuation time in yrs:\n', t)
    
    
    #calucating the discount factors
    for p in range(tn):
        print('\nPlease Enter the interest rate to be used for discounting in period',p+1,'below\n')
        d=float(input('discounting rate in % ='))
        dfp=math.exp(-d*t[p]/100)
        df.append(dfp)
    print('\n The discounting factors :\n', df)
    
    
    #lib0= Libor zero rate at the time of valuation(current period)
    lib0=float(input('\nPlease Enter the libor rate for the current period in %:\n '))
    
    
    #taking in the libor zero rate from the user 
    for j in range(tn):
        print('\nPlease Enter the libor rate for the period ',j+1,'below:')
        lib=float(input('libor rate in % ='))
        z.append(lib)
    print('\n Libor zero rates starting next reset date in %:\n', z)
    
    
    #appending the libor zero at the first upcoming reset date to fcc
    fcc.append(z[0])
    
    
    #Calculating the forward rates with continuous compounding
    for k in range(1,tn):
        fcck=((z[k]*t[k]-z[k-1]*t[k-1])/(t[k]-t[k-1]))
        fcc.append(fcck)
    print('\n The forward rates with continuous compounding in %:\n',fcc)
    
    
    #Calcuating the forward rates with semi-annual compounding
    for l in range(1,tn):
        fsal=2*(math.exp(fcc[l]/200)-1)*100
        fsa.append(fsal)
    print('\n The forward rates with semi-annual compounding in %:\n',fsa)
    
    
    #Calculating the future values & present values of net payments
    for m in range(tn):
        fvm=(fsa[m]-fc)/2
        pvm=fvm*df[m]
        pv.append(pvm)
    
    print('\n The present values of net payments in USD Mn:\n',pv)
    PV=sum(pv)
    print("\n The value of the swap from fixed-rate payer's perspective in USD Mn:\n", PV)
    
else:
    #In case the choice entered isn't one of above two
    print('\nPlease enter a valid choice')
    
    
print('\n\nTo be updated for more functionalities...')

