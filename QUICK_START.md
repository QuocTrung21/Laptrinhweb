# QUICK START GUIDE

## ⚡ Bắt Đầu Nhanh (5 Phút)

### 1️⃣ Clone & Setup
```bash
# Clone project
git clone <repository-url>
cd project-folder

# Cài dependencies
pip install -r requirements.txt
```

### 2️⃣ Chạy Ứng Dụng
```bash
python app.py
```

### 3️⃣ Mở Trình Duyệt
```
http://localhost:5000
```

---

## 📁 Cấu Trúc Project

```
├── app.py                    # Main Flask app + blog data
├── requirements.txt          # Python packages
├── README.md                 # Tài liệu dự án
├── HUONG_DAN.md             # Hướng dẫn chỉnh sửa
├── DEPLOYMENT.md            # Hướng dẫn triển khai
├── CHANGES.md               # Danh sách thay đổi
│
├── templates/               # HTML templates
│   ├── base.html           # Base template (header, footer)
│   ├── index.html          # Trang chủ
│   ├── blog.html           # Danh sách bài viết
│   ├── post-detail.html    # Chi tiết bài viết
│   ├── about.html          # Thông tin cá nhân
│   └── contact.html        # Liên hệ
│
└── static/                  # Tài nguyên tĩnh
    ├── css/
    │   └── style.css       # Styles
    ├── js/
    │   └── script.js       # JavaScript
    └── assets/
        └── images/         # Ảnh & thumbnails
```

---

## 🔧 Các Trang Chính

| Trang | URL | Mô Tả |
|-------|-----|-------|
| Trang Chủ | `/` | Hero, featured posts, skills |
| Blog | `/blog` | Danh sách 10 bài viết |
| Chi Tiết | `/blog/1-10` | Nội dung bài viết |
| Thông Tin | `/about` | Profile, certifications |
| Liên Hệ | `/contact` | Contact form |

---

## 📝 Chỉnh Sửa Nội Dung

### Thêm Bài Viết
File: `app.py` → `BLOG_POSTS` array

```python
{
    'id': 11,
    'title': 'Tiêu đề bài viết',
    'description': 'Mô tả ngắn',
    'image': '/static/assets/images/blog_thumbnails/tên-ảnh.jpg',
    'date': '2024-12-25',
    'category': 'Java',  # hoặc JavaScript
    'content': 'Nội dung đầy đủ...'
}
```

### Chỉnh Sửa Profile
File: `templates/about.html`

- Dòng 24-31: Giới thiệu
- Dòng 33-38: Kỹ năng chính

### Cập Nhật Chứng Chỉ
File: `app.py` → `CERTIFICATIONS` array

```python
{
    'year': '2024',
    'title': 'Tên khóa học',
    'issuer': 'Tổ chức',
    'description': 'Mô tả'
}
```

---

## 🎨 Tùy Chỉnh Giao Diện

### Thay Logo & Avatar
- Logo: `static/assets/images/logo.jpg`
- Avatar: `static/assets/images/avt.jpg`

### Thay Màu
File: `static/css/style.css` → CSS variables

```css
:root {
    --primary-color: #2563eb;    /* Xanh chính */
    --secondary-color: #1e40af;  /* Xanh phụ */
    --text-dark: #1f2937;        /* Chữ chính */
}
```

---

## 🚀 Triển Khai (Deploy)

### Heroku (Recommended)
```bash
# Cài Heroku CLI
heroku login

# Tạo Procfile
echo "web: python app.py" > Procfile

# Deploy
git push heroku main
```

### PythonAnywhere
1. Đăng ký: https://www.pythonanywhere.com
2. Upload project
3. Configure Web App
4. Set domain (nếu cần)

### GitHub Pages
- Dùng HUGO/Publii + convert static files
- Push lên `gh-pages` branch

---

## 📚 Bài Viết Hiện Có

### Java (5 bài)
1. Socket Programming Basics
2. HTTP Server Implementation
3. Network Interface Management
4. UDP Communication
5. Multithreading Server

### JavaScript (5 bài)
6. Fetch API
7. Async/Await
8. WebSocket
9. XMLHttpRequest vs Fetch
10. REST API Client

---

## 🔧 Lệnh Hữu Ích

```bash
# Chạy local server
python app.py

# Cài dependencies
pip install -r requirements.txt

# Cập nhật requirements.txt
pip freeze > requirements.txt

# Xóa cache
find . -type d -name __pycache__ -exec rm -r {} +

# Git commit
git add .
git commit -m "Mô tả thay đổi"
git push origin main
```

---

## ❓ Troubleshooting

### 1. ModuleNotFoundError: Flask
```bash
pip install -r requirements.txt
```

### 2. Address Already in Use
```python
# app.py
app.run(port=5001)  # Thay port
```

### 3. Template Not Found
- Kiểm tra tên file trong `templates/`
- Kiểm tra đúng tên trong `render_template('...')`

### 4. Ảnh không hiển thị
- Đặt ảnh vào `static/assets/images/`
- Dùng `/static/assets/images/file.jpg`

---

## 📖 Tài Liệu Chi Tiết

- **README.md** - Tổng quan dự án
- **HUONG_DAN.md** - Chi tiết chỉnh sửa
- **DEPLOYMENT.md** - Hướng dẫn triển khai
- **CHANGES.md** - Danh sách thay đổi

---

## 🎯 Next Steps

1. ✅ Chạy local: `python app.py`
2. ✅ Thêm ảnh bài viết vào `static/assets/images/blog_thumbnails/`
3. ✅ Viết nội dung chi tiết cho từng bài viết
4. ✅ Test trên mobile
5. ✅ Deploy (Heroku/PythonAnywhere)
6. ✅ Setup custom domain
7. ✅ Enable HTTPS

---

## 📞 Thông Tin

**Tác Giả:** Nguyễn Quốc Trung  
**Khóa Học:** Lập Trình Mạng - Java & JavaScript  
**Năm:** 2024

---

**Hãy chúc vui và hướng tới thành công! 🚀**
