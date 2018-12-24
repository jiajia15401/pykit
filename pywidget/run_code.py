def run_code(code):
    s = str(code)
    code_exec = compile(s, '<module>', 'exec')
    r = code.split('.')
    if not (r[len(r) - 1] == 'py')or(r[len(r) - 1] == 'pyw'):
        exec(code_exec)
def run_path(path):
    s = str(path)
    code_exec = compile(s, '<module>', 'exec')
    r = path.split('.')
    if(r[len(r) - 1] == 'py')or(r[len(r) - 1] == 'pyw'):
        exec(code_exec)
if __name__ == '__main__':
    while True:
         run_code(input('>>'))
