# Trả lời thảo luận Lab 05

## 1. Upstream first vs Release first?
- **Upstream first (Sửa master trước, cherry-pick về release):** 
  - Ưu: Không bao giờ quên cập nhật bản sửa lỗi cho các tính năng tương lai. 
  - Nhược: Dễ bị xung đột (conflict) nặng hoặc không tương thích khi mang ngược một đoạn code từ môi trường mới nhất về môi trường cũ.
- **Release first (Sửa release trước, cherry-pick về master - Cách Lab 05 làm):**
  - Ưu: Cứu khách hàng ngay lập tức trên môi trường bản cũ, độ tương thích 100% không rủi ro.
  - Nhược: Lập trình viên dễ "quên" thao tác cherry-pick mang bản vá lên nhánh master/các nhánh release tương lai, khiến lỗi tái bùng phát ở bản cập nhật sau.

## 2. Nếu quên lan truyền lỗi sang release/lab05, lệnh kiểm toán nào phát hiện?
- Lệnh `git tag --contains <FIX_SHA>` sẽ chỉ liệt kê `v1.0.1` mà vắng bóng `v1.1.0`.
- Chạy script kiểm thử sẽ thấy nhánh `v1.1.0` trả về 0 kết quả (Fail) thay vì 1 (Pass).