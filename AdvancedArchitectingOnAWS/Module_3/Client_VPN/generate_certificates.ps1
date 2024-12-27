# delete folder certificates if it exists
if (Test-Path -Path .\certificates) {
    Remove-Item -Path .\certificates -Recurse
}

# create folder named certificates
New-Item -Path . -Name "certificates" -ItemType "directory"

# create folder named ca
New-Item -Path .\certificates -Name "ca" -ItemType "directory"

# create folder named server
New-Item -Path .\certificates -Name "server" -ItemType "directory"

# create folder named client
New-Item -Path .\certificates -Name "client" -ItemType "directory"

# create folder named certs
New-Item -Path .\certificates\ca -Name "certs" -ItemType "directory"

# create folder named private in certificates folder
New-Item -Path .\certificates\ca -Name "private" -ItemType "directory"

# copy templates\openssl.cnf in certificates folder
Copy-Item -Path .\templates\openssl.cnf -Destination .\certificates\openssl.cnf
Copy-Item -Path .\templates\client.ext -Destination .\certificates\client.ext
Copy-Item -Path .\templates\server.ext -Destination .\certificates\server.ext


# create an empty file named index.txt in certificates\ca folder
New-Item -Path .\certificates\ca -Name "index.txt" -ItemType "file"

# create a file named serial in certificates\ca folder with content 01
Set-Content -Path .\certificates\ca\serial -Value "01"

# move to certificates folder
Set-Location -Path .\certificates

# generate CA private key
openssl genrsa -out ca/private/cakey.pem 2048

# generate CA certificate
openssl req -new -x509 -days 3650 -key ca/private/cakey.pem -out ca/certs/cacert.pem -subj "/CN=ClientVPN-CA" -extensions v3_ca -config openssl.cnf -batch

# generate server private key
openssl genrsa -out server/server.key.pem 2048

# generate server certificate signing request
openssl req -new -key server/server.key.pem -out server/server.csr -subj "/CN=server1.example.com" -batch

# create server certificate
openssl x509 -req -days 365 -in server/server.csr -CA ca/certs/cacert.pem -CAkey ca/private/cakey.pem -CAcreateserial -out server/server.cert.pem -extensions v3_server -extfile server.ext

# generate client private key
openssl genrsa -out client/client.key.pem 2048

# generate server certificate signing request
openssl req -new -key client/client.key.pem -out client/client.csr -subj "/CN=client1.example.com" -batch

# create client certificate
openssl x509 -req -days 365 -in client/client.csr  -CA ca/certs/cacert.pem -CAkey ca/private/cakey.pem -CAcreateserial -out client/client.cert.pem -extensions v3_client -extfile client.ext

aws acm import-certificate --certificate fileb://server/server.cert.pem --certificate-chain fileb://ca/certs/cacert.pem  --private-key fileb://server/server.key.pem

# move to parent folder
Set-Location -Path ..

