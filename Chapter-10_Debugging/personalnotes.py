#! python3
import logging
logging.basicConfig(filename=r'C:\delicious\logfile.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)  # Comment this out to disable logging messages to be diplayed

# I'll be writing the author's suggestion and notes in this code.

# ----------------------------------------
# RAISING EXCEPTIONS

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <=2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height-2):
        print(symbol + (' ' * (width - 2) + symbol))
    print(symbol * width)


for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))

# ----------------------------------------
print('-' * 50)
# GETTING THE TRACEBACK AS A STRING

import traceback


try:
    raise Exception('This is the error message.')
except:
    errorFile = open(r'C:\Users\aline\Documents\Coisas do Vandeilson\errorInfo.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt')

# ----------------------------------------
print('-' * 50)
# ASSERTIONS

podBayDoorStatus = 'open'
# assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'

podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'

# assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'

# ----------------------------------------
print('-' * 50)
# USING AN ASSERTION IN A TRAFFIC LIGHT SIMULATION

market_2nd = {'ns': 'yellow', 'ew': 'green'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switch_lights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'

        if stoplight[key] == 'yellow':
            stoplight[key] = 'red'

        if stoplight[key] == 'red':
            stoplight[key] = 'green'

    print(stoplight.values())
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)


switch_lights(market_2nd)

# ----------------------------------------
print('-' * 50)
# LOGGING

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial (%s%%)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total


print(factorial(5))
logging.debug('End of Program')
