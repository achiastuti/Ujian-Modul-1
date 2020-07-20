
def nomor_telp(listNo):
  no = []
  n = ""
  noTelp = ""
  if len(listNo) == 0:
    return false
  else :
    for nomer in listNo :
      no.append(str(nomer))
    noTelp = "("+n.join(no[0:3])+")-"+n.join(no[3:6])+"-"+n.join(no[6:10])
    return noTelp

print(nomor_telp([1,2,3,4,5,6,7,8,9,0]))