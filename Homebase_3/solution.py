import os
import struct
import itertools
path = "Key.bin"

def manipulate(operationCode,operationParameter,encryptedchar):
    if operationCode == 0:

        return encryptedchar ^ operationParameter
    if operationCode == 1:
        return sum([ encryptedchar , operationParameter]) % 256
    if operationCode == 2:
        return encryptedchar - operationParameter
    print "errrrrrrrrrrrrrr"
all_possible_ops1 = []
all_possible_ops2 = []
all_possible_ops3 = []
all_possible_ops = []
for i1 in range(2):
    for i2 in range(256):
        for i3 in range(1,50):
            possible_op = (i1,i2,i3)
            all_possible_ops1.append(possible_op)

for i1 in range(2):
    for i2 in range(256):
        for i3 in range(1, os.path.getsize('EncryptedMessage.bin')):
            possible_op = (i1, i2, i3)
            all_possible_ops2.append(possible_op)

for i1 in range(2):
    for i2 in range(256):
        for i3 in range(1, os.path.getsize('EncryptedMessage.bin')):
            possible_op = (i1, i2, i3)
            all_possible_ops3.append(possible_op)

# all_possible_ops = list(itertools.product(all_possible_ops,all_possible_ops,all_possible_ops))
all_possible_ops = ([x, y,z] for x in all_possible_ops1 for y in all_possible_ops2  for z in all_possible_ops3)
# print all_possible_ops
for operations in all_possible_ops:
    to_conv=0
    encrypted = open('EncryptedMessage.bin', 'rb')
    encrypted_msg = list((ord(i) for i in encrypted.read()))

    curr_index = 0
    dont_show = False
    total_leng = 0
    for operationCode,operationParameter,lengthToOperateOn in operations:
        total_leng = total_leng + lengthToOperateOn
        for i in range(lengthToOperateOn):
            if curr_index >= len(encrypted_msg):
                curr_index = 0
                encrypted_msg = list(reversed(encrypted_msg))
                to_conv = to_conv + 1
            encrypted_msg[curr_index] = manipulate(operationCode,operationParameter,encrypted_msg[curr_index])
            if not ((encrypted_msg[curr_index] <= 122 and encrypted_msg[curr_index] >=97) or \
                            (encrypted_msg[curr_index] <= 90 and encrypted_msg[curr_index] >=65) or \
                                encrypted_msg[curr_index] == 32 or encrypted_msg[curr_index] == 63 or encrypted_msg[curr_index] == 46):
                dont_show = True
                break
            curr_index = curr_index + 1
        if dont_show:
            break
        if total_leng < os.path.getsize('EncryptedMessage.bin'):
            dont_show = True
            break
    if not dont_show:
        new_list = list(reversed(encrypted_msg)) if to_conv % 2 == 1 else encrypted_msg
        decrepted_msg = "".join(map(chr, new_list))
        print decrepted_msg

