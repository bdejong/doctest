class FooClass:
    def __init__(self):
        """This is the documentation of the FooClass
        __init__ function!"""
        pass
        
    @classmethod
    def complex(self, real=0.0, imag=0.0):
        """Form a complex number.

        Keyword arguments:
        real -- the real part (default 0.0)
        imag -- the imaginary part (default 0.0)
        """
        if imag == 0.0 and real == 0.0:
            return complex_zero
            
            
    def public_fn_with_googley_docstring(self, name, another, state=None):
        """This function does something.

        Args:
            path (str): The path of the file to wrap
            field_storage (FileStorage): The :class:`FileStorage` instance to wrap
            temporary (bool): Whether or not to delete the file when the File
               instance is destructed

        Returns:
            BufferedFileStorage: A buffered writable file descriptor

        A really great idea.  A way you might use me is

        >>> print public_fn_with_googley_docstring(name='foo', state=None)
        0

        BTW, this always returns 0.  **NEVER** use with :class:`MyPublicClass`.

        """
        return 0

    def public_fn_with_sphinxy_docstring(self, name, state=None):
        """This function does something.

        :param name: The name to use.
        :type name: str.
        :param state: Current state to be in.
        :type state: bool.
        :returns:  int -- the return code.
        :raises: AttributeError, KeyError

        """
        return 0

    def public_fn_without_docstring(self):
        return True

    def _private_fn_with_docstring(self, foo, bar='baz', foobarbas=None):
        """I have a docstring, but won't be imported if you just use ``:members:``.
        """
        return None