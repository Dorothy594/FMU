import numpy as np
import fmpy
import matplotlib.pyplot as plt

filename = 'sldemo_bounce.fmu'

# 获取变量名称（先用 fmpy.dump(filename) 检查）
input_variable = 'In1'  # ⚠️ 确保这个名字正确
output_variables = ['Out1', 'Out2']   # ⚠️ 确保这些名字正确

# 创建输入数据：时间 (s) 和 对应的输入值
time_points = np.linspace(0, 0.1, 25)  # 100 个时间点，从 0 到 10s
gravity_values = -9.81 * np.ones_like(time_points)  # -9.81 恒定重力加速度

# 组合成 structured array（必须有 time 字段！）
input_data = np.array(list(zip(time_points, gravity_values)),
                      dtype=[('time', np.float64), (input_variable, np.float64)])

# 运行仿真
result = fmpy.simulate_fmu(filename,
                           start_time=0, stop_time=25,  # 仿真从 0 到 10s
                           input=input_data,
                           output=output_variables)

# 输出仿真结果
print(result)

# 提取时间和输出数据
time = result['time']
out1 = result['Out1']
out2 = result['Out2']

# 绘制图形
plt.figure(figsize=(10, 6))

# 绘制 Out1 和 Out2 随时间变化的图
plt.plot(time, out1, label='Out1', color='blue')
plt.plot(time, out2, label='Out2', color='orange')

# 设置图表标签和标题
plt.xlabel('Time (s)')
plt.ylabel('Output Values')
plt.title('Simulation Results of sldemo_bounce')
plt.legend()

# 显示图形
plt.grid(True)
plt.show()
