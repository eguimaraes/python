def comparar(v1,v2):
    versoStatus=""
    v1Ar=v1.split(".");
    v2Ar=v2.split(".");
    vLen=len(v2Ar) if len(v1Ar) > len(v2Ar) else len(v1Ar)
    if(v1Ar[0]==v2Ar[0]):
        for i in range(0,vLen-1):
            if(v1Ar[i]!=v2Ar[i] ):
                versoStatus="Downgrade" if v1Ar[i]>v2Ar[i] else "Upgrade"
                break;           
    else:
        if(type(v1Ar[0])=="int" and type(v1Ar[0])=="int" ):
            versoStatus="Downgrade" if v1Ar[0]>v2Ar[0] else "Upgrade"
    
    return versoStatus