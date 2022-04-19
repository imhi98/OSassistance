class ExceptionHandler(Exception):
    def __init__(self, func:object) -> None:
        try:
            self._function = func()
            self._name_function = func.__name__
            self.msg="ok!"
        except Exception as x :
            self.msg = x.__str__()
            self._name_function = func.__name__
