# 🎛️ Lý Thuyết Điều Khiển Tự Động - PID & Cascade Control
## PID Cơ Bản | Anti-Windup | Deadband | Cascade | Polar Control

---

## 1. PID CONTROLLER - TỪ CƠ BẢN

### PID là gì?
```
PID = Proportional + Integral + Derivative Controller
(Bộ điều khiển Tỉ lệ + Tích phân + Vi phân)

Setpoint (Mục tiêu) → [PID] → Actuator → [System] → Output
                         ↑                              |
                         └─────── Error ───────────────┘
                                 (Sai số feedback)
```

### Ba thành phần:
```
P (Proportional):
  u_P = Kp × e(t)
  → Tỷ lệ với sai số hiện tại
  → Kp lớn → Phản ứng nhanh, nhưng dễ dao động
  
I (Integral):
  u_I = Ki × ∫e(t)dt
  → Tích lũy sai số theo thời gian
  → Triệt tiêu sai số dư (steady-state error)
  → Ki lớn → Dễ vọt lố (overshoot)
  
D (Derivative):
  u_D = Kd × de(t)/dt
  → Tỷ lệ với tốc độ thay đổi sai số
  → "Nhìn trước" - giảm dao động
  → Nhạy với nhiễu (noise)
  
Tổng output:
  u(t) = Kp×e + Ki×∫e dt + Kd×(de/dt)
```

---

## 2. DISCRETE PID - CODE THỰC TẾ

### Công thức rời rạc (Euler forward):
```
e[k] = setpoint - measurement
integral[k] = integral[k-1] + e[k] × Δt
derivative[k] = (e[k] - e[k-1]) / Δt

u[k] = Kp×e[k] + Ki×integral[k] + Kd×derivative[k]
```

### Full PID code C:
```c
// =============================================
// PID Controller Struct - Tái sử dụng nhiều bánh
// =============================================
typedef struct {
    // Gains
    float Kp;
    float Ki;
    float Kd;
    
    // State
    float integral;
    float prev_error;
    float dt;  // Sampling time (seconds)
    
    // Limits
    float output_min;
    float output_max;
    float integral_min;
    float integral_max;
    
    // Anti-windup
    float deadband;
} PID_Controller_t;

// Khởi tạo PID
void PID_Init(PID_Controller_t *pid,
              float Kp, float Ki, float Kd,
              float dt,
              float out_min, float out_max) {
    pid->Kp = Kp;
    pid->Ki = Ki;
    pid->Kd = Kd;
    pid->dt = dt;
    pid->integral = 0.0f;
    pid->prev_error = 0.0f;
    pid->output_min = out_min;
    pid->output_max = out_max;
    
    // Giới hạn integral = 50% output max (tránh windup)
    pid->integral_min = out_min / (Ki > 0 ? Ki : 1.0f);
    pid->integral_max = out_max / (Ki > 0 ? Ki : 1.0f);
    pid->deadband = 0.0f;
}

// Tính toán PID - Gọi mỗi chu kỳ Δt
float PID_Calculate(PID_Controller_t *pid, float setpoint, float measurement) {
    // Tính sai số
    float error = setpoint - measurement;
    
    // Deadband - Bỏ qua sai số nhỏ (triệt tiêu hunting)
    if (fabsf(error) < pid->deadband) {
        error = 0.0f;
        pid->integral = 0.0f;  // Reset integral trong deadband
    }
    
    // P term
    float p_term = pid->Kp * error;
    
    // I term với Anti-Windup (Clamping)
    pid->integral += error * pid->dt;
    
    // Clamp integral
    if (pid->integral > pid->integral_max) pid->integral = pid->integral_max;
    if (pid->integral < pid->integral_min) pid->integral = pid->integral_min;
    
    float i_term = pid->Ki * pid->integral;
    
    // D term (Derivative on measurement, không phải error - giảm kick)
    float derivative = (error - pid->prev_error) / pid->dt;
    float d_term = pid->Kd * derivative;
    pid->prev_error = error;
    
    // Tổng output
    float output = p_term + i_term + d_term;
    
    // Saturation - Clamp output
    if (output > pid->output_max) {
        output = pid->output_max;
        // Anti-windup: Đừng tích phân khi đã bão hòa
        pid->integral -= error * pid->dt;  // Undo integration step
    }
    if (output < pid->output_min) {
        output = pid->output_min;
        pid->integral -= error * pid->dt;
    }
    
    return output;
}

// Reset PID (khi thay đổi setpoint đột ngột)
void PID_Reset(PID_Controller_t *pid) {
    pid->integral = 0.0f;
    pid->prev_error = 0.0f;
}
```

---

## 3. CASCADE CONTROL - ĐIỀU KHIỂN PHÂN CẤP

### Kiến trúc vòng lặp cho robot:
```
[Outer Loop - Position/Trajectory - 100Hz]
   Setpoint: (x_goal, y_goal)
   Feedback: (x, y, θ) từ Odometry
   Output: v_target, ω_target (vận tốc mong muốn)
                    ↓
[Inner Loop - Velocity - 200Hz trên STM32]
   Setpoint: v_target, ω_target
   Feedback: vL_actual, vR_actual từ Encoder
   Output: Current/Torque setpoint → CAN → Motor Driver
                    ↓
[Innermost Loop - Current/FOC - 1kHz trong Motor Driver]
   Chạy trong DJI/ODrive/ZLAC hardware
   Không cần code thêm!
```

### Code Cascade Control:
```c
// Outer PID: Position → Velocity
PID_Controller_t position_x_pid;
PID_Controller_t heading_pid;

// Inner PID: Velocity → Current
PID_Controller_t left_speed_pid;
PID_Controller_t right_speed_pid;

void Robot_CascadeControl(OdomPose_t *pose, 
                          float x_goal, float y_goal,
                          float theta_goal) {
    // === OUTER LOOP (100Hz) ===
    // Tính khoảng cách và góc đến mục tiêu
    float dx = x_goal - pose->x;
    float dy = y_goal - pose->y;
    float rho = sqrtf(dx*dx + dy*dy);
    float alpha = wrap_angle(atan2f(dy, dx) - pose->theta);
    
    // Outer PID → Velocity setpoints
    float v_cmd = 0.0f, omega_cmd = 0.0f;
    
    if (rho > RHO_THRESHOLD) {
        v_cmd     = PID_Calculate(&position_x_pid, rho, 0);
        omega_cmd = PID_Calculate(&heading_pid, alpha, 0);
    }
    
    // Forward kinematics: v, ω → vL_ref, vR_ref
    float vL_ref = v_cmd - omega_cmd * WHEELBASE / 2.0f;
    float vR_ref = v_cmd + omega_cmd * WHEELBASE / 2.0f;
    
    // === INNER LOOP (200Hz) ===
    // Inner PID → Current setpoints cho motor
    float current_L = PID_Calculate(&left_speed_pid, vL_ref, vL_actual);
    float current_R = PID_Calculate(&right_speed_pid, vR_ref, vR_actual);
    
    // Gửi qua CAN
    CAN_SendMotorCurrent(MOTOR_LEFT, current_L);
    CAN_SendMotorCurrent(MOTOR_RIGHT, current_R);
}
```

---

## 4. ANTI-WINDUP NÂNG CAO

### Back-Calculation (Tốt hơn Clamping):
```c
// Anti-windup bằng Back-Calculation
float PID_AntiWindup_BackCalc(PID_Controller_t *pid, float setpoint, float measurement) {
    float error = setpoint - measurement;
    
    // P term
    float p_term = pid->Kp * error;
    
    // D term
    float d_term = pid->Kd * (error - pid->prev_error) / pid->dt;
    pid->prev_error = error;
    
    // I term với Back-Calculation
    pid->integral += (error + pid->back_calc_error) * pid->dt;
    float i_term = pid->Ki * pid->integral;
    
    // Tổng trước khi saturate
    float output_unsaturated = p_term + i_term + d_term;
    
    // Saturate
    float output = fminf(fmaxf(output_unsaturated, pid->output_min), pid->output_max);
    
    // Back-calculation: Tính sai số do bão hòa
    // Gain Kb = 1 / (tracking time constant)
    float Kb = 1.0f / (pid->tracking_time_const + 0.001f);
    pid->back_calc_error = Kb * (output - output_unsaturated);
    
    return output;
}
```

---

## 5. SLEW RATE LIMITER + DEADBAND

```c
// Slew Rate Limiter - Làm mượt thay đổi vận tốc
typedef struct {
    float max_rate;       // m/s² hoặc rad/s²
    float current_value;
} SlewRateLimiter_t;

float SlewRate_Apply(SlewRateLimiter_t *slew, float target, float dt) {
    float max_change = slew->max_rate * dt;
    float change = target - slew->current_value;
    
    change = fminf(fmaxf(change, -max_change), max_change);
    slew->current_value += change;
    
    return slew->current_value;
}

// Deadband - Không phản ứng khi sai số quá nhỏ
float ApplyDeadband(float value, float deadband) {
    if (fabsf(value) < deadband) return 0.0f;
    return value;
}
```

---

## 6. TUNING PID - PHƯƠNG PHÁP THỰC TẾ

### Phương pháp Ziegler-Nichols (nhanh):
```
1. Đặt Ki = 0, Kd = 0
2. Tăng Kp từ từ cho đến khi hệ thống dao động bền vững (oscillate)
   → Kp tại đó gọi là Ku (Ultimate Gain)
   → Chu kỳ dao động gọi là Tu (Ultimate Period)
   
3. Tính toán:
   PID: Kp = 0.6×Ku, Ki = 1.2×Ku/Tu, Kd = 0.075×Ku×Tu
```

### Phương pháp thực tế cho robot:
```
Bước 1: Tune Inner Loop (Speed PID) trước
  - Chạy motor với speed setpoint cố định
  - Tăng Kp đến khi theo kịp setpoint, không dao động nhiều
  - Thêm Ki để triệt steady-state error
  
Bước 2: Tune Outer Loop (Position PID)
  - Với Inner Loop đã stable
  - Kp nhỏ thôi (nếu Kp lớn → kết hợp với Inner → bất ổn)
  - Thêm Kd để giảm overshoot

Bước 3: Thêm Anti-windup và Deadband
  - Deadband thường là 1-5% của max error
```

---

## 7. LINK TÀI LIỆU

### Phải đọc:
1. **PID Without a PhD - Tim Wescott (ĐÃ TẢI!):**
   Xem: `PID_Without_PhD_Wescott.pdf` (trong thư mục này)

2. **Caltech CDS - PID Control:**
   https://www.cds.caltech.edu/~murray/courses/cds101/fa02/caltech-cds101-ch08.pdf

3. **MIT 2.004 - PID Lecture Notes:**
   https://ocw.mit.edu/courses/2-004-dynamics-and-control-ii-spring-2008/

4. **PID Control System Design - University of Virginia:**
   https://www.cs.virginia.edu/~cs216/resources/other_course_materials/pid.pdf

5. **Ziegler-Nichols tuning method explained:**
   https://www.ni.com/en-us/innovations/white-papers/06/pid-theory-explained.html

### Video:
6. **YouTube - "PID Controller" by Brian Douglas (EXCELLENT):**
   https://www.youtube.com/watch?v=UR0hOmjaHp0

7. **YouTube - "Anti Windup" by Brian Douglas:**
   Search: "Brian Douglas anti windup PID"

8. **MATLAB PID tuning video series:**
   Search: "MATLAB PID control series"

### Cascade Control:
9. **Cascade Control Overview:**
   https://www.sciencedirect.com/topics/engineering/cascade-control

---

*Tài liệu tổng hợp - Phần 6/7 trong lộ trình học Robot STM32*
