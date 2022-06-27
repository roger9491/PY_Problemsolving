from subprocess import call
from unittest import case


production S
    switch()
        case peek() {a,b}
        call    A()
        call    C()