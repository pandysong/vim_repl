import vim


def eval_repl(filetype, firstline, lastline):
    s, e = int(firstline) - 1, int(lastline)

    str_in = ["", "# Input: "] + vim.current.buffer[s:e+1]
    str_out = ["# Output", "output line1", "output line2"]
    # print("start,end", s, e)
    # print(str_in)
    # print(str_out)

    vim.current.buffer[e+1:e+1] = str_in + str_out
