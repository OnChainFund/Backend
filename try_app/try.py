l = [
    "0x5FbDB2315678afecb367f032d93F642f64180aa3",
    "0xd1Cc87496aF84105699E82D46B6c5Ab6775Afae4",
    "TWTR/USD",
]
print(l)


def args_to_string(args: list) -> str:
    result = ""
    for arg in args:
        if type(arg) == str:
            result += "'" + arg + "'"
            result += ","
        elif type(arg) == int:
            result += str(arg)
            result += ","
    result_remove_last =  result[:-1]
    return result_remove_last 


print(args_to_string(l))
