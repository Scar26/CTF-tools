import requests
import json
import binascii
import string

ses = requests.session()

def checkECB(data, block_size):
  n = len(data)//block_size
  for i in range(n):
    for j in range(i+1,n):
      if data[i*block_size:(i+1)*block_size] == data[j*block_size:(j+1)*block_size]:
        return True
  return False

def detect_mode(oracle):
    resp, actual_mode = oracle(b'a'*50)
    if checkECB(resp, 32):
        predicted_mode = 'ECB'
    else:
        predicted_mode = 'CBC'
    success = actual_mode == predicted_mode
    return (predicted_mode, success)


def ECB_oracle(inp):
    payload = inp.hex()
    enc = ses.get(f'http://aes.cryptohack.org/ecb_oracle/encrypt/{payload}').text
    c = json.loads(enc)['ciphertext']
    return (c, 'ECB')

def leak_ECB_secret(oracle):
    mode, confirmation = detect_mode(oracle)
    
    assert(confirmation)
    
    if mode != 'ECB':
        print('The oracle is not ECB')
        return -1
    
    print('ECB Oracle detected')

    blength = 0
    while True:
        a1 = oracle(b'a'*blength)[0]
        a2 = oracle(b'a'*(blength+1))[0]
        if a1[:32] == a2[:32]:
            break
        blength += 1
    print(f'Found Block length: {blength}')
    
    blocks_to_be_scanned = 4
    secret = b'c'
    for block in range(blocks_to_be_scanned):
        for i in range(1, blength + 1):
            if i == blength:
                payload = b'a'*blength
                h = oracle(payload)[0][(block+1)*32:(block+2)*32]
                payload += secret
                for byte in string.printable.encode():
                    if oracle(payload + bytes([byte]))[0][(block+1)*32:(block+2)*32] == h:
                        secret += bytes([byte])
                        print (secret)
            else:
                payload = b'a'*(blength - i)
                h = oracle(payload)[0][block*32:(block+1)*32]
                payload += secret
                for byte in string.printable.encode():
                    if oracle(payload + bytes([byte]))[0][block*32:(block+1)*32] == h:
                        secret += bytes([byte])
                        print (secret)
    
    print ('##################')
    print (secret[:-1].decode())                        

if __name__ == '__main__':
    leak_ECB_secret(ECB_oracle)