import streamlit as st

st.set_page_config(
    page_title="AI Learning Path Generator",
    page_icon="🎓",
    layout="centered",
)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #f3f8ff 0%, #ffffff 45%, #eef7f3 100%);
    }
    .hero {
        background: linear-gradient(135deg, #2563eb 0%, #0ea5e9 100%);
        color: white;
        padding: 1.6rem 1.4rem;
        border-radius: 18px;
        margin-bottom: 1.2rem;
        box-shadow: 0 10px 24px rgba(37, 99, 235, 0.18);
    }
    .hero h1 {
        margin: 0 0 0.35rem 0;
        font-size: 2rem;
    }
    .hero p {
        margin: 0;
        opacity: 0.95;
    }
    .step-card {
        background: white;
        border: 1px solid #dbeafe;
        border-left: 6px solid #2563eb;
        border-radius: 12px;
        padding: 0.9rem 1rem;
        margin-bottom: 0.7rem;
    }
    .project-card {
        background: #ecfdf5;
        border: 1px solid #a7f3d0;
        border-left: 6px solid #059669;
        border-radius: 12px;
        padding: 1rem;
        margin-top: 0.4rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

LEARNING_PATHS = {
    "python": {
        "title": "Python",
        "steps": [
            ("Python Basics", "Install Python, learn how programs run, and practice print statements."),
            ("Variables and Data Types", "Store values using strings, numbers, lists, and dictionaries."),
            ("Conditions", "Use if/else so your program can make decisions."),
            ("Loops", "Repeat tasks with for and while loops."),
            ("Functions", "Write reusable blocks of code to keep programs organized."),
            ("Object-Oriented Programming", "Create classes and objects to model real-world ideas."),
            ("Error Handling and Files", "Handle mistakes safely and read or write simple files."),
        ],
        "project": "Build a Student Grade Calculator that takes marks as input and prints the average and grade.",
    },
    "javascript": {
        "title": "JavaScript",
        "steps": [
            ("JavaScript Basics", "Learn how JavaScript runs in the browser and write your first scripts."),
            ("Variables and Data Types", "Work with let, const, strings, numbers, arrays, and objects."),
            ("Conditions", "Use if/else and comparison operators to control program flow."),
            ("Loops", "Repeat actions with for, while, and array methods."),
            ("Functions", "Create functions and arrow functions to reuse logic."),
            ("DOM Basics", "Select HTML elements and update a webpage with JavaScript."),
            ("Events", "Respond to clicks, typing, and other user actions."),
        ],
        "project": "Build a To-Do List webpage where users can add, complete, and delete tasks.",
    },
    "html": {
        "title": "HTML",
        "steps": [
            ("HTML Basics", "Learn tags, elements, and how a webpage is structured."),
            ("Text and Links", "Add headings, paragraphs, lists, and hyperlinks."),
            ("Images and Media", "Display pictures and simple media on a page."),
            ("Tables and Forms", "Collect user input with forms, buttons, and tables."),
            ("Semantic HTML", "Use meaningful tags like header, main, and footer."),
            ("Page Layout", "Combine sections to create a complete webpage."),
            ("Accessibility Basics", "Write HTML that is easier for everyone to use."),
        ],
        "project": "Create a personal profile webpage with your photo, bio, skills, and contact form.",
    },
    "css": {
        "title": "CSS",
        "steps": [
            ("CSS Basics", "Connect CSS to HTML and change colors, fonts, and spacing."),
            ("Selectors", "Target the right elements with class, id, and tag selectors."),
            ("Box Model", "Understand margin, padding, border, and element size."),
            ("Flexbox", "Align items in rows and columns with Flexbox."),
            ("Responsive Design", "Make pages look good on phones and computers."),
            ("Colors and Typography", "Choose readable fonts and pleasant color combinations."),
            ("Simple Animations", "Add hover effects and small transitions."),
        ],
        "project": "Style a landing page for a study club with a navbar, hero section, and cards.",
    },
    "java": {
        "title": "Java",
        "steps": [
            ("Java Basics", "Set up Java and write a Hello World program."),
            ("Variables and Data Types", "Learn integers, strings, booleans, and arrays."),
            ("Conditions", "Use if/else and switch to make decisions."),
            ("Loops", "Practice for, while, and nested loops."),
            ("Methods", "Write methods that take input and return results."),
            ("Object-Oriented Programming", "Create classes, objects, constructors, and methods."),
            ("Collections Basics", "Store data with ArrayList and simple maps."),
        ],
        "project": "Build a Library Book Tracker that can add books, search titles, and show available copies.",
    },
    "web development": {
        "title": "Web Development",
        "steps": [
            ("Internet and Web Basics", "Learn how websites, browsers, and URLs work."),
            ("HTML", "Build the structure of a webpage."),
            ("CSS", "Style pages so they look clean and readable."),
            ("JavaScript", "Make pages interactive with clicks and forms."),
            ("Responsive Layouts", "Design pages that work on mobile and desktop."),
            ("Simple Hosting", "Put a website online using a beginner-friendly host."),
            ("Project Planning", "Break a website idea into pages, features, and steps."),
        ],
        "project": "Build a portfolio website with Home, About, Projects, and Contact pages.",
    },
    "data science": {
        "title": "Data Science",
        "steps": [
            ("Python for Data", "Learn Python basics needed for data work."),
            ("Working with Spreadsheets", "Understand tables, rows, columns, and clean data."),
            ("NumPy Basics", "Handle numbers and arrays efficiently."),
            ("Pandas Basics", "Load, filter, and summarize datasets."),
            ("Data Cleaning", "Fix missing values and messy text."),
            ("Visualization", "Create charts that explain your findings."),
            ("Simple Analysis", "Ask a question and answer it with data."),
        ],
        "project": "Analyze a student scores dataset and create charts showing average marks by subject.",
    },
}


def normalize_topic(topic: str) -> str:
    return " ".join(topic.strip().lower().split())


def generate_generic_path(topic: str) -> dict:
    clean_title = topic.strip().title()
    return {
        "title": clean_title,
        "steps": [
            (f"{clean_title} Basics", f"Learn what {clean_title} is and why people study it."),
            ("Core Concepts", f"Understand the most important ideas used in {clean_title}."),
            ("Tools and Setup", f"Install the basic tools needed to practice {clean_title}."),
            ("Hands-on Practice", f"Complete small exercises to apply what you learned."),
            ("Common Patterns", f"Study the usual ways beginners solve {clean_title} problems."),
            ("Build Small Skills", f"Combine concepts and start thinking like a {clean_title} learner."),
            ("Review and Improve", f"Revise weak areas and practice with slightly harder tasks."),
        ],
        "project": f"Create a beginner mini project that uses the main ideas of {clean_title} in a real example.",
    }


def get_learning_path(topic: str) -> dict:
    key = normalize_topic(topic)
    aliases = {
        "py": "python",
        "js": "javascript",
        "html5": "html",
        "css3": "css",
        "web": "web development",
        "web dev": "web development",
        "datascience": "data science",
    }
    key = aliases.get(key, key)
    return LEARNING_PATHS.get(key, generate_generic_path(topic))


st.markdown(
    """
    <div class="hero">
        <h1>🎓 AI Learning Path Generator</h1>
        <p>Enter a skill you want to learn and get a simple step-by-step roadmap.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("Perfect for students who want a clear starting plan without feeling overwhelmed.")

with st.form("learning_path_form", clear_on_submit=False):
    topic = st.text_input(
        "What do you want to learn?",
        placeholder="Example: Python, JavaScript, Web Development",
    )
    generate = st.form_submit_button(
        "Generate Learning Path",
        type="primary",
        use_container_width=True,
    )

if generate:
    if not topic.strip():
        st.warning("Please enter a skill or topic before generating a learning path.")
    else:
        path = get_learning_path(topic)
        st.success(f"Here is your learning path for **{path['title']}**.")
        st.subheader("Step-by-step roadmap")

        for index, (name, description) in enumerate(path["steps"], start=1):
            st.markdown(
                f"""
                <div class="step-card">
                    <strong>{index}. {name}</strong>
                    <div>{description}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            f"""
            <div class="project-card">
                <strong>Mini Project</strong>
                <div>{path['project']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.caption("Tip: Try topics like Python, Java, HTML, CSS, JavaScript, or Data Science.")
