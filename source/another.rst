RST tests
=========

Some basic layout
-----------------

.. _list_label:

Lists
+++++

* A *thing*.
* Another **thing**.

or

- Some.
- Thing.
- Different.

Linking
+++++++

This should be a subsection...

There is this page you can use to search for things: http://www.google.com
In HTTPS it looks like this: https://www.google.com
Alternatively like one could click `this <http://www.google.com>`_.
`This <http://www.google.com>`_ syntax is a bit weird with the underscore, but oh well...

I wonder if :doc:`this link <index>` to the index page will work...

This should be a link to the Lists page: :ref:`list_label`

Images
++++++

.. figure::  images/cloud.jpg
   :align:   center
   
   Amazing cloud image

.. figure::  images/cloud.jpg
   
   Another amazing cloud image
   
Something
+++++++++

This is a statement.

.. note::

    This is a note

.. warning::

    This is a warning

.. versionadded:: 0.1

.. versionchanged:: 0.5

.. deprecated:: 0.6

.. seealso::

    See also...
    
.. hlist::
   :columns: 3

   * A list of
   * short items
   * that should be
   * displayed
   * horizontally

It's okay to use this code.

Let's add some code
===================

Here's some python::

    def my_fn(foo, bar=True):
        """A really useful function.

        Returns None
        """

.. highlight:: c++

And some C++::

    int main(void)
    {
        std::cout << "Hello, world" << std::endl;
    }
    
The highlighting is now default C++, but we can also do this with code blocks like this:

.. code-block:: python

   class X:
       def __init__(self):
           self.x = 42
           
Inline code works with backticks ``if __name__ == '__main__':``

.. autoclass:: foo.FooClass
   :members:
   :private-members:
   :special-members: