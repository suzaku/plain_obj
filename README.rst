plain_obj
##########

.. image:: https://travis-ci.org/suzaku/plain_obj.svg?branch=master
    :target: https://travis-ci.org/suzaku/plain_obj
.. image:: https://img.shields.io/pypi/v/plain_obj.svg
    :target: https://pypi.python.org/pypi/plain_obj

A faster alternative to namedtuple.

Basic Usage
***********

Creation
========

.. code-block:: python

    import plain_obj
    Config = plain_obj.new_type('Config', 'is_debug, skips_dist, run_tests')
    config = Config(True, False, True)
    if config.is_debug:
        print("This is a verbose debugging message.")

Make a dict
===========

.. code-block:: python
    
    config.as_dict()

Unpacking
=========

.. code-block:: python
    
    is_debug, _, run_tests = config


.. image:: https://app.codesponsor.io/embed/MY7qFCdB7bDgiBqdjtV9ASYi/suzaku/plain_obj.svg
    :width: 888px
    :height: 68px
    :alt: Sponsor
    :target: https://app.codesponsor.io/link/MY7qFCdB7bDgiBqdjtV9ASYi/suzaku/plain_obj


When to use ``plain_obj`` instead of ``namedtuple``?
************************************************************

**When faster creation time matters to you.**

Comparing ``plain_obj`` with ``namedtuple`` in *Python 2.7*:

.. code-block:: python

    In [3]: %timeit collections.namedtuple('Point', ['x', 'y', 'z'])
    1000 loops, best of 3: 338 µs per loop

    In [4]: %timeit plain_obj.new_type('Point', ['x', 'y', 'z'])
    10000 loops, best of 3: 97.8 µs per loop

    In [5]: Point = collections.namedtuple('Point', ['x', 'y', 'z'])

    In [6]: NewPoint = plain_obj.new_type('Point', ['x', 'y', 'z'])

    In [7]: %timeit Point(1, 2, 3)
    The slowest run took 7.99 times longer than the fastest. This could mean that an intermediate result is being cached.
    1000000 loops, best of 3: 507 ns per loop

    In [8]: %timeit NewPoint(1, 2, 3)
    The slowest run took 6.70 times longer than the fastest. This could mean that an intermediate result is being cached.
    1000000 loops, best of 3: 462 ns per loop

    In [9]: p = Point(1, 2, 3)

    In [10]: new_p = NewPoint(1, 2, 3)

    In [11]: %timeit p.x, p.y, p.z
    The slowest run took 9.92 times longer than the fastest. This could mean that an intermediate result is being cached.
    1000000 loops, best of 3: 408 ns per loop

    In [12]: %timeit new_p.x, new_p.y, new_p.z
    The slowest run took 11.70 times longer than the fastest. This could mean that an intermediate result is being cached.
    10000000 loops, best of 3: 163 ns per loop

Comparing ``plain_obj`` with ``namedtuple`` in *Python 3.6*:

.. code-block:: python

    In [3]: %timeit collections.namedtuple('Point', ['x', 'y', 'z'])
    382 µs ± 3.82 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

    In [4]: %timeit plain_obj.new_type('Point', ['x', 'y', 'z'])
    53.5 µs ± 1.2 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

    In [5]: Point = collections.namedtuple('Point', ['x', 'y', 'z'])

    In [6]: NewPoint = plain_obj.new_type('Point', ['x', 'y', 'z'])

    In [7]: %timeit Point(1, 2, 3)
    521 ns ± 2.5 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

    In [8]: %timeit NewPoint(1, 2, 3)
    438 ns ± 5.53 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

    In [9]: p = Point(1, 2, 3)

    In [10]: new_p = NewPoint(1, 2, 3)

    In [11]: %timeit p.x, p.y, p.z
    282 ns ± 2.52 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

    In [12]: %timeit new_p.x, new_p.y, new_p.z
    148 ns ± 1.7 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

As you can see, it's faster in all cases including *type creation*, *object instantiation* and *attribute access*.
