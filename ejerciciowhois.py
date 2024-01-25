import whois
w= whois.whois('www.bicicletasgonzalo.com')
print (w.expiration_date)
print ("\n")
print (w.text)
