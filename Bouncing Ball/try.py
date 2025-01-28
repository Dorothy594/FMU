from fmpy import *

# 加载 FMU 文件
fmu = 'sldemo_bounce.fmu'
# fmu = 'C:/Users/DELL/AppData/Local/Temp/tmpvbo3lyt6/binaries/x86_64-windows/LowPassFilterSFcn.dll'

# 获取 FMU 信息
dump(fmu)

# import pdb; pdb.set_trace()

# 模拟 FMU
result = simulate_fmu(fmu, fmi_type='CoSimulation')
print(result)

# import pdb; pdb.set_trace()

# 绘制结果
# from fmpy.util import plot_result
#
# plot_result(result)