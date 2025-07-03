const exitRedirectURL = "../index.html";
let idleTimer;
function resetIdleTimer() {
    clearTimeout(idleTimer);
    idleTimer = setTimeout(() => {
    window.location.href = "../index.html"; // redirect after 60s of no input
    }, 60000); // 60000 ms = 60 seconds
}
['mousemove', 'keydown', 'mousedown', 'scroll', 'touchstart'].forEach(event => {
    window.addEventListener(event, resetIdleTimer);
});
resetIdleTimer(); // start timer when page loads