from generator.utilities.utilities import format_message

class ResponseTypes:
    PARAMETERS_ERROR = "ParametersError"
    RESOURCE_ERROR = "ResourceErrror"
    SYSTEM_ERROR = "SystemErrror"
    SUCCESS = "Success"


class ResponseFailure:
    def __init__(self,type_, message) -> None:
        self.type = type_
        self.message = self._format_message(message)

    def _format_message(self,message):
        return format_message(message)
    
    @property
    def value(self):
        return {"type":self.type,"message":self.message}
    
    def __bool__(self):
        return False


class ResponseSuccess:
    def __init__(self, value = None) -> None:
        self.type = ResponseTypes.SUCCESS
        self.value = value
    
    def __bool__(self):
        return True
    
def build_response_from_invalid_request(invalid_request):
    parameter_key =  "parameter"
    message_key = "message"
    message = "\n".join(
        [
            f"{err[parameter_key]}: {err[message_key]}" 
            for err in invalid_request.errors
        ]
    )

    return ResponseFailure(ResponseTypes.PARAMETERS_ERROR, message)

