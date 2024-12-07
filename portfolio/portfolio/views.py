from django.shortcuts import render
from . import models

def home(request):
    return render(request, 'home.html', { "navigation": "home" })

def projects(request):

    projects = [
        { 
            'title': 'type-racing-game',
            'description': 'TYPE-RACING ONLINE GAME is an engaging web-based multiplayer typing challenge where players compete against each other in real-time to type passages of text as quickly and accurately as possible.',
            'image': [
                'https://raw.githubusercontent.com/sheeshhhhhh/type-racing-game/main/frontend/public/appPhoto/DASHBOARD.jpg',
                'https://raw.githubusercontent.com/sheeshhhhhh/type-racing-game/main/frontend/public/appPhoto/HOME.jpg',
                'https://raw.githubusercontent.com/sheeshhhhhh/type-racing-game/main/frontend/public/appPhoto/PROFILE.jpg',
                'https://raw.githubusercontent.com/sheeshhhhhh/type-racing-game/main/frontend/public/appPhoto/CHALLENGES.jpg',
                'https://raw.githubusercontent.com/sheeshhhhhh/type-racing-game/main/frontend/public/appPhoto/CHALLENGE%20MULTIPLAYER.jpg'
                ],
            'github': 'https://github.com/sheeshhhhhh/type-racing-game',
            'websitelink': 'https://type-racing-game.onrender.com/',
            'techstack': 'React, Node.js, Socket.io, Nest Js, Postgres, Docker'
        },
        { 
            'title': 'ecommerce-app',
            'description': 'Our e-commerce app is offering a wide range of products, secure payment options, and real-time order tracking. With an intuitive design and smooth navigation, it ensures a hassle-free shopping experience for both buyers and sellers.',
            'image': [
                'https://res-console.cloudinary.com/dslm0pp9s/media_explorer_thumbnails/f91835b255a435cc73757dfff95c8920/detailed',
                'https://res-console.cloudinary.com/dslm0pp9s/media_explorer_thumbnails/4fc9b5baeb4656eeea0ceb4b0d6151ae/detailed',
                'https://res-console.cloudinary.com/dslm0pp9s/media_explorer_thumbnails/b9253024cddf4f2b4b87eae3ce485450/detailed',
                ],
            'github': 'https://github.com/sheeshhhhhh/Ecommerce_2024',
            'websitelink': '',
            'techstack': 'Next Js, Next Auth, Node Js, Prisma, Postgres, Stripe'
        },
        { 
            'title': 'Recipe Verse',
            'description': 'A sleek recipe app with a modern UI, featuring an intuitive dashboard. Its powerful filtering system ensures easy discovery of dishes by ingredients, cuisine, or difficulty, while smooth navigation and stylish design enhance the user experience.',
            'image': [
                'https://res-console.cloudinary.com/dslm0pp9s/media_explorer_thumbnails/ed08849703eae4d34204138d0d93cec9/detailed',
                'https://res-console.cloudinary.com/dslm0pp9s/media_explorer_thumbnails/553b5e5e8f76544c8f922087aecab857/detailed',
                'https://res-console.cloudinary.com/dslm0pp9s/media_explorer_thumbnails/f4e4f23ef0a4e1d354973647fa60309d/detailed',
                'https://res-console.cloudinary.com/dslm0pp9s/media_explorer_thumbnails/19f264d20f202709aaa0ad5b763d7a7d/detailed'
                ],
            'github': 'https://github.com/sheeshhhhhh/recipeVerse_2',
            'websitelink': '',
            'techstack': 'React, Node Js, Prisma, Postgres, Tailwind, Passport'
        },
        {
            'title': 'portfolio',
            'description': 'This is my portfolio website. I created this website to showcase my projects and skills. I used Django as the backend and HTML, CSS, and JavaScript for the frontend.',
            'image': [
                'https://res-console.cloudinary.com/dslm0pp9s/media_explorer_thumbnails/d67513484dc299c711a4022879a85611/detailed',
                'https://res-console.cloudinary.com/dslm0pp9s/media_explorer_thumbnails/cd3c4df5a7e481e5bcbf5bb2588c3c7e/detailed',
                ],
            'github': 'tobe put',
            'websitelink': '',
            'techstack': 'Django, HTML, CSS, Tailwind CSS, JavaScript'
        }
    ]

    project = models.Project.objects.prefetch_related('images').all()
    print(project[0])
    return render(request, 'projects.html', { "navigation": "projects", "projects": projects })

def about(request):

    techStack = [
        { 'name': "Python", 'icon': "https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png", 'knowledgeLevel': "Intermediate" },
        { 'name': "Django", 'icon': "https://cdn.worldvectorlogo.com/logos/django.svg", 'knowledgeLevel': "Beginner" },
        { 'name': "HTML", 'icon': "https://cdn.worldvectorlogo.com/logos/html-1.svg", 'knowledgeLevel': "Advanced" },
        { 'name': "CSS", 'icon': "https://cdn.worldvectorlogo.com/logos/css-3.svg", 'knowledgeLevel': "Advanced" },
        { 'name': "React", 'icon': "https://cdn.worldvectorlogo.com/logos/react-2.svg", 'knowledgeLevel': "Advanced" },
        { 'name': "JavaScript", 'icon': "https://cdn.worldvectorlogo.com/logos/logo-javascript.svg", 'knowledgeLevel': "Advanced" },
        { 'name': "TypeScript", 'icon': "https://cdn.worldvectorlogo.com/logos/typescript.svg", 'knowledgeLevel': "Advanced" },
        { 'name': "Node.js", 'icon': "https://cdn.worldvectorlogo.com/logos/nodejs-icon.svg", 'knowledgeLevel': "Advanced" },
        { 'name': "Express", 'icon': "https://icon.icepanel.io/Technology/svg/Express.svg", 'knowledgeLevel': "Advanced" },
        { 'name': "Nest Js", 'icon': "https://cdn.worldvectorlogo.com/logos/nestjs.svg", 'knowledgeLevel': "Intermediate" },
        { 'name': "Tailwind CSS", 'icon': "https://cdn.worldvectorlogo.com/logos/tailwind-css-2.svg", 'knowledgeLevel': "Advanced" },
        { 'name': "Prisma", 'icon': "https://cdn.worldvectorlogo.com/logos/prisma-3.svg", 'knowledgeLevel': "Intermediate" },
    ]

    tools = [
        { 'name': "Git", 'icon': "https://cdn.worldvectorlogo.com/logos/git-icon.svg", 'knowledgeLevel': "Advanced" },
        { 'name': "Docker", 'icon': "https://cdn.worldvectorlogo.com/logos/docker-4.svg", 'knowledgeLevel': "Beginner" },
        { 'name': "Postman", 'icon': "https://cdn.worldvectorlogo.com/logos/postman.svg", 'knowledgeLevel': "Advanced" },
        { 'name': "NPM", 'icon': "https://cdn.worldvectorlogo.com/logos/npm.svg", 'knowledgeLevel': "Advanced" },
        { 'name': "VS Code", 'icon': "https://cdn.worldvectorlogo.com/logos/visual-studio-code-1.svg", 'knowledgeLevel': "Advanced" },
    ]

    schools = [
        { 'name': "Sta Clara Elementary School (kindergarten to Grade 6)", 'year': "2010-2016", 'Description': "This is where i learned how to read and write. I also learned the basic of mathematics and science. and also learned how to socialize with other people. as a kid i was very shy and introvert. i am always absent during this time as i was addicted to playing in computer shops" },
        { 'name': "Sacred Heart Academy Sta Maria Bulacan (HighSchool to Senior HighSchool)", 'year': "2017-2022", 'Description': "During these years, I wasn’t consistent in school, nor in programming, as I was often distracted by video games. However, this was also the time when I discovered my passion for programming. While I didn’t learn it from school, my interest drove me to explore and study programming on my own, fueled by curiosity and determination during this years." },
        { 'name': "Sti College, Sta. Maria (BSIT)", 'year': "2022-2024", 'Description': "This is where I ultimately became consistent in my studies, driven by my passion for programming and being in my dream course. I have learned a lot from the curriculum while also continuing to grow through self-study. My dedication has paid off, as I have been achieving good grades and gaining valuable skills for my future career." },
    ]

    return render(request, 'about.html', { "navigation": "about", "techStack": techStack, "tools": tools, "schools": schools })