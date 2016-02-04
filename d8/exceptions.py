class InsufficientNumberOfDocumentsError(Exception):
    def __init__(self, message):
        self.message = message
        super(InsufficientNumberOfDocumentsError, self).__init__(message)
