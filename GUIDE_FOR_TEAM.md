# Hướng Dẫn Hoàn Thiện Lab 13 Dành Cho Nhóm (4 Thành viên)

Xin chào các thành viên, hiện tại toàn bộ mã nguồn của Lab 13 **đã được hoàn thiện 100% công việc lập trình** và đã pass tất cả các bài test `validate_logs.py` (Mức điểm 100/100, bảo vệ PII thành công, setup đầy đủ tính năng Correlation ID). 

Công việc của nhóm bây giờ chỉ còn lại là thao tác trên nền tảng **Langfuse UI** và điền kết luận (chụp ảnh chèn vào) file báo cáo `docs/blueprint-template.md`.

---

## 1. Phân công vai trò (4 thành viên)

Để chia đều khối lượng công việc làm báo cáo, các bạn có thể chia theo định hướng sau để điền vào `Chương 5. Individual Contributions` trong file blueprint:

*   **Thành viên 1:** *Vai trò: Logging & Ẩn dữ liệu nhạy cảm PII.*
    Chịu trách nhiệm chụp ảnh minh chứng `EVIDENCE_CORRELATION_ID_SCREENSHOT` và `EVIDENCE_PII_REDACTION_SCREENSHOT` từ file cấu hình log.
*   **Thành viên 2:** *Vai trò: Tracing & Load Testing.*
    Lên hệ thống UI của Langfuse chụp sơ đồ `EVIDENCE_TRACE_WATERFALL_SCREENSHOT` và giải thích hệ thống các nhánh truy vấn.
*   **Thành viên 3:** *Vai trò: Cấu hình Alert, SLO & Xử lý sự cố.*
    Chụp hình ảnh quy định cảnh báo cho `ALERT_RULES_SCREENSHOT`, tính toán chỉ số SLO chuẩn mực và mô phỏng báo cáo sự cố (Incident mock).
*   **Thành viên 4:** *Vai trò: Langfuse Dashboard & Quản lý Demo.*
    Tổng hợp trực quan giao diện Dashboard (lọc đúng 6 widget báo cáo), lưu tấm ảnh quan trọng `DASHBOARD_6_PANELS_SCREENSHOT`. Hỗ trợ các bạn khác ghép ảnh vào file Markdown chuẩn form.

---

## 2. Các bước cụ thể lấy chứng cứ hình ảnh

Dưới đây là chi tiết các vị trí để chụp màn hình làm bằng chứng ghép vào khung `blueprint-template`:

### A. Bằng chứng Log 
*   **Ví trí Screenshot 1 (Mã Correlation):** Tại file `data/logs.jsonl` trong thư mục project của bạn, chụp nội dung bất kì dòng nào bắt đầu chứa thuộc tính `"correlation_id": "req-..."`.
*   **Ví trí Screenshot 2 (Mã hoá PII):** Cũng tại file jsonl phía trên, rà lại xem dòng nào bị chặn số điện thoại (`[REDACTED_PHONE_VN]`) hoặc chặn định dạng email (`[REDACTED_EMAIL]`). Chụp ngay phần text bị che lại để nộp làm bằng chứng.

### B. Bằng chứng Dashboard (Cực kì quan trọng)
*   Đăng nhập tài khoản Langfuse của nhóm (truy cập cloud.langfuse.com) và vào Project mà nhóm dùng file `.env` kết nối.
*   Bấm vào Menu bên trái phần **Dashboard**.
*   Sắp xếp lại màn hình bố cục Langfuse bằng cách tuỳ chỉnh các Widgets làm sao để nó chứa 6 Panels theo yêu cầu môn học:
    1. Latency P50/P90/P99
    2. Tổng số Traces / Observation (Đại diện cho Traffic)
    3. Biểu đồ báo lỗi (Errors)
    4. Chi phí USD hao tổn (Total Costs)
    5. Token in và Token out
    6. Scores / Feedback
*   Lọc biểu đồ ở phạm vi thời gian thành "1 hour" (Một giờ qua) sau đó **sử dụng phím Print Screen/Snipping tool chụp lại toàn màn hình**.

### C. Bằng chứng Trace Waterfall
*   Quay lại nền tảng **Langfuse**, nhấn sang Tab **Traces**.
*   Click chi tiết vào cái Trace đầu tiên (hoặc bất kỳ).
*   Giao diện sẽ trải rộng ra dạng cấu trúc hình Cây biểu đồ đổ xuống (Waterfall) mô phỏng chính xác Request bạn gọi vào Database tốn độ trễ ms bao nhiêu, và Model chạy tốn bao nhiêu thời gian. Hãy **chụp lại cái cây này**.

### D. Chuẩn bị ảnh file Alert_rules
*   Chụp lại vùng nội dung văn bản của file `config/alert_rules.yaml` có sẵn trong sourse, chứng minh có setup các điều kiện `latency_p95_ms > 5000` như một ngưỡng báo lỗi.

---

## Bước 3: Tổng hợp

*   Nhóm tạo thêm một thư mục mang tên `docs/assets/`.
*   Ném tất cả 5 file ảnh các bạn vừa chụp ở các bước trên vào folder `assets`.
*   Mở file template báo cáo `docs/blueprint-template.md` rồi điền tên của nhóm mình vào, ở mục nào đang ghi ngoặc vuông `[Path to image]` thì thay thế bằng code chèn hình Markdown của bạn (Ví dụ: `![Giao_dien_Dashboard](./assets/dashboard.png)`).

Chúc cả nhóm làm Lab thành công! Code đã chạy rất trơn tru, phần khó nhất đã hoàn tất!
