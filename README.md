# Chiluveri Chethan Kumar - Portfolio Website

A modern, responsive portfolio website built with Django and TailwindCSS.

## Features

- **Responsive Design**: Mobile-first approach with smooth animations
- **Contact Form**: Integrated email functionality with SMTP
- **Modern UI**: Clean design with hover effects and transitions
- **SEO Optimized**: Meta tags and Open Graph integration
- **Database Integration**: Contact messages stored in Django models
- **Admin Panel**: Django admin for managing contact messages

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Email Settings
Edit `portfolio_site/settings.py` and update the email configuration:

```python
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'  # Use App Password for Gmail
```

### 3. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 5. Run Development Server
```bash
python manage.py runserver
```

### 6. Access the Website
- Portfolio: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/

## Email Configuration for Gmail

1. Enable 2-Factor Authentication on your Gmail account
2. Generate an App Password:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate a password for "Mail"
3. Use this App Password in the `EMAIL_HOST_PASSWORD` setting

## Customization

### Adding Your Resume
1. Add your resume PDF to `static/files/resume.pdf`
2. Update the resume link in the navigation

### Adding Your Photo
1. Add your photo to `static/images/profile.jpg`
2. Update the image reference in the About section

### Updating Content
All content is managed through the Django views in `portfolio/views.py`. Update the context dictionary with your information.

## Deployment

### For Production:
1. Set `DEBUG = False` in settings.py
2. Add your domain to `ALLOWED_HOSTS`
3. Configure static files serving
4. Set up proper email credentials
5. Use environment variables for sensitive data

## Technologies Used

- **Backend**: Django 4.2+
- **Frontend**: HTML5, TailwindCSS, JavaScript
- **Database**: SQLite (development) / PostgreSQL (production)
- **Icons**: Font Awesome
- **Animations**: AOS (Animate On Scroll)
- **Fonts**: Google Fonts (Inter)

## Contact Form Features

- CSRF protection
- AJAX submission
- Email notifications
- Database storage
- Success/error alerts
- Form validation

## Admin Features

- View all contact messages
- Mark messages as read/unread
- Search and filter functionality
- Responsive admin interface

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## License

This project is open source and available under the MIT License.