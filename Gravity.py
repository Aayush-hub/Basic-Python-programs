def falling(time, velo):
    """
    return float indicating
    number of meters an object has
    fallen after being dropped/thrown
    with initial velocity given by
    float parameter velo
    (given in meters/second)
    and after falling for float parameter
    time seconds
    """

    return (velo * time) + (0.5 * 9.8 * (time**2))
