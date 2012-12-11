# encoding: utf-8
#from pypy.rlib.jit import hint
from pypy.rlib import jit  # , debug


class StackMixin(object):
    _mixin_ = True

    def __init__(self):
        self._init_stack_()

    def _init_stack_(self, size=1, resize=True):
        self._stack_ = [None] * size
        self._stack_pointer_ = 0
        self._stack_resize_ = resize

    def _stack_pointer(self):
        return jit.promote(self._stack_pointer_)

    def _stack_pop(self):
        e = self._stack_top()
        i = self._stack_pointer() - 1
        assert i >= 0
        self._stack_[i] = None
        self._stack_pointer_ = i
        return e

    def _stack_top(self):
        i = self._stack_pointer() - 1
        if i < 0:
            raise IndexError
        return self._stack_[i]

    def _stack_append(self, element):
        i = self._stack_pointer()
        len_stack = len(self._stack_)

        assert i >= 0
        if len_stack <= i and self._stack_resize_ is True:
            self._stack_ += [None]
        else:
            assert len_stack > i

        self._stack_[i] = element
        self._stack_pointer_ = i + 1

    def _set_stack_pointer(self, p):
        self._stack_pointer_ = p

    #@jit.unroll_safe
    def _stack_pop_n(self, n):
        l = [None] * n
        for i in range(n - 1, -1, -1):
            l[i] = self._stack_pop()
        #debug.make_sure_not_resized(l)
        return l
