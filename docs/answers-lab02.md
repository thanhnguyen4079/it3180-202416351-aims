# Trả lời câu hỏi thảo luận Lab 02

## 1. Vì sao phải đồng bộ master vào nhánh tính năng trước khi gửi PR?
- Để phát hiện và giải quyết sớm các xung đột (merge conflict) cũng như kiểm tra tích hợp (chạy thử chương trình/test) ngay trên nhánh riêng trước khi đưa vào `master`, đảm bảo nhánh `master` luôn ở trạng thái ổn định và chạy được.

## 2. Khi nào không được dùng rebase?
- Không được rebase trên các nhánh công khai đã chia sẻ cho nhiều người cùng làm việc (như `master`, `release/*`), vì rebase viết lại lịch sử (tạo mã băm SHA mới), làm lệch lịch sử với máy của các thành viên khác.

## 3. Nhánh `feature/*` khác nhánh `topic/*` như thế nào?
- `feature/*`: Dùng để phát triển các tính năng mới của sản phẩm dành cho người dùng (ví dụ: `feature/cart-print`, `feature/search-by-title`).
- `topic/*`: Dùng cho các công việc kỹ thuật, tài liệu, cấu hình hoặc thử nghiệm không trực tiếp thêm tính năng phần mềm (ví dụ: `topic/pr-template`, `topic/use-case-diagram`).
