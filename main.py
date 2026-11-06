import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Cozy Bear Cafe 3D",
    page_icon="🐻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
header, footer, #MainMenu {
    visibility: hidden;
}
.block-container {
    padding: 0;
    max-width: 100%;
}
iframe {
    display: block;
}
.stApp {
    background: #f7e9db;
}
</style>
""", unsafe_allow_html=True)

html = r'''
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    overflow: hidden;
    font-family: system-ui, 'Apple SD Gothic Neo', sans-serif;
    color: #684b3b;
    background: #f7e9db;
}

canvas {
    display: block;
}

#ui {
    position: absolute;
    inset: 0;
    pointer-events: none;
}

button, select {
    pointer-events: auto;
    cursor: pointer;
    border: 0;
    border-radius: 15px;
    padding: 10px 13px;
    background: #fff7ed;
    color: #6d4b3c;
    box-shadow: 0 3px 12px #6d4b3c24;
    font-weight: 700;
}

button:hover {
    background: #ffe3dd;
}

.panel {
    background: #fff9f0ed;
    border: 2px solid #edcfb8;
    border-radius: 18px;
    padding: 12px;
    box-shadow: 0 5px 20px #684b3b20;
    pointer-events: auto;
}

.top {
    position: absolute;
    top: 14px;
    left: 14px;
    display: flex;
    gap: 8px;
    align-items: center;
    flex-wrap: wrap;
}

.right {
    position: absolute;
    right: 14px;
    top: 14px;
    width: 245px;
}

.bottom {
    position: absolute;
    bottom: 18px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 8px;
    align-items: center;
    flex-wrap: wrap;
    justify-content: center;
}

.help {
    position: absolute;
    bottom: 14px;
    left: 14px;
    font-size: 12px;
    background: #fff9f0dc;
    padding: 9px;
    border-radius: 12px;
    max-width: 260px;
}

.badge {
    background: #fce5bb;
    border-radius: 10px;
    padding: 8px 10px;
    font-weight: 800;
}

.small {
    font-size: 12px;
    color: #927b6e;
    margin: 6px 0;
}

.hidden {
    display: none !important;
}

#notice {
    position: absolute;
    top: 90px;
    left: 50%;
    transform: translateX(-50%);
    padding: 10px 20px;
    background: #fff9f0ee;
    border-radius: 20px;
    font-weight: 700;
    opacity: 0;
    transition: opacity .2s;
    max-width: 80%;
    text-align: center;
}

.menu {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 7px;
}

.menu button {
    font-size: 12px;
    padding: 10px 5px;
}

.row {
    display: flex;
    gap: 6px;
    align-items: center;
    justify-content: space-between;
    margin: 8px 0;
}

#crosshair {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 25px;
    color: #876b55;
    opacity: .65;
    pointer-events: none;
}

#loading {
    position: absolute;
    inset: 0;
    display: grid;
    place-items: center;
    background: #f7e9db;
    z-index: 10;
    font-size: 20px;
    font-weight: 800;
}

#mobile {
    display: none;
}

@media(max-width:700px) {
    .right {
        top: 105px;
        width: 190px;
    }

    .top {
        right: 10px;
    }

    .help {
        display: none;
    }

    .bottom {
        bottom: 10px;
    }

    #mobile {
        display: block;
        position: absolute;
        bottom: 80px;
        left: 12px;
        pointer-events: auto;
    }

    #mobile button {
        margin: 2px;
    }
}
</style>
</head>

<body>

<div id="loading">
    🐻 카페를 준비하고 있어요...
</div>

<div id="ui">

    <div class="top">
        <div class="panel">
            <b>🐻 Cozy Bear Cafe</b>
            <div class="small">작은 디저트 카페 타이쿤</div>
        </div>

        <span class="badge" id="coins">🪙 0</span>
        <span class="badge" id="level">⭐ Lv.1</span>
    </div>

    <div class="right panel">

        <b>🍰 카페 관리</b>

        <div class="small" id="status">
            손님을 기다리는 중...
        </div>

        <div class="row">
            <span>내 캐릭터</span>

            <select id="character">
                <option value="white">코리락쿠마</option>
                <option value="brown">리락쿠마</option>
                <option value="bird">키이로이토리</option>
                <option value="little">차이로이코구마</option>
            </select>
        </div>

        <div class="row">
            <span>시점</span>
            <button id="camera">3인칭 → 1인칭</button>
        </div>

        <div class="row">
            <span>손님 주문</span>
            <b id="orders">0</b>
        </div>

        <hr style="border:0;border-top:1px solid #e8d1bd">

        <b>🛒 가구 상점</b>

        <div class="small">
            가구 구매 후 카페에 자동 설치
        </div>

        <div class="menu">
            <button data-buy="table">🪑 테이블 80</button>
            <button data-buy="plant">🌿 화분 45</button>
            <button data-buy="lamp">💡 조명 65</button>
            <button data-buy="sofa">🛋️ 소파 120</button>
        </div>

        <div class="small" id="owned">
            구매한 가구: 0개
        </div>

        <button id="save" style="width:100%">
            💾 저장하기
        </button>

    </div>

    <div id="notice"></div>
    <div id="crosshair">+</div>

    <div class="bottom">
        <button id="serve">🍮 주문 서빙 (+35)</button>
        <button id="wave">👋 인사</button>
        <button id="dance">🎵 춤추기</button>
        <button id="reset">↻ 새 게임</button>
    </div>

    <div class="help">
        WASD 이동 · Shift 달리기 · 마우스 드래그 시점 회전
        <br>
        V 시점 전환 · E 주문 서빙
        <br>
        손님에게 다가가 E를 누르면 서빙할 수 있어요.
    </div>

    <div id="mobile">
        <button data-dir="w">▲</button><br>
        <button data-dir="a">◀</button>
        <button data-dir="s">▼</button>
        <button data-dir="d">▶</button>
    </div>

</div>

<script type="module">

import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.160.1/build/three.module.js';

const $ = id => document.getElementById(id);

const scene = new THREE.Scene();

scene.background = new THREE.Color(0xf7e9d8);
scene.fog = new THREE.Fog(0xf7e9d8, 19, 42);

const camera = new THREE.PerspectiveCamera(
    65,
    innerWidth / innerHeight,
    0.08,
    100
);

const renderer = new THREE.WebGLRenderer({
    antialias: true,
    powerPreference: "high-performance"
});

// 키보드 입력을 받을 수 있도록 설정
renderer.domElement.tabIndex = 0;
renderer.domElement.style.outline = "none";
renderer.domElement.style.touchAction = "none";

// 3D 화면 클릭 시 키보드 포커스
renderer.domElement.addEventListener("pointerdown", () => {
    renderer.domElement.focus();
});

// 페이지에 포커스가 들어오면 게임 화면 활성화
window.addEventListener("focus", () => {
    renderer.domElement.focus();
});

setTimeout(() => {
    renderer.domElement.focus();
}, 700);

renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.setSize(innerWidth, innerHeight);

renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;

document.body.prepend(renderer.domElement);


// ================================================
// 조명
// ================================================

scene.add(
    new THREE.HemisphereLight(
        0xffffff,
        0xb8a38b,
        2.2
    )
);

const sun = new THREE.DirectionalLight(
    0xffffff,
    2.2
);

sun.position.set(-5, 12, 8);
sun.castShadow = true;
sun.shadow.mapSize.set(1024, 1024);

sun.shadow.camera.left = -15;
sun.shadow.camera.right = 15;
sun.shadow.camera.top = 15;
sun.shadow.camera.bottom = -15;

scene.add(sun);


// ================================================
// 재질
// ================================================

const mat = (c, roughness = 0.86) =>
    new THREE.MeshStandardMaterial({
        color: c,
        roughness
    });

const M = {
    floor: mat(0xe8c8a5),
    wall: mat(0xfff1dd),
    wood: mat(0xb88765),
    dark: mat(0x6d4a37),
    pink: mat(0xf2b6b6),
    cream: mat(0xfff3dc),
    green: mat(0x91a987),
    glass: mat(0xd2f4f1, 0.18)
};


// ================================================
// 기본 3D 도형
// ================================================

function box(parent, w, h, d, x, y, z, m) {

    const a = new THREE.Mesh(
        new THREE.BoxGeometry(w, h, d),
        m
    );

    a.position.set(x, y, z);
    a.castShadow = true;
    a.receiveShadow = true;

    parent.add(a);

    return a;
}

function sphere(
    parent, r, x, y, z, m,
    sx = 1, sy = 1, sz = 1
) {

    const a = new THREE.Mesh(
        new THREE.SphereGeometry(r, 18, 14),
        m
    );

    a.position.set(x, y, z);
    a.scale.set(sx, sy, sz);
    a.castShadow = true;

    parent.add(a);

    return a;
}

function cylinder(parent, r1, r2, h, x, y, z, m) {

    const a = new THREE.Mesh(
        new THREE.CylinderGeometry(r1, r2, h, 16),
        m
    );

    a.position.set(x, y, z);
    a.castShadow = true;

    parent.add(a);

    return a;
}


// ================================================
// 카페 내부
// ================================================

box(scene, 18, .3, 18, 0, -.15, 0, M.floor);

box(scene, 18, 4, .24, 0, 2, -9, M.wall);
box(scene, .24, 4, 18, -9, 2, 0, M.wall);
box(scene, .24, 4, 18, 9, 2, 0, M.wall);

box(scene, 18, .5, .3, 0, 3.8, -8.85, M.pink);
box(scene, 18, .2, .2, 0, .2, -8.85, M.wood);

// 카운터
box(scene, 5, 1.1, 1.5, 0, .55, -6.8, M.wood);
box(scene, 5, .13, 1.65, 0, 1.14, -6.8, M.cream);

// 장식
box(scene, 2, 1.4, .3, 0, 2.6, -8.7, M.pink);

// 디저트 진열대
box(scene, 1.2, .5, .8, -1.3, 1.5, -6.7, M.glass);

// 커피 머신
box(scene, .7, .7, .7, 1.4, 1.55, -6.7, M.dark);
box(scene, .5, .12, .4, 1.4, 1.95, -6.7, M.cream);


// ================================================
// 테이블
// ================================================

function makeTable(x, z) {

    const g = new THREE.Group();
    g.position.set(x, 0, z);

    cylinder(g, .77, .77, .12, 0, .93, 0, M.cream);
    cylinder(g, .12, .15, .9, 0, .45, 0, M.wood);
    cylinder(g, .48, .48, .09, 0, .07, 0, M.wood);

    for (let a = 0; a < 2; a++) {

        const side = a ? 1 : -1;

        box(g, .8, .12, .7, side * 1.24, .48, 0, M.pink);
        box(g, .8, .8, .12, side * 1.24, .85, side * .37, M.pink);
    }

    scene.add(g);

    return g;
}

makeTable(-4, -2);
makeTable(3, -2);


// ================================================
// 화분
// ================================================

function makePlant(x, z) {

    const g = new THREE.Group();
    g.position.set(x, 0, z);

    cylinder(
        g, .34, .25, .6,
        0, .3, 0,
        mat(0xf5c1a6)
    );

    for (let i = 0; i < 6; i++) {

        const a = i * Math.PI / 3;

        sphere(
            g,
            .3,
            Math.cos(a) * .23,
            .85 + Math.sin(i * 2) * .12,
            Math.sin(a) * .23,
            M.green,
            .8, 1.4, .8
        );
    }

    scene.add(g);
}

makePlant(-7, -7);
makePlant(7, -7);


// ================================================
// 조명 가구
// ================================================

function makeLamp(x, z) {

    const g = new THREE.Group();
    g.position.set(x, 0, z);

    cylinder(g, .15, .3, 2.5, 0, 1.25, 0, M.wood);

    sphere(
        g, .5, 0, 2.55, 0,
        mat(0xffe8a3),
        1, .6, 1
    );

    scene.add(g);
}

makeLamp(6, 5);


// ================================================
// 소파
// ================================================

function makeSofa(x, z) {

    const g = new THREE.Group();
    g.position.set(x, 0, z);

    box(g, 2, .5, .85, 0, .45, 0, M.pink);
    box(g, 2, .9, .25, 0, .9, -.4, M.pink);

    box(g, .23, .65, .9, -1, .65, 0, M.cream);
    box(g, .23, .65, .9, 1, .65, 0, M.cream);

    scene.add(g);
}

makeSofa(-5, 5);


// ================================================
// 캐릭터 색상
// ================================================

const palettes = {

    white: {
        body: 0xfff7e9,
        ear: 0xf8bfc6
    },

    brown: {
        body: 0xb9804b,
        ear: 0xe3b775
    },

    bird: {
        body: 0xffd952,
        ear: 0xffb846
    },

    little: {
        body: 0xc99767,
        ear: 0xe7ba8b
    }
};


// ================================================
// 고퀄리티 3D 캐릭터 생성
// ================================================

function bear(kind = "white") {

    const group = new THREE.Group();

    const colorSets = {

        white: {
            fur: 0xfff8ee,
            ear: 0xf3b2bd,
            muzzle: 0xffffff,
            belly: 0xffffff,
            nose: 0x503b32
        },

        brown: {
            fur: 0xb77e4c,
            ear: 0xe9c47d,
            muzzle: 0xfff4dd,
            belly: 0xffeed1,
            nose: 0x503b32
        },

        little: {
            fur: 0xc79664,
            ear: 0xe7bd89,
            muzzle: 0xffeedb,
            belly: 0xffead1,
            nose: 0x503b32
        },

        bird: {
            fur: 0xffd84c,
            ear: 0xffb84d,
            muzzle: 0xffb84d,
            belly: 0xffe47d,
            nose: 0x503b32
        }

    };

    const colors = colorSets[kind] || colorSets.white;

    function material(hex, roughness = 0.78) {

        return new THREE.MeshStandardMaterial({
            color: hex,
            roughness: roughness,
            metalness: 0
        });
    }

    const fur = material(colors.fur);
    const ear = material(colors.ear);
    const muzzle = material(colors.muzzle);
    const belly = material(colors.belly);

    const eye = material(0x211b19, 0.18);
    const nose = material(colors.nose, 0.35);
    const shine = material(0xffffff, 0.1);
    const blush = material(0xf5b4b7);

    function oval(
        x, y, z,
        sx, sy, sz,
        mat
    ) {

        const mesh = new THREE.Mesh(
            new THREE.SphereGeometry(
                1,
                48,
                32
            ),
            mat
        );

        mesh.position.set(x, y, z);
        mesh.scale.set(sx, sy, sz);

        mesh.castShadow = true;
        mesh.receiveShadow = true;

        group.add(mesh);

        return mesh;
    }

    function curvedLine(points, radius, mat) {

        const curve = new THREE.CatmullRomCurve3(
            points.map(p => new THREE.Vector3(...p))
        );

        const mesh = new THREE.Mesh(
            new THREE.TubeGeometry(
                curve,
                20,
                radius,
                8,
                false
            ),
            mat
        );

        group.add(mesh);

        return mesh;
    }

    // ============================================
    // 키이로이토리
    // ============================================

    if (kind === "bird") {

        oval(
            0, 1.02, 0,
            .55, .62, .49,
            fur
        );

        // 볼
        oval(
            -.35, .97, .29,
            .23, .23, .17,
            fur
        );

        oval(
            .35, .97, .29,
            .23, .23, .17,
            fur
        );

        // 눈
        oval(
            -.21, 1.18, .46,
            .055, .075, .035,
            eye
        );

        oval(
            .21, 1.18, .46,
            .055, .075, .035,
            eye
        );

        // 눈 하이라이트
        oval(
            -.23, 1.21, .49,
            .015, .018, .01,
            shine
        );

        oval(
            .19, 1.21, .49,
            .015, .018, .01,
            shine
        );

        // 부리
        oval(
            0, .98, .52,
            .17, .095, .16,
            ear
        );

        // 날개
        oval(
            -.53, .91, 0,
            .18, .28, .23,
            fur
        );

        oval(
            .53, .91, 0,
            .18, .28, .23,
            fur
        );

        // 발
        oval(
            -.23, .35, .20,
            .22, .09, .23,
            ear
        );

        oval(
            .23, .35, .20,
            .22, .09, .23,
            ear
        );

        // 머리 위 깃털
        oval(
            0, 1.62, 0,
            .09, .17, .09,
            fur
        );

        return group;
    }

    // ============================================
    // 리락쿠마 / 코리락쿠마
    // ============================================

    // 몸통
    oval(
        0, .72, 0,
        .47, .55, .39,
        fur
    );

    // 배
    oval(
        0, .71, .34,
        .33, .39, .12,
        belly
    );

    // 머리
    oval(
        0, 1.51, 0,
        .65, .54, .49,
        fur
    );

    // 볼의 볼륨
    oval(
        -.43, 1.34, .15,
        .24, .22, .27,
        fur
    );

    oval(
        .43, 1.34, .15,
        .24, .22, .27,
        fur
    );

    // 귀
    oval(
        -.48, 1.96, 0,
        .23, .23, .17,
        fur
    );

    oval(
        .48, 1.96, 0,
        .23, .23, .17,
        fur
    );

    // 귀 안쪽
    oval(
        -.48, 1.97, .145,
        .145, .145, .045,
        ear
    );

    oval(
        .48, 1.97, .145,
        .145, .145, .045,
        ear
    );

    // 눈
    oval(
        -.23, 1.53, .465,
        .065, .078, .035,
        eye
    );

    oval(
        .23, 1.53, .465,
        .065, .078, .035,
        eye
    );

    // 눈 반짝임
    oval(
        -.25, 1.565, .495,
        .017, .019, .012,
        shine
    );

    oval(
        .21, 1.565, .495,
        .017, .019, .012,
        shine
    );

    // 입 주변 흰색 부분
    oval(
        0, 1.29, .47,
        .25, .17, .15,
        muzzle
    );

    // 코
    oval(
        0, 1.355, .615,
        .078, .052, .035,
        nose
    );

    // 코에서 입까지 이어지는 선
    curvedLine(
        [
            [0, 1.32, .62],
            [0, 1.275, .625],
            [0, 1.245, .615]
        ],
        .012,
        nose
    );

    // 왼쪽 입
    curvedLine(
        [
            [0, 1.245, .615],
            [-.045, 1.22, .615],
            [-.09, 1.245, .59]
        ],
        .012,
        nose
    );

    // 오른쪽 입
    curvedLine(
        [
            [0, 1.245, .615],
            [.045, 1.22, .615],
            [.09, 1.245, .59]
        ],
        .012,
        nose
    );

    // 코리락쿠마 볼
    if (kind === "white") {

        oval(
            -.42, 1.34, .425,
            .11, .055, .015,
            blush
        );

        oval(
            .42, 1.34, .425,
            .11, .055, .015,
            blush
        );
    }

    // 팔
    const leftArm = oval(
        -.50, .78, .04,
        .18, .28, .20,
        fur
    );

    leftArm.rotation.z = -.18;

    const rightArm = oval(
        .50, .78, .04,
        .18, .28, .20,
        fur
    );

    rightArm.rotation.z = .18;

    // 다리
    oval(
        -.25, .22, .14,
        .27, .20, .29,
        fur
    );

    oval(
        .25, .22, .14,
        .27, .20, .29,
        fur
    );

    // 발바닥
    oval(
        -.25, .20, .405,
        .14, .09, .018,
        ear
    );

    oval(
        .25, .20, .405,
        .14, .09, .018,
        ear
    );

    // 꼬리
    oval(
        0, .47, -.39,
        .16, .16, .14,
        fur
    );

    return group;
}


// ================================================
// 플레이어 캐릭터
// ================================================

const player = new THREE.Group();

scene.add(player);

let character =
    localStorage.getItem('cozy_character') || 'white';

function setCharacter(k) {

    character = k;

    while (player.children.length) {
        player.remove(player.children[0]);
    }

    player.add(bear(k));

    $('character').value = k;

    localStorage.setItem('cozy_character', k);
}

setCharacter(character);

player.position.set(0, 0, 4);


// ================================================
// 게임 데이터
// ================================================

let state;

function initial() {
    return {
        coins: 150,
        level: 1,
        xp: 0,
        bought: [],
        served: 0
    };
}

try {
    state =
        JSON.parse(localStorage.getItem('cozy_cafe_save'))
        || initial();
} catch {
    state = initial();
}

if (
    !Number.isFinite(state.coins) ||
    !Array.isArray(state.bought)
) {
    state = initial();
}

const save = () =>
    localStorage.setItem(
        'cozy_cafe_save',
        JSON.stringify(state)
    );

function ui() {

    $('coins').textContent = '🪙 ' + state.coins;

    $('level').textContent = '⭐ Lv.' + state.level;

    $('owned').textContent =
        '구매한 가구: ' + state.bought.length + '개';

    $('orders').textContent =
        guests.filter(x => x.ready).length;
}


// ================================================
// 알림 메시지
// ================================================

let timer;

function notify(t) {

    $('notice').textContent = t;
    $('notice').style.opacity = 1;

    clearTimeout(timer);

    timer = setTimeout(
        () => $('notice').style.opacity = 0,
        2300
    );
}


// ================================================
// 손님 NPC
// ================================================

const guests = [];

function addGuest(i) {

    const g = new THREE.Group();

    g.add(
        bear(
            ['brown', 'white', 'little', 'bird'][i % 4]
        )
    );

    g.position.set(-7 + i * 1.5, 0, -3.8);

    scene.add(g);

    guests.push({
        group: g,
        ready: true,
        t: Math.random() * 10,
        goal: new THREE.Vector3(-4 + i * 2, 0, -2)
    });
}

for (let i = 0; i < 3; i++) {
    addGuest(i);
}


// ================================================
// 가구 구매
// ================================================

const costs = {
    table: 80,
    plant: 45,
    lamp: 65,
    sofa: 120
};

let furnitureIndex = 0;

function purchase(k) {

    const cost = costs[k];

    if (state.coins < cost) {
        notify('🪙 돈이 부족해요! 주문을 서빙해 보세요.');
        return;
    }

    state.coins -= cost;
    state.bought.push(k);

    install(k, furnitureIndex++);

    save();
    ui();

    notify('✨ 새 가구를 설치했어요!');
}

function install(k, i) {

    const x = -6 + (i % 5) * 2.8;
    const z = 2 + Math.floor(i / 5) * 2.5;

    if (k === 'table') makeTable(x, z);
    if (k === 'plant') makePlant(x, z);
    if (k === 'lamp') makeLamp(x, z);
    if (k === 'sofa') makeSofa(x, z);
}

state.bought.forEach(
    (k, i) => install(k, i)
);

furnitureIndex = state.bought.length;


// ================================================
// 디저트 서빙
// ================================================

function serve() {

    const close = guests
        .filter(
            g =>
                g.ready &&
                g.group.position.distanceTo(player.position) < 3.5
        )
        .sort(
            (a, b) =>
                a.group.position.distanceTo(player.position) -
                b.group.position.distanceTo(player.position)
        );

    if (!close.length) {

        notify('🍰 주문 중인 손님에게 가까이 가세요!');
        return;
    }

    const g = close[0];

    g.ready = false;
    g.t = 0;

    state.coins += 35;
    state.xp += 1;
    state.served += 1;

    if (state.xp >= 5) {

        state.xp = 0;
        state.level++;

        notify('🎉 레벨 업! Lv.' + state.level);

    } else {

        notify('🍮 서빙 완료! +35 코인');
    }

    save();
    ui();
}


// ================================================
// 버튼 이벤트
// ================================================

$('serve').onclick = serve;

$('save').onclick = () => {
    save();
    notify('💾 저장했어요!');
};

document.querySelectorAll('[data-buy]').forEach(
    b => b.onclick = () => purchase(b.dataset.buy)
);

$('character').onchange = e => {

    setCharacter(e.target.value);

    notify('🐻 캐릭터를 변경했어요!');
};

$('reset').onclick = () => {

    if (confirm('저장된 카페를 초기화할까요?')) {

        localStorage.removeItem('cozy_cafe_save');

        location.reload();
    }
};


// ================================================
// 카메라
// ================================================

let firstPerson = false;

let yaw = 0;
let pitch = .26;

let drag = false;

let lastX = 0;
let lastY = 0;

let emote = 0;

function toggleCamera() {

    firstPerson = !firstPerson;

    $('camera').textContent = firstPerson
        ? '1인칭 → 3인칭'
        : '3인칭 → 1인칭';
}

$('camera').onclick = toggleCamera;

$('wave').onclick = () => {

    emote = 1.5;

    notify('👋 안녕!');
};

$('dance').onclick = () => {

    emote = 3;

    notify('🎵 신나는 댄스!');
};


// ================================================
// 키보드 이동 시스템
// ================================================

const keys = {};

function focusGame() {
    renderer.domElement.focus();
}

renderer.domElement.tabIndex = 0;
renderer.domElement.style.outline = "none";

renderer.domElement.addEventListener(
    "pointerdown",
    focusGame
);

window.addEventListener("keydown", (event) => {

    const key = event.key.toLowerCase();

    if (
        event.target.tagName === "INPUT" ||
        event.target.tagName === "SELECT" ||
        event.target.tagName === "TEXTAREA"
    ) {
        return;
    }

    const controlledKeys = [
        "w", "a", "s", "d",
        "arrowup", "arrowdown",
        "arrowleft", "arrowright",
        "shift", "v", "e"
    ];

    if (controlledKeys.includes(key)) {
        event.preventDefault();
    }

    keys[key] = true;

    if (event.repeat) return;

    if (key === "v") {
        toggleCamera();
    }

    if (key === "e") {
        serve();
    }

});

window.addEventListener("keyup", (event) => {
    keys[event.key.toLowerCase()] = false;
});

window.addEventListener("blur", () => {
    Object.keys(keys).forEach(key => {
        keys[key] = false;
    });
});

setTimeout(focusGame, 600);

// ================================================
// 마우스 시점 조절
// ================================================

renderer.domElement.addEventListener(
    'pointerdown',
    e => {

        drag = true;

        lastX = e.clientX;
        lastY = e.clientY;

        renderer.domElement.setPointerCapture(e.pointerId);
    }
);

renderer.domElement.addEventListener(
    'pointerup',
    () => drag = false
);

renderer.domElement.addEventListener(
    'pointermove',
    e => {

        if (!drag) return;

        yaw -= (e.clientX - lastX) * .005;

        pitch = THREE.MathUtils.clamp(
            pitch + (e.clientY - lastY) * .004,
            -.25,
            1.1
        );

        lastX = e.clientX;
        lastY = e.clientY;
    }
);


// ================================================
// 모바일 이동 버튼
// ================================================

document.querySelectorAll('[data-dir]').forEach(b => {

    b.onpointerdown = e => {

        e.preventDefault();

        keys[b.dataset.dir] = true;
    };

    b.onpointerup = b.onpointercancel = () => {
        keys[b.dataset.dir] = false;
    };
});


// ================================================
// 게임 애니메이션
// ================================================

const clock = new THREE.Clock();

const target = new THREE.Vector3();
const wanted = new THREE.Vector3();

function animate() {

    requestAnimationFrame(animate);

    const dt = Math.min(clock.getDelta(), .05);
    const time = clock.elapsedTime;

const f =
    Number(Boolean(keys.w || keys.arrowup)) -
    Number(Boolean(keys.s || keys.arrowdown));

const r =
    Number(Boolean(keys.d || keys.arrowright)) -
    Number(Boolean(keys.a || keys.arrowleft));

    const speed = keys.shift ? 5.4 : 3.1;

    const dir = new THREE.Vector3(
        Math.sin(yaw) * f + Math.cos(yaw) * r,
        0,
        -Math.cos(yaw) * f + Math.sin(yaw) * r
    );

    if (dir.lengthSq()) {

        dir.normalize();

        player.position.addScaledVector(
            dir,
            dt * speed
        );

        player.rotation.y = Math.atan2(dir.x, dir.z);

        player.position.x = THREE.MathUtils.clamp(
            player.position.x,
            -8.1,
            8.1
        );

        player.position.z = THREE.MathUtils.clamp(
            player.position.z,
            -8.1,
            8.1
        );
    }

    player.children[0].position.y = dir.lengthSq()
        ? Math.abs(Math.sin(time * 11)) * .045
        : Math.sin(time * 2) * .015;

    if (emote > 0) {

        emote -= dt;

        player.children[0].rotation.z =
            Math.sin(time * 14) * .18;

    } else {

        player.children[0].rotation.z = 0;
    }

    player.children[0].visible = !firstPerson;


    // 손님 애니메이션
    for (const g of guests) {

        g.t += dt;

        if (!g.ready && g.t > 7) {

            g.ready = true;
            g.t = 0;
        }

        g.group.position.y =
            Math.sin(time * 2 + g.t) * .02;

        g.group.rotation.y =
            Math.sin(time * .6 + g.t) * .25;
    }


    // 카메라 위치
    target.copy(player.position).add(
        new THREE.Vector3(0, 1.4, 0)
    );

    const horizontal = new THREE.Vector3(
        Math.sin(yaw),
        0,
        -Math.cos(yaw)
    );

    if (firstPerson) {

        wanted.copy(target);

        camera.position.lerp(wanted, .23);

        camera.lookAt(
            target.clone()
                .add(horizontal.multiplyScalar(4))
                .add(
                    new THREE.Vector3(
                        0,
                        -Math.tan(pitch) * 3,
                        0
                    )
                )
        );

    } else {

        wanted.copy(target)
            .addScaledVector(
                horizontal,
                -5 * Math.cos(pitch)
            )
            .add(
                new THREE.Vector3(
                    0,
                    2 + 5 * Math.sin(pitch),
                    0
                )
            );

        camera.position.lerp(wanted, .13);

        camera.lookAt(target);
    }

    renderer.render(scene, camera);
}


// ================================================
// 화면 크기 변경
// ================================================

addEventListener('resize', () => {

    camera.aspect = innerWidth / innerHeight;

    camera.updateProjectionMatrix();

    renderer.setSize(innerWidth, innerHeight);
});

ui();

$('loading').remove();

notify('🐻 WASD로 움직여 손님에게 디저트를 서빙하세요!');

animate();

</script>

</body>
</html>
'''

components.html(
    html,
    height=850,
    scrolling=False
)
