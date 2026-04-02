AUTHORIZED_USB = ["MyUSB123"] 

def is_authorized(serial):
    if serial in AUTHORIZED_USB:
        return True
    return False
