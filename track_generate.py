import numpy as np
import yaml
# param
v_max = 10
a_max = 10
n = 5
# param
r_max = v_max*v_max / a_max
r_min = r_max / n
p = np.zeros((8,3))
waypoint = []
pointpath = []

for i in range(8):
    p[i][0] = round(r_max*np.sin(np.pi / 4 * i),2)
    p[i][1] = round(r_min*np.cos(np.pi / 4 * i) - r_min,2)
    p[i][2] = 5

save_path = "track/track5.yaml"
gates=str(p[1:8].tolist())
start=str(p[0].tolist())
end=str(p[0].tolist())
data = {
        "gates":gates,
        "initial":{
            "position":start, 
            "attitude":"[1, 0, 0, 0]", 
            "velocity":"[0, 0, 0]", 
            "omega":"[0, 0, 0]"
            },
        "end":{
        "position":end,
        "velocity":"[0, 0, 0]"
        }
        }
# print(data)
with open(save_path, "w") as f:
    yaml.safe_dump(data, f, sort_keys=False)
