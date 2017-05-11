import os
import struct
path = "Key.bin"

def manipulate(operationCode,operationParameter,encryptedchar):
    if operationCode == 0:
        print encryptedchar ,operationParameter,encryptedchar ^ operationParameter
        return encryptedchar ^ operationParameter
    if operationCode == 1:
        return sum([ encryptedchar , operationParameter]) % 256
    if operationCode == 2:
        return encryptedchar - operationParameter
    print "errrrrrrrrrrrrrr"

with open(path, 'rb') as f:
    try:
        byte3 = " "
        i=0


        byte1 = " "
        operations = []
        while byte1 != "":
            i = i + 1
            # Do stuff with byte.
            byte1 = f.read(1)
            byte2 = f.read(1)
            byte3 = [f.read(1),f.read(1),f.read(1),f.read(1)]
            print i
            if byte1 and byte2 and byte3:
                operationCode =  ord(byte1)
                #operationCode = 'add' if operationCode == 1 else 'xor' if operationCode == 0 else 'sub'
                operationParameter = ord(byte2)
                lengthToOperateOn = struct.unpack("I", bytearray(byte3))[0]
                print 'operationCode={0},operationParameter={1},lengthToOperateOn={2} (byte array: {3})'.format(operationCode,operationParameter,lengthToOperateOn,bytearray(byte3) )
                operations.append((operationCode,operationParameter,lengthToOperateOn))


        encrypted = open('EncryptedMessage.bin', 'rb')
        encrypted_msg = list((ord(i) for i in encrypted.read()))
        print encrypted_msg
        curr_index = 0
        to_conv = 0
        for operationCode,operationParameter,lengthToOperateOn in operations:
            for i in range(lengthToOperateOn):
                if curr_index >= len(encrypted_msg):
                    curr_index = 0
                    to_conv = to_conv + 1
                    encrypted_msg = list(reversed(encrypted_msg))
                encrypted_msg[curr_index] = manipulate(operationCode,operationParameter,encrypted_msg[curr_index])
                curr_index = curr_index + 1

        print "the file content in bytes is:"
        new_list = list(reversed(encrypted_msg)) if to_conv % 2 == 1 else encrypted_msg
        decrepted_msg = "".join(map(unichr, new_list))
        print decrepted_msg





    finally:
        f.close()
