function interseccao(ret1, ret2) {
    for (let i = 0; i < 4; i++) {
        for (let j = 0; j < 4; j++) {
            if (vec2.segmentsIntersect(ret1[i], ret1[(i + 1) % 4], ret2[j], ret2[(j + 1) % 4])) {
                return true;
            }
        }
    }

    let r2insider1 = 0;
    let r1insider2 = 0;
    for (let i = 0; i < 4; i++) {
        if (util2d.pointInPoly(ret1[i], ret2)) {
            r1insider2++;
        }
        if (util2d.pointInPoly(ret2[i], ret1)) {
            r2insider1++;
        }
    }
    if (r1insider2 == 4 || r2insider1 == 4) {
        return true;
    }

    util2d.p
    return false;
}

function interseccao2(ret, circ) {
    if (util2d.pointInPoly(circ[0], ret)) {
        return true;
    }
    for (let i = 0; i < 4; i++) {
        for (let j = 0; j < 360; j++) {
            let radAng = (j * Math.PI / 180);
            let point = [];
            vec2.rotate(point, circ[1], circ[0], radAng);
            //testa as 4 arestas do retangulo, se cada uma toca o circulo
            if (vec2.segmentsIntersect(ret[i], ret[(i + 1) % 4], circ[0], point)) {
                return true;
            }
        }
    }
    util2d.p
    return false;
}

function interseccao3(tri1, tri2) {
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            if (vec2.segmentsIntersect(tri1[i], tri1[(i + 1) % 3], tri2[j], tri2[(j + 1) % 3])) {
                return true;
            }
        }
    }

    let r2insider1 = 0;
    let r1insider2 = 0;
    for (let i = 0; i < 3; i++) {
        if (util2d.pointInPoly(tri1[i], tri2)) {
            r1insider2++;
        }
        if (util2d.pointInPoly(tri2[i], tri1)) {
            r2insider1++;
        }
    }
    if (r1insider2 == 3 || r2insider1 == 3) {
        return true;
    }

    util2d.p
    return false;
}

function interseccao4(tri, circ) {
    if (util2d.pointInPoly(circ[0], tri)) {
        return true;
    }
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 360; j++) {
            let radAng = (j * Math.PI / 180);
            let point = [];
            vec2.rotate(point, circ[1], circ[0], radAng);
            //testa as 4 arestas do retangulo, se cada uma toca o circulo
            if (vec2.segmentsIntersect(tri[i], tri[(i + 1) % 3], circ[0], point)) {
                return true;
            }
        }
    }
    util2d.p
    return false;
}

function interseccao5(circ1, circ2) {
    // circ1[0] ->  centro
    const distCenterToCenter = vec2.dist(circ1[0], circ2[0]);
    const rCirc1 = (circ1[0][1] - circ1[1][1]);
    const rCirc2 = (circ2[0][1] - circ2[1][1])
    const rSummed = rCirc1 + rCirc2;
    if (distCenterToCenter < rSummed || distCenterToCenter < rCirc1 || distCenterToCenter < rCirc2) {
        return true;
    }

    util2d.p
    return false;
}

function interseccao6(ret, tri) {
    for (let i = 0; i < 4; i++) {
        for (let j = 0; j < 3; j++) {
            if (vec2.segmentsIntersect(ret[i], ret[(i + 1) % 4], tri[j], tri[(j + 1) % 3])) {
                return true;
            }
        }
    }

    let r2insider1 = 0;
    let r1insider2 = 0;
    for (let i = 0; i < 4; i++) {
        if (util2d.pointInPoly(ret[i], tri)) {
            r1insider2++;
        }
    }

    for (let i = 0; i < 3; i++) {
        if (util2d.pointInPoly(tri[i], ret)) {
            r2insider1++;
        }
    }

    if (r1insider2 >= 3 || r2insider1 >= 3) {
        return true;
    }

    util2d.p
    return false;
}

function isosceles(basePoint, oppositeVertex) {
    const u = vec2.sub([], basePoint, oppositeVertex);
    const v = [-u[1], u[0]];
    const w = [u[1], -u[0]];
    return [
        oppositeVertex,
        vec2.add([], basePoint, v),
        vec2.add([], basePoint, w)
    ];
}

function retangle(centro, a1, a2, a3, a4) {

    const v1 = vec2.sub([], a1, centro);
    const v2 = vec2.sub([], a2, centro);
    const v3 = vec2.sub([], a3, centro);
    const v4 = vec2.sub([], a4, centro);

    const vertice1 = vec2.add([], centro, vec2.add([], v1, v3));
    const vertice2 = vec2.add([], centro, vec2.add([], v1, v2));
    const vertice3 = vec2.add([], centro, vec2.add([], v3, v4));
    const vertice4 = vec2.add([], centro, vec2.add([], v2, v4));

    return [vertice1, vertice2, vertice4, vertice3]
}