<script setup lang="ts">
import { ArrowUpRight, Heart, ShoppingBag, Star } from 'lucide-vue-next'

type Product = {
  id: number
  name: string
  category: 'Basketballs' | 'Accessories' | 'Protection' | 'Apparel'
  price: number
  image: string
  gallery: string[]
  label?: string
  size: string
  purpose: string
  rating: string
  description: string
}

defineProps<{ product: Product; favorite: boolean }>()
const emit = defineEmits<{
  open: [product: Product]
  favorite: [id: number]
  add: [product: Product]
}>()
const formatPrice = (price: number) => new Intl.NumberFormat('ru-RU').format(price)
</script>

<template>
  <article class="product-card">
    <div class="product-card-visual">
      <button class="product-card-photo" type="button" :aria-label="'View ' + product.name" @click="emit('open', product)">
        <img :src="product.image" :alt="product.name" width="540" height="650" loading="lazy" />
        <span v-if="product.label" class="product-badge">{{ product.label }}</span>
        <span class="product-card-arrow" aria-hidden="true"><ArrowUpRight :size="17" /></span>
      </button>
      <button class="product-favorite" type="button" :aria-pressed="favorite" :aria-label="favorite ? 'Remove ' + product.name + ' from favorites' : 'Add ' + product.name + ' to favorites'" @click="emit('favorite', product.id)">
        <Heart :size="18" :fill="favorite ? 'currentColor' : 'none'" aria-hidden="true" />
      </button>
    </div>
    <div class="product-card-info">
      <div class="product-card-title">
        <div><span class="product-category">{{ product.category }}</span><button type="button" @click="emit('open', product)">{{ product.name }}</button></div>
        <span class="product-rating"><Star :size="13" fill="currentColor" aria-hidden="true" />{{ product.rating }}</span>
      </div>
      <div class="product-card-meta"><span>Size {{ product.size }}</span><span>{{ product.purpose }}</span></div>
      <div class="product-card-bottom"><strong>{{ formatPrice(product.price) }} <small>₸</small></strong><button class="quick-add" type="button" @click="emit('add', product)">Add to bag <ShoppingBag :size="16" aria-hidden="true" /></button></div>
    </div>
  </article>
</template>
