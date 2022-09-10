"use strict";

var vertices = new Float32Array([
    -0.5, -0.5, 0.5, -0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5, 0.5,
]);
var numPoints = vertices.length / 2;
var w;
var h;
var verticesValues = [4, 3, 1, 5];


function mapToViewport(x, y, n = 5) {
    return [((x + n / 2) * w) / n, ((-y + n / 2) * h) / n];
}

function getVertex(i) {
    let j = (i % numPoints) * 2;
    return [vertices[j], vertices[j + 1]];
}
function draw(ctx, angle, vertice) {
    let vertexIndex = vertice

    ctx.fillStyle = "rgba(0, 204, 204, 1)";
    ctx.rect(0, 0, w, h);
    ctx.fill()

    // Finaliza a renderização do quadrado cor verde


    let [x, y] = mapToViewport(...getVertex(vertexIndex));

    ctx.translate(x, y)

    // Pega a posição das coordenadas do vertice

    //AJUSTAR PARA GRAU
    ctx.rotate(-angle * Math.PI / 180);
    ctx.translate(-x, -y)

    //Desenha o quadrado
    ctx.beginPath();

    for (let i = 0; i < numPoints; i++) {
        if (i == 3 || i == 4) continue;
        let [x, y] = mapToViewport(...getVertex(i).map((v) => v));
        ctx.lineTo(x, y);
    }
    ctx.closePath();
    ctx.strokeStyle = "gray";
    ctx.lineWidth = 10;
    ctx.stroke();
    
    if (vertexIndex == 4 || vertexIndex == 3){
        var grad = ctx.createLinearGradient(0,100,0,350);
        grad.addColorStop(0,'red');
        grad.addColorStop(1,'blue');
    }else{
        var grad = ctx.createLinearGradient(0,100,0,350);
        grad.addColorStop(0,'green');
        grad.addColorStop(1,'white');
    }
    
    ctx.fillStyle = grad;
    ctx.fill();

    verticesValues.map(v => {
        ctx.beginPath()
        let [x1, y1] = mapToViewport(...getVertex(v));
        ctx.arc(x1,y1,4,10,Math.PI)
        switch (v) {
            case 5:
                ctx.fillStyle = 'green'
                break;
            case 4:
                ctx.fillStyle = 'red'
                break;
            case 3:
                ctx.fillStyle = 'blue'
                break;
            case 1:
                ctx.fillStyle = 'white'
                break;
        }
        ctx.lineWidth = 2;
        ctx.stroke();
        ctx.fill()

    })
}

function mainEntrance() {
    var canvasElement = document.querySelector("#theCanvas");
    var ctx = canvasElement.getContext("2d");
    let vertice = 3
    w = canvasElement.width;
    h = canvasElement.height;
    document.addEventListener("keydown", (event) => {
        console.log(event.key);
        //AJUSTAR AS TECLAS DO TECLADO
        switch (event.key) {
            case "r":
                vertice = 4;
                break;
            case "b":
                vertice = 3;
                break;
            case "w":
                vertice = 1;
                break;
            case "g":
                vertice = 5;
                break;
        }
    });
    var runanimation = (() => {
        // teta-angulo
        var angle = 2.0;
        return () => {
            draw(ctx, angle, vertice);
            requestAnimationFrame(runanimation);
        };
    })();
    runanimation();
}