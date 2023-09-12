def deviation_measure(aprox):
    dm = 0
    for i in range(aprox.n):
        dm += (aprox.phi_array[i] - aprox.y_array[i])**2
    aprox.dm = dm
    return dm

def calc_phi(aprox):
    for x in aprox.x_array:
        aprox.phi_array.append(aprox.func(x))

def calc_sko(aprox):
    sko = (aprox.dm/aprox.n) ** 0.5
    aprox.sko = sko
    return sko

def calc_r(aprox):
    sr_x = aprox.sum_xi/aprox.n
    sr_y = aprox.sum_yi/aprox.n
    chis = 0
    zn_1 = 0
    zn_2 = 0
    for i in range(aprox.n):
        chis += (aprox.x_array[i] - sr_x)*(aprox.y_array[i] - sr_y)
        zn_1 += (aprox.x_array[i] - sr_x)**2
        zn_2 += (aprox.y_array[i] - sr_y)**2

    answer = chis/((zn_1 * zn_2) ** 0.5)
    return answer
