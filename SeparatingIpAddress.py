ip_address = "127.0.0.1"
firstNumber,secondNumber, thirdNumber , fourthNumber=ip_address.split(".")
transformed=firstNumber +", " + secondNumber+", "+ thirdNumber+","+fourthNumber
print(transformed)