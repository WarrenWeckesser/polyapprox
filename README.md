`polyapprox`
============

Some tools for forming polynomial or rational approximations of the inverse
of a function.  `polyapprox` depends on [`mpmath`](https://mpmath.org/).

Two of the functions in this library are `inverse_taylor(f, x0, n)`
and `inverse_pade(f, x0, m, n)`.

`inverse_taylor`
----------------

`inverse_taylor(f, x0, n)` computes the Taylor polynomial coefficients of the
inverse of `f`.

Given a callable `f`, and a point `x0`, it finds the Taylor polynomial of
degree `n` of the inverse of `f` at `x0`.

If `y0 = f(x0)`, and if the inverse of `f` is `g`, this function returns
the Taylor polynomial coefficients of `g(y)` at `y0`.

`f'(x0)` must be nonzero.

For example,

    >>> from mpmath import mp
    >>> mp.dps = 40
    >>> from polyapprox import inverse_taylor

Compute the Taylor coefficients of the inverse of the sine function
sin(x) at `x=1`.

    >>> inverse_taylor(mp.sin, 1, 5)
    [mpf('1.0'),
     mpf('1.850815717680925617911753241398650193470396'),
     mpf('2.667464736243829370645086306803786566557799'),
     mpf('8.745566949501434796799480049601499630239969'),
     mpf('34.55691117453807764026147509020588920253199'),
     mpf('152.9343377104818039879748855586655382173672')]

Compare that to computing the Taylor polynomial coefficients of
the arcsine function directly:

    >>> mp.taylor(mp.asin, mp.sin(1), 5)
    [mpf('1.0'),
     mpf('1.850815717680925617911753241398650193470396'),
     mpf('2.667464736243829370645086306803786566557799'),
     mpf('8.745566949501434796799480049601499630240153'),
     mpf('34.55691117453807764026147509020588920253199'),
     mpf('152.9343377104818039879748855586655382173702')]


`inverse_pade`
--------------

`inverse_pade(f, x0, m, n)` Padé approximant coefficients of the inverse of `f`.

Given a callable `f`, and a point `x0`, it finds the Padé approximant of degree
`(m, n)` of the inverse of `f` at `x0`.

If `y0 = f(x0)`, and if the inverse of `f` is `g`, this function returns
the Padé approximant coefficients of `g(y)` at `y0`.

`f'(x0)` must be nonzero.

For example,

    >>> from mpmath import mp
    >>> mp.dps = 40
    >>> from polyapprox import inverse_pade

Compute the Padé approximant to the inverse of sin(x) at `x=1`.

    >>> inverse_pade(mp.sin, 1, 5, 4)
    ([mpf('1.0'),
      mpf('-5.428836087225345782152614868037223199487785'),
      mpf('-14.59025586448337482707922792297134121701713'),
      mpf('76.66727054306441691994858675947043862200347'),
      mpf('20.92630843471146736348587129663693571301545'),
      mpf('-91.95538065543221755259217919809770565490541')],
     [mpf('1.0'),
      mpf('-7.279651804906271400064368109435873392958164'),
      mpf('-3.784426620962357975179374311522526358975659'),
      mpf('94.34419434777145262733458338059694153109452'),
      mpf('-114.4848137234397209897780633142520390436954')])

Compare that to computing the Padé approximant of the arcsine
function directly.

    >>> c = mp.taylor(mp.asin, mp.sin(1), 10)
    >>> mp.pade(c, 5, 4)
    ([mpf('1.0'),
      mpf('-5.428836087225345782152614868037223199022362'),
      mpf('-14.59025586448337482707922792297134122127003'),
      mpf('76.66727054306441691994858675947043863057723'),
      mpf('20.92630843471146736348587129663693571903839'),
      mpf('-91.95538065543221755259217919809770566742443')],
     [mpf('1.0'),
      mpf('-7.279651804906271400064368109435873392492793'),
      mpf('-3.784426620962357975179374311522526364090111'),
      mpf('94.34419434777145262733458338059694154789217'),
      mpf('-114.4848137234397209897780633142520390591904')])
