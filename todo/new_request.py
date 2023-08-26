class Request:
    def __init__(self, request, user) -> None:
        self.request = request
        self.user = user
        self.data = {}
    
    def to_dict(self):
        for key in self.request.data:
            self.data[key] = self.request.data[key]
        self.data["owner"] = self.user.pk
        