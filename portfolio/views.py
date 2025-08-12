from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ContactMessage
import logging

logger = logging.getLogger(__name__)

def home(request):
    """Main portfolio page with all sections"""
    context = {
        'personal_info': {
            'name': 'Chiluveri Chethankumar',
            'title': 'Software Engineer | Full-Stack Developer | AI/ML Specialist',
            'tagline': 'Dynamic engineer delivering innovative, data-driven solutions with Python, Django, React Native, AWS, and Google Cloud Storage. Builds secure, scalable platforms: SaaS CRMs, blockchain voting systems, and e-commerce apps. Optimizes workflows, achieving 15% cost savings via AI analytics. Creates user-focused AI chatbots and data dashboards with an Agile approach. Transform your vision connecat chiluverichethankumar@gmail.com or connect Get In Touch as bellow button',
            'phone': '+91 91824 19079',
            'email': 'chethankumarchiluveri@gmail.com',
            'linkedin': 'https://linkedin.com/in/chiluverichethankumar',
            'portfolio': 'https://chiluveri.netlify.app'
        },
        'skills': {
            'technical': [
                'Python', 'Java', 'SQL', 'R', 'JavaScript', 'HTML', 'CSS', 
                'React', 'Node.js', 'Flask', 'Django', 'React Native', 
                'Google Cloud Storage', 'AWS', 'Azure', 'Git', 'API Development', 
                'SMTP Integration', 'PHP', 'Tomcat'
            ],
            'data_science': [
                'Supervised/Unsupervised Learning', 'Feature Extraction', 'EDA', 
                'Statistical Modeling', 'Regression', 'Classification', 
                'Random Forest', 'Model Optimization'
            ],
            'frameworks': [
                'Agile', 'Scrum', 'CI/CD', 'Design Thinking'
            ],
            'soft_skills': [
                'Problem-Solving', 'Communication', 'Teamwork', 
                'Adaptability', 'Detail-Oriented', 'Self-Motivated'
            ]
        },
        'experience': [
            {
                'title': 'Software Engineer',
                'company': 'Zometric, Bengaluru',
                'period': 'May 2025 – Present',
                'responsibilities': [
                    'Developed a B2B SaaS CRM using Django (multi-tenant) and a React Native Android app with Google Cloud Storage for secure file uploads.',
                    'Implemented AI-powered task scoping and call transcription, enhancing user productivity.',
                    'Built project, sales, and finance modules with real-time sync and invoicing, streamlining workflows.',
                    'Deployed on Google Cloud Platform with CI/CD, ensuring scalability and data privacy.'
                ]
            },
            {
                'title': 'Trainee Decision Scientist',
                'company': 'MuSigma, Bengaluru',
                'period': 'July 2024 – October 2024',
                'responsibilities': [
                    'Analyzed fuel consumption data using Python and SQL, optimizing energy strategies and reducing costs by 15%.',
                    'Developed Random Forest models to analyze terabytes of manufacturing data, improving efficiency by 10%.',
                    'Created interactive dashboards using JavaScript and React for real-time stakeholder insights.',
                    'Designed APIs for seamless data integration across applications.'
                ]
            }
        ],
        'education': [
            {
                'degree': 'B.Tech. in CSE',
                'institution': 'GITAM, Hyderabad',
                'year': '2024',
                'cgpa': '8.47'
            },
            {
                'degree': 'Senior Secondary (MPC)',
                'institution': 'Narayana Junior College, Hyderabad',
                'year': '2020',
                'cgpa': '8.1'
            },
            {
                'degree': 'Secondary (High School)',
                'institution': 'Viswa Bharathi High School, Gadwal, Jogulamba Gadwal',
                'year': '2018',
                'cgpa': '8.3'
            }
        ],
        'projects': [
            {
                'title': 'Smart AI-Powered Chatbot (Adib.AI)',
                'description': 'Built a chatbot handling coding queries, math expressions, and tech FAQs with a stylish, responsive UI.',
                'tech_stack': ['Flask', 'Python', 'SMTP', 'Render'],
                'details': 'Integrated SMTP feedback, custom FAQ logic, and social links, enhancing user interaction and engagement. Deployed on Render, showcasing end-to-end development from frontend design to backend logic.',
                'url': 'https://adib-ai-0-1-1.onrender.com/'  # Example URL
            },
            {
                'title': 'Session Management System',
                'description': 'Developed a session management system to enhance user authentication and tracking on e-commerce websites.',
                'tech_stack': ['HTML', 'CSS', 'JavaScript', 'PHP', 'Tomcat'],
                'details': 'Designed a system to improve login security and user experience. Implemented secure protocols, improving login security and user experience. Enhanced tracking on e-commerce platforms.',
                'url': 'https://github.com/Chiluverichethankumar/Chiluverichethankumar-MinProject-on-E-Commerce-website.git'  # No URL provided
            },
            {
                'title': 'Online Voting System Using Blockchain',
                'description': 'Developed a robust voting system integrating SHA-256 encryption to safeguard against cyber threats.',
                'tech_stack': ['Blockchain', 'Web Development', 'HTML', 'CSS', 'JavaScript', 'SQL', 'Django'],
                'details': 'Implemented voter authentication via face recognition and OTP verification, ensuring high security and data integrity. Designed a secure voter registration platform with encrypted data storage and seamless database management.',
                'url': 'https://github.com/Chiluverichethankumar/Major-project-online-voting-System-using-Blockchain-.git'  # Example GitHub URL
            },
            {
                'title': 'Password Generator Application',
                'description': 'Created a tool using Java and OOP principles to generate secure, random passwords.',
                'tech_stack': ['Java', 'OOP'],
                'details': 'Incorporated diverse character sets and adhered to security best practices for robust password generation.',
                'url': 'https://github.com/Chiluverichethankumar/Projects-on-java.git'  # No URL provided
            },
            {
                'title': 'Web Scraping & Business Insights Analysis',
                'description': 'Used web scraping to extract and analyze financial data of India\'s largest companies.',
                'tech_stack': ['Python', 'BeautifulSoup', 'Pandas'],
                'details': 'Delivered business insights on industry-wise revenue, profit, and growth trends through data analysis.',
                'url': 'https://github.com/Chiluverichethankumar/Web-Scraping-of-India-s-Largest-Companies-for-Financial-Insights.git'  # Example GitHub URL
            }
        ],
        'certifications': [
            {'name': 'Data Analysis with Python', 'issuer': 'IBM'},
            {'name': 'Data Visualization with Python', 'issuer': 'IBM'},
            {'name': 'AWS Cloud Architecture', 'issuer': 'AWS'},
            {'name': 'AWS Cloud Foundations', 'issuer': 'AWS'},
            {'name': 'Full Stack Web Development', 'issuer': 'Edureka'}
        ]
    }
    return render(request, 'portfolio/home.html', context)

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if not name or not email or not message:
            return JsonResponse({'success': False, 'message': 'Please fill all fields.'})

        # Save the message to the database
        ContactMessage.objects.create(name=name, email=email, message=message)

        try:
            send_mail(
                subject=f'Contact form submission from {name}',
                message=f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
        except Exception as e:
            logger.error(f'Email sending failed: {e}')
            return JsonResponse({'success': False, 'message': 'Error sending message. Please try again.'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})