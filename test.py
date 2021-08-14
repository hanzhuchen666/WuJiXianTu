import numpy as np

for i in range(4):
    file = np.load(
        'E:\\33_automata\\2_android\\4_python_code\\WuJiXianTu\\GameData\\page{}.npy'.format(i)
    )
    print(file)