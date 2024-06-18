const canvas = document.getElementById('wallpaper');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const colors = ['#ff073a', '#ff8c00', '#ffd700', '#00ff00', '#00ffff', '#1e90ff', '#9370db'];
const lines = [];

function createLine() {
    return {
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        length: Math.random() * 200 + 50,
        speed: Math.random() * 2 + 1,
        color: colors[Math.floor(Math.random() * colors.length)]
    };
}

for (let i = 0; i < 50; i++) {
    lines.push(createLine());
}

function drawLine(line) {
    ctx.shadowBlur = 10;
    ctx.shadowColor = line.color;
    ctx.beginPath();
    ctx.moveTo(line.x, line.y);
    ctx.lineTo(line.x + line.length, line.y);
    ctx.strokeStyle = line.color;
    ctx.lineWidth = 2;
    ctx.stroke();
    ctx.shadowBlur = 0; // Reset shadowBlur
}

function animate() {
    ctx.fillStyle = 'rgba(10, 10, 10, 0.1)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    lines.forEach(line => {
        drawLine(line);
        line.x += line.speed;
        if (line.x > canvas.width) {
            line.x = -line.length;
        }
    });

    requestAnimationFrame(animate);
}

animate();

window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});
