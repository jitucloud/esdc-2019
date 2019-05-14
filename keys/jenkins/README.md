Generating a private RSA key
Generate an RSA private key, of size 2048, and output it to a file named key.pem:

openssl genrsa -out key.pem 2048
Generating RSA private key, 2048 bit long modulus
..........+++
..........................................................................+++
e is 65537 (0x10001)
Extract the public key from the key pair, which can be used in a certificate:

openssl rsa -in key.pem -outform PEM -pubout -out public.pem
writing RSA key

