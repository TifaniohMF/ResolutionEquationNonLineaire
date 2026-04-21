def method_newton(f, df, x0, tol=1e-10, max_iter=100):
    """
    Résout f(x) = 0 par la méthode de Newton.

    Paramètres :
    - f : fonction à résoudre
    - df : dérivée de f
    - x0 : valeur initiale
    - tol : tolérance sur la différence successive
    - max_iter : nombre maximum d'itérations

    Retourne :
    - Liste des approximations successives
    """
    x_vals = [x0]
    for i in range(max_iter):
        x = x_vals[-1]
        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            raise ValueError("Dérivée nulle à x = {}. Méthode de Newton échoue.".format(x))

        x_new = x - fx / dfx
        x_vals.append(x_new)

        print(f"Étape {i+1} : x = {x_new:.6f}, f(x) = {f(x_new):.6f}")

        if abs(x_new - x) < tol:
            break

    else:
        raise RuntimeError("La méthode n'a pas convergé après {} itérations.".format(max_iter))

    return x_vals