alias cs120w='ssh -X jur009@ieng9.ucsd.edu'
alias cs30x='ssh -X cs30x40@ieng9.ucsd.edu'
alias ll='ls -l -a'

function over80 {
    for f in "$@"; do
        expand -t 8 $f | awk 'length($0) > 80 { print "'$f'" ":" NR ":" $0 }'
    done
}
