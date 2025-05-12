from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Your data
portfolio_data = {
    "name": "Navyatej Tummala",
    "title": "Graduate Student in Computer Science",
    "location": "Raleigh, NC",
    "email": "ntummal3@ncsu.edu",
    "linkedin": "www.linkedin.com/in/navyatej-tummala",
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
    # Here you would typically handle the contact form submission
    # For now, we'll just redirect back to the home page
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True) 