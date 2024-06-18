const canvas = document.getElementById('wallpaper');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const colors = ['#ff073a', '#ff8c00', '#ffd700', '#00ff00', '#00ffff', '#1e90ff', '#9370db', '#ff00ff', '#00ff80'];
const lines = [];

function createLine() {
    return {
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        length: Math.random() * 200 + 50,
        speed: Math.random() * 3 + 1,
        color: colors[Math.floor(Math.random() * colors.length)],
        angle: Math.random() * Math.PI * 2
    };
}

for (let i = 0; i < 100; i++) {
    lines.push(createLine());
}

function drawLine(line) {
    ctx.save();
    ctx.translate(line.x, line.y);
    ctx.rotate(line.angle);
    ctx.shadowBlur = 20;
    ctx.shadowColor = line.color;
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(line.length, 0);
    ctx.strokeStyle = line.color;
    ctx.lineWidth = 3;
    ctx.stroke();
    ctx.restore();
}

function animate() {
    ctx.fillStyle = 'rgba(10, 10, 10, 0.1)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    lines.forEach(line => {
        drawLine(line);
        line.x += Math.cos(line.angle) * line.speed;
        line.y += Math.sin(line.angle) * line.speed;
        
        if (line.x > canvas.width || line.x < 0 || line.y > canvas.height || line.y < 0) {
            line.x = Math.random() * canvas.width;
            line.y = Math.random() * canvas.height;
            line.angle = Math.random() * Math.PI * 2;
        }
    });

    requestAnimationFrame(animate);
}

animate();

window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});