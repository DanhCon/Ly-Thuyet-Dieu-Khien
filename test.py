import numpy as np
from scipy.linalg import solve_continuous_are
import matplotlib.pyplot as plt

# 1. Khai báo tham số vật lý
M = 1.0    # Khối lượng xe (kg)
m = 0.1    # Khối lượng thanh (kg)
l = 0.5    # Nửa chiều dài thanh (m)
g = 9.81   # Gia tốc trọng trường (m/s2)

# 2. Ma trận Không gian Trạng thái (A, B)
A = np.array([
    [0, 1, 0, 0],
    [0, 0, -m*g/M, 0],
    [0, 0, 0, 1],
    [0, 0, (M+m)*g/(M*l), 0]
])

B = np.array([
    [0],
    [1/M],
    [0],
    [-1/(M*l)]
])

# 3. Chọn Ma trận Trọng số Q, R (Theo Bryson's Rule)
Q = np.diag([4.0, 1.0, 100.0, 1.0]) # Ưu tiên phạt góc nghiêng theta (100)
R = np.array([[0.01]])              # Cho phép dùng lực tương đối lớn

# 4. Giải phương trình Riccati để tìm P và Gain K
P = solve_continuous_are(A, B, Q, R)
K = np.linalg.inv(R) @ B.T @ P

print("Ma trận Phản hồi Tối ưu K =")
print(K)