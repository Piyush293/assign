import jwt
from django.http import JsonResponse

def verify_certificate(request, token):
    try:
        secret_key = 'your-secret-key'
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])

        # Check the certificate_id in the payload against your database
        certificate_id = payload['certificate_id']

        # Implement further verification logic as needed

        return JsonResponse({"status": "Certificate is valid", "certificate_id": certificate_id})
    except jwt.ExpiredSignatureError:
        return JsonResponse({"status": "Certificate has expired"})
    except jwt.InvalidTokenError:
        return JsonResponse({"status": "Invalid certificate"})
