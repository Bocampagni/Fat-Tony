const demo = html`<canvas width=500 height=500 style="border:1px solid gray">`;
const ctx = demo.getContext("2d");

const p1 = [
    [100, 60],
    [100, 20],
    [140, 60],
    [60, 60],
    [100, 100]
];
const p2 = [
    [250, 60],
    [250, 20],
    [290, 60],
    [210, 60],
    [250, 100]
];

const p3 = [
    [400, 60],
    [400, 20],
    [440, 60],
    [360, 60],
    [400, 100]
];

const c1 = [
    [100, 240],
    [100, 200]
];

const c2 = [
    [200, 240],
    [200, 200]
];
const c3 = [
    [300, 240],
    [300, 200]
];
const t1 = [
    [100, 350],
    [110, 300]
];
const t2 = [
    [200, 350],
    [210, 300]
];
const t3 = [
    [300, 350],
    [310, 300]
];

const discover = [
    { id: 1, item: p1, type: 'rec' },
    { id: 2, item: p2, type: 'rec' },
    { id: 3, item: p3, type: 'rec' },
    { id: 4, item: c1, type: 'circ' },
    { id: 5, item: c2, type: 'circ' },
    { id: 6, item: c3, type: 'circ' },
    { id: 7, item: t1, type: 'tri' },
    { id: 8, item: t2, type: 'tri' },
    { id: 9, item: t3, type: 'tri' }
]


const update = () => {
    ctx.clearRect(0, 0, 500, 500);
    draw(ctx, [p1, p2, p3, c1, c2, c3, t1, t2, t3])
};

update();

let prevM = null;
const dragCenter = (e, r) => {
    let m = [e.offsetX, e.offsetY];
    if (r <= 3) {
        let [c, v1, v2, v3, v4] = p1;

        if (r == 2) {
            [c, v1, v2, v3, v4] = p2;
        }
        if (r == 3) {
            [c, v1, v2, v3, v4] = p3;
        }

        let vetor1 = vec2.sub([], v1, c);
        let vetor2 = vec2.sub([], v2, c);
        let vetor3 = vec2.sub([], v3, c);
        let vetor4 = vec2.sub([], v4, c);

        let d = vec2.sub([], m, prevM);

        prevM = m;
        vec2.add(c, c, d);

        vec2.add(v1, vetor1, c);
        vec2.add(v2, vetor2, c);
        vec2.add(v3, vetor3, c);
        vec2.add(v4, vetor4, c);
    }
    else if (r > 3 && r <= 6) {

        let [centro, v1] = c1;

        if (r === 5) {
            [centro, v1] = c2;
        }

        else if (r == 6) {
            [centro, v1] = c3;
        }

        let vector1 = vec2.sub([], v1, centro);

        let delta = vec2.sub([], m, prevM);

        vec2.add(centro, centro, delta);

        prevM = m;

        vec2.add(v1, vector1, centro);
    }
    else if (r > 6 || r <= 9) {
        let [base, vtx] = t1;

        if (r == 8) {
            [base, vtx] = t2;
        }

        if (r == 9) {
            [base, vtx] = t3;
        }

        let v = vec2.sub([], vtx, base);
        let delta = vec2.sub([], m, prevM);
        prevM = m;

        vec2.add(base, base, delta);
        vec2.add(vtx, base, v);
    }
};

const dragVer = (e, i, r) => {
    let m = [e.offsetX, e.offsetY];
    let d = vec2.sub([], m, prevM);

    prevM = m;

    if (r > 6 && r <= 9) {
        let mouse = [e.offsetX, e.offsetY];
        let [base, vtx] = t1;

        if (r == 8) {
            [base, vtx] = t2;
        }

        if (r == 9) {
            [base, vtx] = t3;
        }

        prevM = m;
        vec2.add(vtx, vtx, d);
    }


    else if (r > 3 && r <= 6) {
        //Circulo
        let [centro, cv1] = c1;

        if (r == 5) {
            [centro, cv1] = c2;
        }
        if (r == 6) {
            [centro, cv1] = c3;
        }

        vec2.add(cv1, cv1, d);

    } else if (r <= 3) {
        let [c, v1, v2, v3, v4] = p1;

        if (r == 2) {
            [c, v1, v2, v3, v4] = p2;
        }

        if (r == 3) {
            [c, v1, v2, v3, v4] = p3;
        }


        if (i == 1) {
            vec2.add(v1, v1, d);
            vec2.add(v4, v4, [-d[0], -d[1]])

            let dif1 = [];
            let dif2 = [];
            vec2.sub(dif1, v1, c);
            vec2.sub(dif2, v2, c);
            vec2.rotate(v2, v2, c, Math.PI / 2 - vec2.angle(dif1, dif2));
            vec2.rotate(v3, v3, c, Math.PI / 2 - vec2.angle(dif1, dif2));

        }
        else if (i == 2) {
            vec2.add(v2, v2, d);
            vec2.add(v3, v3, [-d[0], -d[1]])

            let dif1 = [];
            let dif2 = [];
            vec2.sub(dif1, v2, c);
            vec2.sub(dif2, v4, c);
            vec2.rotate(v1, v1, c, Math.PI / 2 - vec2.angle(dif1, dif2));
            vec2.rotate(v4, v4, c, Math.PI / 2 - vec2.angle(dif1, dif2));

        }
        else if (i == 3) {
            vec2.add(v3, v3, d);
            vec2.add(v2, v2, [-d[0], -d[1]])

            let dif1 = [];
            let dif2 = [];
            vec2.sub(dif1, v3, c);
            vec2.sub(dif2, v1, c);
            vec2.rotate(v1, v1, c, Math.PI / 2 - vec2.angle(dif1, dif2));
            vec2.rotate(v4, v4, c, Math.PI / 2 - vec2.angle(dif1, dif2));
        }
        else if (i == 4) {
            vec2.add(v4, v4, d);
            vec2.add(v1, v1, [-d[0], -d[1]])

            let dif1 = [];
            let dif2 = [];
            vec2.sub(dif1, v4, c);
            vec2.sub(dif2, v3, c);

            vec2.rotate(v3, v3, c, Math.PI / 2 - vec2.angle(dif1, dif2));
            vec2.rotate(v2, v2, c, Math.PI / 2 - vec2.angle(dif1, dif2));
        }


    }


};

demo.onmousedown = (e) => {
    const mouse = [e.offsetX, e.offsetY];
    prevM = mouse;
    demo.onmousemove = null;

    for (let c = 0; c < discover.length; c++) {

        if (discover[c].type == 'rec') {
            for (let i of [0, 1, 2, 3, 4]) {
                let ponto = discover[c].item[i];
                let d = vec2.distance(mouse, ponto);
                if (d <= 5) {
                    demo.onmousemove =
                        i == 0
                            ? (e) => {
                                dragCenter(e, discover[c].id);
                                update();
                            }
                            : (e) => {
                                dragVer(e, i, discover[c].id);
                                update();
                            };
                }
            }
        }


        else if (discover[c].type == 'circ') {
            for (let i of [0, 1]) {
                let p = discover[c].item[i];
                let d = vec2.distance(mouse, p);
                if (d <= 5) {
                    demo.onmousemove =
                        i == 0
                            ? (e) => {
                                dragCenter(e, discover[c].id);
                                update();
                            }
                            : (e) => {
                                dragVer(e, i, discover[c].id);
                                update();
                            };
                }
            }
        }

        else if (discover[c].type == 'tri') {
            for (let i of [0, 1]) {
                let p = discover[c].item[i];
                let d = vec2.distance(mouse, p);
                if (d <= 5) {
                    demo.onmousemove =
                        i == 0
                            ? (e) => {
                                dragCenter(e, discover[c].id);
                                update();
                            }
                            : (e) => {
                                dragVer(e, i, discover[c].id);
                                update();
                            }
                }
            }
        }




    }
};

demo.onmouseup = () => {
    demo.onmousemove = null;
};

function draw(ctx,lista){

    const r1 = retangle(...lista[0]);
    const r2 = retangle(...lista[1]);
    const r3 = retangle(...lista[2]);
    const c1 = lista[3];
    const c2 = lista[4];
    const c3 = lista[5];
    const t1 = isosceles(...lista[6]);
    const t2 = isosceles(...lista[7]);
    const t3 = isosceles(...lista[8]);



    //ret1
    if(interseccao(r1,r2) || interseccao(r1,r3) || interseccao2(r1,c1) || interseccao2(r1,c2) || interseccao2(r1,c3) || interseccao6(r1,t1) || interseccao6(r1,t2) || interseccao6(r1,t3)){
        ctx.fillStyle = ctx.strokeStyle = "red"
      }else{
        ctx.fillStyle = ctx.strokeStyle = "black"
    }
  
    for (let p of lista[0]) {
      ctx.beginPath();
      ctx.arc(...p, 5, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.beginPath();
    for (let p of retangle(...lista[0])) {
      ctx.lineTo(...p);
    }
    ctx.closePath();
    ctx.stroke();
    
    //ret2
    if(interseccao(r2,r1) || interseccao(r2,r3) || interseccao2(r2,c1) || interseccao2(r2,c2) || interseccao2(r2,c3) || interseccao6(r2,t1) || interseccao6(r2,t2) || interseccao6(r2,t3)){
      ctx.fillStyle = ctx.strokeStyle = "red"
    }else{
      ctx.fillStyle = ctx.strokeStyle = "black"
    }
    for (let p of lista[1]) {
      ctx.beginPath();
      ctx.arc(...p, 5, 0, Math.PI * 2);
      ctx.fill();
    }  
    ctx.beginPath();
    for (let p of retangle(...lista[1])) {
      ctx.lineTo(...p);
    }
    ctx.closePath();
    ctx.stroke();

    //ret3
    if(interseccao(r3,r1) || interseccao(r3,r2) || interseccao2(r3,c1) || interseccao2(r3,c2) || interseccao2(r3,c3) || interseccao6(r3,t1) || interseccao6(r3,t2) || interseccao6(r3,t3)){
      ctx.fillStyle = ctx.strokeStyle = "red"
    }else{
      ctx.fillStyle = ctx.strokeStyle = "black"
    }
    for (let p of lista[2]) {
      ctx.beginPath();
      ctx.arc(...p, 5, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.beginPath();
    for (let p of retangle(...lista[2])) {
      ctx.lineTo(...p);
    }
    ctx.closePath();
    ctx.stroke();


    //circ1
    if(interseccao2(r1,c1) || interseccao2(r2,c1) || interseccao2(r3,c1) || interseccao4(t1,c1) || interseccao4(t2,c1) || interseccao4(t3,c1) || interseccao5(c1,c2) || interseccao5(c1,c3)){
      ctx.fillStyle = ctx.strokeStyle = "red"
    }else{
      ctx.fillStyle = ctx.strokeStyle = "black"
    }
    for (let p of lista[3]) {
      ctx.beginPath();
      ctx.arc(...p, 5, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.beginPath();
    ctx.arc(...lista[3][0], vec2.dist(lista[3][0], lista[3][1]), 0, Math.PI * 2);
    ctx.stroke();

    //circ2
    if(interseccao2(r1,c2) || interseccao2(r2,c2) || interseccao2(r3,c2) || interseccao4(t1,c2) || interseccao4(t2,c2) || interseccao4(t3,c2) || interseccao5(c1,c2) || interseccao5(c2,c3) ){
      ctx.fillStyle = ctx.strokeStyle = "red"
    }else{
      ctx.fillStyle = ctx.strokeStyle = "black"
    }
  
    for (let p of lista[4]) {
      ctx.beginPath();
      ctx.arc(...p, 5, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.beginPath();
    ctx.arc(...lista[4][0], vec2.dist(lista[4][0], lista[4][1]), 0, Math.PI * 2);
    ctx.stroke();



    // circ3
    if(interseccao2(r1,c3) || interseccao2(r2,c3) || interseccao2(r3,c3) || interseccao4(t1,c3) || interseccao4(t2,c3) || interseccao4(t3,c3) || interseccao5(c1,c3) || interseccao5(c2,c3) ){
      ctx.fillStyle = ctx.strokeStyle = "red"
    }else{
      ctx.fillStyle = ctx.strokeStyle = "black"
    }
    for (let p of lista[5]) {
      ctx.beginPath();
      ctx.arc(...p, 5, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.beginPath();
    ctx.arc(...lista[5][0], vec2.dist(lista[5][0], lista[5][1]), 0, Math.PI * 2);
    ctx.stroke();

    //tri 1
    if(interseccao3(t1,t2) || interseccao3(t1,t3) || interseccao4(t1,c1) || interseccao4(t1,c2) || interseccao4(t1,c3) || interseccao6(r1,t1) || interseccao6(r2,t1) || interseccao6(r3,t1) ){
      ctx.fillStyle = ctx.strokeStyle = "red"
    }else{
      ctx.fillStyle = ctx.strokeStyle = "black"
    }
  
    for (let p of lista[6]) {
      ctx.beginPath();
      ctx.arc(...p, 5, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.beginPath();
    for (let p of isosceles(...lista[6])) {
      ctx.lineTo(...p);
    }
    ctx.closePath();
    ctx.stroke();






    // tri2
    if(interseccao3(t2,t1) || interseccao3(t2,t3) || interseccao4(t2,c1) || interseccao4(t2,c2) || interseccao4(t2,c3) || interseccao6(r1,t2) || interseccao6(r2,t2) || interseccao6(r3,t2)){
      ctx.fillStyle = ctx.strokeStyle = "red"
    }else{
      ctx.fillStyle = ctx.strokeStyle = "black"
    }
    for (let p of lista[7]) {
      ctx.beginPath();
      ctx.arc(...p, 5, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.beginPath();
    for (let p of isosceles(...lista[7])) {
      ctx.lineTo(...p);
    }
    ctx.closePath();
    ctx.stroke();

    // tri3
    if(interseccao3(t3,t1) || interseccao3(t3,t2) || interseccao4(t3,c1) || interseccao4(t3,c2) || interseccao4(t3,c3) || interseccao6(r1,t3) || interseccao6(r2,t3) || interseccao6(r3,t3)){
      ctx.fillStyle = ctx.strokeStyle = "red"
    }else{
      ctx.fillStyle = ctx.strokeStyle = "black"
    }
    for (let p of lista[8]) {
      ctx.beginPath();
      ctx.arc(...p, 5, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.beginPath();
    for (let p of isosceles(...lista[8])) {
      ctx.lineTo(...p);
    }
    ctx.closePath();
    ctx.stroke();
}