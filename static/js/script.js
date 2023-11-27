let origin = window.location.href;
document.querySelectorAll('.naw').forEach(item => {
    if (origin !== item.href) {
        return;
    }
    item.classList.add('active');
})