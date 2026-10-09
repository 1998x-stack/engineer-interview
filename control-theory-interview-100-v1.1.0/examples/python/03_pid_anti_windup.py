"""Q021-Q030: minimal PI saturation/anti-windup skeleton."""
class PI:
    def __init__(self,kp,ki,dt,umin=-1,umax=1):
        self.kp,self.ki,self.dt=kp,ki,dt
        self.umin,self.umax=umin,umax
        self.i=0.0
    def step(self,e):
        raw=self.kp*e+self.i
        sat=max(self.umin,min(self.umax,raw))
        # conditional integration: do not integrate deeper into saturation
        if raw==sat or (raw>self.umax and e<0) or (raw<self.umin and e>0):
            self.i += self.ki*self.dt*e
        return sat,raw,self.i
