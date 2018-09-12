import vim
import socket


def _eval_in_server(lines):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 9987))
    for line in lines:
        s.send((line+'\n').encode())
        data = s.recv(1024)
    s.close


def eval_repl(filetype, firstline, lastline):
    s, e = int(firstline) - 1, int(lastline)
    if e-s > 1:
        out = [':{'] + vim.current.buffer[s:e] + [':}']
    else:
        out = vim.current.buffer[s:e]

    _eval_in_server(out)

    # str_in = ["", "# Input: "] + vim.current.buffer[s:e+1]
    # str_out = ["# Output", "output line1", "output line2"]
    # print("start,end", s, e)
    # print(str_in)
    # print(str_out)

    #vim.current.buffer[e+1:e+1] = str_in + str_out
