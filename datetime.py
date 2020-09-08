from datetime import datetime

dir (datetime)


suan= datetime.now()

suan

dir(suan)

print(suan.day )#7

print(suan.month)# 9 /eylül

print(suan.year )# 2020

print(suan.hour )#19

print(suan.minute )#26

print(suan.second )#50


print(datetime.strftime(suan,"%A" ) )

# yıl bilgisi : %D 
#ay ismi: %B 
#gün ismi: %A 
#saat bilgisi: %X 
#gün bilgisi: %D

import locale

locale.setlocale(locale.LC_ALL,"")

# timestamp() ve from timestamp()

simdi2=datetime.now()

simdi1

saniye2=datetime.timestamp(simdi2)#tarihi saniyeye cevirir

tarih=datetime.fromtimestamp(saniye2-saniye1)#saniyeyi tarihe cevirir

#saatin miladı 
milad=datetime.fromtimestamp(0)
#milad=1970/1/1 03:00:00







