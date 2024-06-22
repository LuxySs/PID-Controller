class PID(object):
    def __init__(self, **kwargs):
        self.pos = kwargs["pos"]
        self.dest = kwargs["dest"]
        
        self.K = kwargs["K"]
        self.tau_i = kwargs["tau_i"]
        self.tau_d = kwargs["tau_d"]
        
        self.lastError = 0
        self.reset = 0

        print(self.pos, self.dest, self.K, self.tau_i, self.tau_d)
    
    def calculate(self):
        error = self.dest - self.pos

        self.reset += self.K / self.tau_i * error
        errorSlope = self.K / self.tau_d * (error - self.lastError)

        output = self.K * error + self.reset + errorSlope
        
        self.lastError = error
        
        return output

def test_pid():
    # Start
    initial_pos = 8
    
    # Destination
    dest = 50.0
    
    # PID parameters
    K = 1.0
    tau_i = 1.0
    tau_d = 1.0
    
    # Number of iterations to simulate
    num_iterations = 50
    
    # Create a PID controller
    pid = PID(pos=initial_pos, dest = dest, K=K, tau_i=tau_i, tau_d=tau_d)
    
    # Time step for each iteration
    dt = 0.1
    
    # List to store positions for plotting
    positions = [initial_pos]
    
    # Run the PID control loop
    for _ in range(num_iterations):
        # Calculate control output
        control_output = pid.calculate()
        
        # Update position based on control output
        pid.pos += control_output * dt
        
        # Append current position to the list
        positions.append(pid.pos)
    
    return positions

if __name__ == "__main__":
    # Test the PID controller and print the positions
    positions = test_pid()

    for i, pos in enumerate(positions):
        print(f"Step {i}: Position = {pos}")
