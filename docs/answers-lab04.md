# Trả lời câu hỏi thảo luận Lab 04

## 1. Vì sao release/* không bao giờ merge ngược vào master?
- Nhánh `release/*` là nhánh đóng băng để bảo trì một phiên bản cụ thể[cite: 46, 49]. Nếu ta merge toàn bộ nhánh `release/*` vào `master`, ta có thể vô tình làm rối loạn cấu trúc hoặc đè lên các tính năng mới đang được phát triển tích cực trên `master`[cite: 49]. Nếu có lỗi (bug) trên `release`, ta tạo nhánh `hotfix` và dùng lệnh `cherry-pick` để nhặt đúng đoạn mã sửa lỗi đó đưa về `master`[cite: 54, 59].

## 2. So sánh quy trình này với GitFlow?
- **GitFlow:** Dùng nhánh `develop` để tích hợp tính năng hàng ngày và nhánh `master` chỉ để lưu các bản đã phát hành.
- **Release Flow (của học phần):** Chỉ có một nhánh chính sống lâu dài là `master`[cite: 7]. Khi cần phát hành, ta tách nhánh `release/*` từ `master` ra để ổn định và bảo trì[cite: 7, 44]. Cách này giúp nhánh sống ngắn hơn, giữ mọi thứ gần `master` nhất có thể và tránh được tình trạng "merge hell"[cite: 9].

## 3. Vì sao nâng lên 1.0.0 mà không phải 0.4.0?
- Theo nguyên tắc Semantic Versioning (SemVer), các phiên bản bắt đầu bằng `0.y.z` là giai đoạn phát triển ban đầu, mã nguồn chưa ổn định và API có thể thay đổi liên tục[cite: 46]. Khi ứng dụng đạt mốc ổn định, hoàn thiện các tính năng cốt lõi và sẵn sàng xuất bản/nộp bài, ta phải nâng phiên bản MAJOR lên `1.0.0` để đánh dấu sự phá vỡ tính không ổn định của giai đoạn nháp[cite: 46].