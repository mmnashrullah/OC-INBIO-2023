#contoh nested if
EC_tanah = float(input('Input nilai EC tanah: '))
SAR_tanah = float(input('Input nilai SAR tanah: '))

if (EC_tanah <= 4 and EC_tanah > 0) :
    if (SAR_tanah <= 13):
        print('Tanah non-salin')
    elif (SAR_tanah > 13):
        print('Tanah sodik') 
elif (EC_tanah > 4 and EC_tanah > 0):
    if (SAR_tanah <= 13):
        print('Tanah salin')        
    elif (SAR_tanah > 13):
        print('Tanah salin-sodik')
else:
    pass
 
if (EC_tanah < 0):
    if (SAR_tanah <0):
        print('EC dan SAR tidak boleh negatif')
    else:
        print('EC tidak boleh negatif')
else:
    if (SAR_tanah <0):
        print('SAR tidak boleh negatif')
