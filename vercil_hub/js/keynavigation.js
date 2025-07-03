document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.btn');
    let currentIndex = 0;
    
    // Initialize first button as focused
    buttons[currentIndex].classList.add('keyboard-focus');
    
    // Add keyboard event listener
    document.addEventListener('keydown', function(e) {
    // Remove focus class from all buttons
    buttons.forEach(btn => btn.classList.remove('keyboard-focus'));
    
    switch(e.key) {
        case 'ArrowUp':
            e.preventDefault();
            currentIndex = (currentIndex - 3 + buttons.length) % buttons.length;
            break;
        case 'ArrowDown':
            e.preventDefault();
            currentIndex = (currentIndex + 3) % buttons.length;
            break;
        case 'ArrowLeft':
            e.preventDefault();
            currentIndex = (currentIndex - 1 + buttons.length) % buttons.length;
            break;
        case 'ArrowRight':
            e.preventDefault();
            currentIndex = (currentIndex + 1) % buttons.length;
            break;
        case 'Enter':
            e.preventDefault();
            if (buttons[currentIndex]) {
                buttons[currentIndex].click();
            }
        return; // Don't add focus class back if we're navigating away
        default:
        return; // Ignore other keys
    }
    
    // Add focus class to new current button
    buttons[currentIndex].classList.add('keyboard-focus');
    buttons[currentIndex].focus();
    });
    
    // Mouse interaction - remove keyboard focus when mouse is used
    buttons.forEach(btn => {
    btn.addEventListener('mouseenter', function() {
        buttons.forEach(b => b.classList.remove('keyboard-focus'));
        currentIndex = Array.from(buttons).indexOf(btn);
    });
    });
});