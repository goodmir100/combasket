<script setup lang="ts">
import { computed, nextTick, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import {
  ArrowLeft, ArrowRight, ArrowUpRight, Check, ChevronDown, ChevronRight,
  Heart, Menu, Search, ShoppingBag, Star, Trash2, UserRound, X, Zap,
} from 'lucide-vue-next'
import ProductCard from './components/ProductCard.vue'

type Screen = 'home' | 'product' | 'cart' | 'profile' | 'login' | 'register' | 'about' | 'tech' | 'collection' | 'support'
type Category = 'All' | 'Basketballs' | 'Accessories' | 'Protection' | 'Apparel'
type Product = {
  id: number
  name: string
  category: Exclude<Category, 'All'>
  price: number
  image: string
  gallery: string[]
  label?: string
  size: string
  purpose: string
  rating: string
  description: string
}

const products: Product[] = [
  {
    id: 1, name: 'ASPHVLT Streetball', category: 'Basketballs', price: 38946,
    image: '/images/collection-asphalt.png',
    gallery: ['/images/ball-detail.jpg', '/images/ball-yellow.jpg', '/images/collection-asphalt.png'],
    label: 'Court favourite', size: '6', purpose: 'Outdoor', rating: '4.9',
    description: 'A sure grip and true bounce for the concrete courts you know by heart.',
  },
  {
    id: 2, name: 'Grip Basketball Socks', category: 'Accessories', price: 7000,
    image: '/images/collection-socks.png',
    gallery: ['/images/collection-socks.png', '/images/socks.jpg'],
    label: 'Best seller', size: 'M / L', purpose: 'All courts', rating: '4.9',
    description: 'Stay planted through every cut, stop and change of direction.',
  },
  {
    id: 3, name: 'Pechenka Chocolate', category: 'Basketballs', price: 24990,
    image: '/images/collection-pechenka.png',
    gallery: ['/images/collection-pechenka.png', '/images/best-pechenka.png', '/images/ball-chocolate.jpg', '/images/best-chocolate.jpg'],
    label: 'Size 7', size: '7', purpose: 'Indoor', rating: '5.0',
    description: 'A full-size indoor ball with a textured feel and a look all its own.',
  },
  {
    id: 4, name: 'WAVE Street Basketball', category: 'Basketballs', price: 30000,
    image: '/images/best-wave.png',
    gallery: ['/images/best-wave.png', '/images/ball-blue.jpg', '/images/cart-wave.jpg'],
    label: 'New drop', size: '6', purpose: 'Outdoor', rating: '4.8',
    description: 'Built for open-air runs, quick handles and long days on the court.',
  },
  {
    id: 5, name: 'Knee Compression Sleeve', category: 'Protection', price: 9000,
    image: '/images/best-sleeves.png',
    gallery: ['/images/best-sleeves.png', '/images/best-sleeve.jpg', '/images/collection-leggings.png', '/images/leggings.jpg', '/images/cart-sleeve.jpg'],
    label: 'Court tested', size: 'S / M / L', purpose: 'Training', rating: '4.8',
    description: 'Flexible support that stays in place while you move through the game.',
  },
  {
    id: 6, name: 'Court Performance Jersey', category: 'Apparel', price: 18900,
    image: '/images/collection-apparel.png',
    gallery: ['/images/collection-apparel.png', '/images/apparel.jpg'],
    size: 'S / M / L', purpose: 'Training', rating: '4.7',
    description: 'Light, easy-moving apparel for warmups, practice and game day.',
  },
]

const screen = ref<Screen>('home')
const previousScreen = ref<Screen>('home')
const selected = ref<Product>(products[0])
const selectedPhoto = ref(products[0].gallery[0])
const cart = ref<Product[]>([products[3], products[1], products[4]])
const cartOpen = ref(false)
const paying = ref(false)
const orderPlaced = ref(false)
const favorites = ref<number[]>([])
const menuOpen = ref(false)
const query = ref('')
const searchOpen = ref(false)
const activeCategory = ref<Category>('All')
const authEmail = ref('')
const authPassword = ref('')
const confirmPassword = ref('')
const authError = ref('')
const mainContent = ref<HTMLElement | null>(null)
const miniCartClose = ref<HTMLButtonElement | null>(null)
const cartTrigger = ref<HTMLButtonElement | null>(null)
const focusBeforeCart = ref<HTMLElement | null>(null)

const featuredProducts = [products[0], products[3], products[2], products[1], products[5], products[4]]
const categoryOptions: { label: string; value: Category }[] = [
  { label: 'Everything', value: 'All' },
  { label: 'Basketballs', value: 'Basketballs' },
  { label: 'Accessories', value: 'Accessories' },
  { label: 'Protection', value: 'Protection' },
  { label: 'Apparel', value: 'Apparel' },
]
const collectionProducts = computed(() => {
  const normalizedQuery = query.value.trim().toLowerCase()
  return products.filter(product => {
    const matchesCategory = activeCategory.value === 'All' || product.category === activeCategory.value
    const matchesQuery = !normalizedQuery || (product.name + ' ' + product.category + ' ' + product.purpose).toLowerCase().includes(normalizedQuery)
    return matchesCategory && matchesQuery
  })
})
const searchSuggestions = computed(() => query.value.trim() ? collectionProducts.value.slice(0, 4) : [])
const cartTotal = computed(() => cart.value.reduce((total, product) => total + product.price, 0))
const formatPrice = (price: number) => new Intl.NumberFormat('ru-RU').format(price)
const cartImage = (product: Product) => product.id === 4
  ? '/images/cart-wave.jpg'
  : product.id === 2
    ? '/images/cart-socks.jpg'
    : product.id === 5
      ? '/images/cart-sleeve.jpg'
      : product.gallery[0]

function go(next: Screen) {
  if (screen.value !== next) previousScreen.value = screen.value
  screen.value = next
  menuOpen.value = false
  searchOpen.value = false
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

function openProduct(product: Product) {
  previousScreen.value = screen.value
  selected.value = product
  selectedPhoto.value = product.gallery[0]
  screen.value = 'product'
  menuOpen.value = false
  searchOpen.value = false
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

function back() {
  const destination = previousScreen.value === 'login' || previousScreen.value === 'register' ? 'home' : previousScreen.value
  screen.value = destination
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

function toggleFavorite(id: number) {
  favorites.value = favorites.value.includes(id)
    ? favorites.value.filter(item => item !== id)
    : [...favorites.value, id]
}

function addToCart(product: Product, openPage = true) {
  cart.value.push(product)
  if (openPage) {
    previousScreen.value = screen.value
    screen.value = 'cart'
  }
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

function quickAdd(product: Product) {
  addToCart(product, false)
  openMiniCart()
}

function removeFromCart(index: number) {
  cart.value.splice(index, 1)
}

function openMiniCart() {
  focusBeforeCart.value = document.activeElement instanceof HTMLElement ? document.activeElement : cartTrigger.value
  cartOpen.value = true
  menuOpen.value = false
  nextTick(() => miniCartClose.value?.focus())
}

function closeMiniCart() {
  cartOpen.value = false
  nextTick(() => focusBeforeCart.value?.focus())
}

function trapModalFocus(event: KeyboardEvent) {
  if (event.key !== 'Tab') return
  const panel = event.currentTarget as HTMLElement
  const focusable = [...panel.querySelectorAll<HTMLElement>('button:not(:disabled), a[href], input:not(:disabled), [tabindex="0"]')]
  if (!focusable.length) return
  const first = focusable[0]
  const last = focusable[focusable.length - 1]
  if (event.shiftKey && document.activeElement === first) {
    event.preventDefault()
    last.focus()
  } else if (!event.shiftKey && document.activeElement === last) {
    event.preventDefault()
    first.focus()
  }
}

function runSearch() {
  activeCategory.value = 'All'
  go('collection')
}

function submitAuth() {
  authError.value = ''
  if (screen.value === 'register' && authPassword.value !== confirmPassword.value) {
    authError.value = 'Those passwords do not match. Please try again.'
    return
  }
  go('home')
}

function payOrder() {
  if (!cart.value.length || paying.value) return
  paying.value = true
  orderPlaced.value = true
  cart.value = []
  window.setTimeout(() => {
    paying.value = false
    go('profile')
  }, 800)
}

function onGlobalKeydown(event: KeyboardEvent) {
  if (event.key === 'Escape') {
    if (cartOpen.value) closeMiniCart()
    menuOpen.value = false
    searchOpen.value = false
  }
}

watch(cartOpen, open => {
  document.body.style.overflow = open ? 'hidden' : ''
})
watch(screen, async () => {
  await nextTick()
  mainContent.value?.focus({ preventScroll: true })
})
onMounted(() => document.addEventListener('keydown', onGlobalKeydown))
onBeforeUnmount(() => {
  document.removeEventListener('keydown', onGlobalKeydown)
  document.body.style.overflow = ''
})
</script>

<template>
  <div class="combasket" @keydown.esc="menuOpen = false; searchOpen = false">
    <a class="skip-link" href="#main-content">Skip to content</a>
    <div class="announcement-bar">
      <span>Gear for the next generation of the game</span>
      <span class="announcement-note"><span class="live-dot"></span> Made for the court</span>
    </div>

    <header class="site-header">
      <div class="header-inner">
        <button class="menu-toggle icon-button" type="button" :aria-expanded="menuOpen" aria-controls="primary-navigation" :aria-label="menuOpen ? 'Close menu' : 'Open menu'" @click="menuOpen = !menuOpen">
          <X v-if="menuOpen" :size="21" aria-hidden="true" />
          <Menu v-else :size="21" aria-hidden="true" />
        </button>
        <button class="brand-lockup" type="button" aria-label="COMBASKET home" @click="go('home')">
          <img src="/images/combasket-mark-white.png" alt="" width="34" height="34" />
          <span>COMBASKET</span>
        </button>
        <nav id="primary-navigation" class="primary-navigation" :class="{ 'is-open': menuOpen }" aria-label="Main navigation">
          <button type="button" @click="go('collection')">Shop</button>
          <button type="button" @click="go('collection')">Collections</button>
          <button type="button" @click="go('about')">Our story</button>
          <button type="button" @click="go('tech')">Technology</button>
          <button type="button" @click="go('support')">Support</button>
        </nav>
        <form class="header-search" role="search" @submit.prevent="runSearch">
          <Search :size="17" aria-hidden="true" />
          <input v-model="query" type="search" aria-label="Search products" placeholder="Search the court" @focus="searchOpen = true" @keydown.esc="searchOpen = false" />
          <button type="submit" aria-label="Submit search"><ArrowRight :size="17" aria-hidden="true" /></button>
          <div v-if="searchOpen && searchSuggestions.length" class="search-suggestions">
            <button v-for="product in searchSuggestions" :key="product.id" type="button" @click="openProduct(product)">
              <img :src="product.image" alt="" width="46" height="56" />
              <span><strong>{{ product.name }}</strong><small>{{ product.category }} · {{ formatPrice(product.price) }} ₸</small></span>
              <ChevronRight :size="16" aria-hidden="true" />
            </button>
          </div>
        </form>
        <div class="header-actions">
          <button class="mobile-search-trigger icon-button" type="button" :aria-expanded="searchOpen" aria-label="Search products" @click="searchOpen = !searchOpen"><Search :size="20" aria-hidden="true" /></button>
          <button class="icon-button profile-trigger" type="button" aria-label="Open profile" @click="go('profile')"><UserRound :size="19" aria-hidden="true" /></button>
          <button ref="cartTrigger" class="cart-trigger" type="button" :aria-label="'Open cart, ' + cart.length + ' items'" @click="openMiniCart">
            <ShoppingBag :size="18" aria-hidden="true" /><span>Bag</span><b aria-live="polite" aria-atomic="true">{{ cart.length }}</b>
          </button>
        </div>
      </div>
      <form v-if="searchOpen" class="mobile-search" role="search" @submit.prevent="runSearch">
        <Search :size="18" aria-hidden="true" /><input v-model="query" type="search" aria-label="Search products" placeholder="Search the court" /><button type="submit">Search</button>
      </form>
    </header>

    <main id="main-content" ref="mainContent" class="page-main" tabindex="-1">
      <div v-if="screen === 'home'" class="home-page">
        <section class="hero-section page-width" aria-labelledby="hero-title">
          <div class="hero-copy">
            <p class="eyebrow"><span class="eyebrow-mark"></span> COMBASKET / BUILT TO PLAY</p>
            <h1 id="hero-title">Own the<br /><span>next possession.</span></h1>
            <p class="hero-description">Court-tested basketballs and gear for the ones who always want one more game.</p>
            <div class="hero-actions">
              <button class="button button-primary" type="button" @click="go('collection')">Shop the collection <ArrowRight :size="18" aria-hidden="true" /></button>
              <button class="text-link" type="button" @click="go('about')">Meet COMBASKET <ArrowUpRight :size="16" aria-hidden="true" /></button>
            </div>
            <div class="hero-proof"><span class="proof-stars" aria-label="Rated five stars"><Star v-for="n in 5" :key="n" :size="14" fill="currentColor" aria-hidden="true" /></span><span><strong>4.9 / 5</strong> from players on court</span></div>
          </div>
          <div class="hero-visual">
            <img class="hero-decor" src="/images/decor-hero.png" alt="" aria-hidden="true" />
            <img class="hero-outline" src="/images/basketball-outline.png" alt="" aria-hidden="true" width="120" height="120" />
            <figure class="hero-photo">
              <img src="/images/ball-detail.jpg" alt="ASPHVLT yellow streetball on an outdoor basketball court" width="612" height="818" fetchpriority="high" />
              <figcaption class="hero-photo-label"><span>ASPHVLT · SERIES 06</span><span>For outdoor courts</span></figcaption>
            </figure>
            <div class="hero-product-note"><span class="product-note-icon"><Zap :size="16" fill="currentColor" aria-hidden="true" /></span><span><strong>Ready for the run</strong><small>Grip that stays with you</small></span><span class="note-arrow"><ArrowUpRight :size="18" aria-hidden="true" /></span></div>
            <span class="hero-index">01 <i></i> 06</span>
          </div>
        </section>

        <div class="ticker-strip" aria-label="COMBASKET product highlights"><div class="ticker-track"><span>Street ready</span><b aria-hidden="true">✳</b><span>Grip first</span><b aria-hidden="true">✳</b><span>Play your way</span><b aria-hidden="true">✳</b><span>Built for the next run</span><b aria-hidden="true">✳</b><span>Street ready</span><b aria-hidden="true">✳</b><span>Grip first</span></div></div>

        <section id="new-collection" class="product-section page-width" aria-labelledby="products-title">
          <div class="section-heading"><div><p class="eyebrow"><span class="eyebrow-mark"></span> THE STARTING FIVE</p><h2 id="products-title">Pick your <span>game.</span></h2></div><button class="text-link section-link" type="button" @click="go('collection')">View all gear <ArrowRight :size="17" aria-hidden="true" /></button></div>
          <div class="product-grid"><ProductCard v-for="product in featuredProducts" :key="product.id" :product="product" :favorite="favorites.includes(product.id)" @open="openProduct" @favorite="toggleFavorite" @add="quickAdd" /></div>
        </section>

        <section class="why-section" aria-labelledby="why-title">
          <img class="why-decor" src="/images/decor-why.png" alt="" aria-hidden="true" />
          <div class="why-inner page-width">
            <div class="why-heading"><p class="eyebrow eyebrow-light"><span class="eyebrow-mark"></span> MADE FOR MOVEMENT</p><h2 id="why-title">Every detail<br />has a reason.</h2><p>Less thinking about your gear. More feeling the game.</p></div>
            <div class="benefit-grid">
              <article class="benefit-item"><img src="/images/icon-quality.png" alt="" width="50" height="50" loading="lazy" /><h3>Game-ready</h3><p>Durable materials made for full runs.</p></article>
              <article class="benefit-item"><img src="/images/icon-flame.png" alt="" width="50" height="50" loading="lazy" /><h3>More control</h3><p>A confident feel through every move.</p></article>
              <article class="benefit-item"><img src="/images/icon-jersey.png" alt="" width="50" height="50" loading="lazy" /><h3>Street to pro</h3><p>Versatile pieces for every court.</p></article>
              <article class="benefit-item"><img src="/images/icon-basketball.png" alt="" width="50" height="50" loading="lazy" /><h3>Modern by design</h3><p>Clean style with a basketball soul.</p></article>
              <article class="benefit-item"><img src="/images/icon-test-tube.png" alt="" width="50" height="50" loading="lazy" /><h3>Player tested</h3><p>Inspired by real time on court.</p></article>
            </div>
          </div>
        </section>

        <section class="collection-feature page-width" aria-labelledby="collection-feature-title">
          <div class="collection-feature-copy"><p class="eyebrow"><span class="eyebrow-mark"></span> FIND YOUR EDGE</p><h2 id="collection-feature-title">The court<br />is your <span>canvas.</span></h2><p>From grip socks to training layers, build a kit that moves the way you do.</p><button class="button button-dark" type="button" @click="go('collection')">Explore all collections <ArrowRight :size="18" aria-hidden="true" /></button></div>
          <div class="collection-feature-collage">
            <button class="feature-image feature-image-ball" type="button" aria-label="Shop WAVE basketball" @click="openProduct(products[3])"><img src="/images/ball-blue.jpg" alt="Blue WAVE basketball on an outdoor court" width="450" height="600" loading="lazy" /><span>WAVE / 06</span></button>
            <button class="feature-image feature-image-apparel" type="button" aria-label="Shop court apparel" @click="openProduct(products[5])"><img src="/images/apparel.jpg" alt="COMBASKET performance apparel" width="390" height="520" loading="lazy" /><span>COURT / LAYERS</span></button>
            <img class="feature-outline" src="/images/basketball-outline.png" alt="" aria-hidden="true" width="90" height="90" />
          </div>
        </section>

        <section class="brand-story"><div class="brand-story-inner page-width">
          <div class="story-mark"><img src="/images/combasket-mark-white.png" alt="COMBASKET mark" width="122" height="122" loading="lazy" /></div>
          <div class="story-copy"><p class="eyebrow eyebrow-light"><span class="eyebrow-mark"></span> THE GAME BRINGS US TOGETHER</p><h2>Built around<br />basketball culture.</h2><p>COMBASKET makes basketballs and equipment for players who demand quality and confidence on every court. Inspired by street and professional basketball, every piece brings performance and modern style into the game.</p><button class="text-link text-link-light" type="button" @click="go('about')">Read our story <ArrowRight :size="17" aria-hidden="true" /></button></div>
        </div></section>
      </div>

      <section v-else-if="screen === 'collection'" class="catalog-page page-width" aria-labelledby="catalog-title">
        <div class="page-topline"><button class="back-link" type="button" @click="go('home')"><ArrowLeft :size="17" aria-hidden="true" /> Home</button><span>COMBASKET / SHOP</span></div>
        <div class="catalog-heading"><div><p class="eyebrow"><span class="eyebrow-mark"></span> PICK YOUR EQUIPMENT</p><h1 id="catalog-title">The collection.</h1></div><p>Find the pieces that make you feel at home on the court.</p></div>
        <div class="catalog-controls"><div class="filter-list" role="group" aria-label="Filter by category"><button v-for="option in categoryOptions" :key="option.value" type="button" :class="{ active: activeCategory === option.value }" :aria-pressed="activeCategory === option.value" @click="activeCategory = option.value">{{ option.label }}</button></div><label class="catalog-search"><Search :size="17" aria-hidden="true" /><span class="sr-only">Search the collection</span><input v-model="query" type="search" placeholder="Search the collection" /></label></div>
        <p class="results-count" aria-live="polite">{{ collectionProducts.length }} pieces to play in</p>
        <div v-if="collectionProducts.length" class="product-grid"><ProductCard v-for="product in collectionProducts" :key="product.id" :product="product" :favorite="favorites.includes(product.id)" @open="openProduct" @favorite="toggleFavorite" @add="quickAdd" /></div>
        <div v-else class="empty-results"><Search :size="28" aria-hidden="true" /><h2>No gear found</h2><p>Try another name or choose a different category.</p><button class="button button-primary" type="button" @click="query = ''; activeCategory = 'All'">Clear filters</button></div>
      </section>

      <section v-else-if="screen === 'product'" class="detail-page page-width" aria-labelledby="product-title">
        <div class="page-topline"><button class="back-link" type="button" @click="back"><ArrowLeft :size="17" aria-hidden="true" /> Back</button><span>SHOP / {{ selected.category.toUpperCase() }} / {{ selected.name.toUpperCase() }}</span></div>
        <div class="detail-layout">
          <div class="detail-gallery"><figure class="detail-photo"><img :src="selectedPhoto" :alt="selected.name" width="720" height="860" /><span class="photo-count">0{{ selected.gallery.indexOf(selectedPhoto) + 1 }} / 0{{ selected.gallery.length }}</span></figure><div class="gallery-thumbnails" role="group" aria-label="Product photos"><button v-for="(photo, index) in selected.gallery" :key="photo" type="button" :class="{ active: photo === selectedPhoto }" :aria-label="'Show product photo ' + (index + 1)" :aria-pressed="photo === selectedPhoto" @click="selectedPhoto = photo"><img :src="photo" alt="" width="76" height="82" /></button></div></div>
          <div class="detail-info"><p class="eyebrow"><span class="eyebrow-mark"></span> {{ selected.category.toUpperCase() }} / COMBASKET</p><h1 id="product-title">{{ selected.name }}</h1><div class="detail-rating"><span><Star v-for="n in 5" :key="n" :size="15" fill="currentColor" aria-hidden="true" /></span><strong>{{ selected.rating }}</strong><a href="#product-description">845 reviews</a></div><p id="product-description" class="detail-description">{{ selected.description }}</p>
            <div class="detail-price">{{ formatPrice(selected.price) }} <span>₸</span></div>
            <div class="product-specs"><div><span>Type</span><strong>{{ selected.category }}</strong></div><div><span>Size</span><strong>{{ selected.size }}</strong></div><div><span>Best for</span><strong>{{ selected.purpose }}</strong></div><div><span>Certificate</span><strong>FIBA</strong></div><div><span>Origin</span><strong>China</strong></div></div>
            <div class="detail-actions"><button class="button button-primary detail-buy" type="button" @click="addToCart(selected)">Add to bag <ShoppingBag :size="18" aria-hidden="true" /></button><button class="favorite-button" type="button" :aria-pressed="favorites.includes(selected.id)" :aria-label="favorites.includes(selected.id) ? 'Remove from favorites' : 'Add to favorites'" @click="toggleFavorite(selected.id)"><Heart :size="20" :fill="favorites.includes(selected.id) ? 'currentColor' : 'none'" aria-hidden="true" /></button></div>
            <p class="delivery-note"><Check :size="16" aria-hidden="true" /> Made for regular play. Delivery details at checkout.</p><button class="detail-accord" type="button" @click="go('tech')">Materials & care <ArrowUpRight :size="16" aria-hidden="true" /></button>
          </div>
        </div>
        <section class="detail-more" aria-labelledby="more-title"><div class="detail-more-heading"><div><p class="eyebrow"><span class="eyebrow-mark"></span> KEEP PLAYING</p><h2 id="more-title">You may also like.</h2></div><button class="text-link" type="button" @click="go('collection')">Shop all gear <ArrowRight :size="16" aria-hidden="true" /></button></div><div class="product-grid"><ProductCard v-for="product in products.filter(item => item.id !== selected.id).slice(0, 3)" :key="product.id" :product="product" :favorite="favorites.includes(product.id)" @open="openProduct" @favorite="toggleFavorite" @add="quickAdd" /></div></section>
      </section>

      <section v-else-if="screen === 'cart'" class="checkout-page page-width" aria-labelledby="checkout-title">
        <div class="page-topline"><button class="back-link" type="button" @click="go('home')"><ArrowLeft :size="17" aria-hidden="true" /> Keep shopping</button><span>COMBASKET / YOUR BAG</span></div>
        <div class="checkout-heading"><div><p class="eyebrow"><span class="eyebrow-mark"></span> ALMOST GAME TIME</p><h1 id="checkout-title">Your bag<span>.</span></h1></div><span class="checkout-count">{{ cart.length }} {{ cart.length === 1 ? 'item' : 'items' }}</span></div>
        <div v-if="cart.length" class="checkout-layout">
          <div class="checkout-items"><article v-for="(product, index) in cart" :key="product.id + '-' + index" class="checkout-item">
            <button class="checkout-product-photo" type="button" :aria-label="'View ' + product.name" @click="openProduct(product)"><img :src="cartImage(product)" :alt="product.name" width="110" height="130" loading="lazy" /></button>
            <div class="checkout-product-info"><p>{{ product.category }}</p><button type="button" @click="openProduct(product)">{{ product.name }}</button><span>Size {{ product.size }} · {{ product.purpose }}</span></div>
            <strong class="checkout-price">{{ formatPrice(product.price) }} ₸</strong><button class="remove-item" type="button" :aria-label="'Remove ' + product.name + ' from bag'" @click="removeFromCart(index)"><Trash2 :size="17" aria-hidden="true" /></button>
          </article></div>
          <aside class="order-summary" aria-labelledby="summary-title"><h2 id="summary-title">Order summary</h2><div><span>Subtotal</span><strong>{{ formatPrice(cartTotal) }} ₸</strong></div><div><span>Delivery</span><span>At checkout</span></div><div class="summary-total"><span>Total</span><strong>{{ formatPrice(cartTotal) }} ₸</strong></div><button class="button button-primary" type="button" :disabled="paying" @click="payOrder">Confirm order <ArrowRight :size="18" aria-hidden="true" /></button><p><Check :size="14" aria-hidden="true" /> Secure checkout preview</p></aside>
        </div>
        <div v-else class="empty-cart"><div class="empty-cart-mark"><ShoppingBag :size="32" aria-hidden="true" /></div><p class="eyebrow"><span class="eyebrow-mark"></span> NOTHING IN THE BAG YET</p><h2>Ready when you are.</h2><p>Your next game-day essential is waiting in the collection.</p><button class="button button-primary" type="button" @click="go('collection')">Explore the collection <ArrowRight :size="18" aria-hidden="true" /></button></div>
      </section>

      <section v-else-if="screen === 'profile'" class="profile-page page-width" aria-labelledby="profile-title">
        <div class="page-topline"><button class="back-link" type="button" @click="go('home')"><ArrowLeft :size="17" aria-hidden="true" /> Home</button><span>COMBASKET / PROFILE</span></div>
        <div class="profile-heading"><div><p class="eyebrow"><span class="eyebrow-mark"></span> PLAYER AREA</p><h1 id="profile-title">Your profile.</h1></div><button class="button button-outline" type="button" @click="go('login')">Edit profile <ArrowUpRight :size="16" aria-hidden="true" /></button></div>
        <div class="profile-layout"><aside class="profile-card"><img class="profile-avatar" src="/images/profile-avatar.jpg" alt="Basketball player profile portrait" width="100" height="100" /><p class="eyebrow">COMBASKET PLAYER</p><h2>Guest player</h2><span>{{ authEmail || 'Sign in to save your details' }}</span><button class="text-link" type="button" @click="go('login')">Account settings <ArrowRight :size="15" aria-hidden="true" /></button></aside>
          <div class="profile-content"><section class="profile-panel"><div class="panel-title"><div><p class="eyebrow"><span class="eyebrow-mark"></span> ORDER HISTORY</p><h2>On the way to the court.</h2></div><span class="status-pill"><span class="status-dot"></span>{{ orderPlaced ? 'Order confirmed' : 'No recent orders' }}</span></div><p>{{ orderPlaced ? 'Your demo checkout is complete. Thanks for playing with COMBASKET.' : 'Your confirmed orders will show up here.' }}</p><button class="text-link" type="button" @click="go('collection')">Find your next pick <ArrowRight :size="15" aria-hidden="true" /></button></section>
            <section class="profile-panel"><div class="panel-title"><div><p class="eyebrow"><span class="eyebrow-mark"></span> SAVED GEAR</p><h2>Your favourites.</h2></div><Heart :size="20" aria-hidden="true" /></div><div v-if="favorites.length" class="saved-list"><button v-for="product in products.filter(item => favorites.includes(item.id))" :key="product.id" type="button" @click="openProduct(product)"><img :src="product.image" alt="" width="48" height="58" /><span>{{ product.name }}</span><ChevronRight :size="16" aria-hidden="true" /></button></div><p v-else>Tap the heart on a product to keep it close.</p><button class="text-link" type="button" @click="go('collection')">Browse the collection <ArrowRight :size="15" aria-hidden="true" /></button></section></div>
        </div>
      </section>

      <section v-else-if="screen === 'login' || screen === 'register'" class="auth-page" :class="screen === 'register' ? 'auth-register' : 'auth-login'" aria-labelledby="auth-title">
        <div class="auth-photo"><img src="/images/court-background.jpg" alt="Outdoor basketball court" width="900" height="700" /><div class="auth-photo-copy"><img src="/images/combasket-mark-white.png" alt="" width="70" height="70" /><p>Find your<br />next run.</p><span>COMBASKET / PLAY YOUR WAY</span></div></div>
        <div class="auth-content"><button class="back-link" type="button" @click="go('home')"><ArrowLeft :size="17" aria-hidden="true" /> Back to the store</button><p class="eyebrow"><span class="eyebrow-mark"></span> PLAYER ACCOUNT</p><h1 id="auth-title">{{ screen === 'login' ? 'Welcome back.' : 'Join the game.' }}</h1><p class="auth-intro">{{ screen === 'login' ? 'Sign in to keep your gear and orders together.' : 'Create an account and keep your favourite gear close.' }}</p>
          <form class="auth-form" @submit.prevent="submitAuth"><label for="auth-email">Email address</label><input id="auth-email" v-model="authEmail" type="email" autocomplete="email" placeholder="you@example.com" required /><label for="auth-password">Password</label><input id="auth-password" v-model="authPassword" type="password" :autocomplete="screen === 'login' ? 'current-password' : 'new-password'" placeholder="Enter your password" required />
            <template v-if="screen === 'register'"><label for="auth-confirm">Confirm password</label><input id="auth-confirm" v-model="confirmPassword" type="password" autocomplete="new-password" placeholder="Enter it once more" required /></template>
            <p v-if="authError" class="form-error" role="alert">{{ authError }}</p><button class="button button-primary auth-submit" type="submit">{{ screen === 'login' ? 'Sign in' : 'Create account' }} <ArrowRight :size="18" aria-hidden="true" /></button>
          </form>
          <p class="auth-switch">{{ screen === 'login' ? 'New to COMBASKET?' : 'Already have an account?' }} <button type="button" @click="go(screen === 'login' ? 'register' : 'login')">{{ screen === 'login' ? 'Create an account' : 'Sign in' }}</button></p><p class="auth-demo-note"><Check :size="14" aria-hidden="true" /> Demo account only. No details are sent or saved.</p>
        </div>
      </section>

      <section v-else-if="screen === 'about'" class="info-page about-page page-width" aria-labelledby="about-title">
        <div class="page-topline"><button class="back-link" type="button" @click="go('home')"><ArrowLeft :size="17" aria-hidden="true" /> Home</button><span>COMBASKET / OUR STORY</span></div>
        <div class="about-hero"><div class="about-copy"><p class="eyebrow"><span class="eyebrow-mark"></span> A BRAND BUILT AROUND THE GAME</p><h1 id="about-title">Basketball<br />brings us <span>together.</span></h1><p>COMBASKET is a basketball-focused brand driven by passion for the game. We design basketballs and equipment that combine performance, durability and modern style.</p><p>Inspired by street and professional basketball culture, COMBASKET is made for players who demand quality and confidence on every court.</p><button class="button button-primary" type="button" @click="go('collection')">Explore the gear <ArrowRight :size="18" aria-hidden="true" /></button></div>
          <div class="about-visual"><img class="about-decor" src="/images/decor-why.png" alt="" aria-hidden="true" /><img class="about-mark" src="/images/combasket-mark-white.png" alt="" width="130" height="130" /><img class="about-ball" src="/images/ball-chocolate.jpg" alt="Chocolate basketball from the COMBASKET collection" width="380" height="500" loading="lazy" /><span>BUILT FOR PLAYERS. MADE FOR THE GAME.</span></div></div>
        <div class="about-values"><article><strong>01</strong><h2>Made to move</h2><p>Thoughtful details that stay with you through the run.</p></article><article><strong>02</strong><h2>Rooted in the court</h2><p>Real basketball culture is where every idea starts.</p></article><article><strong>03</strong><h2>Play with confidence</h2><p>Reliable feel for the moments that matter.</p></article></div>
      </section>

      <section v-else-if="screen === 'tech'" class="info-page tech-page page-width" aria-labelledby="tech-title">
        <div class="page-topline"><button class="back-link" type="button" @click="go('home')"><ArrowLeft :size="17" aria-hidden="true" /> Home</button><span>COMBASKET / TECHNOLOGY</span></div>
        <div class="tech-layout"><div class="tech-copy"><p class="eyebrow"><span class="eyebrow-mark"></span> BUILT AROUND THE GAME</p><h1 id="tech-title">Feel the<br /><span>difference.</span></h1><p>Every basketball and piece of equipment is developed with materials and manufacturing processes chosen for consistent performance on court.</p><p>Our balls feature textured surfaces for enhanced grip, reliable air retention for a steady bounce and reinforced layers for durability. We test in real game conditions to balance control, comfort and resilience.</p><button class="button button-primary" type="button" @click="go('collection')">Find your gear <ArrowRight :size="18" aria-hidden="true" /></button></div>
          <div class="tech-image-panel"><img class="tech-ball" src="/images/ball-blue.jpg" alt="Close view of the textured WAVE basketball" width="450" height="600" loading="lazy" /><div class="tech-callout callout-one"><span>01</span><strong>Textured grip</strong></div><div class="tech-callout callout-two"><span>02</span><strong>Steady bounce</strong></div><img class="tech-outline" src="/images/basketball-outline.png" alt="" aria-hidden="true" width="110" height="110" /></div></div>
        <div class="tech-points"><article><span>01 / MATERIAL</span><h2>Grip you can trust.</h2><p>A tactile surface helps you keep the ball close through quick changes in pace.</p></article><article><span>02 / CONTROL</span><h2>Built for consistency.</h2><p>Materials are chosen to support reliable handling from warmup to final shot.</p></article><article><span>03 / TESTING</span><h2>Out where you play.</h2><p>Design takes cues from real street courts, indoor arenas and everyday training.</p></article></div>
      </section>

      <section v-else-if="screen === 'support'" class="info-page support-page page-width" aria-labelledby="support-title">
        <div class="page-topline"><button class="back-link" type="button" @click="go('home')"><ArrowLeft :size="17" aria-hidden="true" /> Home</button><span>COMBASKET / SUPPORT</span></div>
        <div class="support-heading"><p class="eyebrow"><span class="eyebrow-mark"></span> HERE FOR YOUR NEXT RUN</p><h1 id="support-title">Need a hand?</h1><p>Quick answers for choosing your COMBASKET gear.</p></div>
        <div class="support-layout"><div class="faq-list"><details open><summary>How do I choose a basketball size?<ChevronDown :size="18" aria-hidden="true" /></summary><p>Size 7 is the standard men's size. Size 6 is commonly used for women's and youth play. Check your league's rules to be sure.</p></details><details><summary>Can I use these balls outdoors?<ChevronDown :size="18" aria-hidden="true" /></summary><p>Look for “Outdoor” in the product details. The ASPHVLT and WAVE basketballs are listed for outdoor courts.</p></details><details><summary>How do I find my order?<ChevronDown :size="18" aria-hidden="true" /></summary><p>This prototype doesn't connect to an order system yet. Demo orders show as confirmed in your profile after checkout.</p></details><details><summary>How do I care for my gear?<ChevronDown :size="18" aria-hidden="true" /></summary><p>Keep equipment clean and dry between sessions. Visit the Technology page for more about product materials.</p></details></div>
          <aside class="support-card"><img src="/images/icon-test-tube.png" alt="" width="54" height="54" loading="lazy" /><p class="eyebrow">STILL EXPLORING?</p><h2>Find the right fit for your game.</h2><button class="button button-dark" type="button" @click="go('collection')">Browse the collection <ArrowRight :size="17" aria-hidden="true" /></button><button class="support-secondary" type="button" @click="go('tech')">Read about our materials <ChevronRight :size="16" aria-hidden="true" /></button></aside></div>
      </section>
    </main>

    <footer class="site-footer">
      <div class="footer-main page-width">
        <div class="footer-brand"><button class="brand-lockup" type="button" aria-label="COMBASKET home" @click="go('home')"><img src="/images/combasket-mark-white.png" alt="" width="36" height="36" loading="lazy" /><span>COMBASKET</span></button><p>Play your way.<br />Every court counts.</p><div class="social-links"><a href="#instagram" aria-label="COMBASKET on Instagram"><img src="/images/social-instagram.png" alt="" width="28" height="28" loading="lazy" /></a><a href="#wildberries" aria-label="COMBASKET on Wildberries"><img src="/images/social-wildberries.png" alt="" width="28" height="28" loading="lazy" /></a><a href="#vk" aria-label="COMBASKET on VK"><img src="/images/social-vk.png" alt="" width="28" height="28" loading="lazy" /></a><a href="#ozon" aria-label="COMBASKET on Ozon"><img src="/images/social-ozon-source.png" alt="" width="28" height="28" loading="lazy" /></a></div></div>
        <nav class="footer-nav" aria-label="Footer navigation"><strong>Explore</strong><button type="button" @click="go('collection')">Shop all gear</button><button type="button" @click="go('about')">Our story</button><button type="button" @click="go('tech')">Technology</button><button type="button" @click="go('support')">Support</button></nav>
        <div class="footer-note"><p class="eyebrow eyebrow-light"><span class="eyebrow-mark"></span> MADE FOR THE GAME</p><p>From the first bounce<br />to the last shot.</p><button class="footer-cta" type="button" @click="go('collection')">Find your next pick <ArrowUpRight :size="17" aria-hidden="true" /></button></div>
      </div>
      <div class="footer-bottom page-width"><span>© 2026 COMBASKET</span><span>Basketball gear for every court.</span><button type="button" @click="go('support')">Help & support <ArrowRight :size="14" aria-hidden="true" /></button></div>
    </footer>

    <div v-if="cartOpen" class="mini-cart-overlay" role="presentation" @click.self="closeMiniCart">
      <section class="mini-cart" role="dialog" aria-modal="true" aria-labelledby="mini-cart-title" @keydown="trapModalFocus">
        <div class="mini-cart-heading"><div><p class="eyebrow"><span class="eyebrow-mark"></span> READY WHEN YOU ARE</p><h2 id="mini-cart-title">Your bag <span>({{ cart.length }})</span></h2></div><button ref="miniCartClose" class="icon-button mini-cart-close" type="button" aria-label="Close bag" @click="closeMiniCart"><X :size="21" aria-hidden="true" /></button></div>
        <div v-if="cart.length" class="mini-cart-items"><article v-for="(product, index) in cart" :key="product.id + '-' + index" class="mini-cart-item"><button class="mini-cart-image" type="button" :aria-label="'View ' + product.name" @click="closeMiniCart(); openProduct(product)"><img :src="cartImage(product)" :alt="product.name" width="72" height="86" loading="lazy" /></button><div class="mini-cart-product"><span>{{ product.category }}</span><button type="button" @click="closeMiniCart(); openProduct(product)">{{ product.name }}</button><strong>{{ formatPrice(product.price) }} ₸</strong></div><button class="mini-cart-remove" type="button" :aria-label="'Remove ' + product.name" @click="removeFromCart(index)"><Trash2 :size="16" aria-hidden="true" /></button></article></div>
        <div v-else class="mini-cart-empty"><ShoppingBag :size="28" aria-hidden="true" /><p>Your bag is ready for a new pick.</p><button class="text-link" type="button" @click="closeMiniCart(); go('collection')">Browse gear <ArrowRight :size="15" aria-hidden="true" /></button></div>
        <div v-if="cart.length" class="mini-cart-footer"><div><span>Subtotal</span><strong>{{ formatPrice(cartTotal) }} ₸</strong></div><button class="button button-primary" type="button" @click="closeMiniCart(); go('cart')">Review your bag <ArrowRight :size="18" aria-hidden="true" /></button><p>Delivery details at checkout</p></div>
      </section>
    </div>
    <div v-if="paying" class="paying-overlay" role="status" aria-live="polite" aria-atomic="true"><div class="paying-card"><span class="paying-spinner" aria-hidden="true"></span><strong>Confirming your order</strong><small>Getting your gear ready for the game.</small></div></div>
  </div>
</template>
