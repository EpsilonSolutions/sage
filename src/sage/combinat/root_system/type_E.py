from ambient_space import AmbientSpace
from sage.rings.all import ZZ
from sage.combinat.family import Family

class ambient_space(AmbientSpace):
    """
    The lattice behind E6, E7, or E8.  The computations are based on Bourbaki,
    Groupes et Algebres de Lie, Ch. 4,5,6 (planche V-VII).
    """
    def __init__(self, root_system, baseRing):
        """
        Create the ambient space for the root system for E6, E7, E8.
        Specify the Base, i.e., the simple roots w.r. to the canonical
        basis for R^8.

        EXAMPLES:
            sage: e = RootSystem(['E',6]).ambient_space()
            sage: e == loads(dumps(e))
            True
            sage: [e.weyl_dimension(v) for v in e.fundamental_weights()]
            [27, 78, 351, 2925, 351, 27]
            sage: e = RootSystem(['E',7]).ambient_space()
            sage: [e.weyl_dimension(v) for v in e.fundamental_weights()]
            [133, 912, 8645, 365750, 27664, 1539, 56]
            sage: e = RootSystem(['E',8]).ambient_space()
            sage: [e.weyl_dimension(v) for v in e.fundamental_weights()]
            [3875, 147250, 6696000, 6899079264, 146325270, 2450240, 30380, 248]
           """
        v = ZZ(1)/ZZ(2)
        self.rank = root_system.cartan_type().rank()
        AmbientSpace.__init__(self, root_system, baseRing)
        if self.rank == 6:
            self.Base = [v*(self.root(0,7)-self.root(1,2,3,4,5,6)),
                         self.root(0,1),
                         self.root(0,1,p1=1),
                         self.root(1,2,p1=1),
                         self.root(2,3,p1=1),
                         self.root(3,4,p1=1)]
        elif self.rank == 7:
            self.Base = [v*(self.root(0,7)-self.root(1,2,3,4,5,6)),
                         self.root(0,1),
                         self.root(0,1,p1=1),
                         self.root(1,2,p1=1),
                         self.root(2,3,p1=1),
                         self.root(3,4,p1=1),
                         self.root(4,5,p1=1)]
        elif self.rank == 8:
            self.Base = [v*(self.root(0,7)-self.root(1,2,3,4,5,6)),
                         self.root(0,1),
                         self.root(0,1,p1=1),
                         self.root(1,2,p1=1),
                         self.root(2,3,p1=1),
                         self.root(3,4,p1=1),
                         self.root(4,5,p1=1),
                         self.root(5,6,p1=1)]
        else:
            raise NotImplementedError, "Type \'E\' root systems only come in flavors 6, 7, 8.  Please make another choice"

    def dimension(self):
        """
        EXAMPLES:
            sage: e = RootSystem(['E',6]).ambient_space()
            sage: e.dimension()
            8
        """
        return 8

    def root(self, i1, i2=None, i3=None, i4=None, i5=None, i6=None, i7=None, i8=None, p1=0, p2=0, p3=0, p4=0, p5=0, p6=0, p7=0, p8=0):
        """
        Compute an element of the underlying lattice, using the specified elements of
        the standard basis, with signs dictated by the corresponding 'pi' arguments.
        We rely on the caller to provide the correct arguments.
        This is typically used to generate roots, although the generated elements
        need not be roots themselves.
        We assume that if one of the indices is not given, the rest are not as well.
        This should work for E6, E7, E8.

        EXAMPLES:
            sage: e = RootSystem(['E',6]).ambient_space()
            sage: [ e.root(i, j, p3=1) for i in xrange(e.n) for j in xrange(i+1, e.n) ]
            [(1, 1, 0, 0, 0, 0, 0, 0),
             (1, 0, 1, 0, 0, 0, 0, 0),
             (1, 0, 0, 1, 0, 0, 0, 0),
             (1, 0, 0, 0, 1, 0, 0, 0),
             (1, 0, 0, 0, 0, 1, 0, 0),
             (1, 0, 0, 0, 0, 0, 1, 0),
             (1, 0, 0, 0, 0, 0, 0, 1),
             (0, 1, 1, 0, 0, 0, 0, 0),
             (0, 1, 0, 1, 0, 0, 0, 0),
             (0, 1, 0, 0, 1, 0, 0, 0),
             (0, 1, 0, 0, 0, 1, 0, 0),
             (0, 1, 0, 0, 0, 0, 1, 0),
             (0, 1, 0, 0, 0, 0, 0, 1),
             (0, 0, 1, 1, 0, 0, 0, 0),
             (0, 0, 1, 0, 1, 0, 0, 0),
             (0, 0, 1, 0, 0, 1, 0, 0),
             (0, 0, 1, 0, 0, 0, 1, 0),
             (0, 0, 1, 0, 0, 0, 0, 1),
             (0, 0, 0, 1, 1, 0, 0, 0),
             (0, 0, 0, 1, 0, 1, 0, 0),
             (0, 0, 0, 1, 0, 0, 1, 0),
             (0, 0, 0, 1, 0, 0, 0, 1),
             (0, 0, 0, 0, 1, 1, 0, 0),
             (0, 0, 0, 0, 1, 0, 1, 0),
             (0, 0, 0, 0, 1, 0, 0, 1),
             (0, 0, 0, 0, 0, 1, 1, 0),
             (0, 0, 0, 0, 0, 1, 0, 1),
             (0, 0, 0, 0, 0, 0, 1, 1)]
        """
        if i1 == i2 or i2 == None:
            return (-1)**p1*self._term(i1)
        if i3 == None:
            return (-1)**p1*self._term(i1) + (-1)**p2*self._term(i2)
        if i4 == None:
            return (-1)**p1*self._term(i1) + (-1)**p2*self._term(i2)+(-1)**p3*self._term(i3)
        if i5 == None:
            return (-1)**p1*self._term(i1) + (-1)**p2*self._term(i2)+(-1)**p3*self._term(i3)+(-1)**p4*self._term(i4)
        if i6 == None:
            return (-1)**p1*self._term(i1) + (-1)**p2*self._term(i2)+(-1)**p3*self._term(i3)+(-1)**p4*self._term(i4)+(-1)**p5*self._term(i5)
        if i7 == None:
            return (-1)**p1*self._term(i1) + (-1)**p2*self._term(i2)+(-1)**p3*self._term(i3)+(-1)**p4*self._term(i4)+(-1)**p5*self._term(i5)+(-1)**p6*self._term(i6)
        if i8 == None:
            return (-1)**p1*self._term(i1) + (-1)**p2*self._term(i2)+(-1)**p3*self._term(i3)+(-1)**p4*self._term(i4)+(-1)**p5*self._term(i5)+(-1)**p6*self._term(i6)+(-1)**p7*self._term(i7)
        return (-1)**p1*self._term(i1) + (-1)**p2*self._term(i2)+(-1)**p3*self._term(i3)+(-1)**p4*self._term(i4)+(-1)**p5*self._term(i5)+(-1)**p6*self._term(i6)+(-1)**p7*self._term(i7)+(-1)**p8*self._term(i8)

    def simple_root(self, i):
        """
        There are computed as what Bourbaki calls the Base:
            a1 = e2-e3, a2 = e3-e4, a3 = e4, a4 = 1/2*(e1-e2-e3-e4)

        EXAMPLES:
            sage: LE6 = RootSystem(['E',6]).ambient_space()
            sage: LE6.simple_roots()
            Finite family {1: (1/2, -1/2, -1/2, -1/2, -1/2, -1/2, -1/2, 1/2), 2: (1, 1, 0, 0, 0, 0, 0, 0), 3: (-1, 1, 0, 0, 0, 0, 0, 0), 4: (0, -1, 1, 0, 0, 0, 0, 0), 5: (0, 0, -1, 1, 0, 0, 0, 0), 6: (0, 0, 0, -1, 1, 0, 0, 0)}
        """
        assert(i in self.index_set())
        return self.Base[i-1]

    def negative_roots(self):
        """
        The negative negative roots.

        EXAMPLES:
            sage: e = RootSystem(['E',6]).ambient_space()
            sage: e.negative_roots()
            [(-1, -1, 0, 0, 0, 0, 0, 0),
             (-1, 0, -1, 0, 0, 0, 0, 0),
             (-1, 0, 0, -1, 0, 0, 0, 0),
             (-1, 0, 0, 0, -1, 0, 0, 0),
             (0, -1, -1, 0, 0, 0, 0, 0),
             (0, -1, 0, -1, 0, 0, 0, 0),
             (0, -1, 0, 0, -1, 0, 0, 0),
             (0, 0, -1, -1, 0, 0, 0, 0),
             (0, 0, -1, 0, -1, 0, 0, 0),
             (0, 0, 0, -1, -1, 0, 0, 0),
             (1, -1, 0, 0, 0, 0, 0, 0),
             (1, 0, -1, 0, 0, 0, 0, 0),
             (1, 0, 0, -1, 0, 0, 0, 0),
             (1, 0, 0, 0, -1, 0, 0, 0),
             (0, 1, -1, 0, 0, 0, 0, 0),
             (0, 1, 0, -1, 0, 0, 0, 0),
             (0, 1, 0, 0, -1, 0, 0, 0),
             (0, 0, 1, -1, 0, 0, 0, 0),
             (0, 0, 1, 0, -1, 0, 0, 0),
             (0, 0, 0, 1, -1, 0, 0, 0),
             (-1/2, -1/2, -1/2, -1/2, -1/2, 1/2, 1/2, -1/2),
             (-1/2, -1/2, -1/2, 1/2, 1/2, 1/2, 1/2, -1/2),
             (-1/2, -1/2, 1/2, -1/2, 1/2, 1/2, 1/2, -1/2),
             (-1/2, -1/2, 1/2, 1/2, -1/2, 1/2, 1/2, -1/2),
             (-1/2, 1/2, -1/2, -1/2, 1/2, 1/2, 1/2, -1/2),
             (-1/2, 1/2, -1/2, 1/2, -1/2, 1/2, 1/2, -1/2),
             (-1/2, 1/2, 1/2, -1/2, -1/2, 1/2, 1/2, -1/2),
             (-1/2, 1/2, 1/2, 1/2, 1/2, 1/2, 1/2, -1/2),
             (1/2, -1/2, -1/2, -1/2, 1/2, 1/2, 1/2, -1/2),
             (1/2, -1/2, -1/2, 1/2, -1/2, 1/2, 1/2, -1/2),
             (1/2, -1/2, 1/2, -1/2, -1/2, 1/2, 1/2, -1/2),
             (1/2, -1/2, 1/2, 1/2, 1/2, 1/2, 1/2, -1/2),
             (1/2, 1/2, -1/2, -1/2, -1/2, 1/2, 1/2, -1/2),
             (1/2, 1/2, -1/2, 1/2, 1/2, 1/2, 1/2, -1/2),
             (1/2, 1/2, 1/2, -1/2, 1/2, 1/2, 1/2, -1/2),
             (1/2, 1/2, 1/2, 1/2, -1/2, 1/2, 1/2, -1/2)]
        """
        return [ -a for a in self.positive_roots()]

    def positive_roots(self):
        """
        These are the roots positive w.r. to lexicographic ordering of the
        basis elements (e1<...<e4).

        EXAMPLES:
            sage: e = RootSystem(['E',6]).ambient_space()
            sage: e.positive_roots()
            [(1, 1, 0, 0, 0, 0, 0, 0),
             (1, 0, 1, 0, 0, 0, 0, 0),
             (1, 0, 0, 1, 0, 0, 0, 0),
             (1, 0, 0, 0, 1, 0, 0, 0),
             (0, 1, 1, 0, 0, 0, 0, 0),
             (0, 1, 0, 1, 0, 0, 0, 0),
             (0, 1, 0, 0, 1, 0, 0, 0),
             (0, 0, 1, 1, 0, 0, 0, 0),
             (0, 0, 1, 0, 1, 0, 0, 0),
             (0, 0, 0, 1, 1, 0, 0, 0),
             (-1, 1, 0, 0, 0, 0, 0, 0),
             (-1, 0, 1, 0, 0, 0, 0, 0),
             (-1, 0, 0, 1, 0, 0, 0, 0),
             (-1, 0, 0, 0, 1, 0, 0, 0),
             (0, -1, 1, 0, 0, 0, 0, 0),
             (0, -1, 0, 1, 0, 0, 0, 0),
             (0, -1, 0, 0, 1, 0, 0, 0),
             (0, 0, -1, 1, 0, 0, 0, 0),
             (0, 0, -1, 0, 1, 0, 0, 0),
             (0, 0, 0, -1, 1, 0, 0, 0),
             (1/2, 1/2, 1/2, 1/2, 1/2, -1/2, -1/2, 1/2),
             (1/2, 1/2, 1/2, -1/2, -1/2, -1/2, -1/2, 1/2),
             (1/2, 1/2, -1/2, 1/2, -1/2, -1/2, -1/2, 1/2),
             (1/2, 1/2, -1/2, -1/2, 1/2, -1/2, -1/2, 1/2),
             (1/2, -1/2, 1/2, 1/2, -1/2, -1/2, -1/2, 1/2),
             (1/2, -1/2, 1/2, -1/2, 1/2, -1/2, -1/2, 1/2),
             (1/2, -1/2, -1/2, 1/2, 1/2, -1/2, -1/2, 1/2),
             (1/2, -1/2, -1/2, -1/2, -1/2, -1/2, -1/2, 1/2),
             (-1/2, 1/2, 1/2, 1/2, -1/2, -1/2, -1/2, 1/2),
             (-1/2, 1/2, 1/2, -1/2, 1/2, -1/2, -1/2, 1/2),
             (-1/2, 1/2, -1/2, 1/2, 1/2, -1/2, -1/2, 1/2),
             (-1/2, 1/2, -1/2, -1/2, -1/2, -1/2, -1/2, 1/2),
             (-1/2, -1/2, 1/2, 1/2, 1/2, -1/2, -1/2, 1/2),
             (-1/2, -1/2, 1/2, -1/2, -1/2, -1/2, -1/2, 1/2),
             (-1/2, -1/2, -1/2, 1/2, -1/2, -1/2, -1/2, 1/2),
             (-1/2, -1/2, -1/2, -1/2, 1/2, -1/2, -1/2, 1/2)]
            sage: e.rho()
            (0, 1, 2, 3, 4, -4, -4, 4)
            sage: E8 = RootSystem(['E',8])
            sage: e = E8.ambient_space()
            sage: e.negative_roots()
            [(-1, -1, 0, 0, 0, 0, 0, 0),
             (-1, 0, -1, 0, 0, 0, 0, 0),
             (-1, 0, 0, -1, 0, 0, 0, 0),
             (-1, 0, 0, 0, -1, 0, 0, 0),
             (-1, 0, 0, 0, 0, -1, 0, 0),
             (-1, 0, 0, 0, 0, 0, -1, 0),
             (-1, 0, 0, 0, 0, 0, 0, -1),
             (0, -1, -1, 0, 0, 0, 0, 0),
             (0, -1, 0, -1, 0, 0, 0, 0),
             (0, -1, 0, 0, -1, 0, 0, 0),
             (0, -1, 0, 0, 0, -1, 0, 0),
             (0, -1, 0, 0, 0, 0, -1, 0),
             (0, -1, 0, 0, 0, 0, 0, -1),
             (0, 0, -1, -1, 0, 0, 0, 0),
             (0, 0, -1, 0, -1, 0, 0, 0),
             (0, 0, -1, 0, 0, -1, 0, 0),
             (0, 0, -1, 0, 0, 0, -1, 0),
             (0, 0, -1, 0, 0, 0, 0, -1),
             (0, 0, 0, -1, -1, 0, 0, 0),
             (0, 0, 0, -1, 0, -1, 0, 0),
             (0, 0, 0, -1, 0, 0, -1, 0),
             (0, 0, 0, -1, 0, 0, 0, -1),
             (0, 0, 0, 0, -1, -1, 0, 0),
             (0, 0, 0, 0, -1, 0, -1, 0),
             (0, 0, 0, 0, -1, 0, 0, -1),
             (0, 0, 0, 0, 0, -1, -1, 0),
             (0, 0, 0, 0, 0, -1, 0, -1),
             (0, 0, 0, 0, 0, 0, -1, -1),
             (1, -1, 0, 0, 0, 0, 0, 0),
             (1, 0, -1, 0, 0, 0, 0, 0),
             (1, 0, 0, -1, 0, 0, 0, 0),
             (1, 0, 0, 0, -1, 0, 0, 0),
             (1, 0, 0, 0, 0, -1, 0, 0),
             (1, 0, 0, 0, 0, 0, -1, 0),
             (1, 0, 0, 0, 0, 0, 0, -1),
             (0, 1, -1, 0, 0, 0, 0, 0),
             (0, 1, 0, -1, 0, 0, 0, 0),
             (0, 1, 0, 0, -1, 0, 0, 0),
             (0, 1, 0, 0, 0, -1, 0, 0),
             (0, 1, 0, 0, 0, 0, -1, 0),
             (0, 1, 0, 0, 0, 0, 0, -1),
             (0, 0, 1, -1, 0, 0, 0, 0),
             (0, 0, 1, 0, -1, 0, 0, 0),
             (0, 0, 1, 0, 0, -1, 0, 0),
             (0, 0, 1, 0, 0, 0, -1, 0),
             (0, 0, 1, 0, 0, 0, 0, -1),
             (0, 0, 0, 1, -1, 0, 0, 0),
             (0, 0, 0, 1, 0, -1, 0, 0),
             (0, 0, 0, 1, 0, 0, -1, 0),
             (0, 0, 0, 1, 0, 0, 0, -1),
             (0, 0, 0, 0, 1, -1, 0, 0),
             (0, 0, 0, 0, 1, 0, -1, 0),
             (0, 0, 0, 0, 1, 0, 0, -1),
             (0, 0, 0, 0, 0, 1, -1, 0),
             (0, 0, 0, 0, 0, 1, 0, -1),
             (0, 0, 0, 0, 0, 0, 1, -1),
             (-1/2, -1/2, -1/2, -1/2, -1/2, -1/2, -1/2, -1/2),
             (-1/2, -1/2, -1/2, -1/2, -1/2, 1/2, 1/2, -1/2),
             (-1/2, -1/2, -1/2, -1/2, 1/2, -1/2, 1/2, -1/2),
             (-1/2, -1/2, -1/2, -1/2, 1/2, 1/2, -1/2, -1/2),
             (-1/2, -1/2, -1/2, 1/2, -1/2, -1/2, 1/2, -1/2),
             (-1/2, -1/2, -1/2, 1/2, -1/2, 1/2, -1/2, -1/2),
             (-1/2, -1/2, -1/2, 1/2, 1/2, -1/2, -1/2, -1/2),
             (-1/2, -1/2, -1/2, 1/2, 1/2, 1/2, 1/2, -1/2),
             (-1/2, -1/2, 1/2, -1/2, -1/2, -1/2, 1/2, -1/2),
             (-1/2, -1/2, 1/2, -1/2, -1/2, 1/2, -1/2, -1/2),
             (-1/2, -1/2, 1/2, -1/2, 1/2, -1/2, -1/2, -1/2),
             (-1/2, -1/2, 1/2, -1/2, 1/2, 1/2, 1/2, -1/2),
             (-1/2, -1/2, 1/2, 1/2, -1/2, -1/2, -1/2, -1/2),
             (-1/2, -1/2, 1/2, 1/2, -1/2, 1/2, 1/2, -1/2),
             (-1/2, -1/2, 1/2, 1/2, 1/2, -1/2, 1/2, -1/2),
             (-1/2, -1/2, 1/2, 1/2, 1/2, 1/2, -1/2, -1/2),
             (-1/2, 1/2, -1/2, -1/2, -1/2, -1/2, 1/2, -1/2),
             (-1/2, 1/2, -1/2, -1/2, -1/2, 1/2, -1/2, -1/2),
             (-1/2, 1/2, -1/2, -1/2, 1/2, -1/2, -1/2, -1/2),
             (-1/2, 1/2, -1/2, -1/2, 1/2, 1/2, 1/2, -1/2),
             (-1/2, 1/2, -1/2, 1/2, -1/2, -1/2, -1/2, -1/2),
             (-1/2, 1/2, -1/2, 1/2, -1/2, 1/2, 1/2, -1/2),
             (-1/2, 1/2, -1/2, 1/2, 1/2, -1/2, 1/2, -1/2),
             (-1/2, 1/2, -1/2, 1/2, 1/2, 1/2, -1/2, -1/2),
             (-1/2, 1/2, 1/2, -1/2, -1/2, -1/2, -1/2, -1/2),
             (-1/2, 1/2, 1/2, -1/2, -1/2, 1/2, 1/2, -1/2),
             (-1/2, 1/2, 1/2, -1/2, 1/2, -1/2, 1/2, -1/2),
             (-1/2, 1/2, 1/2, -1/2, 1/2, 1/2, -1/2, -1/2),
             (-1/2, 1/2, 1/2, 1/2, -1/2, -1/2, 1/2, -1/2),
             (-1/2, 1/2, 1/2, 1/2, -1/2, 1/2, -1/2, -1/2),
             (-1/2, 1/2, 1/2, 1/2, 1/2, -1/2, -1/2, -1/2),
             (-1/2, 1/2, 1/2, 1/2, 1/2, 1/2, 1/2, -1/2),
             (1/2, -1/2, -1/2, -1/2, -1/2, -1/2, 1/2, -1/2),
             (1/2, -1/2, -1/2, -1/2, -1/2, 1/2, -1/2, -1/2),
             (1/2, -1/2, -1/2, -1/2, 1/2, -1/2, -1/2, -1/2),
             (1/2, -1/2, -1/2, -1/2, 1/2, 1/2, 1/2, -1/2),
             (1/2, -1/2, -1/2, 1/2, -1/2, -1/2, -1/2, -1/2),
             (1/2, -1/2, -1/2, 1/2, -1/2, 1/2, 1/2, -1/2),
             (1/2, -1/2, -1/2, 1/2, 1/2, -1/2, 1/2, -1/2),
             (1/2, -1/2, -1/2, 1/2, 1/2, 1/2, -1/2, -1/2),
             (1/2, -1/2, 1/2, -1/2, -1/2, -1/2, -1/2, -1/2),
             (1/2, -1/2, 1/2, -1/2, -1/2, 1/2, 1/2, -1/2),
             (1/2, -1/2, 1/2, -1/2, 1/2, -1/2, 1/2, -1/2),
             (1/2, -1/2, 1/2, -1/2, 1/2, 1/2, -1/2, -1/2),
             (1/2, -1/2, 1/2, 1/2, -1/2, -1/2, 1/2, -1/2),
             (1/2, -1/2, 1/2, 1/2, -1/2, 1/2, -1/2, -1/2),
             (1/2, -1/2, 1/2, 1/2, 1/2, -1/2, -1/2, -1/2),
             (1/2, -1/2, 1/2, 1/2, 1/2, 1/2, 1/2, -1/2),
             (1/2, 1/2, -1/2, -1/2, -1/2, -1/2, -1/2, -1/2),
             (1/2, 1/2, -1/2, -1/2, -1/2, 1/2, 1/2, -1/2),
             (1/2, 1/2, -1/2, -1/2, 1/2, -1/2, 1/2, -1/2),
             (1/2, 1/2, -1/2, -1/2, 1/2, 1/2, -1/2, -1/2),
             (1/2, 1/2, -1/2, 1/2, -1/2, -1/2, 1/2, -1/2),
             (1/2, 1/2, -1/2, 1/2, -1/2, 1/2, -1/2, -1/2),
             (1/2, 1/2, -1/2, 1/2, 1/2, -1/2, -1/2, -1/2),
             (1/2, 1/2, -1/2, 1/2, 1/2, 1/2, 1/2, -1/2),
             (1/2, 1/2, 1/2, -1/2, -1/2, -1/2, 1/2, -1/2),
             (1/2, 1/2, 1/2, -1/2, -1/2, 1/2, -1/2, -1/2),
             (1/2, 1/2, 1/2, -1/2, 1/2, -1/2, -1/2, -1/2),
             (1/2, 1/2, 1/2, -1/2, 1/2, 1/2, 1/2, -1/2),
             (1/2, 1/2, 1/2, 1/2, -1/2, -1/2, -1/2, -1/2),
             (1/2, 1/2, 1/2, 1/2, -1/2, 1/2, 1/2, -1/2),
             (1/2, 1/2, 1/2, 1/2, 1/2, -1/2, 1/2, -1/2),
             (1/2, 1/2, 1/2, 1/2, 1/2, 1/2, -1/2, -1/2)]
            sage: e.rho()
            (0, 1, 2, 3, 4, 5, 6, 23)

        """
        v = ZZ(1)/ZZ(2)
        # Note that
        if not hasattr(self, 'PosRoots'):
            if self.rank == 6:
                self.PosRoots = ( [ self.root(i,j) for i in xrange(self.rank-1) for j in xrange(i+1,self.rank-1) ] +
                                  [ self.root(i,j,p1=1) for i in xrange(self.rank-1) for j in xrange(i+1,self.rank-1) ] +
                                  [ v*(self.root(7)-self.root(6)-self.root(5)+self.root(0,1,2,3,4,p1=p1,p2=p2,p3=p3,p4=p4,p5=p5))
                                    for p1 in [0,1] for p2 in [0,1] for p3 in [0,1] for p4 in [0,1] for p5 in [0,1] if (p1+p2+p3+p4+p5)%2 == 0 ])
            elif self.rank == 7:
                self.PosRoots = ( [ self.root(i,j) for i in xrange(self.rank-1) for j in xrange(i+1,self.rank-1) ] +
                                  [ self.root(i,j,p1=1) for i in xrange(self.rank-1) for j in xrange(i+1,self.rank-1) ] +
                                  [ self.root(6,7,p1=1) ] +
                                  [ v*(self.root(7)-self.root(6)+self.root(0,1,2,3,4,5,p1=p1,p2=p2,p3=p3,p4=p4,p5=p5,p6=p6))
                                    for p1 in [0,1] for p2 in [0,1] for p3 in [0,1] for p4 in [0,1] for p5 in [0,1] for p6 in [0,1] if (p1+p2+p3+p4+p5+p6)%2 == 1 ])
            elif self.rank == 8:
                self.PosRoots = ( [ self.root(i,j) for i in xrange(self.rank) for j in xrange(i+1,self.rank) ] +
                                  [ self.root(i,j,p1=1) for i in xrange(self.rank) for j in xrange(i+1,self.rank) ] +
                                  [ v*(self.root(7)+self.root(0,1,2,3,4,5,6,p1=p1,p2=p2,p3=p3,p4=p4,p5=p5,p6=p6,p7=p7))
                                    for p1 in [0,1] for p2 in [0,1] for p3 in [0,1] for p4 in [0,1] for p5 in [0,1] for p6 in [0,1] for p7 in [0,1] if (p1+p2+p3+p4+p5+p6+p7)%2 == 0 ])

        return self.PosRoots

    def fundamental_weights(self):
        """
        EXAMPLES:
            sage: e = RootSystem(['E',6]).ambient_space()
            sage: e.fundamental_weights()
            Finite family {1: (0, 0, 0, 0, 0, -2/3, -2/3, 2/3), 2: (1/2, 1/2, 1/2, 1/2, 1/2, -1/2, -1/2, 1/2), 3: (-1/2, 1/2, 1/2, 1/2, 1/2, -5/6, -5/6, 5/6), 4: (0, 0, 1, 1, 1, -1, -1, 1), 5: (0, 0, 0, 1, 1, -2/3, -2/3, 2/3), 6: (0, 0, 0, 0, 1, -1/3, -1/3, 1/3)}
        """
        v2 = ZZ(1)/ZZ(2)
        v3 = ZZ(1)/ZZ(3)
        if self.rank == 6:
            return Family({ 1: 2*v3*self.root(7,6,5,p2=1,p3=1),
                            2: v2*self.root(0,1,2,3,4,5,6,7,p6=1,p7=1),
                            3: 5*v2*v3*self.root(7,6,5,p2=1,p3=1)+v2*self.root(0,1,2,3,4,p1=1),
                            4: self.root(2,3,4,5,6,7,p4=1,p5=1),
                            5: 2*v3*self.root(7,6,5,p2=1,p3=1)+self.root(3,4),
                            6: v3*self.root(7,6,5,p2=1,p3=1)+self.root(4)})
        elif self.rank == 7:
            return Family({ 1: self.root(7,6,p2=1),
                            2: v2*self.root(0,1,2,3,4,5)+self.root(6,7,p1=1),
                            3: v2*(self.root(0,1,2,3,4,5,p1=1)+3*self.root(6,7,p1=1)),
                            4: self.root(2,3,4,5)+2*self.root(6,7,p1=1),
                            5: 3*v2*self.root(6,7,p1=1)+self.root(3,4,5),
                            6: self.root(4,5,6,7,p3=1),
                            7: self.root(5)+v2*self.root(6,7,p1=1)})
        elif self.rank == 8:
            return Family({ 1: 2*self.root(7),
                            2: v2*(self.root(0,1,2,3,4,5,6)+5*self.root(7)),
                            3: v2*(self.root(0,1,2,3,4,5,6,p1=1)+7*self.root(7)),
                            4: self.root(2,3,4,5,6)+5*self.root(7),
                            5: self.root(3,4,5,6)+4*self.root(7),
                            6: self.root(4,5,6)+3*self.root(7),
                            7: self.root(5,6)+2*self.root(7),
                            8: self.root(6,7)})


def dynkin_diagram(t):
    """
    Returns a Dynkin diagram for type E.

    EXAMPLES:
        sage: from sage.combinat.root_system.type_E import dynkin_diagram
        sage: ct = CartanType(['E',6])
        sage: e = dynkin_diagram(ct);e
                O 2
                |
                |
        O---O---O---O---O
        1   3   4   5   6
        E6
        sage: edges = e.edges(); edges.sort(); edges
        [(1, 3, 1), (2, 4, 1), (3, 1, 1), (3, 4, 1), (4, 2, 1), (4, 3, 1), (4, 5, 1), (5, 4, 1), (5, 6, 1), (6, 5, 1)]

    """
    from dynkin_diagram import precheck , DynkinDiagram_class
    precheck(t, letter="E", length=2, n_ge=3)
    n = t[1]
    g = DynkinDiagram_class(t)
    g.add_edge(1,3)
    g.add_edge(2,4)
    for i in range(3,n):
        g.add_edge(i, i+1)
    return g

def affine_dynkin_diagram(t):
    """
    Returns the extended Dynkin diagram for affine type E.

    EXAMPLES:
        sage: e = DynkinDiagram(['E', 6, 1])
        sage: edges = e.edges(); edges.sort(); edges
        [(0, 2, 1),
         (1, 3, 1),
         (2, 0, 1),
         (2, 4, 1),
         (3, 1, 1),
         (3, 4, 1),
         (4, 2, 1),
         (4, 3, 1),
         (4, 5, 1),
         (5, 4, 1),
         (5, 6, 1),
         (6, 5, 1)]

    """
    from dynkin_diagram import precheck , DynkinDiagram_class
    precheck(t, letter="E", length=3, affine=1)
    n = t[1]
    g = DynkinDiagram_class(t)
    g.add_edge(1,3)
    g.add_edge(2,4)
    for i in range(3,n):
        g.add_edge(i, i+1)
    if n == 6:
        g.add_edge(0, 2)
    elif n == 7:
        g.add_edge(0, 1)
    elif n == 8:
        g.add_edge(0, 8)
    else:
        raise ValueError, "Invalid Cartan Type for Type E affine"
    return g


