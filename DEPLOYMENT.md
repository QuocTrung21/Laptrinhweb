# HƯỚNG DẪN TRIỂN KHAI (DEPLOYMENT)

## Các Tùy Chọn Triển Khai

### 1. **Heroku** (Recommended - Hỗ trợ Flask)

#### Ưu điểm:
- ✅ Miễn phí (có quota)
- ✅ Hỗ trợ Python Flask
- ✅ Dễ deploy
- ✅ Tự động scale

#### Bước Triển Khai:

**Bước 1: Cài Heroku CLI**
```bash
# Windows: Download từ https://devcenter.heroku.com/articles/heroku-cli
# Hoặc dùng choco:
choco install heroku-cli

# macOS:
brew tap heroku/brew && brew install heroku

# Linux:
curl https://cli-assets.heroku.com/install.sh | sh
```

**Bước 2: Login Heroku**
```bash
heroku login
```

**Bước 3: Chuẩn Bị Project**

Tạo `Procfile` (trong thư mục gốc):
```
web: python app.py
```

Cập nhật `app.py` để chạy trên port từ environment:
```python
if __name__ == '__main__':
    port = os.getenv('PORT', 5000)
    app.run(host='0.0.0.0', port=int(port), debug=False)
```

**Bước 4: Git Setup**
```bash
git init
git add .
git commit -m "Initial commit - Network Programming Blog"
```

**Bước 5: Tạo Heroku App**
```bash
heroku create your-app-name
```

**Bước 6: Deploy**
```bash
git push heroku main
```

**Bước 7: Kiểm Tra**
```bash
heroku logs --tail
heroku open
```

---

### 2. **PythonAnywhere** (Beginner-Friendly)

#### Ưu điểm:
- ✅ Không cần CLI
- ✅ Web interface user-friendly
- ✅ Miễn phí (limited)
- ✅ Support tốt

#### Bước Triển Khai:

1. **Đăng ký:** https://www.pythonanywhere.com
2. **Upload files:**
   - Vào `Files` tab
   - Upload project hoặc clone từ GitHub
3. **Setup Web App:**
   - Vào `Web` tab
   - Click "Add a new web app"
   - Chọn Python version (3.9+)
   - Chọn Flask
4. **Configure:**
   - Set WSGI configuration file
   - Point đến `app.py`
5. **Reload:** Click "Reload"

---

### 3. **Railway.app** (Modern Alternative)

#### Setup:
```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Init & Deploy
railway init
railway up
```

---

### 4. **GitHub Pages + Static Site Generator (HUGO/Publii)**

#### Nếu muốn dùng GitHub Pages (tĩnh):

**HUGO Setup:**
```bash
# Cài Hugo
choco install hugo  # Windows
brew install hugo   # macOS

# Tạo site
hugo new site blog
cd blog
git init
git add .
git commit -m "Initial Hugo site"
```

**Deploy:**
- Push lên GitHub
- Enable GitHub Pages trong Settings
- Chọn `gh-pages` branch

---

## Environment Variables

Tạo file `.env` (không commit lên GitHub):
```
FLASK_ENV=production
SECRET_KEY=your-production-secret-key
DEBUG=False
```

Cập nhật `app.py`:
```python
from dotenv import load_dotenv
import os

load_dotenv()

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key')
app.config['DEBUG'] = os.getenv('DEBUG', False)
```

---

## Domain Custom

### Heroku
```bash
heroku domains:add yourdomain.com
```

Cập nhật DNS records tại registrar

### PythonAnywhere
Vào "Web" tab, set custom domain

---

## SSL/HTTPS

### Heroku
- ✅ Automatic SSL (free)

### PythonAnywhere
- ✅ Free HTTPS included

### Custom Domain
- Sử dụng Let's Encrypt (free)
- Hoặc CloudFlare (free, setup mudah)

---

## CI/CD Setup (GitHub Actions)

Tạo `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Heroku

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Deploy to Heroku
      uses: akhileshns/heroku-deploy@v3.12.12
      with:
        heroku_api_key: ${{ secrets.HEROKU_API_KEY }}
        heroku_app_name: "your-app-name"
        heroku_email: "your-email@example.com"
```

Thêm secrets vào GitHub (Settings > Secrets)

---

## Monitoring & Maintenance

### Logs
```bash
# Heroku
heroku logs --tail

# PythonAnywhere
Vào "Web" tab, xem logs
```

### Database Backup
```bash
# Heroku
heroku pg:backups:capture
heroku pg:backups:download
```

### Updates
```bash
# Cập nhật dependencies
pip install --upgrade -r requirements.txt
pip freeze > requirements.txt
git add . && git commit -m "Update dependencies"
git push heroku main
```

---

## Performance Optimization

### Caching
```python
@app.after_request
def set_cache_headers(response):
    if request.path.startswith('/static/'):
        response.headers['Cache-Control'] = 'public, max-age=31536000'
    else:
        response.headers['Cache-Control'] = 'public, max-age=3600'
    return response
```

### Compression
```bash
pip install flask-compress
```

```python
from flask_compress import Compress
Compress(app)
```

### CDN (Cloudflare)
- Đăng ký Cloudflare
- Update nameservers
- Enable caching rules

---

## Troubleshooting

### Lỗi Port
```
Address already in use
→ app.run(port=5001)
```

### Module Not Found
```
ModuleNotFoundError: No module named 'flask'
→ pip install -r requirements.txt
```

### Permission Denied
```
Permission denied: 'app.py'
→ chmod +x app.py
```

### Heroku Build Failed
```
→ Kiểm tra Procfile
→ Kiểm tra requirements.txt
→ heroku logs --tail
```

---

## Checklist Pre-Deployment

- [ ] Test locally: `python app.py`
- [ ] Tất cả links hoạt động
- [ ] Ảnh load đúng
- [ ] Responsive design tested
- [ ] No console errors (DevTools)
- [ ] `.env` file created (không push)
- [ ] Git initialized & commits clean
- [ ] requirements.txt updated
- [ ] Procfile created (nếu Heroku)
- [ ] SECRET_KEY không hard-coded
- [ ] DEBUG = False cho production
- [ ] Custom domain DNS configured (nếu cần)

---

## Post-Deployment

- ✅ Test live site
- ✅ Setup monitoring (Sentry, New Relic, etc.)
- ✅ Setup logging
- ✅ Backup strategy
- ✅ Security headers
- ✅ Performance audit (Lighthouse)
- ✅ SEO check
- ✅ Mobile test

---

## Monitoring Tools

### Free Options
- **Uptime:** Uptime Robot (free)
- **Analytics:** Google Analytics
- **Errors:** Sentry (free tier)
- **Performance:** Lighthouse

### Setup

**Sentry (Error Tracking):**
```bash
pip install sentry-sdk
```

```python
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="your-sentry-dsn",
    integrations=[FlaskIntegration()]
)
```

**Google Analytics:**
```html
<!-- templates/base.html -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_ID');
</script>
```

---

## Rollback Deployment

### Heroku
```bash
heroku releases
heroku rollback
```

### Git
```bash
git revert <commit-hash>
git push heroku main
```

---

## Backup & Recovery

### Code
```bash
# Clone repository trước deploy
git clone <repo-url> backup/
```

### Database
```bash
# Nếu dùng PostgreSQL
heroku pg:backups:capture
heroku pg:backups:download
```

---

## Updates & Maintenance Schedule

Khuyến nghị:
- 🔄 Weekly: Review logs
- 🔄 Monthly: Update dependencies
- 🔄 Monthly: Backup database
- 🔄 Quarterly: Security audit
- 🔄 Yearly: Performance review

---

## Liên Hệ & Support

- **Heroku Support:** https://help.heroku.com
- **PythonAnywhere Support:** https://www.pythonanywhere.com/help
- **Flask Docs:** https://flask.palletsprojects.com
- **GitHub Help:** https://docs.github.com

---

**Cập nhật lần cuối:** Tháng 12, 2024
