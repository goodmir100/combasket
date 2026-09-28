from pathlib import Path
p=Path('src/App.vue'); s=p.read_text(encoding='utf-8')
s=s.replace("function openProduct(product: Product) { selected.value = product; screen.value = 'product';", "function openProduct(product: Product) { previousScreen.value = screen.value; selected.value = product; screen.value = 'product';")
s=s.replace("function back() { screen.value = previousScreen.value === 'home' ? 'home' : previousScreen.value; window.scrollTo({ top: 0, behavior: 'smooth' }) }", "function back() { screen.value = previousScreen.value === 'home' || previousScreen.value === 'login' ? 'home' : previousScreen.value; window.scrollTo({ top: 0, behavior: 'smooth' }) }\nfunction scrollToProducts() { document.getElementById('new-collection')?.scrollIntoView({ behavior: 'smooth' }) }")
s=s.replace("document.getElementById('new-collection')?.scrollIntoView({behavior:'smooth'})", "scrollToProducts()")
lines=s.splitlines()
for i,line in enumerate(lines):
    if '<main v-else-if="screen === \'cart\'"' in line:
        lines[i] = """    <main v-else-if=\"screen === 'cart'\" class=\"cart-page\"><button class=\"back-pill\" @click=\"go('home')\"><ArrowLeft :size=\"22\"/> BACK</button><div class=\"cart-panel\"><div class=\"cart-alert\"><span class=\"alert-icon\">!</span><h1>ATTENTION!<br/><em>Confirm your<br/>orders and<br/>pay it!</em></h1></div><div v-if=\"cart.length\" class=\"cart-list\"><article v-for=\"(p,i) in checkoutItems\" :key=\"i + '-' + p.id\"><img :src=\"p.image\" :alt=\"p.name\"/><div><strong>{{ p.id === 2 ? 'Basket Socks' : p.id === 5 ? 'Sleeve' : p.id === 4 ? 'Wave Basketball' : p.name }}</strong><b>{{ fmt(p.price) }}</b></div></article><button class=\"pay-button\" @click=\"cart = []; go('home')\">Pay</button></div><div v-else class=\"empty-cart\"><ShoppingCart :size=\"42\"/><h2>Your cart is empty</h2><p>Find your next game-day essential.</p><button class=\"pay-button\" @click=\"go('home')\">Go shopping</button></div></div></main>"""
s='\n'.join(lines)+'\n'
p.write_text(s,encoding='utf-8')
print('cart summary and nav updated')
