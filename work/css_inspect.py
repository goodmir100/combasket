from pathlib import Path
s=Path('src/style.css').read_text()
for key in ['.home-hero{','.intro-glass{','.product-section{','.product-section h1,','.collection-row{','.collection-tile{','.why-section{','.benefit-card{','.benefit-a{','.benefit-b{','.benefit-c{','.benefit-d{','.benefit-e{','.best-section{','.best-tile{','.store-footer{','.auth-page{','.auth-bg{','.auth-page .back-pill{','.auth-glass{','.auth-glass input{','.profile-avatar{']:
 i=s.find(key)
 print(key, s[i:i+320] if i>=0 else 'missing')
