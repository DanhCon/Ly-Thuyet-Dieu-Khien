# 🌀 FOC - Field Oriented Control (Điều Khiển Định Hướng Từ Thông)
## Lý Thuyết FOC | SimpleFOC | Ứng Dụng cho BLDC Motor

---

## 1. FOC LÀ GÌ? TẠI SAO CẦN?

### Vấn đề với PWM thông thường:
```
PWM thông thường → "Điều khiển điện áp"
→ Motor nhận điện áp → Sinh dòng điện → Sinh lực
→ Dòng điện KHÔNG được kiểm soát trực tiếp
→ Hiệu suất thấp, torque không tuyến tính
```

### FOC - Điều khiển dòng điện trực tiếp:
```
FOC → "Điều khiển dòng điện trong hệ tọa độ quay theo rotor"
→ Phân tách dòng điện thành 2 thành phần:
   Id = "Flux component" (dòng tạo từ thông) → Giữ = 0
   Iq = "Torque component" (dòng tạo moment) → Điều khiển tuyến tính
→ Kết quả: Torque tỉ lệ tuyến tính với Iq
→ Hiệu suất tối đa, nhiệt sinh ra ít nhất
```

---

## 2. KIẾN TRÚC FOC

```
        ┌──────────────────────────────────────────────┐
        │                FOC Control Loop               │
        │                                              │
Torque  │   ┌─────┐   ┌─────────┐   ┌────────────┐   │
Request ─────►  Iq ├──►  Current ├──►   Park &    ├───►  Motor
 (Iq*)  │   │  PID│   │  Limit  │   │  Clark inv │   │  Phase A
        │   └─────┘   └─────────┘   │  Transform │   │  Phase B
        │                            │   (αβ→abc) │   │  Phase C
        │   ┌─────┐                  └────────────┘   │
        │   │  Id ├──► 0 (keep zero)                  │
  0  ───────►  PID│          ↑                        │
        │   └─────┘     Sin/Cos(θ)                    │
        │                    ↑                         │
        │          ┌─────────────────┐                 │
        │          │ Position Sensor │                 │
        │          │  (Encoder/Hall) │                 │
        │          └─────────────────┘                 │
        └──────────────────────────────────────────────┘
```

---

## 3. BIẾN ĐỔI CLARK & PARK

### Clark Transform (3-phase → 2-phase):
```
Chuyển từ hệ tọa độ 3 pha (a, b, c) → hệ 2 pha (α, β)

Iα = Ia
Iβ = (Ia + 2×Ib) / √3
```

### Park Transform (Stator frame → Rotor frame):
```
Chuyển từ hệ cố định (α, β) → hệ quay theo rotor (d, q)

Id = Iα × cos(θ) + Iβ × sin(θ)
Iq = -Iα × sin(θ) + Iβ × cos(θ)

θ = góc điện của rotor (từ encoder)
```

---

## 4. TẠI SAO INNER LOOP FOC CHẠY TRONG MOTOR DRIVER?

```
Trong dự án robot của bạn:
- STM32 (Outer Loop, 100-200Hz): Tính toán v, ω mong muốn → gửi current setpoint qua CAN
- Motor Driver DJI/ODrive/ZLAC8015D: Chạy FOC inner loop ở 1-20kHz
  → Đọc encoder, đọc phase current
  → Thực hiện Clark + Park transform
  → Chạy 2 PID (Id, Iq)
  → Inverse Park + Inverse Clark
  → Tạo PWM 3 pha

→ BẠN CHỈ CẦN GỬI "CURRENT SETPOINT" QUA CAN
  Motor Driver tự lo phần còn lại!
```

---

## 5. SIMPLEFOC - THƯ VIỆN FOC MÃ NGUỒN MỞ

### Dành cho ai muốn TỰ implement FOC:
```
SimpleFOC là thư viện Arduino/STM32/ESP32 để build motor driver tự làm
GitHub: https://github.com/simplefoc/Arduino-FOC
Tài liệu: https://docs.simplefoc.com/

Có thể chạy trên STM32 với Arduino framework
Hỗ trợ: Encoder, Hall sensor, Magnetic encoder (AS5048A)
Motor: BLDC, Stepper

→ Dùng khi bạn tự thiết kế motor driver từ đầu
→ Với DJI/ODrive: FOC đã có sẵn, không cần SimpleFOC
```

### Code mẫu SimpleFOC:
```cpp
#include <SimpleFOC.h>

// Motor: 14 pole pairs
BLDCMotor motor = BLDCMotor(14);
BLDCDriver3PWM driver = BLDCDriver3PWM(PA8, PA9, PA10, PB12);

// Encoder: 2048 CPR
Encoder encoder = Encoder(PB6, PB7, 2048);

void setup() {
    encoder.init();
    encoder.enableInterrupts();
    
    driver.voltage_power_supply = 24;
    driver.init();
    
    motor.linkSensor(&encoder);
    motor.linkDriver(&driver);
    
    // FOC modulation
    motor.foc_modulation = FOCModulationType::SpaceVectorPWM;
    motor.controller = MotionControlType::torque;
    
    motor.PID_velocity.P = 0.5;
    motor.PID_velocity.I = 5;
    
    motor.init();
    motor.initFOC();  // Tự calibrate zero angle!
}

void loop() {
    motor.loopFOC();          // Phải gọi liên tục (> 1kHz)
    motor.move(target_torque);
}
```

---

## 6. LINK TÀI LIỆU FOC

1. **SimpleFOC Documentation (Best for DIY):**
   https://docs.simplefoc.com/

2. **SimpleFOC GitHub:**
   https://github.com/simplefoc/Arduino-FOC

3. **ODrive Robotics (Commercial FOC driver):**
   https://odriverobotics.com/

4. **ST Motor Control SDK (MCSDK):**
   https://www.st.com/en/embedded-software/x-cube-mcsdk.html

5. **Video - FOC Explained:**
   https://www.youtube.com/watch?v=cdiZUszYLiA

6. **Nate's FOC tutorial:**
   https://natemere.wordpress.com/2022/10/21/field-oriented-control-foc-on-stm32/

---

*Phần bổ sung về FOC - Cho robot dùng motor BLDC*
