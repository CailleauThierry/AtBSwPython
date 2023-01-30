# 415-555-000

def isPhoneNumber(text):
    if len(text) !=12:
        return False # not phone number sized
    for i in range (0, 3):
        if not text[i].isdecimal():
            return False
            
            # ....