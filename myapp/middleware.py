from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

class GetNotes(MiddlewareMixin):
	def process_request(self, request):
		print("List of Guitarists")
		print(request.user)
		# return HttpResponse("Execution stops after this.")

	def process_exception(self, request, exception):
		print("exception -- ", exception)
		return HttpResponse("Exception occured")