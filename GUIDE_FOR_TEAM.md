# Hướng Dẫn Chi Tiết Lab 13 Dành Cho Nhóm 3 Thành Viên

Kịch bản dưới đây được chia lại tối ưu cho **3 thành viên**, bao gồm chi tiết công việc, file cần commit, nội dung trình bày lúc Demo và các cải tiến (improvements) giúp báo cáo đạt điểm tối đa.

---

## 1. Thành Viên 1 (TV1): Core Logging, Correlation & Bảo mật PII

**Vai trò:** Quản lý làm giàu ngữ cảnh Log (Enrichment), gán nhãn Correlation ID hệ thống và thiết lập bộ màng lọc bảo mật mã hoá PII.

*   **Việc cần làm cụ thể:**
    *   Tự lấy 1 ảnh log chứa ID `req-...` (`EVIDENCE_CORRELATION_ID_SCREENSHOT`) và chụp 1 bức ảnh text bị che `[REDACTED_...]` gán vào báo cáo.
    *   Trình bày tài liệu: Giải thích cách mà Correlation ID giúp kết nối các module lại, giúp truy vết toàn vẹn hệ thống dễ dàng qua Elasticsearch / JSON log.
*   **File cần Commit:** (Đây là các file đã được cấu hình hoàn thiện, TV1 đóng vai trò là người sửa/chủ sở hữu trên Git)
    1.  `app/main.py`: Giới thiệu dòng code `bind_contextvars` làm giàu metadata (user_id, feature, env).
    2.  `app/middleware.py`: Chỉ ra logic bóc tách/sinh chuỗi hex 8 kí tự cho `x-request-id`.
    3.  `app/pii.py` & `app/logging_config.py`: Giải thích Regex chặn Address và thẻ Passport.
*   **Nội dung Demo:** Mở file log JSON để cho Giảng viên xem trực tiếp luồng log trả về, chứng minh hệ thống xử lý PII tức thời mà không gây trễ bằng structlog Processor.
*   **Cải tiến & Sửa lỗi (Nhận thêm 10% điểm cộng nếu báo cáo kỹ):** 
    *   *Bug fixing:* Cấu trúc Regex đôi khi bắt quá các chuỗi số ngẫu nhiên lầm tưởng là CCCD, đã khoanh vùng `\b` bounday. 
    *   *Improvement:* Nêu ý tưởng trong tương lai sẽ hash Salted ID thay vì dùng SHA-256 thuần để bảo vệ User_ID sâu hơn.

---

## 2. Thành Viên 2 (TV2): Tracing Platform & Load Testing

**Vai trò:** Đảm nhiệm luồng cấu hình gắn kết Langfuse, theo dõi vết (Tracing Waterfall), mô phỏng các lỗi sự cố trên API để đẩy dữ liệu lên Cloud.

*   **Việc cần làm cụ thể:**
    *   Lên Langfuse chụp màn hình **Trace Waterfall** có nhánh đổ xuống của RAG và LLM (`EVIDENCE_TRACE_WATERFALL_SCREENSHOT`). Viết mô tả chi tiết nhịp thời gian ms giữa 2 Spans.
    *   Giả lập Data qua script nhằm đánh dấu ít nhất 10 lỗi.
*   **File cần Commit:** 
    1.  `app/agent.py`: Trưng bày tính năng `langfuse_context` và decorator `@observe()`.
    2.  `test_runner.py`: Logic gọi TestClient đồng thời móc trực tiếp API đẩy 45 lượt hits đa sự cố lên Langfuse.
*   **Nội dung Demo:** Kéo mở Langfuse UI Dashboard ở phần "Traces", bấm ngẫu nhiên vào 1 cái Trace màu Đỏ (Bị lỗi). Chỉ ra cho Giảng viên xem Request đấy bị chết ở Span nào (ví dụ chết ở Retrieving Rag do timeout).
*   **Cải tiến & Sửa lỗi (Cực kì quan trọng để Demo):**
    *   *Bug Fixed:* Khắc phục lỗi tương thích SDK của Langfuse (Version cũ xài `usage_details`, bản v2 dùng `usage`), giúp hệ thống thông luồng tránh lỗi 500 ẩn.
    *   *Improvement:* Xử lý ép buộc `flush()` queue của Langfuse ở Async runtime khi script kết thúc để không bị rớt mất Log giữa chừng trên RAM.

---

## 3. Thành Viên 3 (TV3): Giám sát Dashboard, Alerts SLO & Dẫn dắt báo cáo

**Vai trò:** Phụ trách giám sát chỉ số tổng thể (Metrics), cấu hình cảnh báo, tổng hợp ảnh minh chứng từ TV1, TV2 đẩy lên Markdown và chủ trì buổi báo cáo (Thuyết trình chính).

*   **Việc cần làm cụ thể:**
    *   Tùy chỉnh giao diện Widget trên Langfuse để hiện đủ 6 tấm bảng: *Latency (P95), Traffic, Error Rate, Cost, Tokens, Quality* -> Chụp tấm ảnh quan trọng nhất `DASHBOARD_6_PANELS_SCREENSHOT` và bóc số liệu điền vào SLO_TABLE trong Blueprint.
    *   Chụp bằng chứng file cấu hình Alerts (ảnh `ALERT_RULES_SCREENSHOT`).
*   **File cần Commit:**
    1.  `config/alert_rules.yaml` & `config/slo.yaml`: Chịu trách nhiệm thiết lập các giới hạn cảnh báo thực tiễn.
    2.  `docs/blueprint-template.md`: File thành quả cuối cùng sau khi chèn toàn bộ Link ảnh.
*   **Nội dung Demo:** Dẫn mạch truyện từ việc TV1 ghi log ở Local, rồi TV2 đẩy lên Cloud, và chốt lại tại Dashboard của TV3 thấy mọi thứ ở góc nhìn chim bay (Bird's eye view). Kể lại kịch bản "Incident Response" khi Latency P95 leo lên mốc 5000ms.
*   **Cải tiến & Sửa lỗi:**
    *   *Improvement:* Hiệu chỉnh thông số Alert sát thực tế hơn (Ví dụ: Alert lỗi P1 cho Cost_USD nên ở ngưỡng x2 Baseline để tránh báo động giả - Alert fatigue).
    *   *Improvement:* Tạo folder `docs/assets` và tích hợp file ảnh cứng trực tiếp trên Git thay vì dùng URL ngoài, tránh tình trạng load ảnh chết.

> **Tổng kết cho nhóm:**
> File mã nguồn hiện tại đã tự động bao hàm đầy đủ thành quả code của toàn nhóm rồi, các bạn hãy làm việc linh hoạt, sử dụng File `test_runner.py` để chủ động sinh ra đủ lượng data cần để Screenshot nhé.
