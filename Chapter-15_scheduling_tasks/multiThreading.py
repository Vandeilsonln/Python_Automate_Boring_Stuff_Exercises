import threading, time

print('Start of program.')

def takeANap():
    time.sleep(5)
    print('Wake up!')


threadObj = threading.Thread(target=takeANap)

threadObj.start()

print('End of Program.')

print('-' * 40)

threadObj2 = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})

threadObj2.start()