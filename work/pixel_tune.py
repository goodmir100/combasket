from pathlib import Path
p=Path('src/App.vue'); s=p.read_text(encoding='utf-8')
s=s.replace('<button v-else class="auth-switch" type="button" @click="go(\'login\')">Login</button>','')
p.write_text(s,encoding='utf-8')

p=Path('src/style.css'); s=p.read_text(encoding='utf-8')
changes=[
(".home-hero{height:355px;position:relative;padding-top:85px}",".home-hero{height:580px;position:relative;padding-top:130px}"),
(".ball-one{left:4%;top:42px}",".ball-one{left:6%;top:64px}"),
(".ball-two{right:6%;top:190px;width:118px;height:118px}",".ball-two{right:6%;top:365px;width:177px;height:177px}"),
(".hero-slash{position:absolute;right:9%;top:48px;width:390px;height:230px",".hero-slash{position:absolute;right:9%;top:32px;width:520px;height:345px"),
(".intro-glass{position:relative;z-index:1;width:min(760px,76%);min-height:228px;",".intro-glass{position:relative;z-index:1;width:76%;min-height:344px;"),
("border-radius:30px;background:linear-gradient(110deg","border-radius:45px;background:linear-gradient(110deg"),
(".intro-glass p{margin:0;font:italic 26px/1.5 Arial,sans-serif",".intro-glass p{margin:0;font:italic 38px/1.5 Arial,sans-serif"),
(".intro-glass p strong{font:700 26px var(--display)",".intro-glass p strong{font:700 36px var(--display)"),
(".product-section h1,.best-section h2,.why-section h2{font:400 clamp(38px,5.1vw,69px)/1.1 var(--display);color:#0037ff;text-align:center;margin:0 0 22px",".product-section h1,.best-section h2,.why-section h2{font:400 clamp(38px,5.1vw,69px)/1.1 var(--display);color:#0037ff;text-align:center;margin:0 0 48px"),
(".collection-row{display:grid;grid-template-columns:repeat(5,1fr);gap:18px",".collection-row{display:grid;grid-template-columns:repeat(5,1fr);gap:27px"),
(".why-section{height:535px;position:relative;margin:0 5% 16px;display:flex;justify-content:center;align-items:flex-start;padding-top:26px}",".why-section{height:780px;position:relative;margin:0 5% 16px;display:flex;justify-content:center;align-items:flex-start;padding-top:33px}"),
(".benefit-card{position:absolute;z-index:1;width:145px;height:150px;",".benefit-card{position:absolute;z-index:1;width:215px;height:225px;"),
(".benefit-card svg{stroke-width:2.5;margin-bottom:7px}",".benefit-card svg{width:76px;height:76px;stroke-width:2.5;margin-bottom:7px}"),
(".benefit-card p{font:16px/1.05 var(--display)",".benefit-card p{font:21px/1.05 var(--display)"),
(".benefit-a{left:8%;top:118px}.benefit-b{left:39%;top:118px}.benefit-c{right:8%;top:118px}.benefit-d{left:20%;top:300px}.benefit-e{right:20%;top:300px}",".benefit-a{left:8%;top:163px}.benefit-b{left:39%;top:163px}.benefit-c{right:8%;top:163px}.benefit-d{left:20%;top:438px}.benefit-e{right:20%;top:438px}"),
(".best-section{position:relative;padding:3px 4% 94px}",".best-section{position:relative;padding:3px 4% 199px}"),
(".best-section h2{font-size:clamp(47px,6.2vw,76px);margin-bottom:24px}",".best-section h2{font-size:clamp(47px,6.2vw,76px);margin-bottom:40px}"),
(".best-tile{height:clamp(250px,33vw,460px)",".best-tile{height:clamp(250px,29vw,420px)"),
(".store-footer{background:#1e00ff;color:white;min-height:305px",".store-footer{background:#1e00ff;color:white;min-height:371px"),
(".back-pill{position:relative;z-index:3;margin:18px 0 0 3.5%;height:68px;border:0;background:#0037d8;color:#fff;border-radius:50px;padding:0 19px;display:flex;align-items:center;gap:8px;font:36px var(--display)}",".back-pill{position:relative;z-index:3;margin:27px 0 0 3.5%;height:80px;border:0;background:#0037d8;color:#fff;border-radius:50px;padding:0 19px;display:flex;align-items:center;gap:8px;font:44px var(--display)}"),
(".cart-panel{position:relative;z-index:1;margin:34px 3.5% 0;",".cart-panel{position:relative;z-index:1;margin:24px 3.5% 0;"),
(".auth-page{min-height:calc(100vh - 64px);position:relative;background:#152348 url('/images/home-reference.png') center 49%/cover no-repeat;display:flex;align-items:center;justify-content:center;padding:80px 3%}",".auth-page{height:100vh;min-height:700px;position:relative;background:#152348 url('/images/court-background.jpg') center/cover no-repeat;display:flex;align-items:center;justify-content:center;padding:36px 2.5%}"),
(".auth-bg{position:absolute;inset:0;background:#12204a33;backdrop-filter:blur(2px)}.auth-page .back-pill{position:absolute;top:0;left:0}",".auth-bg{position:absolute;inset:0;background:transparent}.auth-page .back-pill{display:none}"),
(".auth-glass{position:relative;z-index:1;width:100%;min-height:545px;border-radius:48px;padding:72px 5%;background:#c9cce5b8;backdrop-filter:blur(22px);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:42px}",".auth-glass{position:relative;z-index:1;width:100%;height:min(71.1vh,728px);min-height:545px;border-radius:50px;padding:0 5%;background:linear-gradient(115deg,#6073c9a8,#a5afd5ad 50%,#dbd2c0d0);backdrop-filter:blur(28px);display:flex;flex-direction:column;align-items:center;justify-content:flex-start;gap:62px}.auth-login .auth-glass{padding-top:160px}.auth-register .auth-glass{padding-top:87px}"),
(".auth-submit{width:36%;height:88px;",".auth-submit{width:32%;height:88px;"),
]
for old,new in changes:
    count=s.count(old)
    if count != 1: print('SKIP',count,old[:100])
    else: s=s.replace(old,new,1)
# Append close-overlay cart visuals and reference-proportioned auth form spacing.
s += "\n.mini-cart-overlay{position:fixed;z-index:25;inset:64px 0 0;display:flex;justify-content:flex-end;align-items:flex-start;padding:0 7% 28px 0;background:#ffffff05}.mini-cart{position:relative;width:min(520px,94vw);min-height:590px;padding:70px 24px 28px;border-radius:34px;background:linear-gradient(130deg,#cbd7ffed,#d5d8ecdb 57%,#e8ded1e8);backdrop-filter:blur(28px);box-shadow:0 18px 50px #00146c25;display:flex;flex-direction:column;gap:28px}.mini-cart:before{content:'';position:absolute;z-index:-1;right:8%;top:-36px;width:70%;height:150px;background:#00197a;border-radius:34px;transform:rotate(-12deg)}.mini-cart-close{position:absolute;right:18px;top:13px;border:0;background:none;color:#fff}.mini-cart-item{height:120px;border-radius:22px;background:#fffffff0;display:grid;grid-template-columns:74px 1fr 34px 34px 34px;align-items:center;padding:8px;gap:7px;color:#fff}.mini-cart-item>img{width:74px;height:104px;object-fit:cover;border-radius:14px}.mini-cart-product{min-width:0;display:grid;gap:12px}.mini-cart-product strong{background:#0037ff;border-radius:20px;padding:6px;text-align:center;font:15px var(--display);white-space:nowrap}.mini-cart-product>div{display:flex;gap:6px;align-items:center;justify-content:center;background:#02ca48;border-radius:18px;padding:3px;color:white}.mini-cart-product b{font:19px var(--display)}.mini-cart-product span{font:10px var(--display)}.mini-cart-item>button{border:0;background:#0037df;color:#fff;border-radius:8px;width:32px;height:32px;display:grid;place-items:center;padding:0}.mini-cart-item>button:last-child{background:#00236f}.mini-cart-buy{margin:0 0 0 auto;width:172px;height:58px;border:0;border-radius:20px;background:#09d447;color:white;font:26px var(--display)}.mini-cart-buy:disabled{opacity:.45}.auth-register .auth-glass{gap:62px}.auth-login .auth-glass{gap:58px}.auth-login .auth-submit,.auth-register .auth-submit{flex:none}.auth-switch{padding:0}.auth-glass input{flex:none}\n"
p.write_text(s,encoding='utf-8')
