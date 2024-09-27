import pytest
from classes import partition, equation, solver

def test_partition():
    """Test the Partition class"""
    p = partition.Partition(lambda x, y: x*y, 1, 1, 1)
    assert str(p) == "+x"
    assert p.solve(1) == 1
def test_derivative_partition():
    p = partition.Partition(lambda x, y: x*y, 4, -1, 3)
    assert str(p.derivative()) == "-12x^3"
    assert p.derivative().solve(1) == -12**3


def test_equation():
    """Test the Equation class"""
    e = equation.Equation([partition.Partition(lambda x, y: x*y, 1, 1, 1), partition.Partition(partition.nilLamb, 1, -1, 1), partition.Partition(lambda x, y: x*y, 4, -1, 3)])
    assert str(e) == "+x-x-3x^4"
    assert str(e.derivative()) == "+1-1-12x^3"
    assert e.solve(1) == 81

def test_solver():
    """Test the Solver class"""
    s = solver.Solver(equation.Equation([partition.Partition(lambda x, y: x*y, 1, 1, 1), partition.Partition(partition.nilLamb, 1, -1, 1), partition.Partition(lambda x, y: x*y, 4, -1, 3)]), (-1, 3))
    assert s.segment_interval() == 1
    assert s.find_roots() == [(79, 6563), (1730, -46654), (1296, 11664)]

def test_integrational():
    """Testing output solutions for the integrals"""
    f = lambda x, y:x*y
    p1 = partition.Partition(f,3,1,2)
    p2 = partition.Partition(f, 2, -1, 7)
    p3 = partition.Partition(f, 1, 1, 3)
    p4 = partition.Partition(partition.nilLamb, 1, -1, 10)
    e = equation.Equation([p1, p2, p3, p4])
    s = solver.Solver(e, (0, 4))
    assert "[0.375, 0.4375]" in str(s.solve_root_approx())
    s.clean_cycle()
    assert "0.144" in str(s.solve_chord())