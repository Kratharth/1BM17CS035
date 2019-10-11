class CallDetail:
	def __init__(self,caller,called,duration,Type):
		self.caller = caller
		self.called = called
		self.duration = duration
		self.Type = Type
class Util:
	def __init__(self):
		self.list_of_call_objects =  []
	def parse_customer(self,list_of_call_strings):
		self.list = []
		for call in list_of_call_strings:
			details = call.split(',')
			self.list_of_call_objects.append(CallDetail(details[0],details[1],details[2],details[3]))
	def print_details(self):
		for call in self.list_of_call_objects:
			print(call.caller)
			print(call.called)
			print(call.duration)
			print(call.Type)

if __name__ == "__main__":
	call1 = '9990000001,9330000001,23,STD'
	call2 = '9990000002,9330000002,54,Local'
	call3 = '9990000003,9330000003,6,ISD'
	list_of_call_string = [call1,call2,call3]
	util = Util()
	util.parse_customer(list_of_call_string)
	util.print_details()
