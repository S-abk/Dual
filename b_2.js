const canvas = document.getElementById('wallpaper');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Example animation: bouncing ball
    const time = new Date().getTime() * 0.002;
    const x = Math.sin(time) * 192 + canvas.width / 2;
    const y = Math.cos(time * 0.9) * 192 + canvas.height / 2;

    ctx.beginPath();
    ctx.arc(x, y, 50, 0, Math.PI * 2);
    ctx.fillStyle = 'rgba(0, 150, 255, 0.5)';
    ctx.fill();
    
    requestAnimationFrame(animate);
}

animate();

window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});

