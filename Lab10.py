import random
import math
import hashlib

def SHA256toBin(val):
    return bin(int(hashlib.sha256(val.encode('utf-8')).hexdigest(), 16)).replace("b", "")


#Lamport One-Time Digital Signature Scheme 
M = "important message"
d = SHA256toBin(M)

#secret keys lists (matrix) sk[i][j] for all 0<=i<2 and 0<=j<256. (initialize with random numbers).
SKarr = [[0 for i in range(256)] for j in range(2)]
for i in range(0, 2):
    for j in range(0, 256):
        SKarr[i][j] = random.randint(0, 1)

#generate public keys lists(matrix) pk[i][j] for all 0<=i<2 and 0<=j<256. (here, pk[i][j] = SHA256(sk[i][j]) for all 0<=i<2 and 0<=j<256.)
PKArr = [[0 for i in range(256)] for j in range(2)]
for i in range(0, 2):
    for j in range(0, 256):
        currentSK = str(SKarr[i][j])
        PKArr[i][j] = SHA256toBin(currentSK)

DS = [0 for i in range(256)]

for i in range(256):
    DS[i] = SKarr[int(d[i])][i]

#Sending M and DS to reciever
M = "important message"
d = SHA256toBin(M)


for i in range(0,256):
    currCondition = True
    if(not PKArr[int(d[i])][i] == SHA256toBin(str(DS[i]))):
        currCondition = False
if(currCondition):
    print("DS has been verified")
else:
    print("DS has not been verified")


#S/KEY One-Time Password

key = "Some very important key"
n = random.randint(2 ** 8, 2 ** 16 - 1) #Number of chained hashes

#Chain hash of server
currentHash = SHA256toBin(key)
hashArr = [0 for i in range(n)]
for i in range(n):
    hashArr[i] = currentHash
    currentHash = SHA256toBin(key)
    
revHashArr = hashArr[::-1]

#Send Hn(K), Hn-1(K), ..., H1(K) (in reverse order) to the Client and delete everything except Server_Key = Hn+1(K) from the server.
#Sends Client_Key = Hi(n) for i from n to 1 sequentially. (Lets assume the client sends the key that server has already, "key")

#Chain hash of client
currentHash = SHA256toBin(key)
clientHashArr = [0 for i in range(n)]
for i in range(n):
    clientHashArr[i] = currentHash
    currentHash = SHA256toBin(currentHash)

clientRevHashArr = clientHashArr[::-1]


for i in range(n):
    currCondition = True
    if(not clientRevHashArr[i] == revHashArr[i]):
        currCondition = False

if(currCondition):
    print("Key has been authenticated")
else:
    print("Key has not been authenticated")