from rest_framework.views import APIView
from rest_framework.response import Response
from .bkash_utils import get_grant_token,create_payment,execute_payment
from django.shortcuts import redirect,render
from .models import Payment

# Payment create view..
class BkashPaymentView(APIView):
    def post(self, request, *args, **kwargs):
        amount = request.data.get('amount','100.00')
        invoice = request.data.get('invoice','INV-001')

        token_response = get_grant_token()
        token = token_response.get('id_token')

        if not token:
            return Response({'error':'Failed to get token','details':token_response},status=400)
        
        payment_response = create_payment(token,amount,invoice)
        bkash_url = payment_response.get('bkashURL')
        payment_id = payment_response.get('paymentID')

        if not bkash_url:
            return Response({'error':'Failed to create payment','details':payment_response},status=400)
        
        return Response({
            'bkashURL':bkash_url,
            'paymentID':payment_id,
            'token':token
        })


class BkashCallbackView(APIView):
    def get(self, request):
        payment_id = request.GET.get("paymentID")
        status = request.GET.get("status")  # success / failed / cancelled

        if not payment_id:
            return redirect('payment_failed')

        token = get_grant_token().get("id_token")
        response = execute_payment(token, payment_id)

        Payment.objects.update_or_create(
        payment_id=payment_id,
        defaults={
            "trx_id": response.get("trxID"),
            "amount": response.get("amount"),
            "status": response.get("transactionStatus"),
            "invoice": response.get("merchantInvoiceNumber"),
        },
)

        # Redirect user based on callback status
        if status == "success":
            return redirect('payment_success')
        else:
            return redirect('payment_failed')


# simple success/cancel views
def success(request):
    return render(request,'payment_success.html')

def cancel(request):
    return render(request,'payment_failed.html')