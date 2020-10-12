a = int(input('hur mycket ringer du per månad i minuter:'))#beräknar vilket abonnemang du borde använda beroende på hur mycket du ringer 
if a> 0 and a < 34:#printar ifall det är högre än 0 minuter och mindre än 34 minuter med en and som änvänds så att både den ska vara störe enen sak och mindre en annnan
    print('kör på abonnemanget Konstant')#en print vad mer vill du veta?
elif a> 33 and a < 67:#printar ifall det är högre än 33 minuter och mindre än 67 minuter med en and som änvänds så att både den ska vara störe enen sak och mindre en annnan
    print('kör på abonnemanget Normal')
elif a> 66 and a <43830:#printar ifall det är högre än 66 minuter och mindre än 43830 minuter med en and som änvänds så att både den ska vara störe enen sak och mindre en annnan
    print('kör på abonnemanget Plus')