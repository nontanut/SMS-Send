import pandas as pd
import requests
import time

file_input = input("File path\n").replace("& ","").replace("'","")

try:
    df = pd.read_excel(file_input, keep_default_na=False)
    data = df["MobilePhone"].apply(str)
    phone = ','.join(data.values.tolist())

    print(phone)

    data_from = {
      "SenderId": "iCARE INSUR",
      "GroupId": "",
      "Is_Unicode": True,
      "Message": "ข้อความทดสอบ",
      "MobileNumbers": phone,
      "ApiKey": "jR7FlmIHJrysgGZ5bSd1iJsfrsC+nX+MMFD/dvD+iP4=",
      "ClientId": "837cd9b7-26fd-4f28-89b2-cb2a75f9f112"
    }
    res = requests.post('https://api.send-sms.in.th/api/v2/SendSMS', json=data_from)

    print(res)
    time.sleep(30)

except Exception as e:
    print("Check file and format", e)
    time.sleep(30)
