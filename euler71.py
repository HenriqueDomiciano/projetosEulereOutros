import time 
start_time=time.time()
'''
isso funciona pois
p/q<a/b
p é o que qeremos saber
p=q*a/b
sabemos que como devemos tratar como integers temos que a mmenor diferença possivel e -1
logo 
p=((q*a)-1)/b
se fizermos os valores s e r como variaveis que se alteram temos que descobrir o valor do denoninador fazemos com que 
s seja o novo denominador e r o novo numerador então se p*s>r*d a precisão é maior pois o denominador é maior
'''
r=0
s=1
for d in range(1000000,2,-1):
    p=int(((3*d)-1)/7)
    if p*s>r*d:
        s=d
        r=p
print(r)
print('---------%s segundos'%(start_time-time.time()))