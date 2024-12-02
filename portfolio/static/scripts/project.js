function openDialog(dialogId) {
    const todoDialog = document.getElementById(dialogId);
    document.body.classList.add('no-scroll'); // to stop scrolling

    // so that we can continue scrolling if closed
    todoDialog.addEventListener('close', () => {
        document.body.classList.remove('no-scroll');
    }, { once: true });

    todoDialog.showModal();
}

function nextImage(projecttitle, length) {
    length = parseInt(length)
    const images = document.getElementById(projecttitle);
    let previous = images.style.transform;

    if(previous) {
        previous = previous.split('(')[1].split('%')[0];
    }

    // if no previous value or if the current image is the last one
    const currentIndex = Math.abs(previous) / 100;
    if (currentIndex >= length - 1) {
        console.log('No more images to move forward.');
        return;
    }
    
    images.style.transform = `translateX(${previous - 100}%)`;
}

function previousImage(projecttitle) {
    const images = document.getElementById(projecttitle);
    let previous = images.style.transform;

    if(previous) {
        previous = previous.split('(')[1].split('%')[0];
    }

    if(!previous || parseInt(previous) === 0) {
        return;
    }

    images.style.transform = `translateX(${parseInt(previous) + 100}%`;
}
