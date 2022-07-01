import pandas as pd
import json

tabla = pd.read_excel("Sinaloa.xls")
cp = tabla.groupby("'d_codigo")("'d_asenta")
mun = tabla.groupby("'D_mnpio")
est = tabla.groupby("'d_estado")

print(pd.DataFrame(tabla))
print(pd.DataFrame(cp))