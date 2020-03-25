from datetime import date
#pip module
import camelcase

today = date.today()
print(today)

camel = camelcase.CamelCase()
text = 'hello there world'
print(camel.hump(text))