"""Q061-Q070: scalar Kalman filter intuition."""
x=0.0; P=1.0; Q=0.02; R=0.25
measurements=[0.2,0.1,0.6,0.4,0.5]
for y in measurements:
    # predict
    P=P+Q
    # update
    K=P/(P+R)
    x=x+K*(y-x)
    P=(1-K)*P
    print(f'y={y:.2f}, K={K:.3f}, xhat={x:.3f}, P={P:.3f}')
