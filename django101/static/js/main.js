function highlight() {
    if (this.className.includes('highlighted')) {
        this.className = this.className.replace('highlighted', '');
    } else {
        this.className += ' highlighted';
    }
}

window.onload = function () {
    [...document.getElementsByClassName('highlightable')]
    .forEach(element => {
        element.addEventListener('mouseenter', highlight);
        element.addEventListener('mouseout', highlight);
    });
}

