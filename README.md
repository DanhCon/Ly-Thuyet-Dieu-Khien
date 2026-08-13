# 📚 Lý Thuyết Điều Khiển — Tài liệu Tự học Toàn diện

Bộ tài liệu tự học về **Lý thuyết Điều khiển Tối ưu**, tập trung vào **LQR (Linear Quadratic Regulator)** và các chủ đề liên quan. Tất cả được viết bằng Tiếng Việt, có công thức LaTeX (MathJax), code Python mô phỏng, và ví dụ thực tế.

## 📖 Danh sách Tài liệu

### Lý thuyết Cốt lõi
| # | Tài liệu | Nội dung |
|---|----------|----------|
| 1 | [LQR Toàn Tập](LQR_ToanTap.html) | LQR cơ bản: State Space, hàm chi phí, ARE, giải tay, code Python |
| 2 | [LQR Nâng Cao & LQG](LQR_NangCao_LQG_ToanTap.html) | DLQR, Integral Action, LQG, Return Difference Inequality |
| 3 | [Kalman Filter Toàn Tập](Kalman_Filter_ToanTap.html) | Kalman Filter tuyến tính: 5 phương trình, ví dụ số, code Python |
| 4 | [EKF Toàn Tập](EKF_ToanTap.html) | Extended Kalman Filter: Jacobian, hệ phi tuyến, GPS+IMU fusion |

### Kiến thức Bổ trợ
| # | Tài liệu | Nội dung |
|---|----------|----------|
| 5 | [Kiến thức Nền tảng Bổ sung P1](KienThuc_NenTang_BoSung_LQR.html) | 9 chương: Dạng toàn phương, Trị riêng, Controllability, Bode, Nyquist, Lyapunov |
| 6 | [Kiến thức Nền tảng Bổ sung P2](KienThuc_NenTang_BoSung_Phan2_LQR.html) | Tín hiệu & Pha, Chứng minh Lyapunov chi tiết, Tại sao LQR tối ưu (Bellman → Riccati) |

### Bài tập & Thực hành
| # | Tài liệu | Nội dung |
|---|----------|----------|
| 7 | [Bài Tập LQR Toàn Tập](BaiTap_LQR_ToanTap.html) | Bài tập hiểu sâu, giải tay, ứng dụng sáng tạo (Robot, Kinh tế vĩ mô) |
| 8 | [Tuần 1-2: Mô Hình Hóa](Tuan1_2_MoHinhHoa_StateSpace.html) | Lagrangian, con lắc ngược, tuyến tính hóa, lấy A/B, code Python mô phỏng |

### Triển khai Thực tế
| # | Tài liệu | Nội dung |
|---|----------|----------|
| 9 | [LQR Thực Chiến Robot Thật](LQR_ThucChien_RobotThat.html) | Phần cứng, System ID, Sensor Fusion, Rời rạc hóa, Tuning, Debug, Quy trình A-Z |

### Tài liệu Khác (PID, FOC)
| # | Tài liệu | Nội dung |
|---|----------|----------|
| 10 | [PID Cascade Control](PID_Cascade_Control_TongQuan.md) | Tổng quan PID xếp tầng |
| 11 | [FOC Field Oriented Control](FOC_Field_Oriented_Control.md) | Điều khiển vector động cơ BLDC |
| 12 | [SimpleFOC README](SimpleFOC_README.md) | Thư viện SimpleFOC |

## 🛠️ Cách sử dụng

1. **Mở file `.html`** trên trình duyệt (Chrome/Edge/Firefox) — công thức LaTeX sẽ tự render qua MathJax.
2. **Copy code Python** trong tài liệu và chạy trên máy (cần `numpy`, `scipy`, `matplotlib`).
3. **Xuất PDF** bằng nút "📄 Xuất PDF" ở góc phải dưới mỗi trang.

## 📅 Lộ trình Học tập Đề xuất

```
Tuần 1-2: Mô hình hóa (Tài liệu #8)
  → Lagrangian, State Space, Python mô phỏng

Tuần 3: LQR Cơ bản (Tài liệu #1)
  → Hàm chi phí, ARE, giải tay, tuning Q/R

Tuần 4: Kalman Filter + LQG (Tài liệu #3, #2)
  → Sensor fusion, Observer, LQG

Tuần 5: Triển khai Robot thật (Tài liệu #9)
  → Phần cứng, Complementary Filter, Debug
```

## 📝 Ghi chú
- Tất cả tài liệu `.html` sử dụng MathJax CDN, cần kết nối internet để hiển thị công thức.
- Font: `-apple-system, Segoe UI, Roboto, Arial, Noto Sans` — hỗ trợ tiếng Việt đầy đủ.

---
*Tài liệu được tạo với sự hỗ trợ của AI, dựa trên kiến thức từ sách giáo khoa Lý thuyết Điều khiển Tối ưu.*
