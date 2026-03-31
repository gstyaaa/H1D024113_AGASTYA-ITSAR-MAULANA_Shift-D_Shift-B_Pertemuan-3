import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

bt = ctrl.Antecedent(np.arange(0, 101, 1), 'barang_terjual')
pm = ctrl.Antecedent(np.arange(0, 301, 1), 'permintaan')
hj = ctrl.Antecedent(np.arange(0, 100001, 100), 'harga_per_item')
pf = ctrl.Antecedent(np.arange(0, 4000001, 1000), 'profit')
stok = ctrl.Consequent(np.arange(0, 1001, 1), 'stok_makanan')

bt['rendah'] = fuzz.trapmf(bt.universe, [0, 0, 20, 50])
bt['sedang'] = fuzz.trimf(bt.universe, [30, 50, 70])
bt['tinggi'] = fuzz.trapmf(bt.universe, [50, 80, 100, 100])

pm['rendah'] = fuzz.trapmf(pm.universe, [0, 0, 50, 150])
pm['sedang'] = fuzz.trimf(pm.universe, [100, 150, 200])
pm['tinggi'] = fuzz.trapmf(pm.universe, [150, 250, 300, 300])

hj['murah'] = fuzz.trapmf(hj.universe, [0, 0, 20000, 50000])
hj['sedang'] = fuzz.trimf(hj.universe, [30000, 50000, 70000])
hj['mahal'] = fuzz.trapmf(hj.universe, [60000, 80000, 100000, 100000])

pf['rendah'] = fuzz.trapmf(pf.universe, [0, 0, 500000, 1500000])
pf['sedang'] = fuzz.trimf(pf.universe, [1500000, 2500000, 3500000])
pf['tinggi'] = fuzz.trapmf(pf.universe, [2500000, 3500000, 4000000, 4000000])

stok['sedang'] = fuzz.trapmf(stok.universe, [0, 0, 400, 700])
stok['banyak'] = fuzz.trapmf(stok.universe, [600, 900, 1000, 1000])

rule1 = ctrl.Rule(bt['tinggi'] & pm['tinggi'] & hj['murah'] & pf['tinggi'], stok['banyak'])
rule2 = ctrl.Rule(bt['tinggi'] & pm['tinggi'] & hj['murah'] & pf['sedang'], stok['sedang'])
rule3 = ctrl.Rule(bt['tinggi'] & pm['sedang'] & hj['murah'] & pf['sedang'], stok['sedang'])
rule4 = ctrl.Rule(bt['sedang'] & pm['tinggi'] & hj['murah'] & pf['sedang'], stok['sedang'])
rule5 = ctrl.Rule(bt['sedang'] & pm['tinggi'] & hj['murah'] & pf['tinggi'], stok['banyak'])
rule6 = ctrl.Rule(bt['rendah'] & pm['rendah'] & hj['sedang'] & pf['sedang'], stok['sedang'])

stok_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
stok_sim = ctrl.ControlSystemSimulation(stok_ctrl)

stok_sim.input['barang_terjual'] = 80
stok_sim.input['permintaan'] = 255
stok_sim.input['harga_per_item'] = 25000
stok_sim.input['profit'] = 3500000

stok_sim.compute()

print(f"Persediaan stok makanan: {stok_sim.output['stok_makanan']:.2f} unit")

bt.view()
pm.view()
hj.view()
pf.view()
stok.view(sim=stok_sim)
plt.show()