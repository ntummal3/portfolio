from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mail import Mail, Message
import json
import os
from dotenv import load_dotenv
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()  # Load environment variables

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', os.urandom(24))

# Mail settings
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD', '').replace(' ', ''),
    MAIL_DEFAULT_SENDER=os.getenv('MAIL_USERNAME')
)

mail = Mail(app)

# Your data
portfolio_data = {
    "name": "Navyatej Tummala",
    "title": "Graduate Student in Computer Science",
    "location": "Raleigh, NC",
    "email": "ntummal3@ncsu.edu",
    "linkedin": "www.linkedin.com/in/navyatej-tummala",
    "bio": "I am a passionate Computer Science graduate student at NC State University with a strong foundation in AI/ML, full-stack development, and cloud technologies. With hands-on experience in developing AI-powered applications and a track record of optimizing systems, I bring a blend of theoretical knowledge and practical expertise to solve complex technical challenges. Currently seeking opportunities to leverage my skills in innovative tech environments.",
    "education": [
        {
            "school": "North Carolina State University",
            "degree": "Master of Computer Science",
            "gpa": "3.95",
            "date": "Expected May 2026",
            "courses": "Design and Analysis of Algorithms, Software Engineering, Automated Learning and Data Analysis, Neural Networks and Deep Learning, Computer Networks, Object Oriented Design & Development, Internet Protocols"
        },
        {
            "school": "GITAM University, Vizag, India",
            "degree": "Bachelor of Technology in Computer Science and Engineering",
            "gpa": "8/10",
            "date": "Aug 2020 - May 2024"
        }
    ],
    "skills": {
        "languages": ["Python", "C/C++", "JavaScript(TypeScript, Nest.js)", "Java", "React Native"],
        "tools": ["Git", "GitLab", "Netconf", "Restconf", "GCP", "AWS", "Unix/Linux", "MySQL", "Docker", "Kubernetes", "CI/CD pipelines"],
        "cloud": ["AWS (EC2, S3, RDS, EKS, Redis, Lambda)"],
        "concepts": ["Computer Networks", "Machine Learning", "AWS", "OS", "System Development", "Object-Oriented Design", "SDN"],
        "ml": ["Pandas", "NumPy", "Pytorch", "Matplotlib", "OpenCV", "Flask", "MATLAB", "PowerBI"]
    },
    "experience": [
        {
            "title": "AI/ML Intern",
            "company": "Symbiosis Technologies, Vizag, India",
            "date": "May 2023 – July 2023",
            "achievements": [
                "Deployed a Python-based sentiment analysis system using Flask, cutting manual data-collection hours by 40%",
                "Utilized OpenCV in tandem with generative AI to capture and analyze image-based signals, improving project insights by 20%",
                "Leveraged MATLAB for predictive analytics to address public apprehensions, optimizing resolution speed by 25%"
            ]
        },
        {
            "title": "Student Researcher",
            "company": "GITAM University, Vizag, India",
            "date": "Aug 2023 – April 2024",
            "achievements": [
                "Employed Pandas and NumPy to preprocess thousands of daily financial news articles",
                "Harnessed PyTorch and Keras to design advanced NLP algorithms, boosting performance by 15%",
                "Built a Flask-based dashboard to visualize sentiment trends and trading signals"
            ]
        }
    ],
    "projects": [
        {
            "title": "Adaptive HireSmart Platform",
            "description": "AI-powered recruitment platform leveraging machine learning",
            "technologies": ["Python", "ReactJS", "Node.js", "PostgreSQL", "AWS"],
            "highlights": [
                "Developed an AI-powered recruitment platform as a college project",
                "Integrated real-time chat and video interview features",
                "Utilized Python for ML algorithms and AWS for deployment"
            ]
        },
        {
            "title": "Generative AI Based Drug Advisory Chatbot",
            "description": "Healthcare chatbot using advanced NLP",
            "technologies": ["Python", "PyTorch", "NLP", "Flask"],
            "highlights": [
                "Designed and developed a Gen AI powered chatbot for healthcare",
                "Implemented NLP techniques for precise pharmaceutical details",
                "Presented at ICSSCGE 2024 with praise for forward-thinking approach"
            ]
        },
        {
            "title": "Distributed Content Delivery Network",
            "description": "High-performance CDN implementation",
            "technologies": ["CDN", "Nginx", "AWS", "Kubernetes"],
            "highlights": [
                "Built a CDN for swift distribution of static content",
                "Employed Nginx for optimization and AWS for cloud hosting",
                "Achieved fault tolerance and seamless scalability with Kubernetes"
            ]
        }
    ]
}

@app.route('/')
def home():
    return render_template('index.html', data=portfolio_data)

@app.route('/contact', methods=['POST'])
def contact():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        logger.info(f"Attempting to send email from {email}")
        
        # Log mail configuration (without password)
        logger.info(f"Mail Configuration: SERVER={app.config['MAIL_SERVER']}, "
                   f"PORT={app.config['MAIL_PORT']}, "
                   f"USERNAME={app.config['MAIL_USERNAME']}")
        
        # Create message
        msg = Message('New Contact Form Submission',
                    sender=app.config['MAIL_USERNAME'],  # Use configured email as sender
                    reply_to=email,  # Set reply-to as the form submitter's email
                    recipients=[app.config['MAIL_USERNAME']])
        
        msg.body = f"""
        New message from your portfolio website:
        
        From: {name} <{email}>
        
        Message:
        {message}
        """
        
        # Send email
        mail.send(msg)
        logger.info("Email sent successfully")
        flash('Thank you for your message! I will get back to you soon.', 'success')
        
    except Exception as e:
        logger.error(f"Error sending email: {str(e)}")
        flash('Sorry, there was an error sending your message. Please try again later.', 'error')
    
    return redirect(url_for('home'))

@app.route('/health')
def health_check():
    """Health check endpoint for uptime monitoring"""
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True) 