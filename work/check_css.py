from pathlib import Path
s=Path('src/style.css').read_text()
for key in ['.home-page{','.home-hero{','.intro-glass{','.product-section{','.collection-row{','.why-section{','.benefit-card{','.best-section{','.best-tile{','.store-footer{','.cart-panel{','.cart-list{','.cart-list article{','.pay-button{','.profile-card{','.profile-data{','.auth-page{','.auth-glass{','.auth-login .auth-glass{','.mini-cart-overlay{']:
 i=s.find(key); print('\n'+key+' '+s[i:i+230])
