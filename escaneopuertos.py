import nmap
Port_ini=70
Port_fin=90
Ip_des="192.168.22.112"
escaneo=nmap.PortScanner()
for j in range(Port_ini,Port_fin+1):

    resultado=escaneo.scan(Ip_des,str(j))
    resultado=resultado['scan'][Ip_des]['tcp'][j]['state']
    print(f'El puerto número {j} se encuentra {resultado}')
