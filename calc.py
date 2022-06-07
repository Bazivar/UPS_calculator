

def UPS_calc(power, battery_cap, battery_num, ext_bat_num, ext_bat_cap, ext_num, efficiency):

    if ((battery_cap * 12 * battery_num + ext_bat_cap * 12 * ext_bat_num * ext_num) * efficiency/100 / power) > 20:
        correction_qt = 1
    else:
        correction_qt = 0.529 * (((battery_cap * 12 * battery_num + ext_bat_cap * 12 * ext_bat_num * ext_num) * efficiency/100 / power) ** 0.207)

    result = (battery_cap * 12 * battery_num + ext_bat_cap * 12 * ext_bat_num * ext_num) * efficiency/100 / power * correction_qt
    return round(result*60)

