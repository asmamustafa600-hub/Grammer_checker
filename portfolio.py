< !DOCTYPE
html >
< html
lang = "en"
data - theme = "dark" >
< head >
< meta
charset = "UTF-8" >
< meta
name = "viewport"
content = "width=device-width, initial-scale=1.0" >
< title > Asma
Mustafa — Data
Science & Machine
Learning
Practitioner < / title >
< meta
name = "description"
content = "Portfolio of Asma Mustafa: Data Science & Machine Learning practitioner specializing in Deep Learning, Computer Vision, NLP, and Streamlit Cloud deployments." >

< !-- Google
Fonts -->
< link
rel = "preconnect"
href = "https://fonts.googleapis.com" >
< link
rel = "preconnect"
href = "https://fonts.gstatic.com"
crossorigin >
< link
href = "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap"
rel = "stylesheet" >

< style >
:root
{
/ * Base
Palette - Executive
Dark * /
--bg - base:  # 090d16;
--bg - surface:  # 0f172a;
--bg - surface - elevated:  # 151f36;
--bg - card: rgba(17, 24, 39, 0.75);
--bg - card - hover: rgba(26, 36, 56, 0.85);
--border - subtle: rgba(255, 255, 255, 0.08);
--border - strong: rgba(255, 255, 255, 0.16);
--border - accent: rgba(56, 189, 248, 0.35);

/ *Text * /
   --text - primary:  # f8fafc;
--text - secondary:  # 94a3b8;
--text - tertiary:  # 64748b;
--text - inverse:  # 090d16;

/ *Accents * /
   --accent - cyan:  # 38bdf8;
--accent - cyan - dim: rgba(56, 189, 248, 0.12);
--accent - blue:  # 3b82f6;
--accent - indigo:  # 6366f1;
--accent - emerald:  # 10b981;
--accent - emerald - dim: rgba(16, 185, 129, 0.12);
--accent - amber:  # f59e0b;
--accent - amber - dim: rgba(245, 158, 11, 0.12);

/ *Gradients * /
   --gradient - hero - glow: radial - gradient(circle
at
50 % 0 %, rgba(56, 189, 248, 0.12)
0 %, rgba(99, 102, 241, 0.05)
50 %, transparent
80 %);
--gradient - text: linear - gradient(135
deg,  # f8fafc 30%, #38bdf8 100%);
--gradient - badge: linear - gradient(135
deg, rgba(56, 189, 248, 0.15), rgba(99, 102, 241, 0.15));

/ *Shadows & Radii * /
   --shadow - sm: 0
2
px
8
px
rgba(0, 0, 0, 0.25);
--shadow - md: 0
10
px
25
px - 5
px
rgba(0, 0, 0, 0.4), 0
8
px
10
px - 6
px
rgba(0, 0, 0, 0.3);
--shadow - glow: 0
0
25
px
rgba(56, 189, 248, 0.18);
--radius - sm: 8
px;
--radius - md: 12
px;
--radius - lg: 18
px;
--radius - full: 9999
px;

--transition - fast: 0.2
s
ease;
--transition - smooth: 0.3
s
cubic - bezier(0.16, 1, 0.3, 1);
}

[data - theme = "light"] {
    --bg - base:  # f8fafc;
        --bg - surface:  # ffffff;
--bg - surface - elevated:  # f1f5f9;
--bg - card: rgba(255, 255, 255, 0.85);
--bg - card - hover:  # ffffff;
--border - subtle: rgba(15, 23, 42, 0.08);
--border - strong: rgba(15, 23, 42, 0.16);
--border - accent: rgba(2, 132, 199, 0.4);

--text - primary:  # 0f172a;
--text - secondary:  # 475569;
--text - tertiary:  # 64748b;
--text - inverse:  # ffffff;

--accent - cyan:  # 0284c7;
--accent - cyan - dim: rgba(2, 132, 199, 0.1);
--accent - blue:  # 2563eb;
--accent - indigo:  # 4f46e5;
--accent - emerald:  # 059669;
--accent - emerald - dim: rgba(5, 150, 105, 0.1);
--accent - amber:  # d97706;
--accent - amber - dim: rgba(217, 119, 6, 0.1);

--gradient - hero - glow: radial - gradient(circle
at
50 % 0 %, rgba(2, 132, 199, 0.08)
0 %, rgba(79, 70, 229, 0.03)
50 %, transparent
80 %);
--gradient - text: linear - gradient(135
deg,  # 0f172a 30%, #0284c7 100%);
--gradient - badge: linear - gradient(135
deg, rgba(2, 132, 199, 0.08), rgba(79, 70, 229, 0.08));

--shadow - sm: 0
1
px
3
px
rgba(0, 0, 0, 0.05);
--shadow - md: 0
10
px
25
px - 5
px
rgba(15, 23, 42, 0.06), 0
8
px
10
px - 6
px
rgba(15, 23, 42, 0.04);
--shadow - glow: 0
0
20
px
rgba(2, 132, 199, 0.12);
}

/ *Reset & Core * /
   *, *::before, *::after
{
    box - sizing: border - box;
margin: 0;
padding: 0;
}
html
{
    scroll - behavior: smooth;
font - size: 16
px;
}
body
{
    background - color: var(--bg - base);
color: var(--text - primary);
font - family: 'Inter', -apple - system, BlinkMacSystemFont, "Segoe UI", Roboto, sans - serif;
line - height: 1.6;
overflow - x: hidden;
transition: background - color
var(--transition - smooth), color
var(--transition - smooth);
background - image: var(--gradient - hero - glow);
background - repeat: no - repeat;
background - size: 100 % 900
px;
}

h1, h2, h3, h4,.brand - title
{
    font - family: 'Plus Jakarta Sans', sans - serif;
letter - spacing: -0.025
em;
color: var(--text - primary);
}

.mono
{
    font - family: 'JetBrains Mono', monospace;
}

a
{
    color: inherit;
text - decoration: none;
transition: color
var(--transition - fast);
}

/ *Container
utility * /
.container
{
    width: 100 %;
max - width: 1180
px;
margin: 0
auto;
padding: 0
24
px;
}

/ *Header / Navbar * /
   header
{
    position: sticky;
top: 0;
z - index: 100;
backdrop - filter: blur(14
px);
-webkit - backdrop - filter: blur(14
px);
background: rgba(9, 13, 22, 0.75);
border - bottom: 1
px
solid
var(--border - subtle);
transition: background
var(--transition - smooth), border - color
var(--transition - smooth);
}
[data - theme = "light"] header
{
    background: rgba(248, 250, 252, 0.85);
}

.nav - wrapper
{
    display: flex;
align - items: center;
justify - content: space - between;
height: 72
px;
}

.brand - group
{
    display: flex;
align - items: center;
gap: 12
px;
}
.brand - avatar
{
    width: 38px;
height: 38
px;
border - radius: var(--radius - sm);
background: linear - gradient(135
deg, var(--accent - blue), var(--accent - cyan));
display: flex;
align - items: center;
justify - content: center;
color:  # ffffff;
font - weight: 700;
font - size: 16
px;
font - family: 'Plus Jakarta Sans', sans - serif;
box - shadow: 0
2
px
10
px
rgba(56, 189, 248, 0.3);
}
.brand - text
{
    display: flex;
flex - direction: column;
}
.brand - title
{
    font - size: 17px;
font - weight: 700;
line - height: 1.2;
}
.brand - subtitle
{
    font - size: 12px;
color: var(--text - secondary);
font - family: 'JetBrains Mono', monospace;
}

nav
{
    display: flex;
align - items: center;
gap: 28
px;
}
nav
a
{
    font - size: 14px;
font - weight: 500;
color: var(--text - secondary);
position: relative;
padding: 6
px
0;
}
nav
a: hover, nav
a.active
{
    color: var(--text - primary);
}
nav
a::after
{
    content: '';
position: absolute;
bottom: 0;
left: 0;
width: 0;
height: 2
px;
background: var(--accent - cyan);
transition: width
var(--transition - fast);
border - radius: 2
px;
}
nav
a: hover::after
{
    width: 100 %;
}

.nav - actions
{
    display: flex;
align - items: center;
gap: 14
px;
}

.theme - toggle - btn
{
    background: var(--bg - surface - elevated);
border: 1
px
solid
var(--border - subtle);
color: var(--text - secondary);
width: 38
px;
height: 38
px;
border - radius: var(--radius - sm);
display: flex;
align - items: center;
justify - content: center;
cursor: pointer;
transition: all
var(--transition - fast);
}
.theme - toggle - btn: hover
{
    color: var(--accent - cyan);
border - color: var(--border - strong);
transform: translateY(-1
px);
}

.btn
{
    display: inline - flex;
align - items: center;
justify - content: center;
gap: 8
px;
font - family: 'Inter', sans - serif;
font - size: 14
px;
font - weight: 600;
padding: 9
px
18
px;
border - radius: var(--radius - sm);
cursor: pointer;
transition: all
var(--transition - fast);
border: 1
px
solid
transparent;
text - decoration: none;
}
.btn - primary
{
    background: linear - gradient(135deg, var(--accent - blue), var(--accent - cyan));
color:  # ffffff;
box - shadow: 0
4
px
14
px
rgba(56, 189, 248, 0.25);
}
.btn - primary: hover
{
    box - shadow: 0 6px 20px rgba(56, 189, 248, 0.4);
transform: translateY(-1
px);
color:  # ffffff;
}
.btn - outline
{
    background: var(--bg - surface);
color: var(--text - primary);
border - color: var(--border - strong);
}
.btn - outline: hover
{
    background: var(--bg - surface - elevated);
border - color: var(--accent - cyan);
color: var(--accent - cyan);
transform: translateY(-1
px);
}
.btn - sm
{
    padding: 6px 12px;
font - size: 13
px;
border - radius: 6
px;
}

/ *Status
indicator
badge * /
.status - pill
{
    display: inline - flex;
align - items: center;
gap: 8
px;
padding: 5
px
12
px;
border - radius: var(--radius - full);
background: var(--accent - emerald - dim);
border: 1
px
solid
rgba(16, 185, 129, 0.25);
font - size: 12.5
px;
font - weight: 500;
color: var(--accent - emerald);
width: fit - content;
}
.pulse - dot
{
    width: 7px;
height: 7
px;
border - radius: 50 %;
background - color: var(--accent - emerald);
box - shadow: 0
0
0
0
rgba(16, 185, 129, 0.7);
animation: pulse
2
s
infinite;
}

@keyframes


pulse
{
    0 % {transform: scale(0.95);
box - shadow: 0
0
0
0
rgba(16, 185, 129, 0.7);}
70 % {transform: scale(1);
box - shadow: 0
0
0
6
px
rgba(16, 185, 129, 0);}
100 % {transform: scale(0.95);
box - shadow: 0
0
0
0
rgba(16, 185, 129, 0);}
}

/ *Hero
Section * /
.hero - section
{
    padding: 75px 0 55px;
}
.hero - content
{
    max - width: 880px;
}
.hero - pretitle
{
    margin - bottom: 20px;
}
.hero - title
{
    font - size: clamp(36px, 5.2
vw, 62
px);
font - weight: 800;
line - height: 1.1;
margin - bottom: 22
px;
letter - spacing: -0.03
em;
}
.gradient - text
{
    background: var(--gradient - text);
-webkit - background - clip: text;
-webkit - text - fill - color: transparent;
}
.hero - lede
{
    font - size: clamp(17px, 2
vw, 19
px);
color: var(--text - secondary);
line - height: 1.65;
margin - bottom: 34
px;
max - width: 720
px;
}
.hero - ctas
{
    display: flex;
flex - wrap: wrap;
align - items: center;
gap: 14
px;
margin - bottom: 48
px;
}

/ *Stats
Row * /
.stats - grid
{
    display: grid;
grid - template - columns: repeat(4, 1
fr);
gap: 16
px;
padding - top: 24
px;
border - top: 1
px
solid
var(--border - subtle);
}
.stat - card
{
    padding: 16px 20px;
background: var(--bg - card);
border: 1
px
solid
var(--border - subtle);
border - radius: var(--radius - md);
transition: all
var(--transition - fast);
}
.stat - card: hover
{
    border - color: var(--border - accent);
transform: translateY(-2
px);
background: var(--bg - card - hover);
}
.stat - number
{
    font - family: 'JetBrains Mono', monospace;
font - size: 26
px;
font - weight: 700;
color: var(--accent - cyan);
margin - bottom: 4
px;
}
.stat - label
{
    font - size: 13px;
color: var(--text - secondary);
line - height: 1.35;
}

/ *Section
Styling * /
section
{
    padding: 70px 0;
border - top: 1
px
solid
var(--border - subtle);
}
.section - header
{
    display: flex;
justify - content: space - between;
align - items: flex - end;
margin - bottom: 44
px;
gap: 20
px;
flex - wrap: wrap;
}
.section - tag
{
    font - family: 'JetBrains Mono', monospace;
font - size: 12
px;
font - weight: 600;
text - transform: uppercase;
letter - spacing: 0.1
em;
color: var(--accent - cyan);
margin - bottom: 6
px;
display: block;
}
.section - title
{
    font - size: clamp(26px, 3.2
vw, 36
px);
font - weight: 700;
}
.section - desc
{
    color: var(--text - secondary);
font - size: 15
px;
max - width: 480
px;
}

/ *About / Narrative
Section * /
.about - grid
{
    display: grid;
grid - template - columns: 1.35
fr
1
fr;
gap: 32
px;
}
.narrative - card
{
    background: var(--bg - card);
border: 1
px
solid
var(--border - subtle);
border - radius: var(--radius - lg);
padding: 34
px;
backdrop - filter: blur(10
px);
}
.narrative - card
h3
{
    font - size: 22px;
margin - bottom: 16
px;
display: flex;
align - items: center;
gap: 10
px;
}
.narrative - card
p
{
    color: var(--text - secondary);
font - size: 16
px;
line - height: 1.7;
margin - bottom: 20
px;
}
.narrative - card
p: last - child
{
    margin - bottom: 0;
}
.highlight - quote
{
    padding: 16px 20px;
background: var(--bg - surface - elevated);
border - left: 3
px
solid
var(--accent - cyan);
border - radius: 0
var(--radius - sm)
var(--radius - sm)
0;
color: var(--text - primary);
font - style: italic;
font - size: 15
px;
margin: 22
px
0;
}

/ *Credentials
Card * /
.credentials - card
{
    background: var(--bg - card);
border: 1
px
solid
var(--border - subtle);
border - radius: var(--radius - lg);
padding: 30
px;
display: flex;
flex - direction: column;
justify - content: space - between;
}
.credential - item
{
    padding: 16px 0;
border - bottom: 1
px
solid
var(--border - subtle);
}
.credential - item: first - child
{
    padding - top: 0;
}
.credential - item: last - child
{
    border - bottom: none;
padding - bottom: 0;
}
.cred - label
{
    font - family: 'JetBrains Mono', monospace;
font - size: 12
px;
color: var(--text - tertiary);
text - transform: uppercase;
letter - spacing: 0.05
em;
margin - bottom: 4
px;
}
.cred - value
{
    font - size: 15px;
font - weight: 600;
color: var(--text - primary);
}
.cred - subtext
{
    font - size: 13px;
color: var(--text - secondary);
margin - top: 2
px;
}

/ *Teaching
Advantage
Card * /
.teaching - box
{
    margin - top: 32px;
background: linear - gradient(135
deg, rgba(56, 189, 248, 0.04), rgba(99, 102, 241, 0.04));
border: 1
px
solid
var(--border - subtle);
border - radius: var(--radius - lg);
padding: 30
px;
}
.teaching - header
{
    display: flex;
align - items: center;
justify - content: space - between;
margin - bottom: 16
px;
flex - wrap: wrap;
gap: 12
px;
}
.teaching - header
h3
{
    font - size: 20px;
}
.badge
{
    display: inline - flex;
align - items: center;
gap: 6
px;
padding: 4
px
10
px;
border - radius: var(--radius - full);
font - size: 12
px;
font - weight: 500;
background: var(--bg - surface - elevated);
border: 1
px
solid
var(--border - subtle);
color: var(--accent - cyan);
font - family: 'JetBrains Mono', monospace;
}
.teaching - box
p
{
    color: var(--text - secondary);
font - size: 15.5
px;
line - height: 1.7;
}

/ *Projects
Filter
Bar * /
.filter - container
{
    display: flex;
flex - wrap: wrap;
gap: 8
px;
margin - bottom: 32
px;
}
.filter - btn
{
    background: var(--bg - card);
border: 1
px
solid
var(--border - subtle);
color: var(--text - secondary);
font - family: 'Inter', sans - serif;
font - size: 13.5
px;
font - weight: 500;
padding: 8
px
16
px;
border - radius: var(--radius - full);
cursor: pointer;
transition: all
var(--transition - fast);
}
.filter - btn: hover
{
    color: var(--text - primary);
border - color: var(--border - strong);
}
.filter - btn.active
{
    background: var(--accent - cyan - dim);
color: var(--accent - cyan);
border - color: var(--border - accent);
font - weight: 600;
}

/ *Projects
Grid * /
.projects - grid
{
    display: grid;
grid - template - columns: repeat(2, 1
fr);
gap: 24
px;
}
.project - card
{
    background: var(--bg - card);
border: 1
px
solid
var(--border - subtle);
border - radius: var(--radius - lg);
padding: 28
px;
display: flex;
flex - direction: column;
justify - content: space - between;
transition: all
var(--transition - smooth);
position: relative;
overflow: hidden;
}
.project - card: hover
{
    transform: translateY(-4px);
border - color: var(--border - accent);
box - shadow: var(--shadow - md);
background: var(--bg - card - hover);
}
.project - card.featured
{
    grid - column: span 2;
}

.card - top
{
    margin - bottom: 20px;
}
.card - meta - bar
{
    display: flex;
align - items: center;
justify - content: space - between;
margin - bottom: 14
px;
}
.project - index
{
    font - family: 'JetBrains Mono', monospace;
font - size: 13
px;
color: var(--accent - cyan);
font - weight: 600;
}
.project - category
{
    font - family: 'JetBrains Mono', monospace;
font - size: 11.5
px;
color: var(--text - tertiary);
text - transform: uppercase;
letter - spacing: 0.05
em;
}
.project - title
{
    font - size: 21px;
font - weight: 700;
margin - bottom: 10
px;
line - height: 1.3;
}
.project - title
a: hover
{
    color: var(--accent - cyan);
}
.project - description
{
    color: var(--text - secondary);
font - size: 14.5
px;
line - height: 1.6;
margin - bottom: 16
px;
}

/ *Impact & Metric
Box
inside
project * /
.project - metric - box
{
    display: flex;
align - items: center;
justify - content: space - between;
padding: 10
px
14
px;
border - radius: var(--radius - sm);
background: var(--bg - surface - elevated);
border: 1
px
solid
var(--border - subtle);
margin - bottom: 18
px;
}
.metric - label
{
    font - size: 12px;
color: var(--text - secondary);
}
.metric - value
{
    font - family: 'JetBrains Mono', monospace;
font - size: 14
px;
font - weight: 700;
color: var(--accent - cyan);
}

.card - bottom
{
    margin - top: auto;
}
.tech - tags
{
    display: flex;
flex - wrap: wrap;
gap: 6
px;
margin - bottom: 20
px;
}
.tech - tag
{
    font - family: 'JetBrains Mono', monospace;
font - size: 12
px;
padding: 3
px
8
px;
border - radius: 4
px;
background: var(--bg - surface - elevated);
color: var(--text - secondary);
border: 1
px
solid
var(--border - subtle);
}

.project - actions
{
    display: flex;
align - items: center;
gap: 12
px;
flex - wrap: wrap;
padding - top: 14
px;
border - top: 1
px
solid
var(--border - subtle);
}
.action - link
{
    font - size: 13px;
font - weight: 600;
display: inline - flex;
align - items: center;
gap: 6
px;
color: var(--text - primary);
transition: color
var(--transition - fast);
}
.action - link: hover
{
    color: var(--accent - cyan);
}
.action - link.primary
{
    color: var(--accent - cyan);
}
.action - link
svg
{
    width: 14px;
height: 14
px;
transition: transform
var(--transition - fast);
}
.action - link: hover
svg
{
    transform: translateX(2px) translateY(-1
px);
}

/ *Skills
Grid * /
.skills - grid
{
    display: grid;
grid - template - columns: repeat(4, 1
fr);
gap: 20
px;
}
.skill - domain - card
{
    background: var(--bg - card);
border: 1
px
solid
var(--border - subtle);
border - radius: var(--radius - lg);
padding: 26
px;
transition: all
var(--transition - fast);
}
.skill - domain - card: hover
{
    border - color: var(--border - accent);
transform: translateY(-2
px);
}
.skill - icon - wrapper
{
    width: 44px;
height: 44
px;
border - radius: var(--radius - md);
background: var(--accent - cyan - dim);
border: 1
px
solid
rgba(56, 189, 248, 0.2);
display: flex;
align - items: center;
justify - content: center;
color: var(--accent - cyan);
margin - bottom: 18
px;
}
.skill - domain - title
{
    font - size: 17px;
font - weight: 700;
margin - bottom: 14
px;
}
.skill - list
{
    list - style: none;
display: flex;
flex - direction: column;
gap: 10
px;
}
.skill - item
{
    font - size: 13.5px;
color: var(--text - secondary);
display: flex;
align - items: center;
gap: 8
px;
}
.skill - item::before
{
    content: '';
width: 5
px;
height: 5
px;
border - radius: 50 %;
background: var(--accent - cyan);
}

/ *Contact / Call
to
Action * /
.contact - section
{
    padding: 80px 0;
}
.contact - card
{
    background: linear - gradient(135deg, rgba(15, 23, 42, 0.9), rgba(21, 31, 54, 0.85));
border: 1
px
solid
var(--border - accent);
border - radius: var(--radius - lg);
padding: 56
px
48
px;
box - shadow: var(--shadow - glow);
display: flex;
justify - content: space - between;
align - items: center;
gap: 40
px;
flex - wrap: wrap;
position: relative;
overflow: hidden;
}
[data - theme = "light"].contact - card
{
    background: linear - gradient(135deg,  # ffffff, #f1f5f9);
border - color: rgba(2, 132, 199, 0.3);
}
.contact - info
{
    max - width: 580px;
}
.contact - info
h2
{
    font - size: clamp(28px, 3.5
vw, 42
px);
margin - bottom: 16
px;
font - weight: 800;
}
.contact - info
p
{
    font - size: 16.5px;
color: var(--text - secondary);
line - height: 1.6;
margin - bottom: 24
px;
}
.location - badge
{
    display: inline - flex;
align - items: center;
gap: 8
px;
color: var(--text - secondary);
font - size: 13.5
px;
}

.contact - buttons
{
    display: flex;
flex - direction: column;
gap: 14
px;
min - width: 280
px;
}
.copy - email - btn
{
    position: relative;
width: 100 %;
}

/ *Toast
Notification * /
.toast
{
    position: fixed;
bottom: 30
px;
right: 30
px;
background: var(--bg - surface);
color: var(--text - primary);
border: 1
px
solid
var(--accent - emerald);
padding: 12
px
20
px;
border - radius: var(--radius - md);
box - shadow: var(--shadow - md);
font - size: 14
px;
font - weight: 600;
display: flex;
align - items: center;
gap: 10
px;
transform: translateY(100
px);
opacity: 0;
pointer - events: none;
transition: all
0.3
s
cubic - bezier(0.16, 1, 0.3, 1);
z - index: 1000;
}
.toast.show
{
    transform: translateY(0);
opacity: 1;
pointer - events: auto;
}

/ *Footer * /
   footer
{
    padding: 36px 0;
border - top: 1
px
solid
var(--border - subtle);
font - size: 13.5
px;
color: var(--text - tertiary);
}
.footer - inner
{
    display: flex;
justify - content: space - between;
align - items: center;
flex - wrap: wrap;
gap: 16
px;
}
.footer - links
{
    display: flex;
gap: 20
px;
}
.footer - links
a: hover
{
    color: var(--text - primary);
}

/ *Responsive
Design * /
@ media(max - width: 980
px) {
    .about - grid
{
    grid - template - columns: 1fr;
}
.stats - grid
{
    grid - template - columns: repeat(2, 1fr);
}
.skills - grid
{
    grid - template - columns: repeat(2, 1fr);
}
.projects - grid
{
    grid - template - columns: 1fr;
}
.project - card.featured
{
    grid - column: span 1;
}
}

@media(max - width

: 720
px) {
    .nav - wrapper
{
    height: 64px;
}
nav
{
    display: none; / *simple
clean
mobile
view * /
}
.hero - section
{
    padding: 45px 0 40px;
}
.stats - grid
{
    grid - template - columns: 1fr;
}
.skills - grid
{
    grid - template - columns: 1fr;
}
.contact - card
{
    padding: 34px 24px;
}
.contact - buttons
{
    width: 100 %;
}
}
< / style >
    < / head >
        < body >

        <!-- Header / Navigation -->
< header >
  < div


class ="container nav-wrapper" >

< div


class ="brand-group" >

< div


class ="brand-avatar" > AM < / div >

< div


class ="brand-text" >

< span


class ="brand-title" > Asma Mustafa < / span >

< span


class ="brand-subtitle" > Data Science & amp; AI < / span >

< / div >
< / div >

< nav >
< a
href = "#about" > Overview < / a >
< a
href = "#expertise" > Advantage < / a >
< a
href = "#projects" > Projects < / a >
< a
href = "#skills" > Skills < / a >
< a
href = "#contact" > Contact < / a >
< / nav >

< div


class ="nav-actions" >

< button


class ="theme-toggle-btn" id="themeToggle" title="Toggle Light / Dark Theme" aria-label="Toggle Theme" >

< !-- Sun
icon -->
< svg
id = "sunIcon"
style = "display:none;"
width = "18"
height = "18"
viewBox = "0 0 24 24"
fill = "none"
stroke = "currentColor"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < circle
cx = "12"
cy = "12"
r = "5" > < / circle > < line
x1 = "12"
y1 = "1"
x2 = "12"
y2 = "3" > < / line > < line
x1 = "12"
y1 = "21"
x2 = "12"
y2 = "23" > < / line > < line
x1 = "4.22"
y1 = "4.22"
x2 = "5.64"
y2 = "5.64" > < / line > < line
x1 = "18.36"
y1 = "18.36"
x2 = "19.78"
y2 = "19.78" > < / line > < line
x1 = "1"
y1 = "12"
x2 = "3"
y2 = "12" > < / line > < line
x1 = "21"
y1 = "12"
x2 = "23"
y2 = "12" > < / line > < line
x1 = "4.22"
y1 = "19.78"
x2 = "5.64"
y2 = "18.36" > < / line > < line
x1 = "18.36"
y1 = "5.64"
x2 = "19.78"
y2 = "4.22" > < / line > < / svg >
< !-- Moon
icon -->
< svg
id = "moonIcon"
width = "18"
height = "18"
viewBox = "0 0 24 24"
fill = "none"
stroke = "currentColor"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < path
d = "M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" > < / path > < / svg >
< / button >
< a
href = "#contact"


class ="btn btn-primary btn-sm" > Get in Touch < / a >

< / div >
< / div >
< / header >

< !-- Hero
Section -->
< section


class ="hero-section" id="home" >

< div


class ="container hero-content" >

< div


class ="hero-pretitle" >

< div


class ="status-pill" >

< span


class ="pulse-dot" > < / span >

< span > Available
for Data Science & amp; ML Opportunities · Lahore, PK < / span >
< / div >
< / div >

< h1


class ="hero-title" >


Transforming
Complex
Data
into < span


class ="gradient-text" > Predictive Intelligence < / span > & amp; Actionable AI.

< / h1 >

< p


class ="hero-lede" >


Data
Science & amp;
Machine
Learning
practitioner
completing
NAVTTC
's advanced program in Lahore. Combining rigorous statistical modeling, deep neural architectures (TensorFlow, ViT, T5), and an educator’s discipline to build transparent, reliable, and production-ready machine learning systems.
< / p >

< div


class ="hero-ctas" >

< a
href = "#projects"


class ="btn btn-primary" >


Explore
Projects
< svg
width = "16"
height = "16"
viewBox = "0 0 24 24"
fill = "none"
stroke = "currentColor"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < line
x1 = "7"
y1 = "17"
x2 = "17"
y2 = "7" > < / line > < polyline
points = "7 7 17 7 17 17" > < / polyline > < / svg >
< / a >
< a
href = "https://github.com/asmamustafa600-hub"
target = "_blank"
rel = "noopener"


class ="btn btn-outline" >

< svg
width = "16"
height = "16"
viewBox = "0 0 24 24"
fill = "none"
stroke = "currentColor"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < path
d = "M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22" > < / path > < / svg >
GitHub
Profile
< / a >
< button


class ="btn btn-outline copy-email-trigger" onclick="copyEmail()" >

< svg
width = "16"
height = "16"
viewBox = "0 0 24 24"
fill = "none"
stroke = "currentColor"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < rect
x = "9"
y = "9"
width = "13"
height = "13"
rx = "2"
ry = "2" > < / rect > < path
d = "M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1" > < / path > < / svg >
Copy
Email
< / button >
< / div >

< !-- Stats
Bar -->
< div


class ="stats-grid" >

< div


class ="stat-card" >

< div


class ="stat-number" > 07+ < / div >

< div


class ="stat-label" > End-to-End Machine Learning & amp; AI Projects < / div >

< / div >
< div


class ="stat-card" >

< div


class ="stat-number" > 04 < / div >

< div


class ="stat-label" > Production Web Apps Deployed on Cloud < / div >

< / div >
< div


class ="stat-card" >

< div


class ="stat-number" > ~98 % < / div >

< div


class ="stat-label" > Peak Computer Vision Model Accuracy < / div >

< / div >
< div


class ="stat-card" >

< div


class ="stat-number" > 2+ Yrs < / div >

< div


class ="stat-label" > Technical Instruction & amp; Mentorship < / div >

< / div >
< / div >
< / div >
< / section >

< !-- Overview & Narrative
Section -->
< section
id = "about" >
< div


class ="container" >

< div


class ="section-header" >

< div >
< span


class ="section-tag" > Executive Summary < / span >

< h2


class ="section-title" > Bridging Theory, Code & amp; Real-World Value < / h2 >

< / div >
< p


class ="section-desc" >


A
structured
approach
to
data
science: uncovering
patterns, engineering
precise
representations, and delivering
verifiable
predictions.
< / p >
< / div >

< div


class ="about-grid" >

< div


class ="narrative-card" >

< h3 >
< svg
width = "22"
height = "22"
viewBox = "0 0 24 24"
fill = "none"
stroke = "var(--accent-cyan)"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < circle
cx = "12"
cy = "12"
r = "10" > < / circle > < polyline
points = "12 6 12 12 14 14" > < / polyline > < / svg >
Professional
Perspective
< / h3 >
< p >
As
a
Data
Science & amp;
Machine
Learning
practitioner
at
NAVTTC
Lahore, I
build, evaluate, and deploy
end - to - end
intelligent
models in Python.My
work
spans
classical
predictive
algorithms, non - linear
regression
pipelines, and modern
deep
neural
architectures
developed in TensorFlow and Keras.
< / p >
< div


class ="highlight-quote" >


"I believe a machine learning model is only as valuable as its reliability and interpretability. I don’t settle for a script that merely runs—I examine why it succeeds, test its breaking points, and ensure its results can be trusted."
< / div >
< p >
Whether
engineering
target
encoders
for volatile real - estate pricing, training transformers for grammatical precision, or overcoming dataset imbalance with SMOTE, I treat every dataset as a critical business problem demanding methodological discipline and reproducible code.
< / p >
< / div >

< div


class ="credentials-card" >

< div >
< h3
style = "font-size: 19px; margin-bottom: 20px;" > Credentials & amp;
Focus < / h3 >

< div


class ="credential-item" >

< div


class ="cred-label" > Current Specialization < / div >

< div


class ="cred-value" > Data Science & amp; Machine Learning < / div >

< div


class ="cred-subtext" > NAVTTC Program · Lahore, Pakistan < / div >

< / div >

< div


class ="credential-item" >

< div


class ="cred-label" > Prior Professional Experience < / div >

< div


class ="cred-value" > Spoken English Instructor & amp; Peer Tutor < / div >

< div


class ="cred-subtext" > Govt.Graduate College for Women, Lahore (2 Years) < / div >

< / div >

< div


class ="credential-item" >

< div


class ="cred-label" > Primary Technical Ecosystem < / div >

< div


class ="cred-value" > Python, TensorFlow, Hugging Face, Streamlit < / div >

< div


class ="cred-subtext" > Deep Learning, Computer Vision, NLP & amp; Tabular Modeling < / div >

< / div >
< / div >

< div
style = "margin-top: 24px; padding-top: 18px; border-top: 1px solid var(--border-subtle);" >
< span


class ="mono" style="font-size: 12px; color: var(--accent-emerald);" > ● Actively taking on ML projects & amp; full-time roles < / span >

< / div >
< / div >
< / div >

< !-- The
Educator
's Advantage -->
< div


class ="teaching-box" id="expertise" >

< div


class ="teaching-header" >

< div
style = "display:flex; align-items:center; gap:10px;" >
< svg
width = "22"
height = "22"
viewBox = "0 0 24 24"
fill = "none"
stroke = "var(--accent-cyan)"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < path
d = "M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z" > < / path > < path
d = "M22 3h-6a4 4 0 0 1-4 4v14a3 3 0 0 1 3-3h7z" > < / path > < / svg >
< h3 > The
Educator’s
Advantage in Machine
Learning < / h3 >
< / div >
< span


class ="badge" > Explainable AI & amp; Communication < / span >

< / div >
< p >
Before
transitioning
into
artificial
intelligence, I
spent
two
years
mentoring
students and teaching
Spoken
English
at < strong > Govt.Graduate
College
for Women, Lahore< / strong >.In education, you learn to pinpoint the exact moment someone becomes confused, isolate the cognitive roadblock, and deliver crystal-clear explanations.
< / p >
< p
style = "margin-top: 12px;" >
This
background
serves as an
uncommon
superpower in machine
learning.Instead
of
treating
neural
networks as opaque
black
boxes, I
systematically
break
down
models
into
their
foundational
mechanics—gradients, loss
landscapes, and attention
heads.More
importantly, it
empowers
me
to
communicate
technical
findings, model
limitations, and business
value
to
stakeholders
with clarity and confidence.
    < / p >
< / div >
< / div >
< / section >

< !-- Projects
Section -->
< section
id = "projects" >
< div


class ="container" >

< div


class ="section-header" >

< div >
< span


class ="section-tag" > Applied Engineering < / span >

< h2


class ="section-title" > Featured Project Portfolio < / h2 >

< / div >
< p


class ="section-desc" >


A
progressive
collection
of
machine
learning
systems,
from deep neural

computer
vision
to
cloud - deployed
transformers and tabular
predictors.
< / p >
< / div >

< !-- Filter
Bar -->
< div


class ="filter-container" >

< button


class ="filter-btn active" onclick="filterProjects('all', this)" > All Projects (7) < / button >

< button


class ="filter-btn" onclick="filterProjects('deep-learning', this)" > Deep Learning & amp; Vision < / button >

< button


class ="filter-btn" onclick="filterProjects('nlp', this)" > NLP & amp; Transformers < / button >

< button


class ="filter-btn" onclick="filterProjects('tabular', this)" > Predictive & amp; Tabular < / button >

< button


class ="filter-btn" onclick="filterProjects('deployed', this)" > Deployed Web Apps < / button >

< / div >

< div


class ="projects-grid" >

< !-- Project
01: CIFAR - 10 -->
< div


class ="project-card" data-category="deep-learning" >

< div


class ="card-top" >

< div


class ="card-meta-bar" >

< span


class ="project-index" > PROJECT 01 < / span >

< span


class ="project-category" > Deep Learning · Computer Vision < / span >

< / div >
< h3


class ="project-title" >

< a
href = "https://github.com/asmamustafa600-hub/Cifer10_NoCNN_Classification"
target = "_blank"
rel = "noopener" >
CIFAR - 10
Image
Classification(Constrained
Architecture)
< / a >
< / h3 >
< p


class ="project-description" >


Engineered
an
image
classifier
under
the
technical
constraint
of
excluding
convolutional
layers, benchmarking
deep
dense
representations
against
a
modern
Vision
Transformer(ViT)
architecture
with custom early stopping to eliminate overfitting.
< / p >
< div


class ="project-metric-box" >

< span


class ="metric-label" > Architectural Innovation < / span >

< span


class ="metric-value" > No-CNN Constraint vs.ViT < / span >

< / div >
< / div >
< div


class ="card-bottom" >

< div


class ="tech-tags" >

< span


class ="tech-tag" > Python < / span >

< span


class ="tech-tag" > TensorFlow < / span >

< span


class ="tech-tag" > Vision Transformers < / span >

< span


class ="tech-tag" > HuggingFace < / span >

< / div >
< div


class ="project-actions" >

< a
href = "https://github.com/asmamustafa600-hub/Cifer10_NoCNN_Classification"
target = "_blank"
rel = "noopener"


class ="action-link primary" >

< svg
viewBox = "0 0 24 24"
fill = "none"
stroke = "currentColor"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < path
d = "M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22" > < / path > < / svg >
View
Repository →
< / a >
< / div >
< / div >
< / div >

< !-- Project
02: MNIST
Digit
Classifier -->
< div


class ="project-card" data-category="deep-learning" >

< div


class ="card-top" >

< div


class ="card-meta-bar" >

< span


class ="project-index" > PROJECT 02 < / span >

< span


class ="project-category" > Neural Networks · CNN < / span >

< / div >
< h3


class ="project-title" >

< a
href = "https://github.com/asmamustafa600-hub"
target = "_blank"
rel = "noopener" >
MNIST
Handwritten
Digit
Neural
Classifier
< / a >
< / h3 >
< p


class ="project-description" >


A
convolutional
neural
network
built
from scratch to

solidify
core
computer
vision
fundamentals: feature
map
extraction, kernel
dynamics, max - pooling
stride
effects, and convergence
stabilization
across
image
datasets.
< / p >
< div


class ="project-metric-box" >

< span


class ="metric-label" > Model Accuracy < / span >

< span


class ="metric-value" > ~97 % – 98 %Test Accuracy < / span >

< / div >
< / div >
< div


class ="card-bottom" >

< div


class ="tech-tags" >

< span


class ="tech-tag" > Python < / span >

< span


class ="tech-tag" > TensorFlow < / span >

< span


class ="tech-tag" > Keras < / span >

< span


class ="tech-tag" > CNN < / span >

< / div >
< div


class ="project-actions" >

< a
href = "https://github.com/asmamustafa600-hub"
target = "_blank"
rel = "noopener"


class ="action-link" >

< svg
viewBox = "0 0 24 24"
fill = "none"
stroke = "currentColor"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < path
d = "M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22" > < / path > < / svg >
GitHub
Project →
< / a >
< / div >
< / div >
< / div >

< !-- Project
03: Wine
Quality -->
< div


class ="project-card" data-category="tabular" >

< div


class ="card-top" >

< div


class ="card-meta-bar" >

< span


class ="project-index" > PROJECT 03 < / span >

< span


class ="project-category" > Tabular ML · Classification < / span >

< / div >
< h3


class ="project-title" >

< a
href = "https://github.com/asmamustafa600-hub/Wine_Quality_classification_by_asma"
target = "_blank"
rel = "noopener" >
Wine
Quality
Predictive
Classification
< / a >
< / h3 >
< p


class ="project-description" >


A
three -


class quality rating classifier engineered from multi-dimensional chemical attributes.Implemented rigorous feature scaling, addressed severe class imbalance between tiers, and calibrated classification probability thresholds.

< / p >
< div


class ="project-metric-box" >

< span


class ="metric-label" > Validation Performance < / span >

< span


class ="metric-value" > ~87 %Balanced Accuracy < / span >

< / div >
< / div >
< div


class ="card-bottom" >

< div


class ="tech-tags" >

< span


class ="tech-tag" > Python < / span >

< span


class ="tech-tag" > scikit-learn < / span >

< span


class ="tech-tag" > Keras < / span >

< span


class ="tech-tag" > Pandas < / span >

< / div >
< div


class ="project-actions" >

< a
href = "https://github.com/asmamustafa600-hub/Wine_Quality_classification_by_asma"
target = "_blank"
rel = "noopener"


class ="action-link primary" >

< svg
viewBox = "0 0 24 24"
fill = "none"
stroke = "currentColor"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < path
d = "M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22" > < / path > < / svg >
View
Repository →
< / a >
< / div >
< / div >
< / div >

< !-- Project
04: House
Rent
Prediction -->
< div


class ="project-card" data-category="tabular deployed" >

< div


class ="card-top" >

< div


class ="card-meta-bar" >

< span


class ="project-index" > PROJECT 04 < / span >

< span


class ="project-category" > Deep Regression · Live Web App < / span >

< / div >
< h3


class ="project-title" >

< a
href = "https://house-rent-prediction-by-asma.streamlit.app/"
target = "_blank"
rel = "noopener" >
Deep
Learning
House
Rent
Predictor
< / a >
< / h3 >
< p


class ="project-description" >


Production - grade
real
estate
rental
forecasting
model.Solved
high - cardinality
geographic
data
using
smooth
target
encoding and deployed
the
resulting
neural
network as an
interactive
web
tool
for real - time rent valuation.
< / p >
< div


class ="project-metric-box" >

< span


class ="metric-label" > Model Fit & amp; Deployment < / span >

< span


class ="metric-value" > R² ≈ 0.80 · Streamlit Cloud < / span >

< / div >
< / div >
< div


class ="card-bottom" >

< div


class ="tech-tags" >

< span


class ="tech-tag" > Python < / span >

< span


class ="tech-tag" > TensorFlow < / span >

< span


class ="tech-tag" > Pandas < / span >

< span


class ="tech-tag" > Streamlit < / span >

< / div >
< div


class ="project-actions" >

< a
href = "https://house-rent-prediction-by-asma.streamlit.app/"
target = "_blank"
rel = "noopener"


class ="action-link primary" >

< svg
viewBox = "0 0 24 24"
fill = "none"
stroke = "currentColor"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < circle
cx = "12"
cy = "12"
r = "10" > < / circle > < polygon
points = "10 8 16 12 10 16 10 8" > < / polygon > < / svg >
Launch
Live
App →
< / a >
< a
href = "https://github.com/asmamustafa600-hub/House_rent_prediction_by_DL"
target = "_blank"
rel = "noopener"


class ="action-link" >

< svg
viewBox = "0 0 24 24"
fill = "none"
stroke = "currentColor"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < path
d = "M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22" > < / path > < / svg >
Repository
< / a >
< / div >
< / div >
< / div >

< !-- Project
05: Water
Potability -->
< div


class ="project-card" data-category="tabular" >

< div


class ="card-top" >

< div


class ="card-meta-bar" >

< span


class ="project-index" > PROJECT 05 < / span >

< span


class ="project-category" > Healthcare & amp; Environment · Tabular < / span >

< / div >
< h3


class ="project-title" >

< a
href = "https://github.com/asmamustafa600-hub"
target = "_blank"
rel = "noopener" >
Water
Potability & amp;
Safety
Classifier
< / a >
< / h3 >
< p


class ="project-description" >


Environmental
data
analysis
classifying
water
samples as safe or hazardous.Explored
synthetic
oversampling(SMOTE)
to
counter
imbalance and analyzed
the
mathematical
accuracy
ceiling
inherent
to
noisy
real - world
sensor
data.
< / p >
< div


class ="project-metric-box" >

< span


class ="metric-label" > Realistic Data Ceiling < / span >

< span


class ="metric-value" > ~66 % – 68 %SMOTE Benchmarked < / span >

< / div >
< / div >
< div


class ="card-bottom" >

< div


class ="tech-tags" >

< span


class ="tech-tag" > Python < / span >

< span


class ="tech-tag" > Random Forest < / span >

< span


class ="tech-tag" > SMOTE < / span >

< span


class ="tech-tag" > scikit-learn < / span >

< / div >
< div


class ="project-actions" >

< a
href = "https://github.com/asmamustafa600-hub"
target = "_blank"
rel = "noopener"


class ="action-link" >

< svg
viewBox = "0 0 24 24"
fill = "none"
stroke = "currentColor"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < path
d = "M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22" > < / path > < / svg >
GitHub
Project →
< / a >
< / div >
< / div >
< / div >

< !-- Project
06: Grammar & Fluency
Checker -->
< div


class ="project-card" data-category="nlp deployed" >

< div


class ="card-top" >

< div


class ="card-meta-bar" >

< span


class ="project-index" > PROJECT 06 < / span >

< span


class ="project-category" > NLP · Transformer Application < / span >

< / div >
< h3


class ="project-title" >

< a
href = "https://grammerchecker-by-asma-mustafa.streamlit.app/"
target = "_blank"
rel = "noopener" >
AI
Grammar & amp;
Fluency
Transformer
< / a >
< / h3 >
< p


class ="project-description" >


Natural
language
processing
web
application
powered
by
Google
T5
architecture
for grammatical error correction, sentence fluency enhancement, automated readability scoring (textstat), and side-by-side textual diff inspection.
< / p >
< div


class ="project-metric-box" >

< span


class ="metric-label" > Model Architecture < / span >

< span


class ="metric-value" > Google T5 + Readability Diff < / span >

< / div >
< / div >
< div


class ="card-bottom" >

< div


class ="tech-tags" >

< span


class ="tech-tag" > Python < / span >

< span


class ="tech-tag" > HuggingFace < / span >

< span


class ="tech-tag" > T5 Transformer < / span >

< span


class ="tech-tag" > Streamlit < / span >

< / div >
< div


class ="project-actions" >

< a
href = "https://grammerchecker-by-asma-mustafa.streamlit.app/"
target = "_blank"
rel = "noopener"


class ="action-link primary" >

< svg
viewBox = "0 0 24 24"
fill = "none"
stroke = "currentColor"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < circle
cx = "12"
cy = "12"
r = "10" > < / circle > < polygon
points = "10 8 16 12 10 16 10 8" > < / polygon > < / svg >
Launch
Live
App →
< / a >
< a
href = "https://github.com/asmamustafa600-hub/Grammer_checker"
target = "_blank"
rel = "noopener"


class ="action-link" >

< svg
viewBox = "0 0 24 24"
fill = "none"
stroke = "currentColor"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < path
d = "M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22" > < / path > < / svg >
Repository
< / a >
< / div >
< / div >
< / div >

< !-- Project
07: Deployed
App
Suite -->
< div


class ="project-card featured" data-category="deployed" >

< div


class ="card-top" >

< div


class ="card-meta-bar" >

< span


class ="project-index" > PROJECT 07 < / span >

< span


class ="project-category" > Full-Stack Cloud Delivery < / span >

< / div >
< h3


class ="project-title" >


Deployed
Streamlit
Cloud
Application
Suite
< / h3 >
< p


class ="project-description" >


Demonstrating
rapid
prototyping and end - to - end
cloud
delivery
with a suite of deployed interactive tools: a
precision
Scientific
Calculator, an
animated
BMI
Health
Calculator, a
pediatric
BMI
assessment
tool, and a
dynamic
task
management
system.
< / p >
< div


class ="project-metric-box" >

< span


class ="metric-label" > Deployment Status < / span >

< span


class ="metric-value" > 4 Cloud-Native Web Applications < / span >

< / div >
< / div >
< div


class ="card-bottom" >

< div


class ="tech-tags" >

< span


class ="tech-tag" > Python < / span >

< span


class ="tech-tag" > Streamlit Cloud < / span >

< span


class ="tech-tag" > Interactive UI / UX < / span >

< span


class ="tech-tag" > Production CI / CD < / span >

< / div >
< div


class ="project-actions" >

< a
href = "https://asma-s-calculator-gd6ckkakju2gmiq6ysmrgw.streamlit.app/"
target = "_blank"
rel = "noopener"


class ="action-link primary" >

< svg
viewBox = "0 0 24 24"
fill = "none"
stroke = "currentColor"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < circle
cx = "12"
cy = "12"
r = "10" > < / circle > < polygon
points = "10 8 16 12 10 16 10 8" > < / polygon > < / svg >
Scientific
Calculator
App →
< / a >
< a
href = "https://bmicalculator-ruad4zenucxiferezlntku.streamlit.app/"
target = "_blank"
rel = "noopener"


class ="action-link primary" >

< svg
viewBox = "0 0 24 24"
fill = "none"
stroke = "currentColor"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < circle
cx = "12"
cy = "12"
r = "10" > < / circle > < polygon
points = "10 8 16 12 10 16 10 8" > < / polygon > < / svg >
Animated
BMI
Calculator
App →
< / a >
< a
href = "https://github.com/asmamustafa600-hub"
target = "_blank"
rel = "noopener"


class ="action-link" >

< svg
viewBox = "0 0 24 24"
fill = "none"
stroke = "currentColor"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < path
d = "M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22" > < / path > < / svg >
View
GitHub
Profile
< / a >
< / div >
< / div >
< / div >

< / div >
< / div >
< / section >

< !-- Technical
Competencies & Skills -->
< section
id = "skills" >
< div


class ="container" >

< div


class ="section-header" >

< div >
< span


class ="section-tag" > Core Competencies < / span >

< h2


class ="section-title" > Technical Expertise & amp; Tooling < / h2 >

< / div >
< p


class ="section-desc" >


A
structured
toolset
optimized
for turning raw, complex inputs into reliable, explainable machine intelligence.
< / p >
< / div >

< div


class ="skills-grid" >

< !-- Domain
1 -->
< div


class ="skill-domain-card" >

< div


class ="skill-icon-wrapper" >

< svg
width = "22"
height = "22"
viewBox = "0 0 24 24"
fill = "none"
stroke = "currentColor"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < line
x1 = "18"
y1 = "20"
x2 = "18"
y2 = "10" > < / line > < line
x1 = "12"
y1 = "20"
x2 = "12"
y2 = "4" > < / line > < line
x1 = "6"
y1 = "20"
x2 = "6"
y2 = "14" > < / line > < / svg >
< / div >
< h3


class ="skill-domain-title" > Machine Learning < / h3 >

< ul


class ="skill-list" >

< li


class ="skill-item" > Supervised Regression & amp; Classification < / li >

< li


class ="skill-item" > Feature Engineering & amp; Target Encoding < / li >

< li


class ="skill-item" > Class Imbalance Handling (SMOTE) < / li >

< li


class ="skill-item" > Precision-Recall & amp; ROC-AUC Calibration < / li >

< li


class ="skill-item" > Random Forest & amp; Ensemble Methods < / li >

< / ul >
< / div >

< !-- Domain
2 -->
< div


class ="skill-domain-card" >

< div


class ="skill-icon-wrapper" >

< svg
width = "22"
height = "22"
viewBox = "0 0 24 24"
fill = "none"
stroke = "currentColor"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < circle
cx = "12"
cy = "12"
r = "3" > < / circle > < path
d = "M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z" > < / path > < / svg >
< / div >
< h3


class ="skill-domain-title" > Deep Learning < / h3 >

< ul


class ="skill-list" >

< li


class ="skill-item" > TensorFlow & amp; Keras Modeling < / li >

< li


class ="skill-item" > Convolutional Neural Networks (CNN) < / li >

< li


class ="skill-item" > Vision Transformers (ViT) < / li >

< li


class ="skill-item" > Early Stopping & amp; Regularization < / li >

< li


class ="skill-item" > Dense Custom Architectures < / li >

< / ul >
< / div >

< !-- Domain
3 -->
< div


class ="skill-domain-card" >

< div


class ="skill-icon-wrapper" >

< svg
width = "22"
height = "22"
viewBox = "0 0 24 24"
fill = "none"
stroke = "currentColor"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < path
d = "M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" > < / path > < / svg >
< / div >
< h3


class ="skill-domain-title" > NLP & amp; Transformers < / h3 >

< ul


class ="skill-list" >

< li


class ="skill-item" > Google T5 Transformer Models < / li >

< li


class ="skill-item" > Hugging Face Transformers Pipeline < / li >

< li


class ="skill-item" > Grammar & amp; Fluency Correction < / li >

< li


class ="skill-item" > Readability Metrics (textstat) < / li >

< li


class ="skill-item" > Text Diff Analysis & amp; Visualization < / li >

< / ul >
< / div >

< !-- Domain
4 -->
< div


class ="skill-domain-card" >

< div


class ="skill-icon-wrapper" >

< svg
width = "22"
height = "22"
viewBox = "0 0 24 24"
fill = "none"
stroke = "currentColor"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < path
d = "M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z" > < / path > < / svg >
< / div >
< h3


class ="skill-domain-title" > Deployment & amp; Tools < / h3 >

< ul


class ="skill-list" >

< li


class ="skill-item" > Streamlit Cloud App Deployment < / li >

< li


class ="skill-item" > Pandas, NumPy, Matplotlib & amp; Seaborn < / li >

< li


class ="skill-item" > Google Colab GPU Pipelines < / li >

< li


class ="skill-item" > Git, GitHub & amp; Version Control < / li >

< li


class ="skill-item" > Rapid Prototyping & amp; UX Polish < / li >

< / ul >
< / div >
< / div >
< / div >
< / section >

< !-- Contact & Call
to
Action -->
< section


class ="contact-section" id="contact" >

< div


class ="container" >

< div


class ="contact-card" >

< div


class ="contact-info" >

< span


class ="section-tag" > Let's Connect</span>

< h2 > Ready
to
build
impactful, data - driven
solutions? < / h2 >
< p >
I
am
currently
available
for entry - level and junior Data Science / Machine Learning roles, collaborative projects, and freelance research.Let’s discuss how I can bring clear, high-performance machine learning models to your team.
< / p >
< div


class ="location-badge" >

< svg
width = "16"
height = "16"
viewBox = "0 0 24 24"
fill = "none"
stroke = "currentColor"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < path
d = "M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z" > < / path > < circle
cx = "12"
cy = "10"
r = "3" > < / circle > < / svg >
Based in Lahore, Pakistan · Open
to
Remote & amp;
Onsite
Opportunities
< / div >
< / div >

< div


class ="contact-buttons" >

< button


class ="btn btn-primary copy-email-btn" onclick="copyEmail()" >

< svg
width = "18"
height = "18"
viewBox = "0 0 24 24"
fill = "none"
stroke = "currentColor"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < rect
x = "9"
y = "9"
width = "13"
height = "13"
rx = "2"
ry = "2" > < / rect > < path
d = "M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1" > < / path > < / svg >
< span
id = "copyBtnText" > Copy
Email
Address < / span >
< / button >
< a
href = "mailto:asmamustafa600@gmail.com"


class ="btn btn-outline" >

< svg
width = "18"
height = "18"
viewBox = "0 0 24 24"
fill = "none"
stroke = "currentColor"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < path
d = "M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" > < / path > < polyline
points = "22,6 12,13 2,6" > < / polyline > < / svg >
asmamustafa600 @ gmail.com
< / a >
< a
href = "https://github.com/asmamustafa600-hub"
target = "_blank"
rel = "noopener"


class ="btn btn-outline" >

< svg
width = "18"
height = "18"
viewBox = "0 0 24 24"
fill = "none"
stroke = "currentColor"
stroke - width = "2"
stroke - linecap = "round"
stroke - linejoin = "round" > < path
d = "M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22" > < / path > < / svg >
github.com / asmamustafa600 - hub
< / a >
< / div >
< / div >
< / div >
< / section >

< !-- Footer -->
< footer >
< div


class ="container footer-inner" >

< div >
© 2026
Asma
Mustafa · Data
Science & amp;
Machine
Learning
Practitioner.
< / div >
< div


class ="footer-links" >

< a
href = "#home" > Back
to
Top ↑ < / a >
< a
href = "https://github.com/asmamustafa600-hub"
target = "_blank"
rel = "noopener" > GitHub < / a >
< a
href = "mailto:asmamustafa600@gmail.com" > Email < / a >
< / div >
< / div >
< / footer >

< !-- Toast
for Email Copying -->
< div


class ="toast" id="toast" >

< svg
width = "18"
height = "18"
viewBox = "0 0 24 24"
fill = "none"
stroke = "var(--accent-emerald)"
stroke - width = "2.5"
stroke - linecap = "round"
stroke - linejoin = "round" > < polyline
points = "20 6 9 17 4 12" > < / polyline > < / svg >
< span > Email
copied
to
clipboard: asmamustafa600 @ gmail.com < / span >
< / div >

< !-- JavaScript
for Interactivity -->
< script >
// Theme
Management
const
themeToggle = document.getElementById('themeToggle');
const
sunIcon = document.getElementById('sunIcon');
const
moonIcon = document.getElementById('moonIcon');
const
html = document.documentElement;

const
savedTheme = localStorage.getItem('portfolio-theme') | | 'dark';
setTheme(savedTheme);

themeToggle.addEventListener('click', () = > {
    const
current = html.getAttribute('data-theme');
const
next = current == = 'dark' ? 'light': 'dark';
setTheme(next);
});

function
setTheme(theme)
{
    html.setAttribute('data-theme', theme);
localStorage.setItem('portfolio-theme', theme);
if (theme === 'light')
{
    sunIcon.style.display = 'block';
moonIcon.style.display = 'none';
} else {
    sunIcon.style.display = 'none';
moonIcon.style.display = 'block';
}
}

// Copy
Email
with Toast
    function
    copyEmail()
    {
        const
    email = 'asmamustafa600@gmail.com';
    navigator.clipboard.writeText(email).then(() = > {
        showToast();
    }).catch(() = > {
                    // Fallback
    const
    tempInput = document.createElement('input');
    tempInput.value = email;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand('copy');
    document.body.removeChild(tempInput);
    showToast();
    });
    }

    function
    showToast()
    {
        const
    toast = document.getElementById('toast');
    toast.classList.add('show');
    setTimeout(() = > {
        toast.classList.remove('show');
    }, 3200);
    }

    // Project
    Category
    Filter
    function
    filterProjects(category, btnElement)
    {
    // Update
    active
    button
    document.querySelectorAll('.filter-btn').forEach(btn= > btn.classList.remove('active'));
    btnElement.classList.add('active');

    // Filter
    cards
    const
    cards = document.querySelectorAll('.project-card');
    cards.forEach(card= > {
        const
    cardCategories = card.getAttribute('data-category') | | '';
    if (category === 'all' | | cardCategories.includes(category)) {
    card.style.display = 'flex';
    } else {
    card.style.display = 'none';
    }
    });
    }
    < / script >

    < / body >
    < / html >