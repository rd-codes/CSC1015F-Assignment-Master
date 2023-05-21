def weighted_val(value, weight):
    return value*weight;
def weighted_ave(values, weights):
    w_ave = 0;
    for i in range(len(values)):
     w_ave += weighted_val(values[i],weights[i])
    return w_ave;

values = [60, 34 , 45, 9, 24]
weights = [0.1,0.3,0.2,0.3]

print()
