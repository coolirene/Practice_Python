# for waiting_no in range(5): # 0, 1, 2, 3, 4
#     print("Waitinglist : {0}".format(waiting_no))

# starbucks = ['alice', 'mimi', 'bongbong']
# for customer in starbucks:
#     print('{0}, Ready'.format(customer))

# While
# customer = 'mimi'
# index = 5
# while index >= 1:
#     print('{0}, Now Ready. {1} left'.format(customer, index))
#     index -= 1
#     if index == 0:
#         print('Throw away!')

customer = 'mimi'
person ='Unknown'
while person != customer:
    print('{0}, Now Ready. '.format(customer))
    person = input('Name?')