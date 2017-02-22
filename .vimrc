" ~/.vimrc
" Updated by Junru Thomas Ren
" Jan 15, 2017
" Based on the original .vimrc by Lisa McCutcheon

" **************************************
" * VARIABLES
" **************************************
set nocompatible		" get rid of strict vi compatibility!
set nu				" line numbering on
set si				" smartindent on
set noerrorbells		" bye bye bells :)
set modeline			" show what I'm doing
set showmode			" show the mode on the dedicated line (see above)
set nowrap			" no wrapping!
set ignorecase			" search without regards to case
set backspace=indent,eol,start	" backspace over everything
set fileformats=unix,dos,mac	" open files from mac/dos
set exrc			" open local config files
set nojoinspaces		" don't add white space when I don't tell you to
set ruler			" which line am I on?
set showmatch			" ensure Dyck language
set incsearch			" incremental searching
"set nohlsearch			" meh
set bs=2			" fix backspacing in insert mode
set bg=light
set mouse=a

" change tabstop width for python files
autocmd BufRead,BufNewFile *.py set tabstop=4
autocmd BufRead,BufNewFile *.py set shiftwidth=4

" Expand tabs in C files to spaces
au BufRead,BufNewFile *.{c,h,java} set expandtab
au BufRead,BufNewFile *.{c,h,java} set shiftwidth=2
au BufRead,BufNewFile *.{c,h,java} set tabstop=2

" Do not expand tabs in assembly file.  Make them 8 chars wide.
au BufRead,BufNewFile *.s set noexpandtab
au BufRead,BufNewFile *.s set shiftwidth=8
au BufRead,BufNewFile *.s set tabstop=8

" Show syntax
syntax on

" This is my prefered colorscheme, open a file with gvim to view others
:colors elflord

" For switching between many opened file by using ctrl+l or ctrl+h
map <C-J> :next <CR>
map <C-K> :prev <CR>

" Spelling toggle via F10 and F11
map <F10> <Esc>setlocal spell spelllang=en_us<CR>
map <F11> <Esc>setlocal nospell<CR>

" setlocal textwidth=80		" used for text wrapping
match ErrorMsg '\%>80v.\+'	" Highlight character after the 80th column red

" Insert a file header (UC San Diego CSE 30 version) via F9
function FileHeading()
	let s:line=line(".")
	call setline (s:line,   "/*")
	call append  (s:line,   " * Filename: " .expand("%"))
	call append  (s:line+1, " * Author: Junru Ren")
	call append  (s:line+2, " * Userid: cs30xxx")
	call append  (s:line+3, " * Description: TODO")
	call append  (s:line+4, " * Date: " .strftime("%b %d %Y"))
	call append  (s:line+5, " * Sources of Help: TODO")
	call append  (s:line+6, " */")
	unlet s:line
endfunction

imap <F9> <ESC>mz:execute FileHeading()<CR>
