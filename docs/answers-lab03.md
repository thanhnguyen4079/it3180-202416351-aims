# Trả lời câu hỏi thảo luận Lab 03

## 1. Merge base là gì?
- Merge base là điểm kỳ cựu chung (common ancestor) gần nhất của hai nhánh đang được hợp nhất. Trong giao diện Pull Request trên GitHub, "base branch" được hiểu là nhánh đích mà bạn muốn gộp code vào (ví dụ: `master` hoặc `feature/discount`).

## 2. Vì sao master/release/* phải dùng revert?
- Các nhánh `master` và `release/*` là nhánh công khai (đã chia sẻ cho nhiều người hoặc đã phát hành). Nếu dùng `reset` (hay `rebase`, `amend`), ta sẽ thay đổi/viết lại lịch sử. Khi đẩy lên, sự sai lệch lịch sử sẽ gây ra lỗi nghiêm trọng (conflict) cho các lập trình viên khác khi họ `git pull`. Lệnh `git revert` tạo ra một commit hoàn toàn mới nhằm đảo ngược sự thay đổi, giúp bảo toàn toàn bộ lịch sử trước đó, do vậy an toàn khi làm việc nhóm.
