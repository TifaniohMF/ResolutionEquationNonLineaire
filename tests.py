import numpy as np
from src.methode_dichotomie.dichotomie import dichotomie
from src.methode_newton.newton import method_newton
from src.methode_point_fixe.point_fixe import point_fixe

def test_dichotomie():
    # Test avec f(x) = x^2 - 2, racine sqrt(2) ≈ 1.414
    f = lambda x: x**2 - 2
    root = dichotomie(f, 1, 2)
    assert abs(root - np.sqrt(2)) < 1e-6
    print("Test dichotomie passé.")

def test_newton():
    # Test avec f(x) = x^2 - 2, df(x) = 2x
    f = lambda x: x**2 - 2
    df = lambda x: 2*x
    x_vals = method_newton(f, df, 1.5)
    root = x_vals[-1]
    assert abs(root - np.sqrt(2)) < 1e-9
    print("Test Newton passé.")

def test_point_fixe():
    # Test avec x = cos(x), point fixe ≈ 0.739
    f = lambda x: np.cos(x)
    root, iters = point_fixe(f, 0.5)
    assert abs(root - 0.739085) < 1e-5
    print("Test point fixe passé.")

if __name__ == "__main__":
    test_dichotomie()
    test_newton()
    test_point_fixe()
    print("Tous les tests sont passés.")