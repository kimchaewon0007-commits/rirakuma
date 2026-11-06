import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Rilakkuma Dessert Cafe 3D",
    page_icon="🐻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
        visibility: hidden;
    }
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    .stApp {
        background: #f8eadc;
    }
    iframe {
        display: block;
    }
</style>
""", unsafe_allow_html=True)

html = r"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">

<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    overflow: hidden;
    font-family: "Apple SD Gothic Neo", Arial, sans-serif;
    background: #f8eadc;
    color: #654735;
}

button, select {
    cursor: pointer;
    border: 1px solid #e9cdb4;
    border-radius: 12px;
    background: #fff9ee;
    color: #654735;
    padding: 9px 12px;
    font-weight: bold;
}

button:hover {
    background: #ffe4d6;
}

button:active {
    transform: scale(.97);
}

#game {
    position: fixed;
    inset: 0;
}

#game canvas {
    display: block;
    outline: none;
}

#ui {
    position: fixed;
    inset: 0;
    pointer-events: none;
}

#ui button,
#ui select,
.panel {
    pointer-events: auto;
}

.panel {
    background: rgba(255, 250, 242, .95);
    border: 2px solid #e9d0b7;
    border-radius: 18px;
    padding: 13px;
    box-shadow: 0 5px 22px #6c493522;
}

#top {
    position: absolute;
    top: 15px;
    left: 15px;
    display: flex;
    align-items: flex-start;
    gap: 10px;
}

#title {
    font-size: 17px;
    font-weight: 900;
}

.subtitle {
    font-size: 11px;
    margin-top: 4px;
    color: #a18572;
}

.badge {
    background: #fff5d8;
    border: 2px solid #eed7a5;
    border-radius: 15px;
    padding: 11px;
    font-weight: 900;
}

#shop {
    position: absolute;
    top: 15px;
    right: 15px;
    width: 260px;
    max-height: 77vh;
    overflow-y: auto;
}

.section {
    margin: 12px 0 8px;
    font-weight: 900;
    color: #a66e58;
}

.row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 6px;
    margin: 9px 0;
    font-size: 13px;
}

.row select {
    max-width: 145px;
}

.grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 7px;
}

.grid button {
    font-size: 12px;
    padding: 11px 4px;
}

#bottom {
    position: absolute;
    left: 50%;
    bottom: 18px;
    transform: translateX(-50%);
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 8px;
}

#hint {
    position: absolute;
    left: 15px;
    bottom: 15px;
    background: #fff9edeb;
    border-radius: 12px;
    padding: 11px;
    font-size: 12px;
    line-height: 1.8;
}

#message {
    position: absolute;
    top: 95px;
    left: 50%;
    transform: translateX(-50%);
    background: #fffaf1;
    border: 2px solid #f0d5b9;
    border-radius: 20px;
    padding: 12px 20px;
    font-weight: bold;
    opacity: 0;
    transition: opacity .25s;
    text-align: center;
    max-width: 75%;
}

#loading {
    position: fixed;
    inset: 0;
    z-index: 100;
    display: flex;
    justify-content: center;
    align-items: center;
    background: #f8eadc;
    font-size: 23px;
    font-weight: 900;
}

#focus {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    font-size: 20px;
    opacity: .4;
}

@media(max-width:700px) {
    #shop {
        width: 190px;
        top: 110px;
    }
    #hint {
        display: none;
    }
    #top {
        flex-wrap: wrap;
        right: 10px;
    }
}
</style>
</head>

<body>

<div id="game"></div>

<div id="loading">🐻 카페를 준비하고 있어요...</div>

<div id="ui">

    <div id="top">
        <div class="panel">
            <div id="title">🐻 Rilakkuma Cafe</div>
            <div class="subtitle">Cozy Dessert Tycoon</div>
        </div>

        <div class="badge" id="coins">🪙 150</div>
        <div class="badge" id="level">⭐ Lv.1</div>
    </div>

    <div id="shop" class="panel">

        <div class="section">🧸 캐릭터</div>

        <div class="row">
            <span>캐릭터 선택</span>
            <select id="character">
                <option value="white">코리락쿠마</option>
                <option value="brown">리락쿠마</option>
                <option value="bird">키이로이토리</option>
                <option value="little">차이로이코구마</option>
            </select>
        </div>

        <div class="row">
            <span>시점 변경</span>
            <button id="view">3인칭</button>
        </div>

        <div class="section">🍰 카페 운영</div>

        <div class="row">
            <span>대기 주문</span>
            <b id="orders">0</b>
        </div>

        <div class="row">
            <span>판매한 디저트</span>
            <b id="served">0</b>
        </div>

        <div class="section">🛍️ 인테리어 상점</div>

        <div class="grid">
            <button data-buy="table">🪑 테이블<br>80🪙</button>
            <button data-buy="plant">🌷 화분<br>45🪙</button>
            <button data-buy="lamp">💡 조명<br>65🪙</button>
            <button data-buy="sofa">🛋️ 소파<br>120🪙</button>
        </div>

        <div class="row">
            <span>구매한 가구</span>
            <b id="furniture">0</b>
        </div>

        <button id="save" style="width:100%;margin-top:8px;">
            💾 게임 저장
        </button>

    </div>

    <div id="message"></div>

    <div id="focus">+</div>

    <div id="bottom">
        <button id="serve">🍮 디저트 서빙</button>
        <button id="wave">👋 손 흔들기</button>
        <button id="dance">🎵 춤추기</button>
        <button id="reset">🔄 초기화</button>
    </div>

    <div id="hint">
        🎮 WASD 이동 / Shift 달리기<br>
        🖱️ 마우스 드래그로 시점 회전<br>
        V 시점 변경 / E 디저트 서빙<br>
        게임 화면을 클릭한 뒤 이동하세요.
    </div>

</div>

<script type="module">

import * as THREE from
"https://cdn.jsdelivr.net/npm/three@0.160.1/build/three.module.js";

const $ = id => document.getElementById(id);

// ============================================
// 기본 3D 환경
// ============================================

const scene = new THREE.Scene();

scene.background = new THREE.Color(0xf8e8d7);
scene.fog = new THREE.Fog(0xf8e8d7, 25, 55);

const camera = new THREE.PerspectiveCamera(
    60,
    window.innerWidth / window.innerHeight,
    0.1,
    100
);

const renderer = new THREE.WebGLRenderer({
    antialias: true,
    powerPreference: "high-performance"
});

renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;

renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.45;

$("game").appendChild(renderer.domElement);

renderer.domElement.tabIndex = 0;
renderer.domElement.style.outline = "none";
renderer.domElement.style.touchAction = "none";

renderer.domElement.addEventListener("pointerdown", () => {
    renderer.domElement.focus();
});

// ============================================
// 조명
// ============================================

scene.add(
    new THREE.HemisphereLight(
        0xffffff,
        0xc8a990,
        2.3
    )
);

const sunlight = new THREE.DirectionalLight(
    0xfff5e5,
    2.8
);

sunlight.position.set(-6, 13, 7);
sunlight.castShadow = true;
sunlight.shadow.mapSize.set(2048, 2048);

sunlight.shadow.camera.left = -15;
sunlight.shadow.camera.right = 15;
sunlight.shadow.camera.top = 15;
sunlight.shadow.camera.bottom = -15;

sunlight.shadow.bias = -0.0003;

scene.add(sunlight);

// ============================================
// 재질
// ============================================

function material(color, roughness = .8) {
    return new THREE.MeshStandardMaterial({
        color,
        roughness,
        metalness: 0
    });
}

const materials = {
    floor: material(0xe5c49f),
    wall: material(0xffefdc),
    wood: material(0xb78660),
    darkWood: material(0x80563e),
    cream: material(0xfff5e5),
    pink: material(0xf0b7b7),
    green: material(0x91ab83),
    yellow: material(0xffe5a4),
    glass: new THREE.MeshPhysicalMaterial({
        color: 0xe8ffff,
        transparent: true,
        opacity: .48,
        roughness: .1,
        metalness: 0,
        depthWrite: false
    })
};

// ============================================
// 기본 도형 생성
// ============================================

function cube(parent, w, h, d, x, y, z, mat) {

    const mesh = new THREE.Mesh(
        new THREE.BoxGeometry(w, h, d),
        mat
    );

    mesh.position.set(x, y, z);
    mesh.castShadow = true;
    mesh.receiveShadow = true;

    parent.add(mesh);

    return mesh;
}

function ball(parent, x, y, z, sx, sy, sz, mat) {

    const mesh = new THREE.Mesh(
        new THREE.SphereGeometry(1, 40, 28),
        mat
    );

    mesh.position.set(x, y, z);
    mesh.scale.set(sx, sy, sz);

    mesh.castShadow = true;
    mesh.receiveShadow = true;

    parent.add(mesh);

    return mesh;
}

function cylinder(parent, top, bottom, height, x, y, z, mat) {

    const mesh = new THREE.Mesh(
        new THREE.CylinderGeometry(
            top, bottom, height, 32
        ),
        mat
    );

    mesh.position.set(x, y, z);
    mesh.castShadow = true;
    mesh.receiveShadow = true;

    parent.add(mesh);

    return mesh;
}

// ============================================
// 카페 건물
// ============================================

cube(scene, 18, .3, 18, 0, -.15, 0, materials.floor);

cube(scene, 18, 4.5, .25, 0, 2.25, -9, materials.wall);
cube(scene, .25, 4.5, 18, -9, 2.25, 0, materials.wall);
cube(scene, .25, 4.5, 18, 9, 2.25, 0, materials.wall);

// 벽 장식
cube(scene, 18, .25, .3, 0, 4.1, -8.85, materials.pink);
cube(scene, 18, .2, .3, 0, .3, -8.85, materials.wood);

// 카운터
cube(scene, 5.5, 1.1, 1.6, 0, .55, -6.8, materials.wood);
cube(scene, 5.7, .15, 1.8, 0, 1.15, -6.8, materials.cream);

// 디저트 진열장
cube(scene, 2.0, .75, .9, -1.4, 1.62, -6.8, materials.glass);

// 진열장 안 디저트
const dessertPink = material(0xf3a6af);
const dessertCream = material(0xffefca);
const dessertBrown = material(0x9a654b);

for (let i = 0; i < 4; i++) {

    const x = -2.05 + i * .43;

    cylinder(
        scene, .17, .19, .18,
        x, 1.36, -6.4,
        i % 2 ? dessertPink : dessertCream
    );

    ball(
        scene,
        x, 1.51, -6.4,
        .12, .09, .12,
        i % 2 ? dessertCream : dessertBrown
    );
}

// 커피 머신
cube(scene, .8, .8, .7, 1.5, 1.62, -6.8, materials.darkWood);
cube(scene, .65, .15, .45, 1.5, 2.08, -6.8, materials.cream);

// ============================================
// 가구
// ============================================

function makeTable(x, z) {

    const g = new THREE.Group();
    g.position.set(x, 0, z);

    cylinder(g, .78, .78, .13, 0, .93, 0, materials.cream);
    cylinder(g, .13, .17, .85, 0, .47, 0, materials.wood);
    cylinder(g, .45, .45, .08, 0, .07, 0, materials.darkWood);

    for (const side of [-1, 1]) {

        cube(
            g, .75, .13, .7,
            side * 1.2, .5, 0,
            materials.pink
        );

        cube(
            g, .75, .7, .13,
            side * 1.2, .9, -.3,
            materials.pink
        );
    }

    scene.add(g);
    return g;
}

function makePlant(x, z) {

    const g = new THREE.Group();
    g.position.set(x, 0, z);

    cylinder(g, .34, .24, .6, 0, .3, 0, materials.pink);

    for (let i = 0; i < 7; i++) {

        const a = i * Math.PI * 2 / 7;

        ball(
            g,
            Math.cos(a) * .24,
            .86 + Math.sin(i * 2) * .1,
            Math.sin(a) * .24,
            .24, .38, .22,
            materials.green
        );
    }

    scene.add(g);
    return g;
}

function makeLamp(x, z) {

    const g = new THREE.Group();
    g.position.set(x, 0, z);

    cylinder(g, .12, .22, 2.4, 0, 1.2, 0, materials.wood);

    ball(
        g, 0, 2.45, 0,
        .48, .32, .48,
        materials.yellow
    );

    scene.add(g);
    return g;
}

function makeSofa(x, z) {

    const g = new THREE.Group();
    g.position.set(x, 0, z);

    cube(g, 2, .5, .9, 0, .4, 0, materials.pink);
    cube(g, 2, .85, .25, 0, .85, -.4, materials.pink);

    cube(g, .25, .65, .9, -1, .65, 0, materials.cream);
    cube(g, .25, .65, .9, 1, .65, 0, materials.cream);

    scene.add(g);
    return g;
}

makeTable(-4, -2);
makeTable(3, -2);
makePlant(-7, -7);
makePlant(7, -7);
makeLamp(6, 5);
makeSofa(-5, 5);

// ============================================
// 캐릭터 제작
// ============================================

function createCharacter(kind = "white") {

    const root = new THREE.Group();
    const model = new THREE.Group();

    root.add(model);

    const palettes = {
        white: {
            fur: 0xfff8ed,
            ear: 0xf4a9bc,
            muzzle: 0xffffff,
            belly: 0xffffff
        },
        brown: {
            fur: 0xb77b43,
            ear: 0xe8bf70,
            muzzle: 0xfff5e2,
            belly: 0xfff0d5
        },
        little: {
            fur: 0xc99762,
            ear: 0xe8bd88,
            muzzle: 0xfff1df,
            belly: 0xffead2
        },
        bird: {
            fur: 0xffd74e,
            ear: 0xffa63e,
            muzzle: 0xffa63e,
            belly: 0xffe77e
        }
    };

    const p = palettes[kind] || palettes.white;

    const fur = material(p.fur, .9);
    const ear = material(p.ear, .85);
    const muzzle = material(p.muzzle, .85);
    const belly = material(p.belly, .85);

    const eye = material(0x241b19, .42);
    const nose = material(0x382820, .65);
    const blush = material(0xf2b0b8, .9);
    const red = material(0xc93836, .45);
    const white = material(0xffffff);

    const parts = {};

    function oval(parent, x, y, z, sx, sy, sz, mat) {
        return ball(parent, x, y, z, sx, sy, sz, mat);
    }

    function line(parent, points, radius, mat) {

        const curve = new THREE.CatmullRomCurve3(
            points.map(p => new THREE.Vector3(...p))
        );

        const mesh = new THREE.Mesh(
            new THREE.TubeGeometry(curve, 20, radius, 8, false),
            mat
        );

        parent.add(mesh);
        return mesh;
    }

    if (kind === "bird") {

        oval(model, 0, 1.0, 0, .54, .62, .48, fur);

        oval(model, -.21, 1.17, .46, .055, .07, .035, eye);
        oval(model, .21, 1.17, .46, .055, .07, .035, eye);

        oval(model, 0, .98, .52, .17, .09, .14, ear);

        parts.leftArm = new THREE.Group();
        parts.rightArm = new THREE.Group();

        parts.leftArm.position.set(-.48, .95, 0);
        parts.rightArm.position.set(.48, .95, 0);

        oval(parts.leftArm, -.08, -.07, 0, .18, .27, .22, fur);
        oval(parts.rightArm, .08, -.07, 0, .18, .27, .22, fur);

        model.add(parts.leftArm, parts.rightArm);

        parts.leftLeg = new THREE.Group();
        parts.rightLeg = new THREE.Group();

        parts.leftLeg.position.set(-.23, .4, .1);
        parts.rightLeg.position.set(.23, .4, .1);

        oval(parts.leftLeg, 0, -.12, .1, .19, .1, .22, ear);
        oval(parts.rightLeg, 0, -.12, .1, .19, .1, .22, ear);

        model.add(parts.leftLeg, parts.rightLeg);

        oval(model, 0, 1.61, 0, .09, .16, .09, fur);

        root.userData = { model, parts };
        return root;
    }

    // 몸통
    oval(model, 0, .74, 0, .46, .54, .38, fur);

    // 배
    oval(model, 0, .72, .34, .31, .37, .105, belly);

// 머리 - 앞면이 조금 더 평평한 형태
oval(
    model,
    0, 1.51, -0.025,
    0.65, 0.53, 0.46,
    fur
);
    // 귀
    oval(model, -.47, 1.96, 0, .22, .22, .16, fur);
    oval(model, .47, 1.96, 0, .22, .22, .16, fur);

    oval(model, -.47, 1.97, .145, .14, .14, .04, ear);
    oval(model, .47, 1.97, .145, .14, .14, .04, ear);

// ============================================
// 코리락쿠마 / 리락쿠마 얼굴 비율 개선
// ============================================

// 눈 - 사진처럼 크고 둥근 검은 눈
// 눈 사이 간격을 넓히고 높이를 약간 낮춤

oval(
    model,
    -0.265, 1.49, 0.444,
    0.082, 0.092, 0.040,
    eye
);

oval(
    model,
    0.265, 1.49, 0.444,
    0.082, 0.092, 0.040,
    eye
);


// ============================================
// 흰색 주둥이
// ============================================

// 얼굴 표면에 붙어 있는 납작한 타원형
// 기존보다 약간 넓고 높이는 낮게

oval(
    model,
    0, 1.285, 0.473,
    0.235, 0.165, 0.055,
    muzzle
);


// ============================================
// 코 - 둥근 역삼각형
// ============================================

const noseShape = new THREE.Shape();

noseShape.moveTo(-0.075, 0.025);

noseShape.bezierCurveTo(
    -0.085, 0.075,
    0.085, 0.075,
    0.075, 0.025
);

noseShape.bezierCurveTo(
    0.065, -0.005,
    0.025, -0.045,
    0, -0.050
);

noseShape.bezierCurveTo(
    -0.025, -0.045,
    -0.065, -0.005,
    -0.075, 0.025
);

const noseGeometry = new THREE.ShapeGeometry(
    noseShape,
    24
);

const noseObject = new THREE.Mesh(
    noseGeometry,
    nose
);

noseObject.position.set(
    0,
    1.345,
    0.536
);

model.add(noseObject);


// ============================================
// 입 - 사진처럼 ㅅ 모양
// ============================================

// 코 바로 아래에서 시작하는 입
// 가운데가 높고 양쪽 끝이 아래로 내려감

line(
    model,
    [
        [-0.115, 1.225, 0.524],
        [-0.085, 1.238, 0.531],
        [-0.045, 1.275, 0.537],
        [0, 1.300, 0.540]
    ],
    0.016,
    nose
);

line(
    model,
    [
        [0, 1.300, 0.540],
        [0.045, 1.275, 0.537],
        [0.085, 1.238, 0.531],
        [0.115, 1.225, 0.524]
    ],
    0.016,
    nose
);


// ============================================
// 코리락쿠마 빨간 단추
// ============================================

if (kind === "white") {

    // 빨간 단추
    oval(
        model,
        0, 0.87, 0.41,
        0.105, 0.105, 0.045,
        red
    );

    // 단추 구멍 4개
    for (const x of [-0.035, 0.035]) {

        for (const y of [-0.035, 0.035]) {

            oval(
                model,
                x,
                0.87 + y,
                0.455,
                0.012,
                0.012,
                0.006,
                white
            );
        }
    }
}
    // 움직이는 팔
    parts.leftArm = new THREE.Group();
    parts.rightArm = new THREE.Group();

    parts.leftArm.position.set(-.47, .94, 0);
    parts.rightArm.position.set(.47, .94, 0);

    oval(
        parts.leftArm,
        -.07, -.19, .03,
        .18, .27, .19,
        fur
    );

    oval(
        parts.rightArm,
        .07, -.19, .03,
        .18, .27, .19,
        fur
    );

    model.add(parts.leftArm, parts.rightArm);

    // 움직이는 다리
    parts.leftLeg = new THREE.Group();
    parts.rightLeg = new THREE.Group();

    parts.leftLeg.position.set(-.24, .38, .08);
    parts.rightLeg.position.set(.24, .38, .08);

    oval(
        parts.leftLeg,
        0, -.15, .08,
        .26, .20, .28,
        fur
    );

    oval(
        parts.rightLeg,
        0, -.15, .08,
        .26, .20, .28,
        fur
    );

    model.add(parts.leftLeg, parts.rightLeg);

    // 꼬리
    oval(model, 0, .45, -.38, .15, .15, .14, fur);

    root.userData = { model, parts };

    return root;
}

// ============================================
// 플레이어
// ============================================

const player = new THREE.Group();
scene.add(player);

let selectedCharacter =
    localStorage.getItem("cafe_character") || "white";

let characterModel = null;

function changeCharacter(kind) {

    selectedCharacter = kind;

    if (characterModel) {
        player.remove(characterModel);
    }

    characterModel = createCharacter(kind);
    characterModel.scale.setScalar(1.1);

    player.add(characterModel);

    $("character").value = kind;

    localStorage.setItem("cafe_character", kind);
}

changeCharacter(selectedCharacter);

player.position.set(0, 0, 4);

// ============================================
// 게임 데이터
// ============================================

function newGame() {
    return {
        coins: 150,
        level: 1,
        xp: 0,
        served: 0,
        furniture: []
    };
}

let state;

try {
    state = JSON.parse(
        localStorage.getItem("rilakkuma_cafe_save")
    ) || newGame();
} catch {
    state = newGame();
}

if (
    !Number.isFinite(state.coins) ||
    !Array.isArray(state.furniture)
) {
    state = newGame();
}

function saveGame() {
    localStorage.setItem(
        "rilakkuma_cafe_save",
        JSON.stringify(state)
    );
}

let noticeTimer;

function notify(message) {

    $("message").textContent = message;
    $("message").style.opacity = 1;

    clearTimeout(noticeTimer);

    noticeTimer = setTimeout(() => {
        $("message").style.opacity = 0;
    }, 2400);
}

function updateUI() {

    $("coins").textContent = "🪙 " + state.coins;
    $("level").textContent = "⭐ Lv." + state.level;
    $("served").textContent = state.served;
    $("furniture").textContent = state.furniture.length;

    $("orders").textContent =
        guests.filter(g => g.ready).length;
}

// ============================================
// 손님
// ============================================

const guests = [];

function createGuest(i) {

    const kinds = [
        "brown",
        "little",
        "bird",
        "white"
    ];

    const model = createCharacter(kinds[i % kinds.length]);

    model.position.set(-5 + i * 3.5, 0, -2.8);

    scene.add(model);

    guests.push({
        model,
        ready: true,
        timer: 0,
        phase: Math.random() * 10
    });
}

for (let i = 0; i < 3; i++) {
    createGuest(i);
}

// ============================================
// 가구 구매
// ============================================

const prices = {
    table: 80,
    plant: 45,
    lamp: 65,
    sofa: 120
};

function installFurniture(type, index) {

    const x = -6 + (index % 5) * 2.8;
    const z = 2 + Math.floor(index / 5) * 2.5;

    if (type === "table") makeTable(x, z);
    if (type === "plant") makePlant(x, z);
    if (type === "lamp") makeLamp(x, z);
    if (type === "sofa") makeSofa(x, z);
}

state.furniture.forEach((type, index) => {
    installFurniture(type, index);
});

function buyFurniture(type) {

    const price = prices[type];

    if (state.coins < price) {
        notify("🪙 코인이 부족해요!");
        return;
    }

    state.coins -= price;

    const index = state.furniture.length;

    state.furniture.push(type);

    installFurniture(type, index);

    saveGame();
    updateUI();

    notify("✨ 새로운 가구를 구매했어요!");
}

// ============================================
// 디저트 서빙
// ============================================

function serveDessert() {

    const nearby = guests
        .filter(g => g.ready)
        .map(g => ({
            guest: g,
            distance: g.model.position.distanceTo(player.position)
        }))
        .filter(g => g.distance < 3.5)
        .sort((a, b) => a.distance - b.distance);

    if (nearby.length === 0) {
        notify("🍰 주문 중인 손님에게 가까이 가세요!");
        return;
    }

    const guest = nearby[0].guest;

    guest.ready = false;
    guest.timer = 0;

    state.coins += 35;
    state.xp += 1;
    state.served += 1;

    if (state.xp >= 5) {
        state.xp = 0;
        state.level += 1;
        notify("🎉 레벨 업! Lv." + state.level);
    } else {
        notify("🍮 디저트 판매 완료! +35코인");
    }

    saveGame();
    updateUI();
}

// ============================================
// 버튼
// ============================================

document.querySelectorAll("[data-buy]").forEach(button => {

    button.addEventListener("click", () => {
        buyFurniture(button.dataset.buy);
    });
});

$("serve").onclick = serveDessert;

$("save").onclick = () => {
    saveGame();
    notify("💾 게임이 저장되었어요!");
};

$("character").onchange = event => {
    changeCharacter(event.target.value);
    notify("🐻 캐릭터를 변경했어요!");
};

$("reset").onclick = () => {

    if (confirm("카페를 처음부터 다시 시작할까요?")) {

        localStorage.removeItem("rilakkuma_cafe_save");
        location.reload();
    }
};

// ============================================
// 카메라
// ============================================

let firstPerson = false;
let yaw = 0;
let pitch = .25;

$("view").onclick = toggleView;

function toggleView() {

    firstPerson = !firstPerson;

    $("view").textContent =
        firstPerson ? "1인칭" : "3인칭";
}

// ============================================
// 키보드
// ============================================

const keys = Object.create(null);

function isTyping(element) {

    if (!element) return false;

    return (
        ["INPUT", "SELECT", "TEXTAREA"].includes(element.tagName) ||
        element.isContentEditable
    );
}

window.addEventListener("keydown", event => {

    if (isTyping(event.target)) return;

    const key = event.key.toLowerCase();

    if ([
        "w", "a", "s", "d",
        "arrowup", "arrowdown",
        "arrowleft", "arrowright",
        "shift", "v", "e"
    ].includes(key)) {
        event.preventDefault();
    }

    keys[key] = true;

    if (event.repeat) return;

    if (key === "v") toggleView();
    if (key === "e") serveDessert();

}, { passive: false });

window.addEventListener("keyup", event => {
    keys[event.key.toLowerCase()] = false;
});

window.addEventListener("blur", () => {
    Object.keys(keys).forEach(key => keys[key] = false);
});

// ============================================
// 마우스
// ============================================

let dragging = false;
let previousX = 0;
let previousY = 0;

renderer.domElement.addEventListener("pointerdown", event => {

    dragging = true;

    previousX = event.clientX;
    previousY = event.clientY;

    renderer.domElement.focus();

    renderer.domElement.setPointerCapture(event.pointerId);
});

renderer.domElement.addEventListener("pointerup", () => {
    dragging = false;
});

renderer.domElement.addEventListener("pointercancel", () => {
    dragging = false;
});

renderer.domElement.addEventListener("pointermove", event => {

    if (!dragging) return;

    yaw -= (event.clientX - previousX) * .005;

    pitch = THREE.MathUtils.clamp(
        pitch + (event.clientY - previousY) * .004,
        -.2,
        1.1
    );

    previousX = event.clientX;
    previousY = event.clientY;
});

// ============================================
// 감정 표현
// ============================================

let emotion = "";
let emotionTime = 0;

$("wave").onclick = () => {
    emotion = "wave";
    emotionTime = 2;
    notify("👋 안녕!");
};

$("dance").onclick = () => {
    emotion = "dance";
    emotionTime = 3;
    notify("🎵 춤추는 중!");
};

// ============================================
// 애니메이션
// ============================================

const clock = new THREE.Clock();

const cameraTarget = new THREE.Vector3();
const cameraWanted = new THREE.Vector3();

function animateCharacter(character, time, moving, running) {

    if (!character || !character.userData.parts) return;

    const parts = character.userData.parts;
    const model = character.userData.model;

    const speed = running ? 15 : 10;
    const amount = moving ? (running ? .75 : .48) : 0;

    if (parts.leftArm) {
        parts.leftArm.rotation.x =
            Math.sin(time * speed) * amount;
    }

    if (parts.rightArm) {
        parts.rightArm.rotation.x =
            -Math.sin(time * speed) * amount;
    }

    if (parts.leftLeg) {
        parts.leftLeg.rotation.x =
            -Math.sin(time * speed) * amount;
    }

    if (parts.rightLeg) {
        parts.rightLeg.rotation.x =
            Math.sin(time * speed) * amount;
    }

    model.position.y = moving
        ? Math.abs(Math.sin(time * speed)) * .045
        : Math.sin(time * 2) * .012;
}

function animate() {

    requestAnimationFrame(animate);

    const dt = Math.min(clock.getDelta(), .05);
    const time = clock.elapsedTime;

    const forward =
        Number(Boolean(keys.w || keys.arrowup)) -
        Number(Boolean(keys.s || keys.arrowdown));

    const sideways =
        Number(Boolean(keys.d || keys.arrowright)) -
        Number(Boolean(keys.a || keys.arrowleft));

    const running = Boolean(keys.shift);

    const speed = running ? 5.5 : 3.2;

    const direction = new THREE.Vector3(
        Math.sin(yaw) * forward + Math.cos(yaw) * sideways,
        0,
        -Math.cos(yaw) * forward + Math.sin(yaw) * sideways
    );

    const moving = direction.lengthSq() > 0;

    if (moving) {

        direction.normalize();

        player.position.addScaledVector(
            direction,
            dt * speed
        );

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

        const targetRotation = Math.atan2(
            direction.x,
            direction.z
        );

        const difference = Math.atan2(
            Math.sin(targetRotation - player.rotation.y),
            Math.cos(targetRotation - player.rotation.y)
        );

        player.rotation.y +=
            difference * Math.min(1, dt * 12);
    }

    animateCharacter(
        characterModel,
        time,
        moving,
        running
    );

    // 손 흔들기 / 춤
    if (emotionTime > 0) {

        emotionTime -= dt;

        const parts = characterModel.userData.parts;

        if (emotion === "wave" && parts.rightArm) {
            parts.rightArm.rotation.z = -2.1;
            parts.rightArm.rotation.x =
                Math.sin(time * 15) * .4;
        }

        if (emotion === "dance") {
            characterModel.userData.model.rotation.z =
                Math.sin(time * 9) * .2;
        }

    } else {

        characterModel.userData.model.rotation.z = 0;

        if (characterModel.userData.parts.rightArm) {
            characterModel.userData.parts.rightArm.rotation.z = 0;
        }
    }

    // 손님 애니메이션
    guests.forEach((guest, index) => {

        guest.timer += dt;

        if (!guest.ready && guest.timer > 7) {
            guest.ready = true;
            guest.timer = 0;
            updateUI();
        }

        animateCharacter(
            guest.model,
            time + guest.phase,
            false,
            false
        );

        guest.model.rotation.y =
            Math.sin(time * .6 + index) * .2;
    });

    // 카메라
    cameraTarget.copy(player.position);
    cameraTarget.y += 1.45;

    const facing = new THREE.Vector3(
        Math.sin(yaw),
        0,
        -Math.cos(yaw)
    );

    if (firstPerson) {

        characterModel.visible = false;

        cameraWanted.copy(cameraTarget);

        camera.position.lerp(cameraWanted, .25);

        const look = cameraTarget.clone()
            .addScaledVector(facing, 4);

        look.y -= Math.tan(pitch) * 3;

        camera.lookAt(look);

    } else {

        characterModel.visible = true;

        cameraWanted.copy(cameraTarget)
            .addScaledVector(
                facing,
                -5 * Math.cos(pitch)
            );

        cameraWanted.y +=
            2 + 5 * Math.sin(pitch);

        camera.position.lerp(cameraWanted, .14);

        camera.lookAt(cameraTarget);
    }

    renderer.render(scene, camera);
}

// ============================================
// 창 크기 변경
// ============================================

window.addEventListener("resize", () => {

    camera.aspect =
        window.innerWidth / window.innerHeight;

    camera.updateProjectionMatrix();

    renderer.setSize(
        window.innerWidth,
        window.innerHeight
    );
});

// ============================================
// 시작
// ============================================

updateUI();

$("loading").remove();

notify("🐻 카페에 오신 것을 환영해요!");

setTimeout(() => {
    renderer.domElement.focus();
}, 500);

animate();

</script>
</body>
</html>
"""

components.html(
    html,
    height=850,
    scrolling=False
)
