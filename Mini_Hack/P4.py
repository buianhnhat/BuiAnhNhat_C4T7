import re
print       ("                 ĐĂNG KÍ TÀI KHOẢN!")
tk = input  ("Tài khoản:        ")
email = input ("Email:            ")
while True:
    if("@" and ".com" not in email):
        print ("Email không hợp lệ!")
        email = input ("Email:            ")
    else:
        break

mk = input  ("Mật khẩu:         ")
count = len( mk )

while True:
    if (count<8):
        print ("Mật khẩu phải có ít nhất 8 chữ số, bao gồm cả chữ và số!")
        mk = input  ("Mật khẩu:         ")
    else :
        if  (bool(re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', mk))):
            mk2 = input ("Nhập lại mật khẩu: ")
            if (mk!=mk2):
                print ("Mật khẩu không trùng với mật khẩu bạn nhập lúc đầu! Hãy nhập lại!")
            else : 
                print ("Đăng kí tài khoản thành công!!!")
                break
        else :
            print ("Mật khẩu phải có ít nhất 8 chữ số, bao gồm cả chữ số!")
            mk = input  ("Mật khẩu:         ")
            
             
           

   


