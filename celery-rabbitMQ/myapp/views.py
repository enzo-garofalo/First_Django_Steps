from .forms import ReviewForm
from django.views.generic.edit import FormView
from django.http import HttpResponse

class ReviewEmailView(FormView):
     form_class = ReviewForm
     template_name = 'review.html'

     def form_valid(self, form):
          form.send_email()
          msg = 'Thanks for the review!'
          return HttpResponse(msg)