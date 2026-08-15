# 🧠 Ký ức Phiên Làm Việc — Tài Liệu Học Tập Kỹ Thuật (Robotics & Control)

> File này ghi lại toàn bộ ngữ cảnh phiên làm việc để lần sau đọc lại là nắm được ngay: bối cảnh, người dùng, các file đã tạo, quy ước phong cách, lỗi gặp phải và cách khắc phục.

---

## 1. Tổng quan phiên làm việc

**Mục đích phiên:** Người dùng đang tự học/nghiên cứu **Robotics & Kỹ thuật điều khiển (Control)**. Các phiên trước đã tạo tài liệu học chi tiết định dạng **HTML + MathJax + quiz** về Kalman Filter và Cảm biến IMU. Phiên này tiếp tục tạo tài liệu toán nền tảng và lưu ký ức phiên.

**Người dùng nói tiếng Việt** → toàn bộ tài liệu và trả lời phải bằng tiếng Việt.

**Model:** `opencode/big-pickle` — **KHÔNG hỗ trợ nhập ảnh** (đã bị lỗi khi người dùng gửi ảnh).

**Thư mục làm việc:** `C:\Users\hocho\OneDrive\Documents\Default Project`
**Thư mục tài liệu (F:):** `F:\anti\Projec\TaiLieu_ThamKhao\06_Ly_Thuyet_Dieu_Khien\`

---

## 2. Các file đã tạo trong phiên

| # | File | Nội dung | Trạng thái |
|---|------|----------|------------|
| 1 | `F:\anti\Projec\TaiLieu_ThamKhao\06_Ly_Thuyet_Dieu_Khien\Kalman_Filter_ToanTap.html` | Đã tồn tại từ trước phiên. Bộ lọc Kalman toàn tập (xác suất nền, phép nhân 2 Gauss → Kalman Gain, 5 bước thuật toán, code Python/C++). Dùng làm **khuôn mẫu phong cách**. | Tham chiếu |
| 2 | `F:\anti\Projec\TaiLieu_ThamKhao\06_Ly_Thuyet_Dieu_Khien\IMU_CanBien_ToanTap.html` | Cảm biến IMU toàn tập: 8 phần (tổng quan, gia tốc kế, con quay, từ kế, Euler/Quaternion, Sensor Fusion, hiệu chuẩn, lập trình Arduino/STM32/Python, ứng dụng). | ✅ Tạo xong |
| 3 | `F:\anti\Projec\TaiLieu_ThamKhao\06_Ly_Thuyet_Dieu_Khien\Toan_NenTang_Robotics_Control.html` | Toán nền tảng Robotics & Control: 5 phần (cách học, đại số tuyến tính, Laplace/Z, tối ưu hóa, xác suất/random process, tổng kết lộ trình). **Điểm đặc biệt: phân cấp mức độ hiểu cho từng mục.** | ✅ Tạo xong |
| 4 | `C:\Users\hocho\OneDrive\Documents\Default Project\ky-uc-phien-lam-viec.md` | File ký ức này. | ✅ Tạo xong |

---

## 3. QUY ƯỚC PHONG CÁCH TÀI LIỆU (bắt buộc tuân theo khi tạo tài liệu mới)

Dựa trên khuôn mẫu `Kalman_Filter_ToanTap.html`, các tài liệu HTML tiếp theo PHẢI giữ nguyên cấu trúc:

1. **DOCTYPE + lang="vi"**, charset UTF-8.
2. **MathJax 3** từ CDN `cdn.jsdelivr.net`, cấu hình `inlineMath: [['$','$']], displayMath: [['$$','$$']]`, `tags: 'ams'`. Polyfill từ polyfill.io.
3. **CSS gần như giữ nguyên** của file Kalman, với các biến CSS `:root` (primary #0f172a, accent #2563eb, quiz-bg #f0f9ff, answer-bg #f0fdf4...).
4. **Cover page** — `.cover-page` với h1, `.subtitle`, `.tagline`, `.meta`.
5. **Mục lục** — `.toc` với liên kết anchor `#partX`, `#sX.Y`.
6. **Phần header** — `.part-header` (xanh gradient), `.part-header-intro` (xanh lá, dùng cho Phần 0), và đã thêm biến thể màu: `.part-header-danger` (đỏ, phần con quay), `.part-header-purple` (tím), `.part-header-orange` (cam).
7. **Boxes:** `.definition`, `.theorem`, `.important-note`, `.example-box`, `.analogy-box`, `.warning-box` (đỏ), `.cheat-sheet` (teal, dùng trong tài liệu toán).
8. **`.step-card` + `.step-number`** cho quy trình từng bước.
9. **Quiz** — `.quiz-section` + `.quiz-question` + `.answer-section` (đáp án hiện ngay, `.box-title` màu xanh lá "✅ Đáp án").
10. **Bảng** — `.table` với header tối `--primary`.
11. **Code** — `<pre><code>` nền `--code-bg` (#0f172a), font Fira Code/Consolas.
12. **Nút in**: `<button class="print-btn" onclick="window.print()">📄 Xuất PDF</button>`.
13. **Tổng kết cuối** — div gradient `linear-gradient(135deg, #0f172a, #1e293b)` với h2 xanh `#60a5fa`, liệt kê điểm chính.
14. **Footer** — "— Hết tài liệu X —" + ghi chú nút xuất PDF.
15. `@media print` cho PDF: ẩn print-btn, `page-break-before: always` cho phần headers, `break-inside: avoid` cho boxes.

### Biến thể mới trong tài liệu toán (đáng dùng lại):
- **Huy hiệu mức độ:** `.level-badge` + 3 loại:
  - `<span class="level-badge level-apply">🔧 CHỈ CẦN CÔNG THỨC</span>` (xanh lá)
  - `<span class="level-badge level-deep">🔬 CẦN HIỂU SÂU</span>` (xanh dương)
  - `<span class="level-badge level-concept">🔎 HIỂU Ý TƯỞNG</span>` (tím)
- **Legend box** giải thích huy hiệu ở đầu tài liệu (`.legend-box`, `.legend-item`).
- **Cheat sheet** `.cheat-sheet` để đóng gói công thức tra nhanh.

---

## 4. QUY ƯỚC NỘI DUNG & SƯ PHẠM

- **Cuốn chiếu từng bước** (từ cơ bản → nâng cao), nhiều ví dụ số cụ thể, ẩn dụ trực quan.
- Mỗi phần lớn có **quiz kèm đáp án ngay dưới**.
- Công thức quan trọng đóng khung: `\boxed{...}`.
- Chứng minh chỉ trình bày khi cần hiểu sâu, phần "chỉ cần công thức" thì đưa cheat sheet + ví dụ áp dụng, KHÔNG chứng minh.
- Phong cách tiếng Việt tự nhiên, dùng ** (bold) và $$ (math).

---

## 5. PHÂN CẤP MỨC ĐỘ HIỂU — KẾT LUẬN QUAN TRỌNG TỪ PHIÊN

Người dùng yêu cầu phân biệt rõ: **phần nào chỉ cần biết công thức để áp dụng, phần nào cần hiểu chi tiết.** Kết luận đã được chốt trong `Toan_NenTang_Robotics_Control.html`:

**🔬 CẦN HIỂU SÂU (70% thời gian):**
- Không gian trạng thái (A, B, C, D; trạng thái ≠ đầu ra; rời rạc hóa)
- Eigenvalue & ổn định (liên tục: Re(λ)<0; rời rạc: |λ|<1; cực = eigenvalue)
- ODE bậc nhất & thời gian hằng số τ
- Laplace & hàm truyền (khái niệm, cực/zero, Bode)
- Gradient Descent (ý nghĩa α, phân kỳ)
- Least Squares & Normal Equation (θ* = (XᵀX)⁻¹Xᵀy, có suy luận)
- Random Process, PSD, nhiễu trắng Gauss (nền Q, R trong Kalman)

**🔧 CHỈ CẦN CÔNG THỨC (20%):**
- Phép toán ma trận (cheat sheet)
- SVD & giả nghịch đảo (np.linalg.pinv)
- Jacobian (linearization cho EKF, động học nghịch)
- Z-transform & bảng tra Laplace/Z
- Ôn tập xác suất nền Kalman

**🔎 HIỂU Ý TƯỞNG (10%):**
- Convex Optimization (nhận dạng QP/LP/SOCP, dùng CVXPY/OSQP)
- MPC (pipeline dự đoán→tối ưu→áp dụng bước đầu→lặp)
- Martingale (random walk = mô hình drift con quay, sai số tăng ~√t)

---

## 6. LỘ TRÌNH HỌC ĐÃ ĐỀ XUẤT (từ phiên trước, chốt trong tài liệu toán)

Thứ tự: **PID → Mô hình hóa (state-space) → LQR → Kalman (đã xong) → ROS → SLAM → MPC/phi tuyến.**
Lộ trình 12 tuần chi tiết nằm ở `Toan_NenTang_Robotics_Control.html` phần 5.2.

Các chủ đề tiếp theo người dùng có thể cần tài liệu (đã đề nghị): **Lý thuyết điều khiển (PID, LQR, ổn định Lyapunov/Bode/Nyquist, MPC), SLAM, Động học robot, ROS/ROS2.**

---

## 7. LỖI ĐÃ GẶP & CÁCH KHẮC PHỤC

| Lỗi | Nguyên nhân | Cách khắc phục |
|-----|-------------|----------------|
| `ERROR: Cannot read "image.png" (this model does not support image input)` | Model `opencode/big-pickle` không hỗ trợ vision | Báo người dùng: (1) gửi đường dẫn file ảnh để đọc như file thường, hoặc (2) chuyển model hỗ trợ vision bằng lệnh `/models` rồi khởi động lại session |
| Người dùng gửi ảnh screenshot | Model không có vision | Hướng dẫn người dùng dán đường dẫn file hoặc mô tả bằng chữ |

**Lưu ý cho lần sau:** Nếu người dùng lại gửi ảnh → không cố đọc, lập tức nhắc nhở model không hỗ trợ + gợi ý giải pháp trên.

---

## 8. LỊCH SỬ TRÒ CHUYỆN TÓM TẮT

1. **"bạn có thể làm gì"** → Giới thiệu khả năng: hiểu codebase, viết/sửa code, chạy lệnh, tìm kiếm web.
2. **"bạn có thể truy cập vào đâu"** → Trả lời: file trong thư mục làm việc, internet (web search), terminal. Không truy cập từ xa.
3. **Gửi ảnh → lỗi vision** → Báo model không hỗ trợ ảnh.
4. **"model nào có thể nhập ảnh"** → Trả lời: là instance đơn lẻ `opencode/big-pickle`, không có danh sách model; gợi ý `/models` hoặc xem https://opencode.ai.
5. **Gửi file `Kalman_Filter_ToanTap.html`** (đọc được) → Xác nhận truy cập được, hỏi người dùng muốn làm gì.
6. **"làm nội dung chi tiết tương tự về cảm biến imu"** → Tạo `IMU_CanBien_ToanTap.html` (8 phần đầy đủ).
7. **"cần thêm kiến thức gì cho robotics/control"** → Đưa roadmap 5 mảng: toán nền, lý thuyết điều khiển, robotics chuyên sâu, lập trình/hệ thống, cơ điện tử.
8. **"tạo file toán nền tảng, phân cấp công thức vs hiểu sâu"** → Tạo `Toan_NenTang_Robotics_Control.html` với huy hiệu mức độ.
9. **"tạo file md lưu ký ức phiên"** → Tạo file này.

---

## 9. NGƯỜI DÙNG & SỞ THÍCH

- **Ngôn ngữ:** tiếng Việt.
- **Lĩnh vực:** Robotics, điều khiển, cảm biến, vi điều khiển (STM32/ESP32/Arduino), lập trình C++/Python.
- **Phong cách mong muốn:** tài liệu học dạng HTML đẹp, có MathJax, có quiz kèm đáp án, cuốn chiếu, ví dụ số cụ thể, phân biệt rõ "hiểu sâu" vs "chỉ cần áp dụng".
- **Yêu cầu lưu file** trong thư mục `F:\anti\Projec\TaiLieu_ThamKhao\06_Ly_Thuyet_Dieu_Khien\` với tên tiếng Việt gợi nhớ (vd `IMU_CanBien_ToanTap.html`, `Toan_NenTang_Robotics_Control.html`).
- Người dùng thích tài liệu **"toàn tập" / "đầy đủ"** — làm thật chi tiết.

---

## 10. TODO / ĐỀ XUẤT TIẾP THEO (khi người dùng yêu cầu)

- [ ] Tài liệu **Lý thuyết điều khiển cơ bản** (PID, đặt cực, LQR, Bode/Nyquist, Lyapunov) — cũng theo phong cách HTML + quiz.
- [ ] Tài liệu **Động học robot cánh tay** (forward/inverse kinematics, DH, Jacobian).
- [ ] Tài liệu **SLAM & Định vị** (odometry, EKF-SLAM, Graph SLAM, GMapping/Cartographer).
- [ ] Tài liệu **ROS/ROS2** căn bản.
- [ ] Có thể tạo **bản PDF** từ các file HTML nếu người dùng muốn.

**Quy tắc chung:** Mỗi tài liệu mới → theo đúng quy ước phong cách ở mục 3 & 4, đặt cùng thư mục F:, tên file tiếng Việt không dấu hoặc gợi nhớ.