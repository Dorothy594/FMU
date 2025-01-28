import numpy as np
import fmpy
import matplotlib.pyplot as plt


def simulate_and_plot_fmu(filename, input_variable, output_variables, start_time, stop_time, timestamps, input_values):
    """
    Simulates an FMU and plots the specified outputs.

    Parameters:
    - filename (str): Path to the FMU file.
    - input_variable (str): Name of the input variable.
    - output_variables (list): List of output variable names.
    - start_time (float): Start time of the simulation.
    - stop_time (float): Stop time of the simulation.
    - timestamps (list or numpy array): List of time points for the simulation.
    - input_values (list or numpy array): List of input values corresponding to each time point.

    Returns:
    - None
    """
    # Ensure timestamps and input_values have the same length
    if len(timestamps) != len(input_values):
        raise ValueError("timestamps and input_values must have the same length")

    # Combine time and input values into a structured array
    input_data = np.array(list(zip(timestamps, input_values)),
                          dtype=[('time', np.float64), (input_variable, np.float64)])

    # Run the simulation
    result = fmpy.simulate_fmu(filename,
                               start_time=start_time, stop_time=stop_time,
                               input=input_data,
                               output=output_variables)

    # Extract time and output data
    time = result['time']
    outputs = {var: result[var] for var in output_variables}

    # Plot the results
    plt.figure(figsize=(10, 6))

    for var, values in outputs.items():
        plt.plot(time, values, label=var)

    # Set plot labels and title
    plt.xlabel('Time (s)')
    plt.ylabel('Output Values')
    plt.title(f'Simulation Results of {filename}')
    plt.legend()
    plt.grid(True)
    plt.show()


# Example usage
timestamps = np.linspace(0, 0.1, 25)
input_values = -9.81 * np.ones_like(timestamps)
simulate_and_plot_fmu(
    filename='ego.fmu',
    input_variable='In1',
    output_variables=['Out1', 'Out2'],
    start_time=0,
    stop_time=25,
    timestamps=timestamps,
    input_values=input_values
)
