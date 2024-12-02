from django.shortcuts import render

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
                'https://utfs.io/f/58o2ZgHTdjoJfNfszH9E2vRe8mgHByN7aJAcOI9sx6kSqjYU',
                'https://utfs.io/f/58o2ZgHTdjoJZwI1vvkM6xsuNYpqLkMm1yKUwDZl3WOz0I4h',
                'https://utfs.io/f/58o2ZgHTdjoJzypUKZVnfBkyKH5avE9b0OM6mRsjXFWSliZp',
                ],
            'github': 'https://github.com/sheeshhhhhh/Ecommerce_2024',
            'websitelink': '',
            'techstack': 'Next Js, Next Auth, Node Js, Prisma, Postgres, Stripe'
        },
        { 
            'title': 'Recipe Verse',
            'description': 'A sleek recipe app with a modern UI, featuring an intuitive dashboard. Its powerful filtering system ensures easy discovery of dishes by ingredients, cuisine, or difficulty, while smooth navigation and stylish design enhance the user experience.',
            'image': [
                'https://utfs.io/f/58o2ZgHTdjoJiJGwYynOtnujDqmbyTxXe05rwQdlFI6PfYzK',
                'https://utfs.io/f/58o2ZgHTdjoJMQjqI2pPQP1uWCr8aVEgpB0fD7iIvAqzGtjT',
                'https://utfs.io/f/58o2ZgHTdjoJ6t56ZeoriwGxD7K82ZISC1gqk9f0JP3Rlura',
                ],
            'github': 'https://github.com/sheeshhhhhh/recipeVerse_2',
            'websitelink': '',
            'techstack': 'React, Node Js, Prisma, Postgres, Tailwind, Passport'
        },
        {
            'title': 'portfolio',
            'description': 'This is my portfolio website. I created this website to showcase my projects and skills. I used Django as the backend and HTML, CSS, and JavaScript for the frontend.',
            'image': [
                'https://utfs.io/f/58o2ZgHTdjoJwZ52FBQHYTfvaSucyd5OeXzkPrp7WwgtKRVm',
                'https://utfs.io/f/58o2ZgHTdjoJSipK4G5HQ9Z3yAz4Jo7VU2kaIROpvD6n8TFd',
                ],
            'github': 'tobe put',
            'websitelink': '',
            'techstack': 'Django, HTML, CSS, Tailwind CSS, JavaScript'
        }
    ]

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