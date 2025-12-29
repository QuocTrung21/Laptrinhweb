# Blog Cá Nhân - Lập Trình Mạng Với Java & JavaScript

## Thông Tin Đồ Án

**Sinh Viên:** Nguyễn Quốc Trung  
**Yêu Cầu:** Phát triển trang Blog cá nhân chia sẻ về lập trình mạng  
**Công Nghệ:** Flask, HTML5, CSS3, JavaScript, Python  
**Repository:** GitHub (Đã sử dụng GitHub Repository)

---

## Yêu Cầu Đồ Án

### ✅ 1. Phát triển trang Blog cá nhân chia sẻ về lập trình mạng
- Blog hiển thị 10 bài viết chuyên sâu về lập trình mạng
- Tập trung vào Java Socket Programming, JavaScript WebSocket, HTTP Protocol
- Các bài viết chi tiết, dễ hiểu và có giá trị thực tế

### ✅ 2. Lựa chọn và chia sẻ bài viết theo các khóa học đã được học
- **Java:** 5 bài viết về Socket, Server, UDP, Multithreading, Network Interface
- **JavaScript:** 5 bài viết về Fetch API, Async/Await, WebSocket, HTTP Client
- Tất cả nội dung viết bằng **tiếng Việt** và dễ theo dõi

### ✅ 3. Yêu cầu Blog

#### 📌 Cấu Trúc Menu
- **Trang Chủ (Home)** - Giới thiệu, featured posts, skills
- **Trang Blog** - Danh sách tất cả bài viết với filter theo category
- **Trang Thông Tin (About)** - Profile, certifications, kỹ năng chi tiết
- **Trang Liên Hệ (Contact)** - Form liên hệ

#### 📝 Nội Dung Profile & Bài Viết
**Profile:**
- Giới thiệu chi tiết về Nguyễn Quốc Trung
- Mục tiêu: chia sẻ kiến thức lập trình mạng
- Các khóa học hoàn thành về Java & JavaScript
- Kỹ năng: Socket, HTTP, WebSocket, Multithreading, Async/Await, etc.

**10 Bài Viết (Tiếng Việt):**
1. Nhập Môn Lập Trình Mạng với Java - Socket Programming
2. Xây Dựng Server HTTP Đơn Giản Với Java
3. Java Network Interface: Quản Lý Kết Nối Mạng
4. UDP Programming trong Java - Giao Tiếp Không Liên Kết
5. Java Multithreading trong Network Server
6. JavaScript Fetch API - Giao Tiếp HTTP Đơn Giản
7. Async/Await trong JavaScript - Xử Lý Yêu Cầu Mạng
8. WebSocket với JavaScript - Giao Tiếp Real-time
9. XMLHttpRequest vs Fetch - So Sánh Và Lựa Chọn
10. Xây Dựng REST API Client Với JavaScript

#### 🎨 Trình Bày: Đẹp & Tối Giản
- Design minimalist, professional
- Color scheme: Clean, modern
- Responsive design cho mobile & desktop
- Typography clear, dễ đọc
- Navigation intuitive

#### 💻 Kỹ Thuật

**Backend:**
- Flask Framework (Python)
- Routes: /, /blog, /blog/<id>, /about, /contact

**Frontend:**
- HTML5 semantic markup
- CSS3 responsive design
- Vanilla JavaScript (no jQuery dependency)
- Font Awesome icons

**Version Control:**
- Git & GitHub Repository
- Commit history lưu trữ quá trình phát triển

---

## Cấu Trúc Thư Mục

```
project/
├── app.py                 # Flask application & blog data
├── requirements.txt       # Python dependencies
├── README.md             # Tài liệu dự án
├── index.html            # Trang chủ (extends base.html)
├── static/
│   ├── assets/
│   │   ├── images/
│   │   │   ├── avt.jpg   # Avatar
│   │   │   ├── logo.jpg  # Logo
│   │   │   └── blog_thumbnails/  # Ảnh bài viết
│   ├── css/
│   │   └── style.css     # Stylesheet chính
│   └── js/
│       └── script.js     # JavaScript client-side
└── templates/
    ├── base.html         # Base template (header, footer, navigation)
    ├── index.html        # Trang chủ
    ├── blog.html         # Danh sách blog posts
    ├── post-detail.html  # Chi tiết bài viết
    ├── about.html        # Trang thông tin cá nhân
    └── contact.html      # Trang liên hệ
```

---

## Hướng Dẫn Cài Đặt & Chạy

### 1. Clone Repository
```bash
git clone https://github.com/QuocTrung21/Laptrinhweb.git
cd Laptrinhweb
```

### 2. Cài Đặt Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Chạy Flask Application
```bash
python app.py
```

### 4. Mở Trình Duyệt
```
http://127.0.0.1:5000
```

---

## Nội Dung Bài Viết

### Java (5 bài viết)
1. **Socket Programming Basics** - Khái niệm Socket, ServerSocket, ClientSocket
2. **HTTP Server** - Xây dựng web server từ đầu, xử lý request/response
3. **Network Interface** - Lấy thông tin mạng, IP address, MAC address
4. **UDP Programming** - DatagramSocket, giao tiếp không liên kết, ứng dụng thời gian thực
5. **Multithreading** - Xử lý nhiều client đồng thời, Thread pools

### JavaScript (5 bài viết)
1. **Fetch API** - Gửi HTTP request, xử lý response, JSON parsing
2. **Async/Await** - Xử lý Promise, callback, error handling
3. **WebSocket** - Kết nối hai chiều, real-time communication
4. **XMLHttpRequest vs Fetch** - So sánh, lịch sử, best practices
5. **REST API Client** - Gọi API, authentication, error handling

---

## Công Nghệ Sử Dụng

| Lĩnh Vực | Công Nghệ |
|---------|-----------|
| **Backend** | Flask (Python 3.8+) |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Version Control** | Git & GitHub |
| **Icons** | Font Awesome 6.4.0 |
| **Design** | Responsive, Mobile-first |

---

## Tiêu Chuẩn Code

- ✅ Clean code principles
- ✅ Semantic HTML5
- ✅ CSS BEM methodology
- ✅ Responsive design (Mobile first)
- ✅ Accessibility (WCAG)
- ✅ Git commit history clean & meaningful

---

## Tính Năng Chính

✅ **Home Page**
- Hero section với CTA buttons
- Featured posts (3 bài viết nổi bật)
- Skills showcase
- Social media links

✅ **Blog Page**
- Danh sách tất cả bài viết
- Filter theo category (Java, JavaScript)
- Search functionality
- Pagination

✅ **Post Detail Page**
- Nội dung bài viết đầy đủ
- Related posts suggestions
- Meta information (date, category, author)

✅ **About Page**
- Profile cá nhân
- Certifications & achievements
- Detailed skills by category
- CV download links

✅ **Contact Page**
- Contact form
- Social media links
- Direct contact information

---

## Liên Hệ & Thông Tin

**Tác Giả:** Nguyễn Quốc Trung  
**Email:** quoctrung@email.com  
**GitHub Repository:** https://github.com/QuocTrung21/Laptrinhweb  
**GitHub:** https://github.com/QuocTrung21

---

**Ngày Hoàn Thành:** Tháng 12, 2024  
**Phiên Bản:** 1.0
