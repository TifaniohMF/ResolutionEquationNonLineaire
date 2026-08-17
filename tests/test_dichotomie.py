"""Tests pour la méthode de dichotomie."""

import math

import pytest

from src.exceptions import IntervalleInvalideError, NonConvergenceError
from src.methode_dichotomie.dichotomie import dichotomie


def test_racine_carree_de_2():
    """f(x) = x^2 - 2 a pour racine positive sqrt(2)."""
    resultat = dichotomie(lambda x: x**2 - 2, 1, 2, tol=1e-8)
    assert resultat.racine == pytest.approx(math.sqrt(2), abs=1e-6)


def test_racine_negative():
    """La méthode doit aussi trouver une racine négative."""
    resultat = dichotomie(lambda x: x**2 - 2, -2, -1, tol=1e-8)
    assert resultat.racine == pytest.approx(-math.sqrt(2), abs=1e-6)


def test_fonction_polynomiale():
    """f(x) = x^3 - x - 2 a une racine réelle proche de 1.5214."""
    resultat = dichotomie(lambda x: x**3 - x - 2, 1, 2)
    assert resultat.racine == pytest.approx(1.5213797, abs=1e-5)


def test_intervalle_sans_racine_leve_une_erreur():
    """f(a) et f(b) de même signe doit lever IntervalleInvalideError."""
    with pytest.raises(IntervalleInvalideError):
        dichotomie(lambda x: x**2 + 1, -1, 1)


def test_racine_exacte_a_une_borne():
    """Si f(a) == 0, la méthode doit gérer ce cas sans planter."""
    resultat = dichotomie(lambda x: x - 1, 1, 2)
    assert resultat.racine == pytest.approx(1.0, abs=1e-6)


def test_non_convergence_avec_peu_diterations():
    """Un budget d'itérations trop faible doit lever NonConvergenceError."""
    with pytest.raises(NonConvergenceError):
        dichotomie(lambda x: x**2 - 2, 1, 2, tol=1e-15, max_iter=1)


def test_historique_a_la_bonne_longueur():
    """L'historique doit contenir un point par itération effectuée."""
    resultat = dichotomie(lambda x: x**2 - 2, 1, 2)
    assert len(resultat.historique) == resultat.iterations


def test_tolerance_stricte_ameliore_la_precision():
    """Une tolérance plus fine doit donner un résultat plus précis."""
    resultat_large = dichotomie(lambda x: x**2 - 2, 1, 2, tol=1e-3)
    resultat_fin = dichotomie(lambda x: x**2 - 2, 1, 2, tol=1e-10)
    erreur_large = abs(resultat_large.racine - math.sqrt(2))
    erreur_fin = abs(resultat_fin.racine - math.sqrt(2))
    assert erreur_fin < erreur_large
    