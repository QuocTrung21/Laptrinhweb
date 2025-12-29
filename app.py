"""
Personal Blog Application - Nguyễn Quốc Trung
Framework: Flask
Author: Nguyễn Quốc Trung
Description: A minimalist, professional personal blog website
"""

from flask import Flask, render_template, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Sample blog posts data
BLOG_POSTS = [
    {
        'id': 1,
        'title': 'Nhập Môn Lập Trình Mạng với Java - Socket Programming',
        'description': 'Tìm hiểu cơ bản về Socket trong Java, cách tạo kết nối TCP/IP giữa client và server.',
        'image': '/static/assets/images/blog_thumbnails/java_socket.jpg',
        'date': '2024-12-20',
        'category': 'Java',
        'content': 'Socket là nền tảng của lập trình mạng...'
    },
    {
        'id': 2,
        'title': 'Xây Dựng Server HTTP Đơn Giản Với Java',
        'description': 'Hướng dẫn từng bước xây dựng một web server HTTP đơn giản bằng Java từ đầu.',
        'image': '/static/assets/images/blog_thumbnails/java_server.jpg',
        'date': '2024-12-18',
        'category': 'Java',
        'content': 'Để hiểu HTTP server hoạt động như thế nào...'
    },
    {
        'id': 3,
        'title': 'Java Network Interface: Quản Lý Kết Nối Mạng',
        'description': 'Tìm hiểu cách sử dụng Java NetworkInterface để truy cập thông tin mạng của hệ thống.',
        'image': '/static/assets/images/blog_thumbnails/java_network.jpg',
        'date': '2024-12-15',
        'category': 'Java',
        'content': 'NetworkInterface cung cấp thông tin...'
    },
    {
        'id': 4,
        'title': 'UDP Programming trong Java - Giao Tiếp Không Liên Kết',
        'description': 'Khám phá lập trình UDP trong Java, sử dụng DatagramSocket cho các ứng dụng thời gian thực.',
        'image': '/static/assets/images/blog_thumbnails/java_udp.jpg',
        'date': '2024-12-12',
        'category': 'Java',
        'content': 'UDP là giao thức không liên kết...'
    },
    {
        'id': 5,
        'title': 'Java Multithreading trong Network Server',
        'description': 'Hướng dẫn sử dụng Multithreading để xử lý nhiều client đồng thời trong server ứng dụng.',
        'image': '/static/assets/images/blog_thumbnails/java_threading.jpg',
        'date': '2024-12-10',
        'category': 'Java',
        'content': 'Multithreading cho phép server...'
    },
    {
        'id': 6,
        'title': 'JavaScript Fetch API - Giao Tiếp HTTP Đơn Giản',
        'description': 'Học cách sử dụng Fetch API để gửi yêu cầu HTTP từ trình duyệt tới server một cách hiệu quả.',
        'image': '/static/assets/images/blog_thumbnails/js_fetch.jpg',
        'date': '2024-12-08',
        'category': 'JavaScript',
        'content': 'Fetch API là phương thức hiện đại...'
    },
    {
        'id': 7,
        'title': 'Async/Await trong JavaScript - Xử Lý Yêu Cầu Mạng',
        'description': 'Nắm vững async/await để xử lý các tác vụ bất đồng bộ trong ứng dụng web hiệu quả.',
        'image': '/static/assets/images/blog_thumbnails/js_async.jpg',
        'date': '2024-12-05',
        'category': 'JavaScript',
        'content': 'Async/await giúp viết code...'
    },
    {
        'id': 8,
        'title': 'WebSocket với JavaScript - Giao Tiếp Real-time',
        'description': 'Khám phá WebSocket API để xây dựng ứng dụng giao tiếp thời gian thực giữa client và server.',
        'image': '/static/assets/images/blog_thumbnails/js_websocket.jpg',
        'date': '2024-12-02',
        'category': 'JavaScript',
        'content': 'WebSocket cung cấp kết nối...'
    },
    {
        'id': 9,
        'title': 'XMLHttpRequest vs Fetch - So Sánh Và Lựa Chọn',
        'description': 'So sánh chi tiết giữa XMLHttpRequest cũ và Fetch API mới để hiểu cách tiến hóa của lập trình mạng web.',
        'image': '/static/assets/images/blog_thumbnails/js_xhr.jpg',
        'date': '2024-11-28',
        'category': 'JavaScript',
        'content': 'XMLHttpRequest từng là...'
    },
    {
        'id': 10,
        'title': 'Xây Dựng REST API Client Với JavaScript',
        'description': 'Hướng dẫn tạo client gọi REST API, xử lý response, error handling và authentication.',
        'image': '/static/assets/images/blog_thumbnails/js_rest.jpg',
        'date': '2024-11-25',
        'category': 'JavaScript',
        'content': 'REST API client là thành phần...'
    }
]

# Certificate/Achievement data
CERTIFICATIONS = [
    {
        'year': '2024',
        'title': 'Networking Basics',
        'issuer': 'Cisco Networking Academy',
        'description': 'Nắm vững các khái niệm cơ bản về mạng, kiến trúc mạng, và các giao thức'
    },
    {
        'year': '2024',
        'title': 'Java Socket Programming',
        'issuer': 'Udemy',
        'description': 'Lập trình mạng với Socket, TCP/UDP, xây dựng Client-Server ứng dụng'
    },
    {
        'year': '2024',
        'title': 'JavaScript ES6+ Essentials',
        'issuer': 'Cisco Networking Academy',
        'description': 'Hiểu sâu về JavaScript ES6+, Arrow Functions, Destructuring, Modules'
    },
    {
        'year': '2024',
        'title': 'Java Multithreading & Concurrency',
        'issuer': 'Udemy',
        'description': 'Lập trình đa luồng trong Java, xử lý nhiều client đồng thời'
    },
    {
        'year': '2024',
        'title': 'Async/Await và Promises trong JavaScript',
        'issuer': 'Coursera',
        'description': 'Xử lý bất đồng bộ trong JavaScript, lập trình hàm, callback handling'
    },
    {
        'year': '2024',
        'title': 'HTTP Protocol & Web Communication',
        'issuer': 'Cisco Networking Academy',
        'description': 'Hiểu chi tiết giao thức HTTP, Request-Response, Web Server'
    },
    {
        'year': '2024',
        'title': 'REST API Development',
        'issuer': 'Udemy',
        'description': 'Thiết kế và xây dựng REST API, Client-Server Communication'
    },
    {
        'year': '2023',
        'title': 'WebSocket & Real-time Communication',
        'issuer': 'Online Course',
        'description': 'Giao tiếp thời gian thực với WebSocket, Full-duplex communication'
    }
]


@app.route('/')
def index():
    """Home page route"""
    return render_template('index.html')


@app.route('/blog')
def blog():
    """Blog page with list of articles"""
    return render_template('blog.html', posts=BLOG_POSTS)


@app.route('/blog/<int:post_id>')
def blog_detail(post_id):
    """Detailed view of a blog post"""
    # Find the post by ID
    post = next((p for p in BLOG_POSTS if p['id'] == post_id), None)
    
    if not post:
        return render_template('404.html'), 404
    
    # Get related posts (same category, different post)
    related_posts = [p for p in BLOG_POSTS if p['category'] == post['category'] and p['id'] != post_id][:3]
    
    return render_template('post-detail.html', post=post, related_posts=related_posts)


@app.route('/about')
def about():
    """About page with CV and certifications"""
    return render_template('about.html', certifications=CERTIFICATIONS)


@app.route('/contact')
def contact():
    """Contact page with form"""
    return render_template('contact.html')


@app.route('/api/send-message', methods=['POST'])
def send_message():
    """API endpoint to handle contact form submission"""
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        
        # Validate data
        if not all([name, email, subject, message]):
            return jsonify({'success': False, 'error': 'Vui lòng điền đầy đủ thông tin'}), 400
        
        # In a real application, you would save this to a database or send an email
        # For now, we'll just return success
        print(f"New message from {name} ({email}): {message}")
        
        return jsonify({
            'success': True,
            'message': 'Tin nhắn đã được gửi thành công! Cảm ơn bạn đã liên hệ.'
        }), 200
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/blog/<int:post_id>')
def get_blog_post(post_id):
    """API endpoint to get a specific blog post"""
    post = next((p for p in BLOG_POSTS if p['id'] == post_id), None)
    if post:
        return jsonify(post)
    return jsonify({'error': 'Post not found'}), 404


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
