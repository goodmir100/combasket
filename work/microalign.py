from pathlib import Path
p=Path('src/style.css');s=p.read_text(encoding='utf-8')
changes=[
('.home-page{background:var(--paper);background-image:radial-gradient(ellipse at 13% 8%,#dbe4ff 0 4%,transparent 4.3%),radial-gradient(ellipse at 85% 34%,#dae2ff 0 4%,transparent 4.3%),radial-gradient(ellipse at 24% 63%,#dbe4ff 0 4%,transparent 4.3%),radial-gradient(ellipse at 78% 79%,#dbe4ff 0 4%,transparent 4.3%)}', '.home-page{background:var(--paper);position:relative}'),
('.cart-panel{position:relative;z-index:1;margin:24px 2.8% 0;min-height:728px;border-radius:50px;background:linear-gradient(110deg,#cdd8ffde,#cbd2f1bb);backdrop-filter:blur(16px);display:grid;grid-template-columns:40% 60%;padding:55px 0;gap:0;align-items:center}', '.cart-panel{position:relative;z-index:1;margin:24px 2.8% 0;min-height:728px;border-radius:50px;background:linear-gradient(110deg,#cdd8ffde,#cbd2f1bb);backdrop-filter:blur(16px);display:grid;grid-template-columns:40% 60%;padding:55px 0;gap:0;align-items:center}'),
('.cart-list{display:flex;flex-direction:column;gap:0;padding-left:17.5%;padding-right:6%;transform:translateY(48px)}', '.cart-list{display:flex;flex-direction:column;gap:0;padding-left:18.75%;padding-right:6%;transform:translateY(56px)}'),
('.pay-button{align-self:flex-end;margin:52px 0 0 auto;min-width:264px;height:74px;', '.pay-button{align-self:flex-end;margin:51px 0 0 auto;min-width:264px;height:74px;'),
('.cart-alert{transform:translateY(-18px)}', '.cart-alert{transform:translateY(-29px)}'),
('.cart-panel{position:relative;z-index:1;margin:24px 2.8% 0;', '.cart-panel{position:relative;z-index:1;margin:24px 2.8% 0;'),
('.profile-data{width:100%;display:grid;grid-template-columns:repeat(4,1fr);text-align:center;gap:45px 10px;', '.profile-data{width:100%;display:grid;grid-template-columns:repeat(4,1fr);text-align:center;gap:55px 10px;'),
('.profile-card{position:relative;z-index:1;margin:40px 3.5% 0;min-height:728px;border-radius:50px;background:#cbd4f6;box-shadow:inset 0 0 95px #fff7;display:flex;justify-content:center;align-items:flex-start;padding:315px 4% 90px}', '.profile-card{position:relative;z-index:1;margin:40px 3.5% 0;min-height:728px;border-radius:50px;background:#cbd4f6;box-shadow:inset 0 0 95px #fff7;display:flex;justify-content:center;align-items:flex-start;padding:315px 4% 90px}'),
]
for old,new in changes:
 c=s.count(old)
 if c==1:s=s.replace(old,new,1)
 else:print('skip',c,old[:80])
# Use one set of floating line-art balls and the oversized dark blue floor ribbon.
s += "\n.product-section h1{position:relative;z-index:1}.collection-ball{top:-5px;left:29%;width:205px;height:205px;z-index:0}.best-section h2,.best-grid{position:relative;z-index:1}.best-ribbon{position:absolute;z-index:0;left:-22px;bottom:0;width:62%;height:255px;border-radius:40px;background:#001b84;transform:rotate(-6deg);clip-path:polygon(0 7%,70% 0,100% 23%,70% 28%,45% 50%,23% 54%,100% 85%,70% 100%,5% 88%)}.best-ball-lower{left:26%;bottom:78px;width:175px;height:175px}.best-ball-right{right:13%;bottom:18px;width:145px;height:145px}.mini-cart-product b{font-size:18px}.cart-list .pay-button{margin-top:51px}.cart-panel .cart-list article button{display:none}.logo-symbol{width:32px;height:25px;line-height:1;transform:none;flex:none}.cart-list article+article{margin-top:52px}.profile-card .profile-edit{cursor:pointer}\n"
s=s.replace(".collection-ball{top:-5px;left:29%;width:205px;height:205px;z-index:0}",".collection-ball{top:-5px;left:29%;width:205px;height:205px;z-index:0}")
p.write_text(s,encoding='utf-8')
