import matplotlib.pyplot as plt

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
    dest = 250
    
    # PID parameters
    K = 1
    tau_i = 1
    tau_d = 1
    
    # Number of iterations to simulate
    num_iterations = 200
    
    # Create a PID controller
    pid = PID(pos=initial_pos, dest = dest, K=K, tau_i=tau_i, tau_d=tau_d)
    
    # Time interval 
    dt = 0.1
    
    positions = [initial_pos]
    
    for _ in range(num_iterations):
        control_output = pid.calculate()
        pid.pos += control_output * dt
        positions.append(pid.pos)
    
    return positions

if __name__ == "__main__":
    positions = test_pid()
    print(positions)

    plt.figure(figsize=(10, 5))
    plt.plot(positions)
    plt.show()
