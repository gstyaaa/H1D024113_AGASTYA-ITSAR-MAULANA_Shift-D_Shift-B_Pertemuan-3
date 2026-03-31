import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

inf = ctrl.Antecedent(np.arange(0, 101, 1), 'kejelasan_informasi')
syar = ctrl.Antecedent(np.arange(0, 101, 1), 'kejelasan_persyaratan')
pet = ctrl.Antecedent(np.arange(0, 101, 1), 'kemampuan_petugas')
sar = ctrl.Antecedent(np.arange(0, 101, 1), 'ketersediaan_sarpras')
puas = ctrl.Consequent(np.arange(0, 401, 1), 'kepuasan_pelayanan')

inf['tm'] = fuzz.trapmf(inf.universe, [0, 0, 60, 75])
inf['cm'] = fuzz.trimf(inf.universe, [60, 75, 90])
inf['m'] = fuzz.trapmf(inf.universe, [75, 90, 100, 100])

syar['tm'] = fuzz.trapmf(syar.universe, [0, 0, 60, 75])
syar['cm'] = fuzz.trimf(syar.universe, [60, 75, 90])
syar['m'] = fuzz.trapmf(syar.universe, [75, 90, 100, 100])

pet['tm'] = fuzz.trapmf(pet.universe, [0, 0, 60, 75])
pet['cm'] = fuzz.trimf(pet.universe, [60, 75, 90])
pet['m'] = fuzz.trapmf(pet.universe, [75, 90, 100, 100])

sar['tm'] = fuzz.trapmf(sar.universe, [0, 0, 60, 75])
sar['cm'] = fuzz.trimf(sar.universe, [60, 75, 90])
sar['m'] = fuzz.trapmf(sar.universe, [75, 90, 100, 100])

puas['tm'] = fuzz.trapmf(puas.universe, [0, 0, 50, 100])
puas['km'] = fuzz.trimf(puas.universe, [50, 100, 150])
puas['cm'] = fuzz.trimf(puas.universe, [100, 175, 250])
puas['m'] = fuzz.trimf(puas.universe, [175, 250, 325])
puas['sm'] = fuzz.trapmf(puas.universe, [250, 325, 400, 400])

rules = [
    ctrl.Rule(inf['tm'] & syar['tm'] & pet['tm'] & sar['tm'], puas['tm']),
    ctrl.Rule(inf['tm'] & syar['tm'] & pet['tm'] & sar['cm'], puas['tm']),
    ctrl.Rule(inf['tm'] & syar['tm'] & pet['tm'] & sar['m'], puas['tm']),
    ctrl.Rule(inf['tm'] & syar['tm'] & pet['cm'] & sar['tm'], puas['tm']),
    ctrl.Rule(inf['tm'] & syar['tm'] & pet['cm'] & sar['cm'], puas['tm']),
    ctrl.Rule(inf['tm'] & syar['tm'] & pet['cm'] & sar['m'], puas['cm']),
    ctrl.Rule(inf['tm'] & syar['tm'] & pet['m'] & sar['tm'], puas['tm']),
    ctrl.Rule(inf['tm'] & syar['tm'] & pet['m'] & sar['cm'], puas['cm']),
    ctrl.Rule(inf['tm'] & syar['tm'] & pet['m'] & sar['m'], puas['cm']),
    ctrl.Rule(inf['cm'] & syar['cm'] & pet['cm'] & sar['m'], puas['m']),
    ctrl.Rule(inf['cm'] & syar['cm'] & pet['m'] & sar['m'], puas['m']),
    ctrl.Rule(inf['cm'] & syar['m'] & pet['m'] & sar['m'], puas['sm']),
    ctrl.Rule(inf['m'] & syar['m'] & pet['m'] & sar['m'], puas['sm']),
    ctrl.Rule(pet['tm'], puas['tm']),
    ctrl.Rule(inf['m'] & syar['m'], puas['m'])
]

puas_ctrl = ctrl.ControlSystem(rules)
puas_sim = ctrl.ControlSystemSimulation(puas_ctrl)

try:
    puas_sim.input['kejelasan_informasi'] = 80
    puas_sim.input['kejelasan_persyaratan'] = 60
    puas_sim.input['kemampuan_petugas'] = 50
    puas_sim.input['ketersediaan_sarpras'] = 90

    puas_sim.compute()
    print(f"Tingkat kepuasan pelayanan: {puas_sim.output['kepuasan_pelayanan']:.2f}")
    
    inf.view()
    syar.view()
    pet.view()
    sar.view()
    puas.view(sim=puas_sim)
    plt.show()

except KeyError:
    print("cek kembali aturan fuzzy nya")