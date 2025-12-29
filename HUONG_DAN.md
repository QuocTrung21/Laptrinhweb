# HƯỚNG DẪN CHỈNH SỬA & MỞ RỘNG DỰ ÁN

## 1. Thêm Bài Viết Blog Mới

### Cách Thêm Bài Viết

Mở file `app.py` và tìm section `BLOG_POSTS`, thêm object mới:

```python
{
    'id': 11,  # ID duy nhất, tăng từ bài viết trước
    'title': 'Tiêu đề bài viết',
    'description': 'Mô tả ngắn (1-2 dòng)',
    'image': '/static/assets/images/blog_thumbnails/ten_file_anh.jpg',
    'date': '2024-12-25',  # Định dạng: YYYY-MM-DD
    'category': 'Java',    # Hoặc 'JavaScript'
    'content': 'Nội dung bài viết...'
}
```

### Ảnh Bài Viết

1. Chuẩn bị ảnh thumbnail (kích thước: 600x400px hoặc tương tự)
2. Đặt vào folder: `static/assets/images/blog_thumbnails/`
3. Đặt tên file: theo convention (e.g., `java_socket.jpg`)
4. Cập nhật đường dẫn trong `'image'` field

---

## 2. Cập Nhật Profile & Thông Tin

### Chỉnh Sửa Trang Thông Tin (About)

File: `templates/about.html`

- Phần giới thiệu: Dòng 24-31
- Kỹ năng chính: Dòng 33-38
- Chứng chỉ: Cập nhật trong `app.py` section `CERTIFICATIONS`

### Cập Nhật Chứng Chỉ

File: `app.py`, section `CERTIFICATIONS`:

```python
{
    'year': '2024',
    'title': 'Tên khóa học',
    'issuer': 'Tổ chức cấp chứng chỉ',
    'description': 'Mô tả nội dung khóa học'
}
```

---

## 3. Tùy Chỉnh Giao Diện

### Màu Sắc & Styling

File: `static/css/style.css`

Các biến CSS chính:
```css
:root {
    --primary-color: #2563eb;      /* Màu xanh chính */
    --secondary-color: #1e40af;    /* Màu xanh phụ */
    --text-dark: #1f2937;          /* Màu chữ chính */
    --text-light: #6b7280;         /* Màu chữ phụ */
    --bg-light: #f9fafb;           /* Màu nền nhạt */
}
```

### Logo & Avatar

- **Logo:** `static/assets/images/logo.jpg`
- **Avatar:** `static/assets/images/avt.jpg`

Thay thế bằng ảnh của bạn, giữ nguyên tên file

---

## 4. Thêm Tính Năng Mới

### Thêm Trang Mới

1. Tạo route trong `app.py`:
```python
@app.route('/new-page')
def new_page():
    return render_template('new-page.html')
```

2. Tạo template trong `templates/new-page.html`:
```html
{% extends "base.html" %}

{% block title %}Tiêu Đề Trang{% endblock %}

{% block content %}
<!-- Nội dung trang -->
{% endblock %}
```

3. Thêm link vào menu navigation (`templates/base.html`):
```html
<li><a href="/new-page" class="nav-link">Trang Mới</a></li>
```

---

## 5. Triển Khai (Deployment)

### Lựa Chọn Hosting

#### GitHub Pages (Tĩnh)
- Không thể chạy Flask backend
- Sử dụng SSG (Static Site Generator) như HUGO hoặc Publii

#### Heroku, Render, PythonAnywhere (Động)
- Hỗ trợ Flask Python
- Dễ triển khai

### Triển Khai Lên Heroku

1. **Cài Đặt Heroku CLI:**
```bash
# Download từ https://devcenter.heroku.com/articles/heroku-cli
heroku login
```

2. **Khởi Tạo Git Repository:**
```bash
git init
git add .
git commit -m "Initial commit"
```

3. **Tạo Heroku App:**
```bash
heroku create your-app-name
```

4. **Tạo Procfile:**
```
web: python app.py
```

5. **Deploy:**
```bash
git push heroku main
```

### Triển Khai Lên PythonAnywhere

1. Đăng ký tại https://www.pythonanywhere.com
2. Upload files qua Web Interface hoặc Git
3. Configure Web App
4. Restart Web App

---

## 6. Tối Ưu Hóa SEO

### Meta Tags

File: `templates/base.html`

```html
<meta name="description" content="Mô tả trang để hiển thị trên Google">
<meta name="keywords" content="lập trình mạng, java, javascript">
<meta name="author" content="Nguyễn Quốc Trung">
```

### Open Graph (Chia sẻ Social)

```html
<meta property="og:title" content="Tiêu đề bài viết">
<meta property="og:description" content="Mô tả bài viết">
<meta property="og:image" content="URL ảnh">
```

---

## 7. Tối Ưu Hóa Hiệu Suất

### Nén Ảnh

```bash
# Sử dụng ImageMagick hoặc online tool
convert input.jpg -quality 80 -resize 800x600 output.jpg
```

### Cache & Compression

Trong `app.py`:
```python
@app.after_request
def set_cache_headers(response):
    response.headers['Cache-Control'] = 'public, max-age=3600'
    return response
```

---

## 8. Bảo Mật

### Form Protection

Sử dụng CSRF token trong contact form:
```html
<input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
```

### Environment Variables

Tạo `.env` file:
```
SECRET_KEY=your-secret-key
DEBUG=False
```

Load trong `app.py`:
```python
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
```

---

## 9. Kiểm Thử & Debug

### Testing

Chạy local server:
```bash
python app.py
```

Mở browser: `http://localhost:5000`

### Debug Mode

Bật debug trong `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True)
```

**Cảnh báo:** Chỉ bật DEBUG=True khi phát triển, TẮT khi production

---

## 10. Git Workflow

### Commit & Push

```bash
# Xem thay đổi
git status

# Thêm tất cả thay đổi
git add .

# Commit với message rõ ràng
git commit -m "Add new blog post about WebSocket"

# Push lên GitHub
git push origin main
```

### Branch Workflow (Tùy chọn)

```bash
# Tạo branch mới
git checkout -b feature/new-feature

# ... thực hiện thay đổi ...

# Push branch
git push origin feature/new-feature

# Tạo Pull Request trên GitHub
```

---

## Các Lệnh Hữu Ích

```bash
# Cài đặt dependencies
pip install -r requirements.txt

# Chạy Flask server
python app.py

# Cập nhật requirements.txt
pip freeze > requirements.txt

# Xóa cache __pycache__
find . -type d -name __pycache__ -exec rm -r {} +

# Tạo virtual environment
python -m venv venv

# Kích hoạt virtual environment (Windows)
venv\Scripts\activate

# Kích hoạt virtual environment (macOS/Linux)
source venv/bin/activate
```

---

## Troubleshooting

### Lỗi Import

```
ModuleNotFoundError: No module named 'flask'
→ Chạy: pip install flask
```

### Port đang được sử dụng

```
Address already in use
→ Chạy Flask với port khác: app.run(port=5001)
```

### Template không tìm thấy

```
jinja2.exceptions.TemplateNotFound: index.html
→ Kiểm tra tên file trong templates/
→ Kiểm tra route render_template('index.html')
```

---

## Tài Liệu Tham Khảo

- Flask: https://flask.palletsprojects.com/
- Jinja2: https://jinja.palletsprojects.com/
- Python.org: https://www.python.org/
- MDN Web Docs: https://developer.mozilla.org/
- GitHub: https://github.com/

---

**Cập nhật lần cuối:** Tháng 12, 2024
