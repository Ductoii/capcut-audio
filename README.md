# CapCut Audio

**Tool local cân thoại bằng thuật toán. Chọn project → cân âm → nghe A/B → Apply/Undo.**

[English](README.en.md) · [Releases](https://github.com/Ductoii/capcut-audio/releases)

Không cần Codex, chatbot, plugin, MCP, API key hay gửi yêu cầu về chat. Tool không làm card hoặc đọc kịch bản. Time/location và giới thiệu nhân vật dùng riêng [skill CapCut Cinematic Cards](https://github.com/Ductoii/capcut-cinematic-cards).

## Cài và mở

Máy có Python 3.10–3.13 và FFmpeg/ffprobe:

```bash
curl -fsSL https://raw.githubusercontent.com/Ductoii/capcut-audio/v0.1.0/install-audio.py | python3
```

Mở bằng:

```bash
~/.local/bin/capcut-audio
```

Bộ cài tạo runtime riêng. Khi nâng cấp từ bản CapCut Harness cũ, nó gỡ đúng plugin/skill/launcher và runtime cũ do bộ cài đó quản lý, giữ toàn bộ job/audio/backup Undo. Không cài skill mới và không sửa các plugin khác. Nếu máy thiếu dependency, có thể nhờ Codex cài hộ; lúc chạy tool không dùng Codex.

## Cách dùng

- Danh sách tự đọc kho/index CapCut, đường dẫn lưu tùy chỉnh và OS search. Có nút **Quét lại project**; project chưa hỗ trợ vẫn hiện lý do. Tìm ngoài kho phụ thuộc quyền truy cập và chỉ mục OS.
- **Cân âm thoại** chạy thẳng thuật toán trên máy, tạo bản nghe mà chưa sửa project. Có tiến độ và hủy.
- Nghe **Bản gốc / Sau xử lý**, bỏ chọn đoạn nhận nhầm hoặc đổi thiết lập nếu cần. Link phát riêng cho job không phụ thuộc cookie; có **Tải lại audio**.
- Lưu và đóng CapCut rồi **Áp dụng vào project**. Một master audio được thêm ngoài clip ghép; các đoạn gốc tham gia mix bị tắt âm để tránh phát đôi. Hình, cấu trúc compound, text và nhịp dựng được giữ.
- Khi timeline hoặc nguồn đã đổi, bản cũ không được ghi đè: UI báo **Bản cân đã cũ** và có **Cân lại bản hiện tại**. Ví dụ đổi tốc độ 1,0 → 0,95 cần audio mới khớp timeline.
- **Hoàn tác** dùng backup chính xác; từ chối ghi đè chỉnh sửa mới của bạn.

## Thuật toán

Cân từng nguồn trước khi trộn: VAD local → mốc LUFS có trọng số thời lượng → tinh chỉnh câu nhỏ → nén RMS nhẹ 2:1 → bảo vệ peak nguồn/master. Preset: thoại −16 LUFS, peak −1,5 dBTP, stereo 48 kHz PCM24, bù tối đa 48 dB. Đây là preset khởi đầu cho phim online, không phải chuẩn chung cho mọi phim/MV.

Nhạc/SFX ở nguồn riêng không bị kéo theo gain của thoại. Nhạc/noise đã nằm chung file thoại vẫn thay đổi theo file; VAD không tách stem, không chắc phân biệt giọng hát và không phục hồi tiếng đã méo. Bù lớn có thể kéo noise lên. Nguồn chưa nhận diện thoại được giữ mức và báo riêng.

## Dữ liệu và phạm vi

Đọc project local JSON không mã hóa, schema `360000`. Từ chối hiệu ứng/routing/tốc độ biến thiên chưa hỗ trợ. Không Computer Use. Mọi audio ở máy; audio dựng lại từ nguồn không chứng minh playback/export native CapCut.

Giữ **`~/.local/share/capcut-harness`**: tên thư mục cũ được giữ để bảo toàn đường dẫn job và Undo. Không xóa hoặc di chuyển nó. Runtime mới ở `~/.local/share/capcut-audio-tool`; tool có thể dùng nhiều GB cho phim dài.

Đã kiểm tra cú pháp, HTTP audio/link có phạm vi job và đóng gói. Không chạy lại vòng phân tích cả phim hoặc 300 nguồn để kiểm chứng. macOS là môi trường phát triển; hệ điều hành khác chưa được xác minh.

[Mã nguồn](capcut_harness) · [MIT](LICENSE)
