"""
This file contains functions for calculating properties of rectangular
sections.

    - section(b,d) : section modulus
    - inertia(b,d) : moment of interia

"""


def rectsect(b, d):
    """section modulus of rectangle

    Args:
        b (float): width
        d (float): depth

    Returns:
        float: section modulus
    """
    return b * d**2 / 6.0


def rectinertia(b, d):
    """moment of inertia of rectangle

    Args:
        b (float): width
        d (float): depth

    Returns:
        float: inertia
    """
    return b * d**3 / 12.0


def midspan_delta(ln, w, e, i):
    """mid-span deflection of simply supported beam with UDL

    Args:
        l (float): span
        w (float): uniform load
        e (float): modulus of elasticity
        i (float): moment of inertia

    Returns:
        float: mid-span deflection
    """
    return 5 * w * ln**4 / (384 * e * i)


def bending_stress_udl(ln, w, b, d):
    """Maximum bending stress in a simply supported beam with UDL.

    Args:
        ln (float): span
        w (float): uniform load
        b (float): beam width
        d (float): beam depth

    Returns:
        float: maximum bending stress
    """
    moment = w * ln**2 / 8.0
    section_modulus = rectsect(b, d)
    return moment / section_modulus


def nds_beam_check(**kwargs):
    """Check stress and deflection for a simply supported wood beam using NDS.

    Args:
    ln_1 = 8.,  # beam span
    w_1 = 45*.5  # uniform linear load
    b_1 = 5.5/12  # beam width
    d_1 = 1.5/12  # beam depth
    E_1 = 1.5*(10**6)/144  # modulus of elasticity
    F_b = 1000 allowable bending stress
    C_D = 1.0   # load duration factor
    C_M = 0.85 # wet service factor
    C_F = 1.0  # size factor
    C_t = 1.0  # temperature factor
    C_i = 0.8  # incising factor
    C_r = 1.0  # repetitive member factor
    C_c = 1.0  # curvature factor
    C_L = 1.0  # beam stability factor
    C_b = 1.0  # bearing area factor
    deflect_limit = 360.0 # max allowable deflection ln_1/deflect_limit
    """
    from types import SimpleNamespace

    ns = SimpleNamespace(**kwargs)
    moment = (ns.w_1 * ns.ln_1**2) / 8.0
    section_modulus = ns.b_1 * ns.d_1**2 / 6.0
    fb = moment / section_modulus
    inertia = ns.b_1 * ns.d_1**3 / 12.0
    E_prime = ns.E_1 * ns.C_M * ns.C_t
    Fb = ns.F_b
    Fb_prime = (
        Fb
        * ns.C_D
        * ns.C_M
        * ns.C_F
        * ns.C_t
        * ns.C_i
        * ns.C_r
        * ns.C_c
        * ns.C_L
        * ns.C_b
    )

    deflection = 5 * ns.w_1 * ns.ln_1**4 / (384 * E_prime * inertia)
    delta_limit = ns.ln_1 / ns.deflect_limit
    if deflection <= delta_limit:
        deflect_ratio = f"{delta_limit:.2f}"
    else:
        deflect_ratio = "Not OK"
    if fb <= Fb_prime:
        stress_ratio = f"{fb / Fb_prime:.2f}"
    else:
        stress_ratio = "Not OK"

    funcretvalS = f"""
        Beam Check Results:
        ===============================    
        total UDL: {ns.w_1:.2f}
        fb: {fb:.2f}
        Fb_prime: {Fb_prime:.2f}
        E_prime: {E_prime:.2f}
        stress_ratio: {stress_ratio}
        deflection: {deflection:.2f}
        deflection_ratio:  {deflect_ratio}
        """

    return funcretvalS.replace("        ", "")


def nds_post_check(**kwargs):
    """Check stress at cantilever post

    Args:
    h_1 = 8.  # post height
    P_1 = 100  # concentrated load
    b_1 = 5.5/12  # post width
    d_1 = 1.5/12  # post depth
    E_1 = 1.5*(10**6)/144  # modulus of elasticity
    F_b = 1000 # allowable bending stress
    C_D = 1.0  # load duration factor
    C_M = 0.85 # wet service factor
    C_F = 1.0  # size factor
    C_t = 1.0  # temperature factor
    C_i = 0.8  # incising factor
    C_r = 1.0  # repetitive member factor
    C_c = 1.0  # curvature factor
    C_L = 1.0  # beam stability factor
    C_b = 1.0  # bearing area factor
    deflect_limit = 360.0 # max allowable deflection ln_1/deflect_limit
    """
    from types import SimpleNamespace

    ns = SimpleNamespace(**kwargs)
    moment = ns.P_1 * ns.h_1
    section_modulus = ns.b_1 * ns.d_1**2 / 6.0
    fb = moment / section_modulus
    inertia = ns.b_1 * ns.d_1**3 / 12.0
    E_prime = ns.E_1 * ns.C_M * ns.C_t
    Fb = ns.F_b
    Fb_prime = (
        Fb
        * ns.C_D
        * ns.C_M
        * ns.C_F
        * ns.C_t
        * ns.C_i
        * ns.C_r
        * ns.C_c
        * ns.C_L
        * ns.C_b
    )

    deflection = 5 * ns.P_1 * ns.h_1**3 / (3 * E_prime * inertia)
    delta_limit = ns.h_1 / ns.deflect_limit
    if deflection <= delta_limit:
        deflect_ratio = f"{delta_limit:.2f}"
    else:
        deflect_ratio = "Not OK"
    if fb <= Fb_prime:
        stress_ratio = f"{fb / Fb_prime:.2f}"
    else:
        stress_ratio = "Not OK"

    funcretvalS = f"""
        Post Check Results:
        ===============================    
        P: {ns.P_1:.2f}
        fb: {fb:.2f}
        Fb_prime: {Fb_prime:.2f}
        E_prime: {E_prime:.2f}
        stress_ratio: {stress_ratio}
        deflection: {deflection:.2f}
        deflection_ratio:  {deflect_ratio}
        """

    return funcretvalS.replace("        ", "")
