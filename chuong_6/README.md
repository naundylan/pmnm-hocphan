# Chương 6: Làm việc với Cơ sở dữ liệu (SQLite & SQLAlchemy)

## 1. Giới thiệu
Bài thực hành Chương 6 sử dụng:
- **Flask**: Framework web
- **Flask-SQLAlchemy** & **SQLAlchemy 2.0**: ORM kết nối và quản lý cơ sở dữ liệu
- **SQLite**: Cơ sở dữ liệu nhẹ, không cần cài đặt server, lưu trữ trực tiếp vào file `instance/qlsv.db`.

## 2. Cách chạy ứng dụng

### Cách 1: Chạy trực tiếp file `app.py`
Mở PowerShell tại thư mục dự án:
```powershell
cd D:\Project\pmnm-hocphan\chuong_6
..\.venv\Scripts\python.exe app.py
```

### Cách 2: Chạy bằng lệnh Flask CLI (theo slide bài giảng)
```powershell
cd D:\Project\pmnm-hocphan\chuong_6
..\.venv\Scripts\flask.exe --app app run --debug
```

Mở trình duyệt truy cập: `http://127.0.0.1:5000/`

---

## 3. Các đường dẫn (Routes) và kiểm tra

| Endpoint | Phương thức | Mô tả |
| :--- | :---: | :--- |
| `/` | GET | **Trang chủ:** Hiển thị danh sách toàn bộ sinh viên rõ ràng lấy từ CSDL `qlsv.db`. |
| `/them-mau` | GET | **Bước 5 bài giảng:** Thêm 5 sinh viên mẫu vào bảng `student`, tự động kiểm tra `total > 0` để tránh thêm trùng khi tải lại trang. |
| `/thu-truy-van` | GET | **Bước 6 bài giảng:** Thử nghiệm các câu truy vấn SQLAlchemy: `get(id)`, `select().all()`, `where()`, `order_by()`, `filter_by()`, `func.count()`, `func.avg()`. Trả về dạng plain text. |

---

## 4. Kiểm tra dữ liệu trong file CSDL
File CSDL được tự động tạo và lưu tại:
```text
chuong_6/instance/qlsv.db
```
Bạn có thể mở file này bằng:
- **VS Code Extension:** Cài extension `SQLite Viewer`, sau đó bấm chuột trái vào file `instance/qlsv.db`.
- **DB Browser for SQLite:** Mở DB Browser -> chọn *Open Database* -> trỏ đến file `instance/qlsv.db` -> chuyển sang tab *Browse Data* để xem các dòng sinh viên.
