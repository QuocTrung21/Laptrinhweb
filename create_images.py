"""
Generate placeholder images for blog posts
"""

import os

try:
    from PIL import Image, ImageDraw, ImageFont
except Exception as e:
    raise RuntimeError(
        "Pillow is required to run this script. Install with: python -m pip install Pillow"
    ) from e

# Tạo thư mục nếu chưa tồn tại
os.makedirs('static/assets/images/blog_thumbnails', exist_ok=True)

# Màu sắc cho các loại bài viết
colors = {
    'java_basic_1': '#F39C12',
    'java_oop': '#E74C3C',
    'java_collections': '#C0392B',
    'java_stream': '#D35400',
    'java_patterns': '#A93226',
    'js_es6': '#9B59B6',
    'js_async': '#8E44AD',
    'js_dom': '#6C3483',
    'react_hooks': '#3498DB',
    'css_layout': '#1ABC9C'
}

# Tiêu đề cho mỗi ảnh
titles = {
    'java_basic_1': 'Java\nCơ Bản',
    'java_oop': 'Java\nOOP',
    'java_collections': 'Java\nCollections',
    'java_stream': 'Java\nStream API',
    'java_patterns': 'Design\nPatterns',
    'js_es6': 'JavaScript\nES6+',
    'js_async': 'Async/\nAwait',
    'js_dom': 'DOM\nManipulation',
    'react_hooks': 'React\nHooks',
    'css_layout': 'CSS\nLayout'
}

def create_placeholder_image(filename, color, title):
    """Tạo ảnh placeholder với màu và text"""
    # Kích thước ảnh
    width, height = 600, 400
    
    # Tạo ảnh
    image = Image.new('RGB', (width, height), color)
    draw = ImageDraw.Draw(image)
    
    # Thêm text (sử dụng font mặc định)
    text = title
    text_color = 'white'

    # Sử dụng font mặc định (portable)
    try:
        font = ImageFont.load_default()
    except Exception:
        font = None

    # Tính kích thước text (hỗ trợ multiline)
    try:
        bbox = draw.multiline_textbbox((0, 0), text, font=font, spacing=6)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
    except AttributeError:
        # Fallback cho Pillow cũ: dùng textsize / multiline_textsize
        try:
            text_width, text_height = draw.multiline_textsize(text, font=font)
        except Exception:
            text_width, text_height = draw.textsize(text, font=font)

    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # Vẽ multiline text căn giữa
    try:
        draw.multiline_text((x, y), text, fill=text_color, font=font, align='center', spacing=6)
    except Exception:
        draw.text((x, y), text, fill=text_color, font=font)
    
    # Lưu ảnh
    image.save(f'static/assets/images/blog_thumbnails/{filename}.jpg', 'JPEG', quality=85)
    print(f'Created: {filename}.jpg')

# Tạo tất cả các ảnh placeholder
for filename, color in colors.items():
    title = titles.get(filename, filename)
    create_placeholder_image(filename, color, title)

print('✅ Tất cả ảnh placeholder đã được tạo!')
