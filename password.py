#密碼重試程式 
#先在程式碼中 設訂好密碼 passwaod = 'a123456' 
#讓使用者[最多輸入3次密碼] 
#不對的話，就印出"密碼錯誤! 還有_次機會"
#對的話，就印出'登入成功' 

#----------------------------------
# test = 0
# pass_answer = 'a123456' 
# while True: 
    # try_answer = input('請輸入密碼:')
    # if try_answer == pass_answer: 
        # print('登入成功')
        # break 
    # elif try_answer != pass_answer: 
        # test = test + 1 
        # number = 3 - test 
        # number = int(number) 
        # print('密碼錯誤! 還有',number,'次機會') 
        # if number == 0: 
            # break
#----------------------------------            
#老師解法一 :
# pass_answer = 'a123456'
# i = 3 
# while i > 0: 
    # try_answer = input('請輸入密碼:') 
    # if try_answer == pass_answer: 
        # print('登入成功') 
        # break 
    # else:
        # try_answer != pass_answer: 
        # i = i - 1 
        # print('密碼錯誤! 還有',i,'次機會')  

#----------------------------------
### 老師解法二 :
pass_answer = 'a123456'
i = 3 
while i > 0: 
    i = i - 1 
    try_answer = input('請輸入密碼:') 
    if try_answer == pass_answer: 
        print('登入成功') 
        break 
    else:
        print('密碼錯誤!')
        if i > 0:
            print('還有',i,'次機會')
        else:
            print('沒機會嘗試了! 要索帳號了啦!')        