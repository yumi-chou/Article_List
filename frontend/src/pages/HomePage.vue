<template>
  <main class="max-w-3xl mx-auto p-4 space-y-6">
    <section v-for="post in posts" :key="post.id" class="border rounded-md">
      <div class="border m-2 p-4 rounded">
        <h2 class="text-3xl font-semibold"> {{ post.title }} </h2>
        <p class="mt-1 text-sm">By {{ post.author }}</p>
        <p class="mt-4 leading-relaxed">{{ post.excerpt }}</p>
        <div class="mt-4 text-right">
          <RouterLink
            class="underline hover:no-underline"
            :to="{ name: 'article', params: { id: post.id } }"
          >
            More
          </RouterLink>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup>
import { posts } from '../components/posts.js'
</script>

