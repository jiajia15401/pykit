__all__ = ['Make_error']
class Make_error(Exception):
    def __init__(self):
        self.new-make_error = []
    def error(self):
        class new_error(Exception):
            def __init__(self,erro_name):
                self.error = erro_name
            def __str__(self):
                return 'error make by Make_error()'
        self.new-make_error.append(new_error())
        return new_error()
    def __str__(self):
        return 'make_error use to make a error'
