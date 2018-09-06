if !has("python3")
    echo "vim has to be compiled with +python3 to run this"
    finish
endif

let s:map_key_default = "<Space>"
let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

py3 import sys
py3 from os.path import normpath, join
py3 import vim
py3 plugin_root_dir = vim.eval('s:plugin_root_dir')
py3 python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
py3 sys.path.insert(0, python_root_dir)
py3 import repl_client

function! EvalRepl(filetype) range
    py3 repl_client.eval_repl(vim.eval("a:filetype"), vim.eval("a:firstline"), vim.eval("a:lastline"))
endfunction

function! EvalFileType(filetype)
    let l:map_key = exists('g:vim_repl_map_key') ? g:vim_repl_map_key : s:map_key_default
    execute "vm <buffer> ". l:map_key . " :call EvalRepl('". a:filetype ."')<CR>" 
endfunction

au FileType * call EvalFileType(&filetype)
