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

    projects = models.Project.objects.prefetch_related('images').all()
    return render(request, 'projects.html', { "navigation": "projects", "projects": projects })

def about(request):

    techStack = models.Skills.objects.all()

    schools = models.Education.objects.all()

    return render(request, 'about.html', { "navigation": "about", "techStack": techStack, "schools": schools })