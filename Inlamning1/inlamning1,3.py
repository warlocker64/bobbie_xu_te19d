m = float(input("Ange hur många gånger du har åkt med västtrafik den här månaden "))

e=30*m
s=775
if m > 25:
    print("Du skulle ha köpt månads kort fat ass")
    print(f"om du åker {m} gånger kostar det {e}kr ")
    print(f"månadskort kostar {s}Kr")
else:   
    print(f"om du åker {m} gånger kostar det {e}kr ")
