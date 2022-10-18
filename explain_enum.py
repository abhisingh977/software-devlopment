from enum import Enum

# Magic Number

# check how much 100 dollar equals to different currency
def dollar_convertor(currency):
    return 100 * currency

# #indian_rupee
# print(dollar_convertor(80))

# print(dollar_convertor(1.02))
    
# print(dollar_convertor(1.37))

# print(dollar_convertor(7.19))

# print(dollar_convertor(62.1))















# indian_rupee = 80
# euro = 1.01

# print(dollar_convertor(indian_rupee))


# print(dollar_convertor(euro))

# canadian_dollar = 1.37
 
# print(dollar_convertor(canadian_dollar))

# chinese_yen = 7.19

# print(dollar_convertor(chinese_yen))

# russian_ruble = 62.1 
# print(dollar_convertor(russian_ruble))












# class Currency:
#     indian_rupee = 80
#     euro = 1.01
#     canadian_dollar = 1.37
#     chinese_yen = 7.19
#     russian_ruble = 62.1

# currency = Currency()

# print(dollar_convertor(currency.indian_rupee))

# print(dollar_convertor(currency.euro))
    
# print(dollar_convertor(currency.canadian_dollar))

# print(dollar_convertor(currency.chinese_yen))

# print(dollar_convertor(currency.russian_ruble))


# currency.indian_rupee = 100
# print(dollar_convertor(currency.indian_rupee))








class EnumCurrency(Enum):
    indian_rupee = 80
    euro = 1.01
    canadian_dollar = 1.37
    chinese_yen = 7.19
    russian_ruble = 62.1

# print(EnumCurrency)
print(dollar_convertor(EnumCurrency.indian_rupee.value))

print(dollar_convertor(EnumCurrency.euro.value))
    
print(dollar_convertor(EnumCurrency.canadian_dollar.value))

print(dollar_convertor(EnumCurrency.chinese_yen.value))

print(dollar_convertor(EnumCurrency.russian_ruble.value))






























