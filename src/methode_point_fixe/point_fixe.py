def point_fixe(f, x0, tol=1e-8, max_iter=50):
    """
    Résout x = f(x) par la méthode du point fixe.

    Paramètres :
    - f : fonction de point fixe
    - x0 : valeur initiale
    - tol : tolérance sur la différence successive
    - max_iter : nombre maximum d'itérations

    Retourne :
    - Tuple (approximation finale, nombre d'itérations)
    """
    x_vals = [x0]
    for i in range(max_iter):
        x = x_vals[-1]
        x_new = f(x)
        x_vals.append(x_new)
        if abs(x_new - x) < tol:
            return x_new, i + 1
        print(f"Étape {i+1} : x = {x_new:.6f}, f(x) = {f(x_new):.6f}")

    raise RuntimeError("La méthode n'a pas convergé après {} itérations.".format(max_iter))
